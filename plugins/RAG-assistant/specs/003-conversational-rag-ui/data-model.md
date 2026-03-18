# Data Model: Conversational RAG UI

**Branch**: `003-conversational-rag-ui` | **Date**: 2026-03-18

## Entities

### ConversationMessage

A single message in the conversation, as understood by the Anthropic messages API.

| Field | Type | Constraints | Notes |
|-------|------|-------------|-------|
| role | string | `"user"` or `"assistant"` | Required |
| content | string \| list | Non-empty | String for simple text; list of content blocks for tool_use/tool_result turns |

The client JS array holds `ConversationMessage[]`. The server receives this array in `POST /api/chat` and forwards it (trimmed to 20 entries) to the Anthropic API.

---

### ConversationTurn *(logical, client-side)*

One logical exchange: user message → assistant response (with optional tool calls). Composed of 2–4 `ConversationMessage` entries in the history array:

1. `{role: "user", content: "<user text>"}` — user message
2. `{role: "assistant", content: [text_block, ...tool_use_block]}` — assistant with tool calls (if any)
3. `{role: "user", content: [tool_result_block, ...]}` — tool results returned to Claude (if any)
4. `{role: "assistant", content: "<final answer text>"}` — final assistant response

---

### RetrievedChunk *(Python dataclass, `lib/searcher.py`)*

A document chunk returned by vector similarity search.

| Field | Type | Constraints | Notes |
|-------|------|-------------|-------|
| text | str | Non-empty | The chunk text (up to `chunk_size` characters) |
| source_name | str | Non-empty | Source label from `.rag-plugin.toml` |
| origin_path | str | Non-empty | Original file path at ingestion time |
| similarity_score | float | `0.0–1.0` | Cosine similarity; higher = more relevant |

---

### LlmConfig *(Python dataclass, `lib/config.py`)*

Runtime configuration for the LLM subsystem, parsed from the `[llm]` section of `.rag-plugin.toml`.

| Field | Type | Default | Notes |
|-------|------|---------|-------|
| model | str | `"claude-sonnet-4-6"` | Anthropic model ID |
| llm_key_env | str | `"ANTHROPIC_API_KEY"` | Name of env var holding the API key |

---

### Tool Schemas *(Anthropic tool_use format, `lib/ingest_tool.py`)*

Three tool schemas are included in every `POST /api/chat` call. Claude selects the appropriate tool.

#### `ingest_documents`

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| path | string | Yes | Local file system path to ingest (file or directory) |

#### `query_registry`

| Parameter | Type | Required | Default | Description |
|-----------|------|----------|---------|-------------|
| query | string | No | — | Filter string matched against `source_name` and `origin_path` via LIKE |
| limit | integer | No | 50 | Maximum records to return |

#### `search_knowledge_base`

| Parameter | Type | Required | Default | Description |
|-----------|------|----------|---------|-------------|
| query | string | Yes | — | Natural language query for semantic search |
| n_results | integer | No | `pipeline.top_k` (default 5) | Number of chunks to retrieve |

---

## SSE Event Envelope

All events from `POST /api/chat` are `data: <JSON>\n\n` lines. The `event` field distinguishes types.

| Event | Fields | When emitted |
|-------|--------|--------------|
| `text_delta` | `event`, `text: string` | Each streaming text token from Claude |
| `tool_start` | `event`, `name: string`, `id: string` | Claude returned a `tool_use` block; server begins executing |
| `tool_result` | `event`, `name: string`, `result: string` | Tool execution completed; result sent back to Claude |
| `citations` | `event`, `sources: [{source_name, origin_path}]` | `search_knowledge_base` returned chunks; max 5 sources |
| `error` | `event`, `message: string` | Unhandled exception or API timeout; input re-enabled |
| `done` | `event` | Stream complete (always emitted in `finally`); input re-enabled |

---

## In-Memory Server State (feature 003 additions)

| Name | Type | Scope | Description |
|------|------|-------|-------------|
| `_MAX_CHAT_MESSAGE_LEN` | int constant | module | `4000` — maximum accepted message length in characters |
| `_MAX_HISTORY_MESSAGES` | int constant | module | `20` — server-side trim limit (10 turns × 2 messages) |

No new module-level mutable state is added. The chat endpoint is fully stateless per-request. The existing `_run_lock` (from feature 002) is shared: `execute_ingest_documents` acquires it non-blocking and returns an error string if a run is already in progress.

---

## `.rag-plugin.toml` — `[llm]` Section

```toml
[llm]
model = "claude-sonnet-4-6"           # Anthropic model ID
llm_key_env = "ANTHROPIC_API_KEY"     # Name of env var holding the API key
```

Both fields are optional; defaults apply if the section is absent. The API key value is never stored in config — only the env var name.
