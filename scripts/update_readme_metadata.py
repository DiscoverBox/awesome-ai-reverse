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
from enum import Enum
from pathlib import Path
from typing import Any
from urllib.error import HTTPError, URLError
from urllib.parse import quote
from urllib.request import Request, urlopen


class RepositoryStatus(Enum):
    """Lifecycle state of an observed repository."""

    ACTIVE = "active"
    ARCHIVED = "archived"
    REMOVED = "removed"
    MOVED = "moved"


@dataclass(frozen=True)
class TableLocale:
    base_headers: tuple[str, ...]
    metadata_headers: tuple[str, ...]
    legacy_metadata_headers: tuple[str, ...]
    active: str
    inactive: str
    no_description: str
    no_release: str
    fetch_failed: str
    deprecated: str


ZH_LOCALE = TableLocale(
    base_headers=("项目", "形态", "核心定位", "适用场景"),
    metadata_headers=("GitHub 简介", "最近更新", "最新 Release", "Stars"),
    legacy_metadata_headers=("GitHub 简介", "最近更新", "最新 Release"),
    active="是",
    inactive="否",
    no_description="暂无简介",
    no_release="暂无",
    fetch_failed="获取失败",
    deprecated="已废弃",
)
EN_LOCALE = TableLocale(
    base_headers=("Project", "Type", "Core Focus", "Best For"),
    metadata_headers=("GitHub Description", "Recently Updated", "Latest Release", "Stars"),
    legacy_metadata_headers=("GitHub Description", "Recently Updated", "Latest Release"),
    active="Yes",
    inactive="No",
    no_description="No description",
    no_release="None",
    fetch_failed="Fetch failed",
    deprecated="Deprecated",
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
    stargazers_count: int | None = None
    status: RepositoryStatus = RepositoryStatus.ACTIVE
    new_full_name: str | None = None
    # True when the release endpoint failed transiently (5xx / rate limit /
    # network). Distinct from a 404 (definitely no release): a transient
    # failure must preserve the README's previous release value instead of
    # wiping it to "暂无".
    release_fetch_failed: bool = False


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

    # A 404 on the repository itself means it was deleted or made private
    # (and the token cannot see it). Treat both as "removed/deprecated".
    try:
        repository = github_request(f"{api_base}/repos/{slug}", token)
    except GitHubAPIError as error:
        if error.status == 404:
            return RepositoryMetadata(
                description="",
                pushed_at="",
                release_tag=None,
                release_published_at=None,
                release_url=None,
                status=RepositoryStatus.REMOVED,
            )
        raise

    full_name = repository.get("full_name", f"{owner}/{repo}")
    archived = bool(repository.get("archived"))
    moved = full_name.lower() != f"{owner}/{repo}".lower()

    # Archived takes precedence over moved: a redirected-then-archived repo
    # is surfaced as deprecated, not silently rewritten.
    if archived:
        status = RepositoryStatus.ARCHIVED
    elif moved:
        status = RepositoryStatus.MOVED
    else:
        status = RepositoryStatus.ACTIVE

    release = None
    release_fetch_failed = False
    # Archived repos render the deprecated row (release column is always
    # "暂无"), so the release endpoint is not queried — saves an API call and
    # avoids a transient release failure polluting an archived entry.
    if not archived:
        release_slug = "/".join(quote(part, safe="") for part in full_name.split("/", 1))
        try:
            release = github_request(
                f"{api_base}/repos/{release_slug}/releases/latest",
                token,
            )
        except GitHubAPIError as error:
            if error.status == 404:
                # The repo genuinely has no published release.
                release = None
            else:
                # Transient (5xx / rate limit / network). Preserve the
                # already-determined archived/moved status and flag the
                # release as fetch-failed so the README keeps its previous
                # release value instead of being wiped to "暂无".
                release = None
                release_fetch_failed = True

    return RepositoryMetadata(
        description=repository.get("description") or "",
        pushed_at=repository["pushed_at"],
        release_tag=release.get("tag_name") if release else None,
        release_published_at=release.get("published_at") if release else None,
        release_url=release.get("html_url") if release else None,
        stargazers_count=repository.get("stargazers_count"),
        status=status,
        new_full_name=full_name if moved else None,
        release_fetch_failed=release_fetch_failed,
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


SEPARATOR_CELL_RE = re.compile(r"^:?-+:?$")


def is_separator_row(cells: list[str], expected_count: int) -> bool:
    """True if *cells* is a valid GFM separator row of *expected_count* columns."""
    return bool(cells) and len(cells) == expected_count and all(
        SEPARATOR_CELL_RE.fullmatch(cell) for cell in cells
    )


@dataclass(frozen=True)
class ManagedTableHeader:
    """A recognized managed-table header and its input column count.

    source_column_count is the count of the *input* header row (4 for a base
    header being extended, 7 for the legacy metadata schema, or 8 for the
    current schema). The separator that follows must match this count.
    """

    locale: TableLocale
    source_column_count: int


def parse_managed_table_header(
    cells: list[str],
) -> ManagedTableHeader | None:
    """Recognize a managed project-table header.

    Returns a header for an exact base, legacy, or current schema match, None
    for a non-managed table, and raises ValueError when the base columns match
    but the trailing columns are not managed metadata columns (a schema
    conflict that must not be silently rewritten).
    """
    for locale in TABLE_LOCALES:
        base = locale.base_headers
        if len(cells) < len(base) or tuple(cells[: len(base)]) != base:
            continue
        full = (*base, *locale.metadata_headers)
        legacy_full = (*base, *locale.legacy_metadata_headers)
        if tuple(cells) == base:
            return ManagedTableHeader(locale, len(base))
        if tuple(cells) == full:
            return ManagedTableHeader(locale, len(full))
        if tuple(cells) == legacy_full:
            return ManagedTableHeader(locale, len(legacy_full))
        raise ValueError("Unexpected columns in managed project table header")
    return None


def metadata_cells(
    metadata: RepositoryMetadata,
    today: date,
    locale: TableLocale = ZH_LOCALE,
    previous_release: str | None = None,
) -> tuple[str, str, str, str]:
    pushed_on = iso_date(metadata.pushed_at)
    age = (today - pushed_on).days
    recently_updated = age <= ACTIVE_DAYS
    activity = f"{locale.active if recently_updated else locale.inactive} · {pushed_on.isoformat()}"

    if metadata.release_fetch_failed:
        # Transient release failure: keep the README's previous release value
        # verbatim (no prefix) so the cell stays idempotent across runs; the
        # failure is surfaced in stderr + step summary by main() instead.
        release = previous_release if previous_release else locale.no_release
    elif metadata.release_tag and metadata.release_url and metadata.release_published_at:
        tag = sanitize_cell(metadata.release_tag)
        release_on = iso_date(metadata.release_published_at).isoformat()
        release = f"[{tag}]({metadata.release_url}) · {release_on}"
    else:
        release = locale.no_release

    description = metadata.description or locale.no_description
    stars = (
        str(metadata.stargazers_count)
        if metadata.stargazers_count is not None
        else locale.fetch_failed
    )
    return sanitize_cell(description), activity, release, stars


def deprecated_cells(
    metadata: RepositoryMetadata,
    locale: TableLocale = ZH_LOCALE,
) -> tuple[str, str, str, str]:
    """Render cells for a repository that is archived or removed (hard-deprecated).

    Old metadata is intentionally cleared so reviewers are forced to re-check the
    entry instead of trusting possibly-stale values.
    """
    marker = f"🗄️ {locale.deprecated}"
    stars = (
        str(metadata.stargazers_count)
        if metadata.stargazers_count is not None
        else "—"
    )
    return marker, locale.deprecated, locale.no_release, stars


def replace_repository_url(cell: str, old: tuple[str, str], new_full_name: str) -> str:
    """Rewrite the GitHub URL in a table cell to point at a transferred repo."""
    pattern = re.compile(
        rf"https://github\.com/{re.escape(old[0])}/{re.escape(old[1])}(?=[)/#\s|]|$)"
    )
    return pattern.sub(f"https://github.com/{new_full_name}", cell)


def update_readme(
    content: str,
    metadata_by_repository: dict[tuple[str, str], RepositoryMetadata],
    *,
    today: date,
) -> tuple[str, int, int]:
    lines = content.splitlines(keepends=True)
    output: list[str] = []
    current_header: ManagedTableHeader | None = None
    expect_separator = False
    table_count = 0
    repository_count = 0

    for original_line in lines:
        newline = "\n" if original_line.endswith("\n") else ""
        line = original_line.rstrip("\r\n")
        cells = parse_markdown_row(line)

        header = parse_managed_table_header(cells) if cells else None
        if header:
            locale = header.locale
            output.append(
                render_markdown_row((*locale.base_headers, *locale.metadata_headers)) + newline
            )
            current_header = header
            expect_separator = True
            table_count += 1
            continue

        if current_header and expect_separator:
            if not is_separator_row(cells, current_header.source_column_count):
                raise ValueError("Project table header is not followed by a valid separator row")
            locale = current_header.locale
            output.append(
                render_markdown_row(
                    ["---"] * (len(locale.base_headers) + len(locale.metadata_headers))
                )
                + newline
            )
            expect_separator = False
            continue

        if current_header:
            if not cells:
                current_header = None
            else:
                locale = current_header.locale
                base_count = len(locale.base_headers)
                metadata_count = len(locale.metadata_headers)
                source_metadata_count = current_header.source_column_count - base_count
                repository = parse_github_repository(line)
                if repository:
                    if len(cells) not in (
                        base_count,
                        current_header.source_column_count,
                    ):
                        raise ValueError(f"Unexpected project table row: {line}")
                    metadata = metadata_by_repository.get(repository)
                    base_cells = list(cells[:base_count])

                    if (
                        metadata
                        and metadata.status is RepositoryStatus.MOVED
                        and metadata.new_full_name
                    ):
                        base_cells = [
                            replace_repository_url(c, repository, metadata.new_full_name)
                            for c in base_cells
                        ]

                    if metadata and metadata.status in (
                        RepositoryStatus.ARCHIVED,
                        RepositoryStatus.REMOVED,
                    ):
                        managed_cells = deprecated_cells(metadata, locale)
                    elif metadata:
                        previous_release = (
                            cells[base_count + 2]
                            if len(cells) > base_count and source_metadata_count >= 3
                            else None
                        )
                        managed_cells = metadata_cells(
                            metadata, today, locale, previous_release
                        )
                    elif len(cells) > base_count:
                        # Transient fetch failure (rate limit / network / 5xx):
                        # keep the last good values but flag with a warning prefix
                        # so it does not read as fresh data. Skip the prefix if the
                        # previous run already added one, otherwise repeated runs
                        # accumulate "⚠️ ⚠️ ..." prefixes.
                        previous = list(cells[base_count:])
                        if not previous[0].lstrip().startswith("⚠️"):
                            previous[0] = "⚠️ " + previous[0]
                        if len(previous) == len(locale.legacy_metadata_headers):
                            previous.append(locale.fetch_failed)
                        managed_cells = tuple(previous)
                    else:
                        managed_cells = (locale.fetch_failed,) * metadata_count
                    output.append(
                        render_markdown_row([*base_cells, *managed_cells]) + newline
                    )
                    repository_count += 1
                    continue

        output.append(original_line)

    if expect_separator:
        # The file ended right after a header with no separator row.
        raise ValueError("Project table header is not followed by a valid separator row")

    return "".join(output), table_count, repository_count


def repositories_in_managed_tables(content: str) -> list[tuple[str, str]]:
    repositories: list[tuple[str, str]] = []
    in_managed_table = False

    for line in content.splitlines():
        cells = parse_markdown_row(line)
        if cells and parse_managed_table_header(cells):
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


def _sanitize_summary_text(value: str) -> str:
    """Collapse newlines and replace backticks so a message survives being
    wrapped in a Markdown inline-code span (backslash escapes do not work
    inside code spans, so backticks are replaced with single quotes)."""
    return value.replace("\r", " ").replace("\n", " ").replace("`", "'")


def write_step_summary(
    *,
    moved_repos: list[tuple[str, str]],
    failures: list[str],
    release_failed_repos: list[tuple[str, str]],
    deprecated_repos: list[tuple[tuple[str, str], "RepositoryMetadata"]],
) -> None:
    """Append a structured run summary to GITHUB_STEP_SUMMARY.

    No-op when nothing happened or no summary path is configured. Write errors
    are surfaced as a warning and never raise — the README update result must
    not depend on summary writability.
    """
    summary_path = os.environ.get("GITHUB_STEP_SUMMARY")
    if not summary_path:
        return
    if not (moved_repos or failures or release_failed_repos or deprecated_repos):
        return

    sections: list[str] = ["### README repository metadata update", ""]
    if failures:
        sections.append("#### Repository fetch failures")
        for failure in failures:
            slug, _, message = failure.partition(": ")
            sections.append(
                f"- `{_sanitize_summary_text(slug)}` — `{_sanitize_summary_text(message)}`"
            )
        sections.append("")
    if release_failed_repos:
        sections.append("#### Release fetch failures")
        for owner, repo in release_failed_repos:
            sections.append(f"- `{owner}/{repo}` — previous release retained")
        sections.append("")
    if moved_repos:
        sections.append("#### Moved repositories")
        for owner, repo in moved_repos:
            sections.append(f"- `{owner}/{repo}` — repository URL rewritten")
        sections.append("")
    if deprecated_repos:
        sections.append("#### Deprecated repositories")
        for (owner, repo), metadata in deprecated_repos:
            label = (
                "archived"
                if metadata.status is RepositoryStatus.ARCHIVED
                else "removed"
            )
            sections.append(f"- `{owner}/{repo}` — {label}")
        sections.append("")

    try:
        with Path(summary_path).open("a", encoding="utf-8") as summary:
            summary.write("\n".join(sections) + "\n")
    except OSError as error:
        print(f"Warning: could not write step summary: {error}", file=sys.stderr)


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

    # Generate every README before writing any of them, so a validation
    # failure in one file cannot leave another already written to disk.
    pending_updates: dict[Path, tuple[str, int, int]] = {}
    total_table_count = 0
    total_repository_count = 0
    for readme, content in contents.items():
        updated, table_count, repository_count = update_readme(
            content,
            metadata_by_repository,
            today=args.today,
        )
        pending_updates[readme] = (updated, table_count, repository_count)
        total_table_count += table_count
        total_repository_count += repository_count

    for readme, (updated, table_count, repository_count) in pending_updates.items():
        readme.write_text(updated, encoding="utf-8")
        print(f"Updated {readme}: {repository_count} rows across {table_count} tables")

    print(
        f"Updated {total_repository_count} rows across {total_table_count} tables "
        f"in {len(readmes)} README files"
    )

    moved_repos = [
        slug
        for slug, metadata in metadata_by_repository.items()
        if metadata.status is RepositoryStatus.MOVED
    ]
    deprecated_repos = [
        (slug, metadata)
        for slug, metadata in metadata_by_repository.items()
        if metadata.status in (RepositoryStatus.ARCHIVED, RepositoryStatus.REMOVED)
    ]
    release_failed_repos = [
        slug
        for slug, metadata in metadata_by_repository.items()
        if metadata.release_fetch_failed
    ]

    # Always return 0: deprecated markers must be written AND committed so
    # reviewers see them in the README. Surfacing happens via stderr + the
    # GitHub Actions step summary, not via a failing exit code (which would
    # skip the commit step in the workflow).
    if moved_repos:
        print("Rewrote transferred repository link(s):", file=sys.stderr)
        for owner, repo in moved_repos:
            print(f"  - {owner}/{repo}", file=sys.stderr)

    if failures:
        print(
            f"Completed with {len(failures)} transient fetch failure(s):",
            file=sys.stderr,
        )
        for failure in failures:
            print(f"  - {failure}", file=sys.stderr)

    if release_failed_repos:
        print(
            f"{len(release_failed_repos)} repository(ies) had transient release "
            "fetch failures; previous release values retained:",
            file=sys.stderr,
        )
        for owner, repo in release_failed_repos:
            print(f"  - {owner}/{repo}", file=sys.stderr)

    if deprecated_repos:
        print(
            f"Flagged {len(deprecated_repos)} deprecated repository(ies); "
            "markers written to README, please review and prune:",
            file=sys.stderr,
        )
        for (owner, repo), metadata in deprecated_repos:
            label = (
                "archived"
                if metadata.status is RepositoryStatus.ARCHIVED
                else "removed"
            )
            print(f"  - {owner}/{repo} ({label})", file=sys.stderr)

    write_step_summary(
        moved_repos=moved_repos,
        failures=failures,
        release_failed_repos=release_failed_repos,
        deprecated_repos=deprecated_repos,
    )

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
