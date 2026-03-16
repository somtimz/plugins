"""Text chunker for the RAG ingestion pipeline."""
from dataclasses import dataclass
import math


@dataclass
class Chunk:
    chunk_id: str
    chunk_index: int
    text: str
    char_start: int
    char_end: int


def chunk_text(
    text: str,
    chunk_size: int,
    chunk_overlap: int,
    source_path: str,
) -> list[Chunk]:
    """Split *text* into overlapping chunks using a sliding window.

    Parameters
    ----------
    text:
        The full document text to split.
    chunk_size:
        Maximum number of characters per chunk.
    chunk_overlap:
        Number of characters shared between consecutive chunks.
    source_path:
        Identifier embedded in each ``chunk_id`` (typically the file path).

    Returns
    -------
    list[Chunk]
        Ordered list of Chunk objects.

    Raises
    ------
    ValueError
        If *text* is an empty string.
    """
    if text == "":
        raise ValueError("Cannot chunk empty text")

    step = chunk_size - chunk_overlap
    chunks: list[Chunk] = []
    index = 0
    start = 0

    while start < len(text):
        end = min(start + chunk_size, len(text))
        chunks.append(
            Chunk(
                chunk_id=f"{source_path}::chunk::{index}",
                chunk_index=index,
                text=text[start:end],
                char_start=start,
                char_end=end,
            )
        )
        index += 1
        if end == len(text):
            # Reached the end of the text; no further chunks needed.
            break
        start += step

    return chunks
