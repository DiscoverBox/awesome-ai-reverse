#!/usr/bin/env python3
"""Update GitHub repository metadata in the Chinese and English README tables."""

from __future__ import annotations

import argparse
import http.client
import json
import os
import re
import sys
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from dataclasses import dataclass
from datetime import date, datetime, timezone
from pathlib import Path
from typing import Any
from urllib.error import HTTPError, URLError
from urllib.parse import quote
from urllib.request import Request, urlopen


@dataclass(frozen=True)
class TableLocale:
    base_headers: tuple[str, ...]
    metadata_headers: tuple[str, ...]
    active: str
    inactive: str
    no_description: str
    no_release: str
    fetch_failed: str


ZH_LOCALE = TableLocale(
    base_headers=("项目", "形态", "核心定位", "适用场景"),
    metadata_headers=("GitHub 简介", "最近更新", "最新 Release"),
    active="是",
    inactive="否",
    no_description="暂无简介",
    no_release="暂无",
    fetch_failed="获取失败",
)
EN_LOCALE = TableLocale(
    base_headers=("Project", "Type", "Core Focus", "Best For"),
    metadata_headers=("GitHub Description", "Recently Updated", "Latest Release"),
    active="Yes",
    inactive="No",
    no_description="No description",
    no_release="None",
    fetch_failed="Fetch failed",
)
TABLE_LOCALES = (ZH_LOCALE, EN_LOCALE)
ACTIVE_DAYS = 90
GITHUB_REPOSITORY_RE = re.compile(
    r"https://github\.com/(?P<owner>[A-Za-z0-9_.-]+)/(?P<repo>[A-Za-z0-9_.-]+?)(?:/)?(?=[)#\s|]|$)"
)


class GitHubAPIError(RuntimeError):
    """Raised when GitHub metadata cannot be fetched."""

    def __init__(self, message: str, *, status: int | None = None) -> None:
        super().__init__(message)
        self.status = status


@dataclass(frozen=True)
class RepositoryMetadata:
    description: str
    pushed_at: str
    release_tag: str | None
    release_published_at: str | None
    release_url: str | None


def github_request(url: str, token: str | None = None) -> Any:
    headers = {
        "Accept": "application/vnd.github+json",
        "User-Agent": "awesome-ai-reverse-readme-updater",
        "X-GitHub-Api-Version": "2022-11-28",
    }
    if token:
        headers["Authorization"] = f"Bearer {token}"

    for attempt in range(3):
        request = Request(url, headers=headers)
        try:
            with urlopen(request, timeout=30) as response:
                return json.load(response)
        except HTTPError as error:
            if error.code >= 500 and attempt < 2:
                time.sleep(2**attempt)
                continue
            message = error.reason
            try:
                payload = json.load(error)
                message = payload.get("message", message)
            except (json.JSONDecodeError, AttributeError):
                pass
            raise GitHubAPIError(
                f"GitHub API returned {error.code} for {url}: {message}",
                status=error.code,
            ) from error
        except (
            URLError,
            TimeoutError,
            ConnectionError,
            http.client.RemoteDisconnected,
            OSError,
        ) as error:
            if attempt < 2:
                time.sleep(2**attempt)
                continue
            raise GitHubAPIError(f"Could not reach GitHub API for {url}: {error}") from error

    raise AssertionError("unreachable")


def fetch_repository_metadata(
    owner: str,
    repo: str,
    *,
    token: str | None = None,
    api_base: str = "https://api.github.com",
) -> RepositoryMetadata:
    slug = f"{quote(owner, safe='')}/{quote(repo, safe='')}"
    repository = github_request(f"{api_base}/repos/{slug}", token)

    full_name = repository.get("full_name", f"{owner}/{repo}")
    release_slug = "/".join(quote(part, safe="") for part in full_name.split("/", 1))
    try:
        release = github_request(
            f"{api_base}/repos/{release_slug}/releases/latest",
            token,
        )
    except GitHubAPIError as error:
        if error.status != 404:
            raise
        release = None

    return RepositoryMetadata(
        description=repository.get("description") or "",
        pushed_at=repository["pushed_at"],
        release_tag=release.get("tag_name") if release else None,
        release_published_at=release.get("published_at") if release else None,
        release_url=release.get("html_url") if release else None,
    )


def parse_markdown_row(line: str) -> list[str] | None:
    stripped = line.strip()
    if not stripped.startswith("|") or not stripped.endswith("|"):
        return None
    return [cell.strip() for cell in stripped[1:-1].split("|")]


def render_markdown_row(cells: list[str] | tuple[str, ...]) -> str:
    return "| " + " | ".join(cells) + " |"


def sanitize_cell(value: str) -> str:
    return " ".join(value.split()).replace("|", "&#124;")


def parse_github_repository(line: str) -> tuple[str, str] | None:
    match = GITHUB_REPOSITORY_RE.search(line)
    if not match:
        return None
    return match.group("owner"), match.group("repo")


def iso_date(timestamp: str) -> date:
    return datetime.fromisoformat(timestamp.replace("Z", "+00:00")).astimezone(timezone.utc).date()


def table_locale(cells: list[str]) -> TableLocale | None:
    for locale in TABLE_LOCALES:
        if tuple(cells[: len(locale.base_headers)]) == locale.base_headers:
            return locale
    return None


def metadata_cells(
    metadata: RepositoryMetadata,
    today: date,
    locale: TableLocale = ZH_LOCALE,
) -> tuple[str, str, str]:
    pushed_on = iso_date(metadata.pushed_at)
    age = (today - pushed_on).days
    recently_updated = age <= ACTIVE_DAYS
    activity = f"{locale.active if recently_updated else locale.inactive} · {pushed_on.isoformat()}"

    if metadata.release_tag and metadata.release_url and metadata.release_published_at:
        tag = sanitize_cell(metadata.release_tag)
        release_on = iso_date(metadata.release_published_at).isoformat()
        release = f"[{tag}]({metadata.release_url}) · {release_on}"
    else:
        release = locale.no_release

    description = metadata.description or locale.no_description
    return sanitize_cell(description), activity, release


def update_readme(
    content: str,
    metadata_by_repository: dict[tuple[str, str], RepositoryMetadata],
    *,
    today: date,
) -> tuple[str, int, int]:
    lines = content.splitlines(keepends=True)
    output: list[str] = []
    current_locale: TableLocale | None = None
    expect_separator = False
    table_count = 0
    repository_count = 0

    for original_line in lines:
        newline = "\n" if original_line.endswith("\n") else ""
        line = original_line.rstrip("\r\n")
        cells = parse_markdown_row(line)

        locale = table_locale(cells) if cells else None
        if locale:
            base_count = len(locale.base_headers)
            metadata_count = len(locale.metadata_headers)
            if len(cells) not in (base_count, base_count + metadata_count):
                raise ValueError(f"Unexpected project table header: {line}")
            output.append(
                render_markdown_row((*locale.base_headers, *locale.metadata_headers)) + newline
            )
            current_locale = locale
            expect_separator = True
            table_count += 1
            continue

        if current_locale and expect_separator:
            base_count = len(current_locale.base_headers)
            metadata_count = len(current_locale.metadata_headers)
            if not cells or len(cells) not in (
                base_count,
                base_count + metadata_count,
            ):
                raise ValueError("Project table header is not followed by a valid separator row")
            output.append(
                render_markdown_row(["---"] * (base_count + metadata_count)) + newline
            )
            expect_separator = False
            continue

        if current_locale:
            if not cells:
                current_locale = None
            else:
                base_count = len(current_locale.base_headers)
                metadata_count = len(current_locale.metadata_headers)
                repository = parse_github_repository(line)
                if repository:
                    if len(cells) not in (
                        base_count,
                        base_count + metadata_count,
                    ):
                        raise ValueError(f"Unexpected project table row: {line}")
                    metadata = metadata_by_repository.get(repository)
                    if metadata:
                        managed_cells = metadata_cells(metadata, today, current_locale)
                    elif len(cells) == base_count + metadata_count:
                        managed_cells = tuple(cells[-metadata_count:])
                    else:
                        managed_cells = (current_locale.fetch_failed,) * metadata_count
                    output.append(
                        render_markdown_row([*cells[:base_count], *managed_cells]) + newline
                    )
                    repository_count += 1
                    continue

        output.append(original_line)

    return "".join(output), table_count, repository_count


def repositories_in_managed_tables(content: str) -> list[tuple[str, str]]:
    repositories: list[tuple[str, str]] = []
    in_managed_table = False

    for line in content.splitlines():
        cells = parse_markdown_row(line)
        if cells and table_locale(cells):
            in_managed_table = True
            continue
        if in_managed_table and not cells:
            in_managed_table = False
            continue
        if in_managed_table:
            repository = parse_github_repository(line)
            if repository and repository not in repositories:
                repositories.append(repository)

    return repositories


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--readme",
        dest="readmes",
        action="append",
        type=Path,
        help="README to update; repeat for multiple files (defaults to README.md and README_EN.md)",
    )
    parser.add_argument("--api-base", default="https://api.github.com")
    parser.add_argument("--today", type=date.fromisoformat, default=date.today())
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    root = Path(__file__).resolve().parents[1]
    readmes = args.readmes or [root / "README.md", root / "README_EN.md"]
    contents = {readme: readme.read_text(encoding="utf-8") for readme in readmes}
    repositories: list[tuple[str, str]] = []
    for content in contents.values():
        for repository in repositories_in_managed_tables(content):
            if repository not in repositories:
                repositories.append(repository)
    if not repositories:
        print("No GitHub repositories found in managed project tables", file=sys.stderr)
        return 1

    token = os.environ.get("GITHUB_TOKEN")
    metadata_by_repository: dict[tuple[str, str], RepositoryMetadata] = {}
    failures: list[str] = []
    with ThreadPoolExecutor(max_workers=min(4, len(repositories))) as executor:
        future_to_repository = {
            executor.submit(
                fetch_repository_metadata,
                owner,
                repo,
                token=token,
                api_base=args.api_base.rstrip("/"),
            ): (owner, repo)
            for owner, repo in repositories
        }
        for future in as_completed(future_to_repository):
            owner, repo = future_to_repository[future]
            try:
                metadata_by_repository[(owner, repo)] = future.result()
                print(f"Fetched {owner}/{repo}", flush=True)
            except Exception as error:
                failures.append(f"{owner}/{repo}: {error}")
                print(f"Warning: {failures[-1]}", file=sys.stderr, flush=True)

    total_table_count = 0
    total_repository_count = 0
    for readme, content in contents.items():
        updated, table_count, repository_count = update_readme(
            content,
            metadata_by_repository,
            today=args.today,
        )
        readme.write_text(updated, encoding="utf-8")
        total_table_count += table_count
        total_repository_count += repository_count
        print(f"Updated {readme}: {repository_count} rows across {table_count} tables")

    print(
        f"Updated {total_repository_count} rows across {total_table_count} tables "
        f"in {len(readmes)} README files"
    )

    if failures:
        print(f"Completed with {len(failures)} repository fetch failure(s)", file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
