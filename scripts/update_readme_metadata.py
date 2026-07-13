#!/usr/bin/env python3
"""Update GitHub repository metadata in the curated README tables."""

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


BASE_HEADERS = ("项目", "形态", "核心定位", "适用场景")
METADATA_HEADERS = ("GitHub 简介", "最近更新", "最新 Release")
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
        description=repository.get("description") or "暂无简介",
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


def metadata_cells(metadata: RepositoryMetadata, today: date) -> tuple[str, str, str]:
    pushed_on = iso_date(metadata.pushed_at)
    age = (today - pushed_on).days
    recently_updated = age <= ACTIVE_DAYS
    activity = f"{'是' if recently_updated else '否'} · {pushed_on.isoformat()}"

    if metadata.release_tag and metadata.release_url and metadata.release_published_at:
        tag = sanitize_cell(metadata.release_tag)
        release_on = iso_date(metadata.release_published_at).isoformat()
        release = f"[{tag}]({metadata.release_url}) · {release_on}"
    else:
        release = "暂无"

    return sanitize_cell(metadata.description), activity, release


def update_readme(
    content: str,
    metadata_by_repository: dict[tuple[str, str], RepositoryMetadata],
    *,
    today: date,
) -> tuple[str, int, int]:
    lines = content.splitlines(keepends=True)
    output: list[str] = []
    in_managed_table = False
    expect_separator = False
    table_count = 0
    repository_count = 0

    for original_line in lines:
        newline = "\n" if original_line.endswith("\n") else ""
        line = original_line.rstrip("\r\n")
        cells = parse_markdown_row(line)

        if cells and tuple(cells[: len(BASE_HEADERS)]) == BASE_HEADERS:
            if len(cells) not in (len(BASE_HEADERS), len(BASE_HEADERS) + len(METADATA_HEADERS)):
                raise ValueError(f"Unexpected project table header: {line}")
            output.append(render_markdown_row((*BASE_HEADERS, *METADATA_HEADERS)) + newline)
            in_managed_table = True
            expect_separator = True
            table_count += 1
            continue

        if in_managed_table and expect_separator:
            if not cells or len(cells) not in (
                len(BASE_HEADERS),
                len(BASE_HEADERS) + len(METADATA_HEADERS),
            ):
                raise ValueError("Project table header is not followed by a valid separator row")
            output.append(render_markdown_row(["---"] * (len(BASE_HEADERS) + len(METADATA_HEADERS))) + newline)
            expect_separator = False
            continue

        if in_managed_table:
            if not cells:
                in_managed_table = False
            else:
                repository = parse_github_repository(line)
                if repository:
                    if len(cells) not in (
                        len(BASE_HEADERS),
                        len(BASE_HEADERS) + len(METADATA_HEADERS),
                    ):
                        raise ValueError(f"Unexpected project table row: {line}")
                    metadata = metadata_by_repository.get(repository)
                    if metadata:
                        managed_cells = metadata_cells(metadata, today)
                    elif len(cells) == len(BASE_HEADERS) + len(METADATA_HEADERS):
                        managed_cells = tuple(cells[-len(METADATA_HEADERS) :])
                    else:
                        managed_cells = ("获取失败", "获取失败", "获取失败")
                    output.append(
                        render_markdown_row([*cells[: len(BASE_HEADERS)], *managed_cells]) + newline
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
        if cells and tuple(cells[: len(BASE_HEADERS)]) == BASE_HEADERS:
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
    root = Path(__file__).resolve().parents[1]
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--readme", type=Path, default=root / "README.md")
    parser.add_argument("--api-base", default="https://api.github.com")
    parser.add_argument("--today", type=date.fromisoformat, default=date.today())
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    content = args.readme.read_text(encoding="utf-8")
    repositories = repositories_in_managed_tables(content)
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

    updated, table_count, repository_count = update_readme(
        content,
        metadata_by_repository,
        today=args.today,
    )
    args.readme.write_text(updated, encoding="utf-8")
    print(f"Updated {repository_count} rows across {table_count} tables")

    if failures:
        print(f"Completed with {len(failures)} repository fetch failure(s)", file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
