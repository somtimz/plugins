# Data Model: Transparent RAG Search

**Branch**: `001-rag-search-transparency` | **Date**: 2026-03-18

## Entities

### RetrievedChunk (existing — `lib/searcher.py`)

Already defined in feature 003. No schema changes needed.

| Field | Type | Description |
|-------|------|-------------|
| chunk_id | str | ChromaDB document ID |
| text | str | Full chunk text |
| source_name | str | Source name from metadata |
| origin_path | str | Original file path from metadata |
| similarity_score | float | 1.0 - distance (higher = more similar) |

### ChunkDisplay (new — SSE payload only)

Derived from `RetrievedChunk` for the `chunks` SSE event. Not a stored entity.

| Field | Type | Description |
|-------|------|-------------|
| number | int | 1-indexed display position (matches citation numbers) |
| source_name | str | From RetrievedChunk.source_name |
| origin_path | str | From RetrievedChunk.origin_path |
| similarity_score | float | Rounded to 3 decimal places for display |
| excerpt | str | First 300 characters of chunk text |
| full_text | str | Complete chunk text (for "Show full text" toggle) |

### AugmentedPrompt (new — transient)

Constructed per-query, never persisted. Assembled in `execute_search_knowledge_base()`.

| Component | Description |
|-----------|-------------|
| system_instruction | Hardcoded `RAG_SYSTEM_INSTRUCTION` constant |
| context_block | Numbered entries: `[N] (source — path):\n{text}` |
| user_question | Original user query prefixed with `Question: ` |

**Serialization**: Single concatenated string. Sent as `augmented_prompt` SSE event payload and displayed verbatim in the Inspect Prompt panel.

## Relationships

```
User Query
    │
    ├── embed_query() → QueryEmbedding (vector)
    │
    ├── search_similar() → list[RetrievedChunk] (up to 5)
    │       │
    │       ├── → list[ChunkDisplay] (SSE: chunks event)
    │       │
    │       └── → AugmentedPrompt (SSE: augmented_prompt event)
    │               │
    │               └── → Claude API → GroundedAnswer (SSE: text_delta events)
    │
    └── (if KB empty) → Error message (no API calls)
```

## No Schema Migrations

This feature adds no new database tables or ChromaDB collection fields. All new data structures are transient (computed per-request, emitted via SSE, rendered in the browser).
