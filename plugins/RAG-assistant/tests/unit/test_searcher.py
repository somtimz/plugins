"""Tests for scripts/lib/searcher.py — T003"""
from __future__ import annotations

import sys
from pathlib import Path
from unittest.mock import MagicMock

import pytest

sys.path.insert(0, str(Path(__file__).parent.parent.parent / "scripts"))

from lib.searcher import RetrievedChunk, search_similar


def _make_collection(ids, documents, metadatas, distances):
    """Return a mock ChromaDB collection whose query() returns the given data."""
    col = MagicMock()
    col.query.return_value = {
        "ids": [ids],
        "documents": [documents],
        "metadatas": [metadatas],
        "distances": [distances],
    }
    return col


class TestRetrievedChunk:
    def test_fields_stored(self):
        chunk = RetrievedChunk(
            chunk_id="c1",
            text="hello",
            source_name="src",
            origin_path="/path/doc.pdf",
            similarity_score=0.9,
        )
        assert chunk.chunk_id == "c1"
        assert chunk.text == "hello"
        assert chunk.source_name == "src"
        assert chunk.origin_path == "/path/doc.pdf"
        assert chunk.similarity_score == pytest.approx(0.9)


class TestSearchSimilar:
    def test_empty_result(self):
        """When collection returns no results, search_similar returns empty list."""
        col = _make_collection([], [], [], [])
        result = search_similar(col, [0.1, 0.2], n_results=5)
        assert result == []

    def test_n_results_passed_to_collection(self):
        """n_results is forwarded to collection.query."""
        col = _make_collection([], [], [], [])
        search_similar(col, [0.1], n_results=3)
        col.query.assert_called_once()
        call_kwargs = col.query.call_args[1] if col.query.call_args[1] else {}
        call_args = col.query.call_args[0] if col.query.call_args[0] else ()
        # n_results can be positional or keyword
        combined = {**call_kwargs}
        if len(call_args) >= 2:
            combined.setdefault("n_results", call_args[1])
        assert combined.get("n_results") == 3

    def test_returns_retrieved_chunks(self):
        """search_similar maps ChromaDB result rows to RetrievedChunk objects."""
        ids = ["c1", "c2"]
        documents = ["text one", "text two"]
        metadatas = [
            {"source_name": "src1", "origin_path": "/a.pdf"},
            {"source_name": "src2", "origin_path": "/b.docx"},
        ]
        distances = [0.1, 0.3]
        col = _make_collection(ids, documents, metadatas, distances)

        result = search_similar(col, [0.0] * 3, n_results=2)

        assert len(result) == 2
        assert result[0].chunk_id == "c1"
        assert result[0].text == "text one"
        assert result[0].source_name == "src1"
        assert result[0].origin_path == "/a.pdf"
        # similarity_score = 1 - distance for cosine-like metric
        assert result[0].similarity_score == pytest.approx(1 - 0.1)

    def test_results_sorted_by_score_descending(self):
        """Results are returned with highest similarity first."""
        ids = ["low", "high"]
        documents = ["low doc", "high doc"]
        metadatas = [
            {"source_name": "s", "origin_path": "/low.txt"},
            {"source_name": "s", "origin_path": "/high.txt"},
        ]
        # lower distance = higher similarity
        distances = [0.8, 0.2]
        col = _make_collection(ids, documents, metadatas, distances)

        result = search_similar(col, [0.0], n_results=2)

        assert result[0].chunk_id == "high"
        assert result[1].chunk_id == "low"
        assert result[0].similarity_score > result[1].similarity_score

    def test_missing_metadata_keys_use_empty_string(self):
        """Missing source_name or origin_path in metadata defaults to empty string."""
        col = _make_collection(
            ids=["c1"],
            documents=["text"],
            metadatas=[{}],
            distances=[0.5],
        )
        result = search_similar(col, [0.0], n_results=1)
        assert result[0].source_name == ""
        assert result[0].origin_path == ""
