"""Tool schemas and executor functions for the conversational RAG chat interface — T007"""
from __future__ import annotations

import json
import threading
from pathlib import Path

from lib.pipeline import run_ingestion
from lib.config import LocalSourceConfig
from lib.embedder import embed_query
from lib.searcher import search_similar, RetrievedChunk


# ---------------------------------------------------------------------------
# Anthropic tool schema constants
# ---------------------------------------------------------------------------

INGEST_DOCUMENTS_TOOL: dict = {
    "name": "ingest_documents",
    "description": (
        "Ingest documents from a local file system path into the knowledge base. "
        "Use this tool when the user wants to add, index, load, or ingest documents "
        "from a specific path or folder."
    ),
    "input_schema": {
        "type": "object",
        "properties": {
            "path": {
                "type": "string",
                "description": "The local file system path to ingest documents from (file or directory).",
            }
        },
        "required": ["path"],
    },
}

QUERY_REGISTRY_TOOL: dict = {
    "name": "query_registry",
    "description": (
        "Query the document registry to list ingested documents. "
        "Use this tool when the user asks what documents are available, "
        "what sources have been ingested, or wants to explore the knowledge base contents."
    ),
    "input_schema": {
        "type": "object",
        "properties": {
            "query": {
                "type": "string",
                "description": "Optional filter string to match against source_name or origin_path. Omit to return all records.",
            },
            "limit": {
                "type": "integer",
                "description": "Maximum number of records to return. Defaults to 50.",
                "default": 50,
            },
        },
        "required": [],
    },
}

SEARCH_KNOWLEDGE_BASE_TOOL: dict = {
    "name": "search_knowledge_base",
    "description": (
        "Search the knowledge base using semantic similarity to retrieve relevant document chunks. "
        "Use this tool to answer questions grounded in ingested content."
    ),
    "input_schema": {
        "type": "object",
        "properties": {
            "query": {
                "type": "string",
                "description": "The natural language query to search for.",
            },
            "n_results": {
                "type": "integer",
                "description": "Number of chunks to retrieve. Defaults to 5.",
                "default": 5,
            },
        },
        "required": ["query"],
    },
}

TOOL_SCHEMAS: list[dict] = [
    INGEST_DOCUMENTS_TOOL,
    QUERY_REGISTRY_TOOL,
    SEARCH_KNOWLEDGE_BASE_TOOL,
]


# ---------------------------------------------------------------------------
# RAG system instruction (hardcoded for v1 — FR-005)
# ---------------------------------------------------------------------------

RAG_SYSTEM_INSTRUCTION = (
    "You are a knowledge base assistant. Answer questions using ONLY the "
    "provided context chunks below.\n"
    "Rules:\n"
    "- Cite your sources using numbered inline citations like [1], [2] that "
    "match the chunk numbers.\n"
    "- If the context does not contain enough information to answer, say so "
    "explicitly.\n"
    "- Do not fabricate information not present in the context."
)


def build_augmented_prompt(query: str, chunks: list[RetrievedChunk]) -> str:
    """Assemble the full augmented prompt from system instruction, chunks, and query.

    Returns the exact string that will be shown in the "Inspect prompt" panel.
    """
    parts = [RAG_SYSTEM_INSTRUCTION, "\n\nContext:\n"]
    for i, chunk in enumerate(chunks, 1):
        parts.append(
            f"\n[{i}] ({chunk.source_name} \u2014 {chunk.origin_path}):\n"
            f"{chunk.text}\n"
        )
    parts.append(f"\nQuestion: {query}")
    return "".join(parts)


# ---------------------------------------------------------------------------
# Executor functions
# ---------------------------------------------------------------------------

def execute_ingest_documents(
    path: str,
    cfg,
    chroma_client,
    collection,
    reg_conn,
    run_lock: threading.Lock,
    logger,
) -> str:
    """Execute ingestion for the given path and return a summary string.

    Acquires *run_lock* non-blocking — returns an error string if the lock
    is already held (i.e. another run is in progress).  Releases the lock in
    a ``finally`` block so it is always freed.
    """
    p = Path(path)
    if not p.exists():
        return f"ERROR: Path does not exist: {path!r}"

    acquired = run_lock.acquire(blocking=False)
    if not acquired:
        return "ERROR: An ingestion run is already in progress. Please wait for it to finish."

    try:
        source_cfg = LocalSourceConfig(name="chat-ingest", type="local", path=str(p))
        results = run_ingestion(
            sources=[source_cfg],
            cfg=cfg,
            logger=logger,
            chroma_client=chroma_client,
            collection=collection,
            reg_conn=reg_conn,
        )

        total_discovered = sum(r.discovered for r in results)
        total_succeeded = sum(r.succeeded for r in results)
        total_skipped = sum(r.skipped for r in results)
        total_failed = sum(r.failed for r in results)

        return (
            f"Ingestion complete for {path!r}. "
            f"Discovered: {total_discovered}, "
            f"Succeeded: {total_succeeded}, "
            f"Skipped: {total_skipped}, "
            f"Failed: {total_failed}."
        )
    finally:
        run_lock.release()


def execute_query_registry(
    query: str | None,
    limit: int,
    reg_conn,
) -> str:
    """Query the document registry and return matching records as a JSON string.

    Parameters
    ----------
    query:
        Optional filter string matched against source_name and origin_path via LIKE.
    limit:
        Maximum number of records to return.
    reg_conn:
        An open sqlite3 connection to the registry database.

    Returns
    -------
    str
        JSON-encoded list of record dicts.
    """
    cursor = reg_conn.cursor()

    if query:
        pattern = f"%{query}%"
        cursor.execute(
            "SELECT source_name, origin_path, content_hash, chunk_count, "
            "version_count, last_ingested FROM documents "
            "WHERE source_name LIKE ? OR origin_path LIKE ? "
            "LIMIT ?",
            (pattern, pattern, limit),
        )
    else:
        cursor.execute(
            "SELECT source_name, origin_path, content_hash, chunk_count, "
            "version_count, last_ingested FROM documents LIMIT ?",
            (limit,),
        )

    columns = [desc[0] for desc in cursor.description]
    rows = [dict(zip(columns, row)) for row in cursor.fetchall()]
    return json.dumps(rows)


def execute_search_knowledge_base(
    query: str,
    n_results: int,
    embedding_cfg,
    collection,
) -> tuple[str, list[RetrievedChunk], str]:
    """Embed the query and search ChromaDB for relevant chunks.

    Parameters
    ----------
    query:
        Natural language query string.
    n_results:
        Number of chunks to retrieve.
    embedding_cfg:
        EmbeddingConfig-like object with api_base, embedding_key_env, model.
    collection:
        ChromaDB collection to query.

    Returns
    -------
    tuple[str, list[RetrievedChunk], str]
        (formatted_summary_string, list_of_retrieved_chunks, augmented_prompt)
    """
    query_vector = embed_query(query, embedding_cfg)
    chunks = search_similar(collection, query_vector, n_results=n_results)

    if not chunks:
        return (
            "No relevant documents found in the knowledge base for this query. "
            "Consider ingesting documents first.",
            [],
            "",
        )

    lines = [f"Found {len(chunks)} relevant chunk(s):\n"]
    for i, chunk in enumerate(chunks, 1):
        lines.append(
            f"{i}. [{chunk.source_name}] {chunk.origin_path} "
            f"(score: {chunk.similarity_score:.3f})\n{chunk.text[:200]}"
        )

    augmented_prompt = build_augmented_prompt(query, chunks)
    return "\n".join(lines), chunks, augmented_prompt
