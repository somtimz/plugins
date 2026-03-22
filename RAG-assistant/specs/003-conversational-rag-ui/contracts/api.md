# API Contract: Conversational RAG UI

**Branch**: `003-conversational-rag-ui` | **Date**: 2026-03-18
**Base URL**: `http://localhost:7842`

This document covers the two new endpoints added by feature 003. For existing endpoints (ingestion, registry, config) see `specs/002-ingestion-web-ui/contracts/api.md`.

---

## `GET /api/chat/preflight`

Check whether the LLM API key is configured and available before the user sends their first message.

### Response: `200 OK`

```json
{
  "ok": true,
  "model": "claude-sonnet-4-6"
}
```

### Response: `412 Precondition Failed`

Returned when the config is missing/invalid or the LLM API key env var is not set.

```json
{
  "ok": false,
  "reason": "Environment variable 'ANTHROPIC_API_KEY' is not set."
}
```

| Condition | Status |
|-----------|--------|
| Config valid and API key env var set | `200` |
| `.rag-plugin.toml` missing or invalid | `412` |
| `llm_key_env` env var not set | `412` |

---

## `POST /api/chat`

Submit a user message and receive a streaming SSE response. The request carries the full conversation history; the server is stateless.

### Request Body

```json
{
  "message": "What does our onboarding policy say about remote work?",
  "history": [
    {"role": "user", "content": "Hello"},
    {"role": "assistant", "content": "Hi! How can I help you?"}
  ]
}
```

| Field | Type | Required | Constraints |
|-------|------|----------|-------------|
| message | string | Yes | 1–4000 characters; rejected with `400` if exceeded |
| history | array | No | List of `{role, content}` objects; server trims to last 20 entries |

### Response: `200 OK` — `text/event-stream`

The response body is a Server-Sent Events stream. Each line is `data: <JSON>\n\n`. The client must read via `fetch` + `ReadableStream` (not `EventSource`, which does not support `POST`).

#### Event: `text_delta`
Streaming text token from Claude's response.
```json
{"event": "text_delta", "text": "According to the policy"}
```

#### Event: `tool_start`
Claude has invoked a tool; server is executing it. Show spinner.
```json
{"event": "tool_start", "name": "search_knowledge_base", "id": "toolu_01abc"}
```

#### Event: `tool_result`
Tool execution complete. Result returned to Claude for continuation.
```json
{"event": "tool_result", "name": "search_knowledge_base", "result": "Found 3 relevant chunk(s):\n..."}
```

#### Event: `citations`
Emitted only after `search_knowledge_base` returns results. Maximum 5 sources.
```json
{
  "event": "citations",
  "sources": [
    {"source_name": "hr-docs", "origin_path": "./docs/onboarding.pdf"},
    {"source_name": "hr-docs", "origin_path": "./docs/remote-work-policy.docx"}
  ]
}
```

#### Event: `error`
An unhandled exception or timeout occurred. Input should be re-enabled.
```json
{"event": "error", "message": "Anthropic API timeout after 30s"}
```

#### Event: `done`
Stream complete. Always emitted in `finally`. Re-enable input and hide spinner.
```json
{"event": "done"}
```

### Response: `400 Bad Request`

Message exceeds 4,000 characters.
```json
{
  "error": "message_too_long",
  "message": "Message exceeds 4000 character limit."
}
```

### Response: `422 Unprocessable Entity`

Config is missing or invalid at request time.
```json
{
  "error": "config_invalid",
  "message": "pipeline.chunk_size must be greater than 0"
}
```

### Full Status Code Summary

| Status | Condition |
|--------|-----------|
| `200` (SSE stream) | Valid request; stream begins immediately |
| `400` | `message` exceeds 4,000 characters |
| `422` | `.rag-plugin.toml` missing or fails validation |

---

## Tool Execution Within `/api/chat`

When Claude returns a `tool_use` block, the server executes the tool synchronously within the SSE generator and appends the result as a `tool_result` message before resuming the Claude stream. The following tools are available:

| Tool | Executor | Side Effects |
|------|----------|--------------|
| `search_knowledge_base` | `execute_search_knowledge_base()` | Read-only ChromaDB query |
| `ingest_documents` | `execute_ingest_documents()` | Writes to ChromaDB + registry; acquires `_run_lock` |
| `query_registry` | `execute_query_registry()` | Read-only SQLite query |

`ingest_documents` returns an error string (not an HTTP error) if `_run_lock` is already held by a concurrent ingestion run triggered from the Ingestion tab.
