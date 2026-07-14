import os
import unittest
from contextlib import redirect_stderr
from datetime import date
from io import StringIO
from pathlib import Path
from tempfile import TemporaryDirectory
from types import SimpleNamespace
from unittest.mock import patch

from scripts.update_readme_metadata import (
    EN_LOCALE,
    GitHubAPIError,
    RepositoryMetadata,
    RepositoryStatus,
    fetch_repository_metadata,
    main,
    metadata_cells,
    replace_repository_url,
    repositories_in_managed_tables,
    update_readme,
)


class ReadmeUpdateTests(unittest.TestCase):
    def setUp(self):
        self.metadata = RepositoryMetadata(
            description="A tool | for reverse engineering",
            pushed_at="2026-06-01T12:00:00Z",
            release_tag="v1.2.3",
            release_published_at="2026-05-20T08:30:00Z",
            release_url="https://github.com/example/tool/releases/tag/v1.2.3",
        )

    def test_updates_only_project_tables(self):
        original = """Intro stays unchanged.

| 项目 | 形态 | 核心定位 | 适用场景 |
| --- | --- | --- | --- |
| [Tool](https://github.com/example/tool) | MCP | 人工定位 | 人工场景 |

| 需求 | 推荐项目 |
| --- | --- |
| Test | Tool |

Outro stays unchanged.
"""
        updated, table_count, repository_count = update_readme(
            original,
            {("example", "tool"): self.metadata},
            today=date(2026, 7, 13),
        )

        self.assertEqual(table_count, 1)
        self.assertEqual(repository_count, 1)
        self.assertIn("Intro stays unchanged.", updated)
        self.assertIn("Outro stays unchanged.", updated)
        self.assertIn("| Test | Tool |", updated)
        self.assertIn(
            "| 项目 | 形态 | 核心定位 | 适用场景 | GitHub 简介 | 最近更新 | 最新 Release |",
            updated,
        )
        self.assertIn("A tool &#124; for reverse engineering", updated)
        self.assertIn("是 · 2026-06-01", updated)
        self.assertIn("[v1.2.3](https://github.com/example/tool/releases/tag/v1.2.3) · 2026-05-20", updated)

    def test_second_update_is_idempotent(self):
        original = """| 项目 | 形态 | 核心定位 | 适用场景 |
| --- | --- | --- | --- |
| [Tool](https://github.com/example/tool) | MCP | 人工定位 | 人工场景 |
"""
        first, _, _ = update_readme(
            original,
            {("example", "tool"): self.metadata},
            today=date(2026, 7, 13),
        )
        second, _, _ = update_readme(
            first,
            {("example", "tool"): self.metadata},
            today=date(2026, 7, 13),
        )
        self.assertEqual(first, second)

    def test_transfetch_failure_keeps_previous_values_with_warning(self):
        original = """| 项目 | 形态 | 核心定位 | 适用场景 | GitHub 简介 | 最近更新 | 最新 Release |
| --- | --- | --- | --- | --- | --- | --- |
| [Tool](https://github.com/example/tool) | MCP | 人工定位 | 人工场景 | Old description | 否 · 2020-01-01 | 暂无 |
"""
        updated, _, _ = update_readme(original, {}, today=date(2026, 7, 13))
        # Transient fetch failure (no metadata) keeps the last good values but
        # flags the description cell with a warning prefix.
        self.assertIn("⚠️ Old description", updated)
        self.assertIn("否 · 2020-01-01", updated)

    def test_transfetch_failure_prefix_does_not_accumulate(self):
        # Running the updater twice on a transiently-failing row must not stack
        # "⚠️ ⚠️ ..." prefixes on the description cell.
        once = """| 项目 | 形态 | 核心定位 | 适用场景 | GitHub 简介 | 最近更新 | 最新 Release |
| --- | --- | --- | --- | --- | --- | --- |
| [Tool](https://github.com/example/tool) | MCP | 人工定位 | 人工场景 | Old description | 否 · 2020-01-01 | 暂无 |
"""
        first, _, _ = update_readme(once, {}, today=date(2026, 7, 13))
        second, _, _ = update_readme(first, {}, today=date(2026, 7, 13))
        self.assertEqual(second.count("⚠️"), 1)
        self.assertIn("⚠️ Old description", second)

    def test_fetch_failure_without_previous_values_is_localized(self):
        original = """| 项目 | 形态 | 核心定位 | 适用场景 |
| --- | --- | --- | --- |
| [Tool](https://github.com/example/tool) | MCP | 人工定位 | 人工场景 |
"""
        updated, _, _ = update_readme(original, {}, today=date(2026, 7, 13))
        self.assertIn("获取失败", updated)

    def test_marks_repository_inactive_after_ninety_days(self):
        metadata = RepositoryMetadata(
            description="Tool",
            pushed_at="2026-04-13T00:00:00Z",
            release_tag=None,
            release_published_at=None,
            release_url=None,
        )
        _, activity, release = metadata_cells(metadata, date(2026, 7, 13))
        self.assertEqual(activity, "否 · 2026-04-13")
        self.assertEqual(release, "暂无")

    def test_discovers_only_repositories_in_project_tables(self):
        content = """[Outside](https://github.com/outside/repo)

| 项目 | 形态 | 核心定位 | 适用场景 |
| --- | --- | --- | --- |
| [Tool](https://github.com/example/tool/) | MCP | 定位 | 场景 |
"""
        self.assertEqual(repositories_in_managed_tables(content), [("example", "tool")])

    def test_updates_english_project_tables_with_english_statuses(self):
        original = """| Project | Type | Core Focus | Best For |
| --- | --- | --- | --- |
| [Tool](https://github.com/example/tool) | MCP | Analysis | Debugging |
"""
        updated, table_count, repository_count = update_readme(
            original,
            {("example", "tool"): self.metadata},
            today=date(2026, 7, 13),
        )

        self.assertEqual(table_count, 1)
        self.assertEqual(repository_count, 1)
        self.assertIn(
            "| Project | Type | Core Focus | Best For | GitHub Description | Recently Updated | Latest Release |",
            updated,
        )
        self.assertIn("Yes · 2026-06-01", updated)

    def test_english_empty_metadata_values_are_localized(self):
        metadata = RepositoryMetadata(
            description="",
            pushed_at="2026-07-01T00:00:00Z",
            release_tag=None,
            release_published_at=None,
            release_url=None,
        )
        description, _, release = metadata_cells(metadata, date(2026, 7, 13), EN_LOCALE)
        self.assertEqual(description, "No description")
        self.assertEqual(release, "None")

    def test_archived_repository_is_marked_deprecated(self):
        metadata = RepositoryMetadata(
            description="A archived tool",
            pushed_at="2026-06-01T12:00:00Z",
            release_tag="v1.2.3",
            release_published_at="2026-05-20T08:30:00Z",
            release_url="https://github.com/example/tool/releases/tag/v1.2.3",
            status=RepositoryStatus.ARCHIVED,
        )
        original = """| 项目 | 形态 | 核心定位 | 适用场景 | GitHub 简介 | 最近更新 | 最新 Release |
| --- | --- | --- | --- | --- | --- | --- |
| [Tool](https://github.com/example/tool) | MCP | 人工定位 | 人工场景 | Old description | 否 · 2020-01-01 | 暂无 |
"""
        updated, _, _ = update_readme(
            original, {("example", "tool"): metadata}, today=date(2026, 7, 13)
        )
        self.assertIn("🗄️ 已废弃", updated)
        self.assertIn("| 已废弃 | 暂无 |", updated)
        self.assertNotIn("Old description", updated)
        self.assertNotIn("2020-01-01", updated)

    def test_removed_repository_is_marked_deprecated(self):
        metadata = RepositoryMetadata(
            description="",
            pushed_at="",
            release_tag=None,
            release_published_at=None,
            release_url=None,
            status=RepositoryStatus.REMOVED,
        )
        original = """| 项目 | 形态 | 核心定位 | 适用场景 | GitHub 简介 | 最近更新 | 最新 Release |
| --- | --- | --- | --- | --- | --- | --- |
| [Tool](https://github.com/example/tool) | MCP | 人工定位 | 人工场景 | Old description | 否 · 2020-01-01 | 暂无 |
"""
        updated, _, _ = update_readme(
            original, {("example", "tool"): metadata}, today=date(2026, 7, 13)
        )
        self.assertIn("🗄️ 已废弃", updated)
        self.assertNotIn("Old description", updated)

    def test_moved_repository_link_is_rewritten(self):
        metadata = RepositoryMetadata(
            description="A moved tool",
            pushed_at="2026-06-01T12:00:00Z",
            release_tag=None,
            release_published_at=None,
            release_url=None,
            status=RepositoryStatus.MOVED,
            new_full_name="newowner/tool",
        )
        original = """| 项目 | 形态 | 核心定位 | 适用场景 |
| --- | --- | --- | --- |
| [Tool](https://github.com/example/tool) | MCP | 人工定位 | 人工场景 |
"""
        updated, _, _ = update_readme(
            original, {("example", "tool"): metadata}, today=date(2026, 7, 13)
        )
        self.assertIn("https://github.com/newowner/tool", updated)
        self.assertNotIn("https://github.com/example/tool", updated)
        self.assertIn("A moved tool", updated)

    def test_replace_repository_url_handles_cell(self):
        cell = "[Tool](https://github.com/example/tool)"
        result = replace_repository_url(cell, ("example", "tool"), "newowner/tool")
        self.assertEqual(result, "[Tool](https://github.com/newowner/tool)")

    def test_archived_takes_precedence_over_moved(self):
        metadata = RepositoryMetadata(
            description="",
            pushed_at="2026-06-01T12:00:00Z",
            release_tag=None,
            release_published_at=None,
            release_url=None,
            status=RepositoryStatus.ARCHIVED,
            new_full_name="newowner/tool",
        )
        original = """| 项目 | 形态 | 核心定位 | 适用场景 |
| --- | --- | --- | --- |
| [Tool](https://github.com/example/tool) | MCP | 人工定位 | 人工场景 |
"""
        updated, _, _ = update_readme(
            original, {("example", "tool"): metadata}, today=date(2026, 7, 13)
        )
        # Archived wins over moved: no link rewrite, deprecated marker shown.
        self.assertIn("🗄️ 已废弃", updated)
        self.assertNotIn("newowner", updated)


class MultiReadmeUpdateTests(unittest.TestCase):
    @patch("scripts.update_readme_metadata.fetch_repository_metadata")
    @patch("scripts.update_readme_metadata.parse_args")
    def test_main_updates_multiple_readmes_and_fetches_each_repository_once(
        self, parse_args_mock, fetch_metadata_mock
    ):
        fetch_metadata_mock.return_value = RepositoryMetadata(
            description="Description",
            pushed_at="2026-07-01T00:00:00Z",
            release_tag=None,
            release_published_at=None,
            release_url=None,
        )

        with TemporaryDirectory() as directory:
            chinese_readme = Path(directory) / "README.md"
            english_readme = Path(directory) / "README_EN.md"
            chinese_readme.write_text(
                """| 项目 | 形态 | 核心定位 | 适用场景 |
| --- | --- | --- | --- |
| [Shared](https://github.com/example/shared) | MCP | 定位 | 场景 |
| [Chinese](https://github.com/example/chinese) | MCP | 定位 | 场景 |
""",
                encoding="utf-8",
            )
            english_readme.write_text(
                """| Project | Type | Core Focus | Best For |
| --- | --- | --- | --- |
| [Shared](https://github.com/example/shared) | MCP | Focus | Usage |
| [English](https://github.com/example/english) | MCP | Focus | Usage |
""",
                encoding="utf-8",
            )
            parse_args_mock.return_value = SimpleNamespace(
                readmes=[chinese_readme, english_readme],
                api_base="https://api.github.com",
                today=date(2026, 7, 13),
            )

            self.assertEqual(main(), 0)

            self.assertEqual(fetch_metadata_mock.call_count, 3)
            self.assertIn("是 · 2026-07-01", chinese_readme.read_text(encoding="utf-8"))
            self.assertIn("Yes · 2026-07-01", english_readme.read_text(encoding="utf-8"))

    @patch("scripts.update_readme_metadata.fetch_repository_metadata")
    @patch("scripts.update_readme_metadata.parse_args")
    def test_main_returns_zero_and_lists_deprecated_repositories(
        self, parse_args_mock, fetch_metadata_mock
    ):
        fetch_metadata_mock.return_value = RepositoryMetadata(
            description="Archived",
            pushed_at="2026-07-01T00:00:00Z",
            release_tag=None,
            release_published_at=None,
            release_url=None,
            status=RepositoryStatus.ARCHIVED,
        )
        with TemporaryDirectory() as directory:
            readme = Path(directory) / "README.md"
            readme.write_text(
                "| 项目 | 形态 | 核心定位 | 适用场景 |\n"
                "| --- | --- | --- | --- |\n"
                "| [Shared](https://github.com/example/shared) | MCP | 定位 | 场景 |\n",
                encoding="utf-8",
            )
            parse_args_mock.return_value = SimpleNamespace(
                readmes=[readme],
                api_base="https://api.github.com",
                today=date(2026, 7, 13),
            )
            with redirect_stderr(StringIO()) as err:
                code = main()
            # Must return 0 so the workflow's commit step runs and the marker
            # is actually persisted to the README.
            self.assertEqual(code, 0)
            self.assertIn("example/shared (archived)", err.getvalue())

    @patch("scripts.update_readme_metadata.fetch_repository_metadata")
    @patch("scripts.update_readme_metadata.parse_args")
    def test_main_writes_step_summary_when_deprecated(
        self, parse_args_mock, fetch_metadata_mock
    ):
        fetch_metadata_mock.return_value = RepositoryMetadata(
            description="",
            pushed_at="2026-07-01T00:00:00Z",
            release_tag=None,
            release_published_at=None,
            release_url=None,
            status=RepositoryStatus.REMOVED,
        )
        with TemporaryDirectory() as directory:
            readme = Path(directory) / "README.md"
            summary = Path(directory) / "summary.md"
            readme.write_text(
                "| 项目 | 形态 | 核心定位 | 适用场景 |\n"
                "| --- | --- | --- | --- |\n"
                "| [Shared](https://github.com/example/shared) | MCP | 定位 | 场景 |\n",
                encoding="utf-8",
            )
            parse_args_mock.return_value = SimpleNamespace(
                readmes=[readme],
                api_base="https://api.github.com",
                today=date(2026, 7, 13),
            )
            with patch.dict(os.environ, {"GITHUB_STEP_SUMMARY": str(summary)}):
                with redirect_stderr(StringIO()):
                    self.assertEqual(main(), 0)
            summary_text = summary.read_text(encoding="utf-8")
            self.assertIn("Deprecated repositories detected", summary_text)
            self.assertIn("example/shared", summary_text)
            self.assertIn("removed", summary_text)


class GitHubFetchTests(unittest.TestCase):
    @patch("scripts.update_readme_metadata.github_request")
    def test_missing_latest_release_is_not_an_error(self, request):
        request.side_effect = [
            {
                "description": "Tool",
                "full_name": "example/tool",
                "pushed_at": "2026-07-01T00:00:00Z",
            },
            GitHubAPIError("Not Found", status=404),
        ]
        metadata = fetch_repository_metadata("example", "tool")
        self.assertEqual(metadata.description, "Tool")
        self.assertIsNone(metadata.release_tag)

    @patch("scripts.update_readme_metadata.github_request")
    def test_missing_repository_is_reported_as_removed(self, request):
        request.side_effect = GitHubAPIError("Not Found", status=404)
        metadata = fetch_repository_metadata("example", "tool")
        self.assertEqual(metadata.status, RepositoryStatus.REMOVED)

    @patch("scripts.update_readme_metadata.github_request")
    def test_archived_repository_is_reported_as_archived(self, request):
        request.side_effect = [
            {
                "description": "Tool",
                "full_name": "example/tool",
                "pushed_at": "2026-07-01T00:00:00Z",
                "archived": True,
            },
            GitHubAPIError("Not Found", status=404),
        ]
        metadata = fetch_repository_metadata("example", "tool")
        self.assertEqual(metadata.status, RepositoryStatus.ARCHIVED)

    @patch("scripts.update_readme_metadata.github_request")
    def test_transferred_repository_is_reported_as_moved(self, request):
        request.side_effect = [
            {
                "description": "Tool",
                "full_name": "newowner/tool",
                "pushed_at": "2026-07-01T00:00:00Z",
                "archived": False,
            },
            GitHubAPIError("Not Found", status=404),
        ]
        metadata = fetch_repository_metadata("example", "tool")
        self.assertEqual(metadata.status, RepositoryStatus.MOVED)
        self.assertEqual(metadata.new_full_name, "newowner/tool")

    @patch("scripts.update_readme_metadata.github_request")
    def test_release_failure_keeps_archived_status(self, request):
        # Archived repos skip the release endpoint entirely (the deprecated
        # row renders "暂无" regardless), so a 5xx there must not even be
        # requested and must not pollute the archived status.
        request.side_effect = [
            {
                "description": "Tool",
                "full_name": "example/tool",
                "pushed_at": "2026-07-01T00:00:00Z",
                "archived": True,
            },
            GitHubAPIError("Server Error", status=503),
        ]
        metadata = fetch_repository_metadata("example", "tool")
        self.assertEqual(metadata.status, RepositoryStatus.ARCHIVED)
        self.assertIsNone(metadata.release_tag)
        self.assertFalse(metadata.release_fetch_failed)
        # release endpoint never queried for archived repos.
        self.assertEqual(request.call_count, 1)

    @patch("scripts.update_readme_metadata.github_request")
    def test_release_failure_keeps_moved_status(self, request):
        request.side_effect = [
            {
                "description": "Tool",
                "full_name": "newowner/tool",
                "pushed_at": "2026-07-01T00:00:00Z",
                "archived": False,
            },
            GitHubAPIError("Server Error", status=503),
        ]
        metadata = fetch_repository_metadata("example", "tool")
        self.assertEqual(metadata.status, RepositoryStatus.MOVED)
        self.assertEqual(metadata.new_full_name, "newowner/tool")
        self.assertIsNone(metadata.release_tag)
        self.assertTrue(metadata.release_fetch_failed)

    @patch("scripts.update_readme_metadata.github_request")
    def test_release_404_is_not_marked_fetch_failed(self, request):
        request.side_effect = [
            {
                "description": "Tool",
                "full_name": "example/tool",
                "pushed_at": "2026-07-01T00:00:00Z",
                "archived": False,
            },
            GitHubAPIError("Not Found", status=404),
        ]
        metadata = fetch_repository_metadata("example", "tool")
        self.assertEqual(metadata.status, RepositoryStatus.ACTIVE)
        self.assertIsNone(metadata.release_tag)
        self.assertFalse(metadata.release_fetch_failed)

    def test_release_transient_failure_preserves_previous_release(self):
        metadata = RepositoryMetadata(
            description="Tool",
            pushed_at="2026-06-01T12:00:00Z",
            release_tag=None,
            release_published_at=None,
            release_url=None,
            release_fetch_failed=True,
        )
        original = """| 项目 | 形态 | 核心定位 | 适用场景 | GitHub 简介 | 最近更新 | 最新 Release |
| --- | --- | --- | --- | --- | --- | --- |
| [Tool](https://github.com/example/tool) | MCP | 人工定位 | 人工场景 | Old description | 否 · 2020-01-01 | [v1.2.3](https://github.com/example/tool/releases/tag/v1.2.3) · 2020-05-20 |
"""
        updated, _, _ = update_readme(
            original, {("example", "tool"): metadata}, today=date(2026, 7, 13)
        )
        # Previous release value is retained verbatim, not wiped to 暂无.
        self.assertIn(
            "[v1.2.3](https://github.com/example/tool/releases/tag/v1.2.3) · 2020-05-20",
            updated,
        )
        self.assertNotIn("| 暂无 |", updated)

    def test_release_transient_failure_preserves_previous_release_idempotent(self):
        metadata = RepositoryMetadata(
            description="Tool",
            pushed_at="2026-06-01T12:00:00Z",
            release_tag=None,
            release_published_at=None,
            release_url=None,
            release_fetch_failed=True,
        )
        row = (
            "| [Tool](https://github.com/example/tool) | MCP | 人工定位 | 人工场景 | "
            "Old description | 否 · 2020-01-01 | "
            "[v1.2.3](https://github.com/example/tool/releases/tag/v1.2.3) · 2020-05-20 |"
        )
        once = (
            "| 项目 | 形态 | 核心定位 | 适用场景 | GitHub 简介 | 最近更新 | 最新 Release |\n"
            "| --- | --- | --- | --- | --- | --- | --- |\n"
            f"{row}\n"
        )
        first, _, _ = update_readme(once, {("example", "tool"): metadata}, today=date(2026, 7, 13))
        second, _, _ = update_readme(first, {("example", "tool"): metadata}, today=date(2026, 7, 13))
        # Repeated runs must not duplicate or drift the retained release cell.
        self.assertEqual(first, second)
        release_cell = (
            "[v1.2.3](https://github.com/example/tool/releases/tag/v1.2.3) · 2020-05-20"
        )
        self.assertEqual(second.count(release_cell), 1)

    def test_release_404_clears_previous_release(self):
        metadata = RepositoryMetadata(
            description="Tool",
            pushed_at="2026-06-01T12:00:00Z",
            release_tag=None,
            release_published_at=None,
            release_url=None,
            release_fetch_failed=False,
        )
        original = """| 项目 | 形态 | 核心定位 | 适用场景 | GitHub 简介 | 最近更新 | 最新 Release |
| --- | --- | --- | --- | --- | --- | --- |
| [Tool](https://github.com/example/tool) | MCP | 人工定位 | 人工场景 | Old description | 否 · 2020-01-01 | [v1.2.3](https://github.com/example/tool/releases/tag/v1.2.3) · 2020-05-20 |
"""
        updated, _, _ = update_readme(
            original, {("example", "tool"): metadata}, today=date(2026, 7, 13)
        )
        # A genuine 404 (no release) clears the stale release value.
        self.assertIn("| 暂无 |", updated)
        self.assertNotIn("v1.2.3", updated)


if __name__ == "__main__":
    unittest.main()
