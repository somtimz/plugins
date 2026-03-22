"""ChromaDB vector store helpers for the RAG ingestion pipeline."""
import datetime
from dataclasses import dataclass

import chromadb

from lib.embedder import EmbeddedChunk


class ModelMismatchError(Exception):
    pass


def get_or_create_collection(
    client: chromadb.Client,
    collection_name: str,
    model_name: str,
) -> chromadb.Collection:
    """Return an existing collection or create a new one tagged with *model_name*.

    Parameters
    ----------
    client:
        An active :class:`chromadb.Client` instance.
    collection_name:
        Name of the collection to get or create.
    model_name:
        Embedding model name stored in collection metadata on creation.

    Returns
    -------
    chromadb.Collection
    """
    try:
        return client.get_collection(name=collection_name)
    except Exception:
        return client.create_collection(
            name=collection_name,
            metadata={"embedding_model": model_name},
        )


def check_model_consistency(
    collection: chromadb.Collection,
    model_name: str,
) -> None:
    """Raise :class:`ModelMismatchError` if the stored model differs from *model_name*.

    Parameters
    ----------
    collection:
        The ChromaDB collection to inspect.
    model_name:
        The model name currently configured for embedding.

    Raises
    ------
    ModelMismatchError
        When the collection was created with a different embedding model.
    """
    metadata = collection.metadata
    if metadata is None or "embedding_model" not in metadata:
        return  # new / untagged collection — no conflict

    stored = metadata["embedding_model"]
    if stored != model_name:
        raise ModelMismatchError(
            f"The vector store was created with model {stored!r} but the config "
            f"specifies {model_name!r}. Delete .rag-store/ and .rag-registry.db, "
            f"then re-run."
        )


def upsert_chunks(
    collection,
    embedded_chunks,
    source_name: str,
    origin_path: str,
    content_hash: str,
) -> None:
    """Insert or update *embedded_chunks* in *collection*.

    Parameters
    ----------
    collection:
        Target ChromaDB collection.
    embedded_chunks:
        Iterable of :class:`~lib.embedder.EmbeddedChunk` objects.
    source_name:
        Logical document source identifier stored in metadata.
    origin_path:
        Filesystem path of the source document stored in metadata.
    content_hash:
        Content hash of the source document stored in metadata.
    """
    ids: list[str] = []
    documents: list[str] = []
    embeddings: list[list[float]] = []
    metadatas: list[dict] = []

    ingested_at = datetime.datetime.utcnow().isoformat()

    for i, chunk in enumerate(embedded_chunks):
        ids.append(chunk.chunk_id)
        documents.append(chunk.text)
        embeddings.append(chunk.vector)
        metadatas.append(
            {
                "source_name": source_name,
                "origin_path": origin_path,
                "content_hash": content_hash,
                "chunk_index": i,
                "model": chunk.model,
                "ingested_at": ingested_at,
            }
        )

    collection.upsert(
        ids=ids,
        documents=documents,
        embeddings=embeddings,
        metadatas=metadatas,
    )


def delete_by_document(
    collection,
    source_name: str,
    origin_path: str,
) -> None:
    """Delete all chunks belonging to a specific document from *collection*.

    Parameters
    ----------
    collection:
        Target ChromaDB collection.
    source_name:
        Logical document source identifier used as a filter.
    origin_path:
        Filesystem path used as a filter.
    """
    results = collection.get(
        where={
            "$and": [
                {"source_name": {"$eq": source_name}},
                {"origin_path": {"$eq": origin_path}},
            ]
        }
    )
    if results["ids"]:
        collection.delete(ids=results["ids"])
