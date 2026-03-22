"""Tests for scripts/lib/sources.py (local source) — T017"""
from __future__ import annotations

import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).parent.parent.parent / "scripts"))

from lib.sources import discover_local, SourceFile


SUPPORTED = ["txt", "md", "pdf", "docx"]


class TestDiscoverLocalFile:
    def test_single_file_returns_that_file(self, tmp_path):
        f = tmp_path / "doc.txt"
        f.write_text("hello")
        results = discover_local(str(f), SUPPORTED)
        assert len(results) == 1
        assert results[0].origin_path == str(f)

    def test_single_file_has_correct_source_name(self, tmp_path):
        f = tmp_path / "doc.txt"
        f.write_text("hello")
        results = discover_local(str(f), SUPPORTED)
        assert results[0].source_name == str(f)

    def test_single_file_has_correct_size(self, tmp_path):
        f = tmp_path / "doc.txt"
        f.write_bytes(b"x" * 100)
        results = discover_local(str(f), SUPPORTED)
        assert results[0].file_size_bytes == 100

    def test_single_file_unsupported_extension_still_returned(self, tmp_path):
        # When a single file is specified directly, return it regardless of extension
        f = tmp_path / "data.csv"
        f.write_text("a,b,c")
        results = discover_local(str(f), SUPPORTED)
        assert len(results) == 1


class TestDiscoverLocalDirectory:
    def test_returns_all_matching_files(self, tmp_path):
        (tmp_path / "a.txt").write_text("a")
        (tmp_path / "b.md").write_text("b")
        (tmp_path / "c.pdf").write_bytes(b"c")
        results = discover_local(str(tmp_path), SUPPORTED)
        assert len(results) == 3

    def test_excludes_non_matching_extensions(self, tmp_path):
        (tmp_path / "a.txt").write_text("a")
        (tmp_path / "b.csv").write_text("b")
        (tmp_path / "c.py").write_text("c")
        results = discover_local(str(tmp_path), SUPPORTED)
        assert len(results) == 1
        assert results[0].origin_path.endswith("a.txt")

    def test_empty_directory_returns_empty_list(self, tmp_path):
        results = discover_local(str(tmp_path), SUPPORTED)
        assert results == []

    def test_nested_subdirectories_included(self, tmp_path):
        sub = tmp_path / "sub"
        sub.mkdir()
        (tmp_path / "top.txt").write_text("top")
        (sub / "nested.md").write_text("nested")
        results = discover_local(str(tmp_path), SUPPORTED)
        paths = {r.origin_path for r in results}
        assert str(tmp_path / "top.txt") in paths
        assert str(sub / "nested.md") in paths
        assert len(results) == 2

    def test_source_name_is_file_path(self, tmp_path):
        f = tmp_path / "doc.txt"
        f.write_text("x")
        results = discover_local(str(tmp_path), SUPPORTED)
        assert results[0].source_name == str(f)

    def test_file_size_bytes_matches_actual(self, tmp_path):
        f = tmp_path / "doc.txt"
        f.write_bytes(b"0" * 512)
        results = discover_local(str(tmp_path), SUPPORTED)
        assert results[0].file_size_bytes == 512

    def test_deeply_nested_files_included(self, tmp_path):
        deep = tmp_path / "a" / "b" / "c"
        deep.mkdir(parents=True)
        (deep / "deep.docx").write_bytes(b"d")
        results = discover_local(str(tmp_path), SUPPORTED)
        assert len(results) == 1
        assert results[0].origin_path.endswith("deep.docx")


class TestSourceFileDataclass:
    def test_source_file_has_required_fields(self, tmp_path):
        f = tmp_path / "x.txt"
        f.write_text("x")
        sf = SourceFile(origin_path=str(f), source_name="my-source", file_size_bytes=1)
        assert sf.origin_path == str(f)
        assert sf.source_name == "my-source"
        assert sf.file_size_bytes == 1
