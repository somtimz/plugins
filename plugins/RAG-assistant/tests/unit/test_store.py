"""Tests for scripts/lib/store.py"""
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import List

import pytest

sys.path.insert(0, str(Path(__file__).parent.parent.parent / "scripts"))

from lib.store import (
    ModelMismatchError,
    get_or_create_collection,
    check_model_consistency,
    upsert_chunks,
    delete_by_document,
)
from lib.embedder import EmbeddedChunk


# ---------------------------------------------------------------------------
# Fixtures
# ---------------------------------------------------------------------------

@pytest.fixture
def chroma_client():
    """In-memory ChromaDB client, isolated per test."""
    import chromadb
    return chromadb.EphemeralClient()


def make_embedded_chunks(n: int = 2, model: str = "text-embedding-3-small") -> List[EmbeddedChunk]:
    """Return a list of n deterministic EmbeddedChunk objects."""
    return [
        EmbeddedChunk(
            chunk_id=f"doc.txt::chunk::{i}",
            text=f"This is the text of chunk number {i}.",
            vector=[0.1 * (i + 1), 0.2 * (i + 1), 0.3 * (i + 1)],
            model=model,
        )
        for i in range(n)
    ]


# ---------------------------------------------------------------------------
# get_or_create_collection
# ---------------------------------------------------------------------------

class TestGetOrCreateCollection:
    def test_creates_new_collection_when_absent(self, chroma_client):
        col = get_or_create_collection(chroma_client, "my-col", "text-embedding-3-small")
        assert col is not None
        assert col.name == "my-col"

    def test_stores_embedding_model_metadata_on_new_collection(self, chroma_client):
        model = "text-embedding-3-small"
        col = get_or_create_collection(chroma_client, "meta-col", model)
        metadata = col.metadata or {}
        assert metadata.get("embedding_model") == model

    def test_returns_existing_collection_on_second_call(self, chroma_client):
        col1 = get_or_create_collection(chroma_client, "shared-col", "text-embedding-3-small")
        col2 = get_or_create_collection(chroma_client, "shared-col", "text-embedding-3-small")
        assert col1.name == col2.name


# ---------------------------------------------------------------------------
# check_model_consistency
# ---------------------------------------------------------------------------

class TestCheckModelConsistency:
    def test_no_error_when_collection_is_new_no_metadata(self, chroma_client):
        """A brand-new collection with no stored model should not raise."""
        # Create via raw chromadb (no model metadata) to simulate absence
        import chromadb
        col = chroma_client.create_collection("raw-col")
        # Should not raise
        check_model_consistency(col, "text-embedding-3-small")

    def test_no_error_when_stored_model_matches(self, chroma_client):
        model = "text-embedding-3-small"
        col = get_or_create_collection(chroma_client, "match-col", model)
        # Should not raise
        check_model_consistency(col, model)

    def test_raises_model_mismatch_error_when_model_differs(self, chroma_client):
        col = get_or_create_collection(chroma_client, "mismatch-col", "model-A")
        with pytest.raises(ModelMismatchError):
            check_model_consistency(col, "model-B")


# ---------------------------------------------------------------------------
# upsert_chunks
# ---------------------------------------------------------------------------

class TestUpsertChunks:
    def test_upsert_adds_correct_number_of_entries(self, chroma_client):
        col = get_or_create_collection(chroma_client, "upsert-count-col", "text-embedding-3-small")
        chunks = make_embedded_chunks(n=3)
        upsert_chunks(col, chunks, source_name="docs", origin_path="/docs/a.txt", content_hash="abc123")
        assert col.count() == 3

    def test_upsert_stores_source_name_in_metadata(self, chroma_client):
        col = get_or_create_collection(chroma_client, "upsert-meta-col", "text-embedding-3-small")
        chunks = make_embedded_chunks(n=1)
        upsert_chunks(col, chunks, source_name="my-source", origin_path="/docs/b.txt", content_hash="hash42")

        results = col.get(include=["metadatas"])
        meta = results["metadatas"][0]
        assert meta["source_name"] == "my-source"

    def test_upsert_stores_origin_path_in_metadata(self, chroma_client):
        col = get_or_create_collection(chroma_client, "upsert-origin-col", "text-embedding-3-small")
        chunks = make_embedded_chunks(n=1)
        upsert_chunks(col, chunks, source_name="src", origin_path="/some/path/doc.txt", content_hash="h1")

        results = col.get(include=["metadatas"])
        assert results["metadatas"][0]["origin_path"] == "/some/path/doc.txt"

    def test_upsert_stores_content_hash_in_metadata(self, chroma_client):
        col = get_or_create_collection(chroma_client, "upsert-hash-col", "text-embedding-3-small")
        chunks = make_embedded_chunks(n=1)
        upsert_chunks(col, chunks, source_name="src", origin_path="/doc.txt", content_hash="deadbeef")

        results = col.get(include=["metadatas"])
        assert results["metadatas"][0]["content_hash"] == "deadbeef"

    def test_upsert_stores_chunk_index_in_metadata(self, chroma_client):
        col = get_or_create_collection(chroma_client, "upsert-idx-col", "text-embedding-3-small")
        chunks = make_embedded_chunks(n=2)
        upsert_chunks(col, chunks, source_name="src", origin_path="/doc.txt", content_hash="h1")

        results = col.get(include=["metadatas"])
        indices = {m["chunk_index"] for m in results["metadatas"]}
        assert indices == {0, 1}

    def test_upsert_stores_model_in_metadata(self, chroma_client):
        model = "text-embedding-3-small"
        col = get_or_create_collection(chroma_client, "upsert-model-col", model)
        chunks = make_embedded_chunks(n=1, model=model)
        upsert_chunks(col, chunks, source_name="src", origin_path="/doc.txt", content_hash="h1")

        results = col.get(include=["metadatas"])
        assert results["metadatas"][0]["model"] == model

    def test_upsert_stores_ingested_at_in_metadata(self, chroma_client):
        col = get_or_create_collection(chroma_client, "upsert-ts-col", "text-embedding-3-small")
        chunks = make_embedded_chunks(n=1)
        upsert_chunks(col, chunks, source_name="src", origin_path="/doc.txt", content_hash="h1")

        results = col.get(include=["metadatas"])
        assert "ingested_at" in results["metadatas"][0]
        # ingested_at should be a non-empty string (ISO timestamp or epoch)
        assert results["metadatas"][0]["ingested_at"]


# ---------------------------------------------------------------------------
# delete_by_document
# ---------------------------------------------------------------------------

class TestDeleteByDocument:
    def test_delete_removes_all_entries_for_given_source_and_path(self, chroma_client):
        col = get_or_create_collection(chroma_client, "delete-col", "text-embedding-3-small")
        chunks = make_embedded_chunks(n=3)
        upsert_chunks(col, chunks, source_name="src", origin_path="/doc.txt", content_hash="h1")

        delete_by_document(col, source_name="src", origin_path="/doc.txt")
        assert col.count() == 0

    def test_delete_on_nonexistent_document_does_not_raise(self, chroma_client):
        col = get_or_create_collection(chroma_client, "delete-noop-col", "text-embedding-3-small")
        # Should not raise even with no matching records
        delete_by_document(col, source_name="ghost", origin_path="/nowhere.txt")

    def test_delete_only_removes_matching_document(self, chroma_client):
        col = get_or_create_collection(chroma_client, "delete-partial-col", "text-embedding-3-small")

        chunks_a = make_embedded_chunks(n=2)
        chunks_b = [
            EmbeddedChunk(
                chunk_id="other.txt::chunk::0",
                text="Other doc chunk.",
                vector=[0.9, 0.8, 0.7],
                model="text-embedding-3-small",
            )
        ]

        upsert_chunks(col, chunks_a, source_name="src", origin_path="/a.txt", content_hash="ha")
        upsert_chunks(col, chunks_b, source_name="src", origin_path="/b.txt", content_hash="hb")

        delete_by_document(col, source_name="src", origin_path="/a.txt")

        # Only b.txt entries remain
        assert col.count() == 1
        results = col.get(include=["metadatas"])
        assert results["metadatas"][0]["origin_path"] == "/b.txt"

    def test_upsert_then_delete_leaves_zero_entries(self, chroma_client):
        col = get_or_create_collection(chroma_client, "round-trip-col", "text-embedding-3-small")
        chunks = make_embedded_chunks(n=4)

        upsert_chunks(col, chunks, source_name="src", origin_path="/round.txt", content_hash="rr")
        assert col.count() == 4

        delete_by_document(col, source_name="src", origin_path="/round.txt")
        assert col.count() == 0
