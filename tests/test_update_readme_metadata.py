import unittest
from datetime import date
from pathlib import Path
from tempfile import TemporaryDirectory
from types import SimpleNamespace
from unittest.mock import patch

from scripts.update_readme_metadata import (
    EN_LOCALE,
    GitHubAPIError,
    RepositoryMetadata,
    fetch_repository_metadata,
    main,
    metadata_cells,
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

    def test_preserves_previous_values_after_fetch_failure(self):
        original = """| 项目 | 形态 | 核心定位 | 适用场景 | GitHub 简介 | 最近更新 | 最新 Release |
| --- | --- | --- | --- | --- | --- | --- |
| [Tool](https://github.com/example/tool) | MCP | 人工定位 | 人工场景 | Old description | 否 · 2020-01-01 | 暂无 |
"""
        updated, _, _ = update_readme(original, {}, today=date(2026, 7, 13))
        self.assertEqual(original, updated)

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


if __name__ == "__main__":
    unittest.main()
