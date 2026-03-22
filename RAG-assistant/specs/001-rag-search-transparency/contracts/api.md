# API Contract: Transparent RAG Search

**Branch**: `001-rag-search-transparency` | **Date**: 2026-03-18
**Base URL**: `http://localhost:7842`

This document covers the new and modified SSE events added by feature 001 to the existing `POST /api/chat` endpoint (defined in feature 003's `specs/003-conversational-rag-ui/contracts/api.md`). No new HTTP endpoints are added.

---

## Modified Endpoint: `POST /api/chat`

The request format is unchanged. Two new SSE event types are added to the response stream.

### New Event: `chunks`

Emitted after `search_knowledge_base` tool execution completes. Contains full metadata for each retrieved chunk. Emitted **before** any `text_delta` events for the answer.

```json
{
  "event": "chunks",
  "chunks": [
    {
      "number": 1,
      "source_name": "hr-docs",
      "origin_path": "./docs/onboarding.pdf",
      "similarity_score": 0.892,
      "excerpt": "The onboarding policy requires all new employees to complete orientation within their first week...",
      "full_text": "The onboarding policy requires all new employees to complete orientation within their first week. This includes meeting with their manager, completing IT setup, and reviewing the employee handbook. Remote employees should schedule a virtual orientation session..."
    },
    {
      "number": 2,
      "source_name": "hr-docs",
      "origin_path": "./docs/remote-work-policy.docx",
      "similarity_score": 0.847,
      "excerpt": "Remote work arrangements are available to all full-time employees after completing their probation...",
      "full_text": "Remote work arrangements are available to all full-time employees after completing their probationary period..."
    }
  ]
}
```

| Field | Type | Description |
|-------|------|-------------|
| chunks | array | Up to 5 chunk objects, ordered by descending similarity_score |
| chunks[].number | int | 1-indexed position, matches inline citation numbers in answer |
| chunks[].source_name | string | Source name from document registry metadata |
| chunks[].origin_path | string | Original file path from document registry metadata |
| chunks[].similarity_score | float | Similarity score rounded to 3 decimal places |
| chunks[].excerpt | string | First 300 characters of chunk text |
| chunks[].full_text | string | Complete chunk text |

**Empty results**: If no chunks are found, `chunks` is an empty array `[]`. The frontend should display a "No relevant content found" message.

### New Event: `augmented_prompt`

Emitted once per query, after `chunks` and before `text_delta` events. Contains the exact text sent to the LLM.

```json
{
  "event": "augmented_prompt",
  "prompt": "You are a knowledge base assistant. Answer questions using ONLY the provided context chunks below.\nRules:\n- Cite your sources using numbered inline citations like [1], [2] that match the chunk numbers.\n- If the context does not contain enough information to answer, say so explicitly.\n- Do not fabricate information not present in the context.\n\nContext:\n\n[1] (hr-docs — ./docs/onboarding.pdf):\nThe onboarding policy requires all new employees...\n\n[2] (hr-docs — ./docs/remote-work-policy.docx):\nRemote work arrangements are available...\n\nQuestion: What does the onboarding policy say about remote work?"
}
```

| Field | Type | Description |
|-------|------|-------------|
| prompt | string | The complete augmented prompt text, verbatim as submitted to the LLM |

### Modified Event Sequence

With transparency features, the SSE event sequence for a search query becomes:

```
tool_start (name: search_knowledge_base)
tool_result (name: search_knowledge_base)
citations (sources: [...])          ← existing, retained for compatibility
chunks (chunks: [...])              ← NEW: full chunk metadata
augmented_prompt (prompt: "...")     ← NEW: exact prompt text
text_delta (text: "According to")   ← answer streaming begins
text_delta (text: " [1], the...")
...
done
```

### Edge Case: Empty Knowledge Base (FR-008)

When the knowledge base has no documents, the stream short-circuits:

```
error (message: "No documents in knowledge base. Please ingest documents first using the Ingestion tab or by typing 'ingest ./path' in chat.")
done
```

No `tool_start`, `chunks`, `augmented_prompt`, or `text_delta` events are emitted. No embedding or LLM API calls are made.

### Edge Case: No Relevant Chunks Found (FR-007)

When search returns zero results:

```
tool_start (name: search_knowledge_base)
tool_result (name: search_knowledge_base)
chunks (chunks: [])
done
```

No `augmented_prompt` or `text_delta` events. The frontend displays "No relevant content found."

---

## Unchanged

- `GET /api/chat/preflight` — no changes
- Request body format for `POST /api/chat` — no changes
- All existing SSE events (`text_delta`, `tool_start`, `tool_result`, `citations`, `error`, `done`) — retained unchanged
- HTTP status codes (200, 400, 422) — unchanged
