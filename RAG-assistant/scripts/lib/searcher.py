"""Vector similarity search wrapper — T006"""
from __future__ import annotations

from dataclasses import dataclass


@dataclass
class RetrievedChunk:
    chunk_id: str
    text: str
    source_name: str
    origin_path: str
    similarity_score: float


def search_similar(collection, query_embedding: list[float], n_results: int = 5) -> list[RetrievedChunk]:
    """Query ChromaDB and return top-N chunks sorted by similarity score (descending).

    Parameters
    ----------
    collection:
        A ChromaDB Collection object.
    query_embedding:
        The query vector to search with.
    n_results:
        Maximum number of results to return.

    Returns
    -------
    list[RetrievedChunk]
        Results sorted by similarity score descending (highest first).
        Empty list if no results found.
    """
    result = collection.query(
        query_embeddings=[query_embedding],
        n_results=n_results,
        include=["documents", "metadatas", "distances"],
    )

    ids = result.get("ids", [[]])[0]
    documents = result.get("documents", [[]])[0]
    metadatas = result.get("metadatas", [[]])[0]
    distances = result.get("distances", [[]])[0]

    chunks: list[RetrievedChunk] = []
    for chunk_id, text, meta, distance in zip(ids, documents, metadatas, distances):
        meta = meta or {}
        chunks.append(
            RetrievedChunk(
                chunk_id=chunk_id,
                text=text,
                source_name=meta.get("source_name", ""),
                origin_path=meta.get("origin_path", ""),
                similarity_score=1.0 - distance,
            )
        )

    chunks.sort(key=lambda c: c.similarity_score, reverse=True)
    return chunks
