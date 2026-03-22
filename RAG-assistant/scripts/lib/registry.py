"""SQLite document registry for the RAG ingestion pipeline — T021

The registry tracks every ingested document: its content hash, chunk count,
number of versions ingested, and timestamp of last ingestion.  It is used by
the incremental logic in ingest.py to detect unchanged and modified documents.

Schema
------
Table: documents
    source_name   TEXT  — logical source identifier (from [[sources]] config)
    origin_path   TEXT  — filesystem path of the source document
    content_hash  TEXT  — MD5 hex digest of the document at last ingestion
    chunk_count   INT   — number of chunks stored in the vector store
    version_count INT   — incremented on every successful re-ingestion
    last_ingested TEXT  — ISO-8601 timestamp of last successful ingestion
    PRIMARY KEY (source_name, origin_path)
"""
from __future__ import annotations

import datetime
import sqlite3
from dataclasses import dataclass, field
from typing import Optional


# ---------------------------------------------------------------------------
# Data classes
# ---------------------------------------------------------------------------

@dataclass
class DocumentRecord:
    source_name: str
    origin_path: str
    content_hash: str
    chunk_count: int
    version_count: int = 1
    last_ingested: str = field(
        default_factory=lambda: datetime.datetime.now(datetime.timezone.utc).isoformat()
    )


# ---------------------------------------------------------------------------
# Public API
# ---------------------------------------------------------------------------

def open_registry(path: str) -> sqlite3.Connection:
    """Open (or create) the SQLite registry at *path*.

    Pass ``':memory:'`` for an in-memory database (useful in tests).
    The connection uses ``isolation_level=None`` (autocommit disabled) so that
    callers control transactions explicitly via ``BEGIN`` / ``COMMIT`` /
    ``ROLLBACK``.
    """
    conn = sqlite3.connect(path)
    conn.row_factory = sqlite3.Row
    # Enable WAL for better concurrent read performance.
    conn.execute("PRAGMA journal_mode=WAL")
    return conn


def create_schema(conn: sqlite3.Connection) -> None:
    """Create the ``documents`` table if it does not already exist (idempotent)."""
    conn.execute(
        """
        CREATE TABLE IF NOT EXISTS documents (
            source_name   TEXT NOT NULL,
            origin_path   TEXT NOT NULL,
            content_hash  TEXT NOT NULL,
            chunk_count   INTEGER NOT NULL,
            version_count INTEGER NOT NULL DEFAULT 1,
            last_ingested TEXT NOT NULL,
            PRIMARY KEY (source_name, origin_path)
        )
        """
    )
    conn.commit()


def lookup(
    conn: sqlite3.Connection,
    source_name: str,
    origin_path: str,
) -> Optional[DocumentRecord]:
    """Return the registry row for *(source_name, origin_path)*, or ``None``."""
    row = conn.execute(
        """
        SELECT source_name, origin_path, content_hash, chunk_count,
               version_count, last_ingested
        FROM documents
        WHERE source_name = ? AND origin_path = ?
        """,
        (source_name, origin_path),
    ).fetchone()

    if row is None:
        return None

    return DocumentRecord(
        source_name=row["source_name"],
        origin_path=row["origin_path"],
        content_hash=row["content_hash"],
        chunk_count=row["chunk_count"],
        version_count=row["version_count"],
        last_ingested=row["last_ingested"],
    )


def insert(conn: sqlite3.Connection, record: DocumentRecord) -> None:
    """Insert *record* into the registry.

    Does **not** commit — the caller controls the transaction so that the
    registry write and the vector store write can be made atomic together.
    Call ``conn.commit()`` after a successful vector store upsert, or
    ``conn.rollback()`` to discard on failure.
    """
    conn.execute(
        """
        INSERT INTO documents
            (source_name, origin_path, content_hash, chunk_count, version_count, last_ingested)
        VALUES (?, ?, ?, ?, ?, ?)
        """,
        (
            record.source_name,
            record.origin_path,
            record.content_hash,
            record.chunk_count,
            record.version_count,
            record.last_ingested,
        ),
    )


def update(
    conn: sqlite3.Connection,
    source_name: str,
    origin_path: str,
    content_hash: str,
    chunk_count: int,
) -> None:
    """Increment ``version_count`` and update hash/chunk_count/timestamp for the row.

    Does **not** commit — same transaction semantics as :func:`insert`.
    """
    now = datetime.datetime.now(datetime.timezone.utc).isoformat()
    conn.execute(
        """
        UPDATE documents
        SET content_hash  = ?,
            chunk_count   = ?,
            version_count = version_count + 1,
            last_ingested = ?
        WHERE source_name = ? AND origin_path = ?
        """,
        (content_hash, chunk_count, now, source_name, origin_path),
    )


# ---------------------------------------------------------------------------
# Within-run deduplication
# ---------------------------------------------------------------------------

class RunDedupSet:
    """Tracks content hashes already processed in the current pipeline run.

    If two different source files have the same content hash, only the first
    is embedded; subsequent occurrences are skipped as duplicates.
    """

    def __init__(self) -> None:
        self._seen: set[str] = set()

    def seen(self, content_hash: str) -> bool:
        """Return ``True`` if *content_hash* was already marked in this run."""
        return content_hash in self._seen

    def mark(self, content_hash: str) -> None:
        """Record *content_hash* as processed."""
        self._seen.add(content_hash)
