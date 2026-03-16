"""Tests for scripts/lib/chunker.py"""
import sys
import math
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).parent.parent.parent / "scripts"))

from lib.chunker import Chunk, chunk_text


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def _make_text(n: int) -> str:
    """Return a deterministic string of exactly n characters."""
    alphabet = "abcdefghijklmnopqrstuvwxyz "
    return "".join(alphabet[i % len(alphabet)] for i in range(n))


# ---------------------------------------------------------------------------
# Chunk count
# ---------------------------------------------------------------------------

class TestChunkCount:
    def test_text_shorter_than_chunk_size_produces_one_chunk(self):
        text = _make_text(50)
        chunks = chunk_text(text, chunk_size=100, chunk_overlap=10, source_path="doc.txt")
        assert len(chunks) == 1

    def test_text_equal_to_chunk_size_produces_one_chunk(self):
        text = _make_text(100)
        chunks = chunk_text(text, chunk_size=100, chunk_overlap=10, source_path="doc.txt")
        assert len(chunks) == 1

    def test_text_longer_than_chunk_size_produces_correct_number_of_chunks(self):
        chunk_size = 100
        overlap = 20
        text = _make_text(350)
        chunks = chunk_text(text, chunk_size=chunk_size, chunk_overlap=overlap, source_path="doc.txt")
        expected = math.ceil((len(text) - overlap) / (chunk_size - overlap))
        assert len(chunks) == expected

    def test_exactly_two_chunk_sizes_minus_overlap_produces_two_chunks(self):
        chunk_size = 100
        overlap = 20
        text = _make_text(2 * chunk_size - overlap)
        chunks = chunk_text(text, chunk_size=chunk_size, chunk_overlap=overlap, source_path="doc.txt")
        assert len(chunks) == 2


# ---------------------------------------------------------------------------
# Char positions
# ---------------------------------------------------------------------------

class TestCharPositions:
    def test_first_chunk_char_start_is_zero(self):
        text = _make_text(300)
        chunks = chunk_text(text, chunk_size=100, chunk_overlap=20, source_path="doc.txt")
        assert chunks[0].char_start == 0

    def test_last_chunk_char_end_equals_len_text(self):
        text = _make_text(300)
        chunks = chunk_text(text, chunk_size=100, chunk_overlap=20, source_path="doc.txt")
        assert chunks[-1].char_end == len(text)

    def test_overlap_between_consecutive_chunks(self):
        chunk_size = 100
        overlap = 20
        text = _make_text(350)
        chunks = chunk_text(text, chunk_size=chunk_size, chunk_overlap=overlap, source_path="doc.txt")
        for i in range(len(chunks) - 1):
            actual_overlap = chunks[i].char_end - chunks[i + 1].char_start
            assert actual_overlap == overlap, (
                f"Expected overlap {overlap} between chunk {i} and {i+1}, "
                f"got {actual_overlap}"
            )

    def test_chunk_text_matches_slice_of_original(self):
        text = _make_text(300)
        chunks = chunk_text(text, chunk_size=100, chunk_overlap=20, source_path="doc.txt")
        for chunk in chunks:
            assert chunk.text == text[chunk.char_start:chunk.char_end]


# ---------------------------------------------------------------------------
# Chunk metadata
# ---------------------------------------------------------------------------

class TestChunkMetadata:
    def test_chunk_index_is_sequential_starting_at_zero(self):
        text = _make_text(350)
        chunks = chunk_text(text, chunk_size=100, chunk_overlap=20, source_path="doc.txt")
        for i, chunk in enumerate(chunks):
            assert chunk.chunk_index == i

    def test_chunk_id_follows_expected_pattern(self):
        source = "some/path/doc.txt"
        text = _make_text(350)
        chunks = chunk_text(text, chunk_size=100, chunk_overlap=20, source_path=source)
        for chunk in chunks:
            expected_id = f"{source}::chunk::{chunk.chunk_index}"
            assert chunk.chunk_id == expected_id

    def test_chunk_is_dataclass_with_required_fields(self):
        text = _make_text(150)
        chunks = chunk_text(text, chunk_size=100, chunk_overlap=10, source_path="x.txt")
        c = chunks[0]
        assert hasattr(c, "chunk_id")
        assert hasattr(c, "chunk_index")
        assert hasattr(c, "text")
        assert hasattr(c, "char_start")
        assert hasattr(c, "char_end")


# ---------------------------------------------------------------------------
# No overlap
# ---------------------------------------------------------------------------

class TestNoOverlap:
    def test_zero_overlap_produces_non_overlapping_chunks(self):
        chunk_size = 100
        text = _make_text(300)
        chunks = chunk_text(text, chunk_size=chunk_size, chunk_overlap=0, source_path="doc.txt")
        for i in range(len(chunks) - 1):
            # The end of chunk i must equal the start of chunk i+1 (no gap, no overlap)
            assert chunks[i].char_end == chunks[i + 1].char_start

    def test_zero_overlap_correct_chunk_count(self):
        chunk_size = 100
        text = _make_text(300)
        chunks = chunk_text(text, chunk_size=chunk_size, chunk_overlap=0, source_path="doc.txt")
        expected = math.ceil(len(text) / chunk_size)
        assert len(chunks) == expected


# ---------------------------------------------------------------------------
# Error cases
# ---------------------------------------------------------------------------

class TestErrorCases:
    def test_empty_string_raises_value_error(self):
        with pytest.raises(ValueError):
            chunk_text("", chunk_size=100, chunk_overlap=10, source_path="doc.txt")
