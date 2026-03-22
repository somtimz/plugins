"""Tests for scripts/lib/registry.py — T020"""
from __future__ import annotations

import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).parent.parent.parent / "scripts"))

from lib.registry import (
    open_registry,
    create_schema,
    lookup,
    insert,
    update,
    DocumentRecord,
    RunDedupSet,
)


@pytest.fixture
def conn():
    """In-memory registry for each test."""
    c = open_registry(":memory:")
    create_schema(c)
    yield c
    c.close()


def _insert(conn, record):
    """Insert and commit (normal non-atomic path)."""
    insert(conn, record)
    conn.commit()


def _update(conn, source_name, origin_path, content_hash, chunk_count):
    """Update and commit."""
    update(conn, source_name, origin_path, content_hash, chunk_count)
    conn.commit()


class TestLookup:
    def test_returns_none_for_new_doc(self, conn):
        assert lookup(conn, "src", "/path/to/doc.txt") is None

    def test_returns_record_after_insert(self, conn):
        record = DocumentRecord(
            source_name="src",
            origin_path="/doc.txt",
            content_hash="abc123",
            chunk_count=5,
        )
        _insert(conn, record)
        found = lookup(conn, "src", "/doc.txt")
        assert found is not None
        assert found.content_hash == "abc123"
        assert found.chunk_count == 5

    def test_different_source_name_returns_none(self, conn):
        record = DocumentRecord(
            source_name="src-a",
            origin_path="/doc.txt",
            content_hash="abc",
            chunk_count=1,
        )
        _insert(conn, record)
        assert lookup(conn, "src-b", "/doc.txt") is None

    def test_different_path_returns_none(self, conn):
        record = DocumentRecord(
            source_name="src",
            origin_path="/doc-a.txt",
            content_hash="abc",
            chunk_count=1,
        )
        _insert(conn, record)
        assert lookup(conn, "src", "/doc-b.txt") is None


class TestInsert:
    def test_insert_creates_row_with_correct_fields(self, conn):
        record = DocumentRecord(
            source_name="my-source",
            origin_path="/data/file.md",
            content_hash="deadbeef",
            chunk_count=3,
        )
        _insert(conn, record)
        row = lookup(conn, "my-source", "/data/file.md")
        assert row.source_name == "my-source"
        assert row.origin_path == "/data/file.md"
        assert row.content_hash == "deadbeef"
        assert row.chunk_count == 3

    def test_insert_sets_version_count_to_one(self, conn):
        record = DocumentRecord(
            source_name="s", origin_path="/f.txt", content_hash="h", chunk_count=1
        )
        _insert(conn, record)
        row = lookup(conn, "s", "/f.txt")
        assert row.version_count == 1

    def test_insert_sets_last_ingested(self, conn):
        record = DocumentRecord(
            source_name="s", origin_path="/f.txt", content_hash="h", chunk_count=1
        )
        _insert(conn, record)
        row = lookup(conn, "s", "/f.txt")
        assert row.last_ingested is not None
        assert len(row.last_ingested) > 0


class TestUpdate:
    def test_update_increments_version_count(self, conn):
        record = DocumentRecord(
            source_name="s", origin_path="/f.txt", content_hash="old", chunk_count=2
        )
        _insert(conn, record)
        _update(conn, "s", "/f.txt", "new", 4)
        row = lookup(conn, "s", "/f.txt")
        assert row.version_count == 2

    def test_update_changes_content_hash(self, conn):
        record = DocumentRecord(
            source_name="s", origin_path="/f.txt", content_hash="old", chunk_count=2
        )
        _insert(conn, record)
        _update(conn, "s", "/f.txt", "new", 4)
        row = lookup(conn, "s", "/f.txt")
        assert row.content_hash == "new"

    def test_update_changes_chunk_count(self, conn):
        record = DocumentRecord(
            source_name="s", origin_path="/f.txt", content_hash="old", chunk_count=2
        )
        _insert(conn, record)
        _update(conn, "s", "/f.txt", "new", 10)
        row = lookup(conn, "s", "/f.txt")
        assert row.chunk_count == 10

    def test_multiple_updates_increment_version_count(self, conn):
        record = DocumentRecord(
            source_name="s", origin_path="/f.txt", content_hash="v1", chunk_count=1
        )
        _insert(conn, record)
        _update(conn, "s", "/f.txt", "v2", 2)
        _update(conn, "s", "/f.txt", "v3", 3)
        row = lookup(conn, "s", "/f.txt")
        assert row.version_count == 3


class TestRunDedupSet:
    def test_new_hash_not_seen(self):
        dedup = RunDedupSet()
        assert not dedup.seen("abc123")

    def test_after_mark_hash_is_seen(self):
        dedup = RunDedupSet()
        dedup.mark("abc123")
        assert dedup.seen("abc123")

    def test_different_hash_not_seen(self):
        dedup = RunDedupSet()
        dedup.mark("abc")
        assert not dedup.seen("xyz")

    def test_mark_twice_still_seen(self):
        dedup = RunDedupSet()
        dedup.mark("abc")
        dedup.mark("abc")
        assert dedup.seen("abc")


class TestAtomicRollback:
    def test_registry_row_not_committed_on_exception(self, tmp_path):
        db_path = str(tmp_path / "reg.db")
        c = open_registry(db_path)
        create_schema(c)

        record = DocumentRecord(
            source_name="s", origin_path="/f.txt", content_hash="h", chunk_count=1
        )
        # insert() does NOT commit; explicit rollback discards the row
        insert(c, record)
        c.rollback()

        assert lookup(c, "s", "/f.txt") is None
        c.close()
