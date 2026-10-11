"""Offline regressions for escaped table delimiters and bilingual updates."""
import os
import unittest
from contextlib import redirect_stderr, redirect_stdout
from dataclasses import replace
from datetime import date
from io import StringIO
from pathlib import Path
from tempfile import TemporaryDirectory
from types import SimpleNamespace
from unittest.mock import patch

from scripts.update_readme_metadata import (
    EN_LOCALE, ZH_LOCALE, RepositoryMetadata, main, parse_markdown_row,
    render_markdown_row, repositories_in_managed_tables, update_readme,
)

ROOT = Path(__file__).resolve().parents[1]
TODAY = date(2026, 10, 11)
METADATA = RepositoryMetadata(
    description="Test | description", default_branch_committed_at="2026-10-10T00:00:00Z",
    release_tag=None, release_published_at=None, release_url=None, stargazers_count=42,
)


class MarkdownRowRegressionTests(unittest.TestCase):
    def test_backslash_parity_and_content_preservation(self):
        for count in range(9):
            slashes = "\\" * count
            with self.subTest(backslashes=count):
                expected = ["a " + slashes + "| b"] if count % 2 else [("a " + slashes).strip(), "b"]
                self.assertEqual(parse_markdown_row("| a " + slashes + "| b |"), expected)

    def test_backslash_count_resets_after_other_characters(self):
        self.assertEqual(parse_markdown_row(r"| a\x| b\|c| d |"), [r"a\x", r"b\|c", "d"])

    def test_empty_cells_and_whitespace(self):
        self.assertEqual(parse_markdown_row(" \t| | 中文 | |\r\n"), ["", "中文", ""])
        self.assertEqual(parse_markdown_row("||"), [""])
        self.assertEqual(parse_markdown_row("|"), [""])

    def test_missing_outer_delimiters(self):
        for row in ["", "a | b |", "| a | b", "plain"]:
            with self.subTest(row=row):
                self.assertIsNone(parse_markdown_row(row))

    def test_escaped_final_pipe_is_not_an_outer_delimiter(self):
        for count in (1, 3, 5):
            with self.subTest(backslashes=count):
                self.assertIsNone(parse_markdown_row("| a " + "\\" * count + "|"))
        for count in (0, 2, 4):
            with self.subTest(backslashes=count):
                self.assertEqual(parse_markdown_row("| a " + "\\" * count + "|"), [("a " + "\\" * count).strip()])

    def test_render_parse_roundtrip(self):
        cells = ["中文", "", r"one\|pipe", r"two\\", r"`a\|b`", "&#124;"]
        self.assertEqual(parse_markdown_row(render_markdown_row(cells)), cells)

    def test_bilingual_schema_update_and_failure_idempotence(self):
        for locale in (ZH_LOCALE, EN_LOCALE):
            for width in (4, 7, 8):
                for mode in ("success", "fetch_failure", "release_failure"):
                    with self.subTest(locale=locale.base_headers[0], width=width, mode=mode):
                        headers = (*locale.base_headers, *locale.metadata_headers)[:width]
                        base = ["[Tool](https://github.com/example/tool)", "MCP", r"分析\|调试", ""]
                        previous = [r"Old\|description", "Old activity", r"Old\|release", "10"]
                        original = "Intro\n" + render_markdown_row(headers) + "\n" + render_markdown_row(["---"] * width) + "\n" + render_markdown_row((base + previous)[:width]) + "\n\nOutro\n"
                        metadata = {} if mode == "fetch_failure" else {("example", "tool"): replace(METADATA, release_fetch_failed=mode == "release_failure")}
                        first, tables, rows = update_readme(original, metadata, today=TODAY)
                        self.assertEqual((tables, rows), (1, 1))
                        self.assertEqual(repositories_in_managed_tables(first), [("example", "tool")])
                        self.assertEqual(parse_markdown_row(first.splitlines()[3])[:4], base)
                        second, _, _ = update_readme(first, metadata, today=TODAY)
                        self.assertEqual(first, second)
                        if width > 4 and mode == "release_failure":
                            self.assertIn(r"Old\|release", first)

    def test_actual_bilingual_readmes_full_main_twice(self):
        sources = {name: (ROOT / name).read_text(encoding="utf-8") for name in ("README.md", "README_EN.md")}
        repositories = set().union(*(set(repositories_in_managed_tables(text)) for text in sources.values()))
        self.assertGreater(len(repositories), 0)
        with TemporaryDirectory() as directory:
            paths = [Path(directory) / name for name in sources]
            for path in paths:
                path.write_text(sources[path.name], encoding="utf-8")
            args = SimpleNamespace(readmes=paths, api_base="https://api.github.com", today=TODAY)
            with patch("scripts.update_readme_metadata.parse_args", return_value=args), patch("scripts.update_readme_metadata.fetch_repository_metadata", return_value=METADATA) as fetch, patch("socket.socket", side_effect=AssertionError("network forbidden")), patch.dict(os.environ, {"GITHUB_STEP_SUMMARY": ""}), redirect_stdout(StringIO()), redirect_stderr(StringIO()):
                self.assertEqual(main(), 0)
                first = [path.read_bytes() for path in paths]
                self.assertEqual(fetch.call_count, len(repositories))
                fetch.reset_mock()
                self.assertEqual(main(), 0)
                self.assertEqual(first, [path.read_bytes() for path in paths])
                self.assertEqual(fetch.call_count, len(repositories))
            for path in paths:
                original = sources[path.name]
                updated = path.read_text(encoding="utf-8")
                self.assertEqual(repositories_in_managed_tables(original), repositories_in_managed_tables(updated))
                before, after = original.splitlines(keepends=True), updated.splitlines(keepends=True)
                self.assertEqual(len(before), len(after))
                for old, new in zip(before, after):
                    if old != new:
                        old_cells, new_cells = parse_markdown_row(old), parse_markdown_row(new)
                        self.assertIsNotNone(old_cells)
                        self.assertEqual(old_cells[:4], new_cells[:4])
                        self.assertEqual(len(new_cells), 8)
