# Implementation Plan: Conversational RAG UI

**Branch**: `003-conversational-rag-ui` | **Date**: 2026-03-18 | **Spec**: [spec.md](spec.md)
**Input**: Feature specification from `/specs/003-conversational-rag-ui/spec.md`

## Summary

Extend the existing Flask web UI (port 7842) with a conversational RAG chat tab. The feature adds two new endpoints (`GET /api/chat/preflight`, `POST /api/chat`) to `scripts/ui.py`, a Chat tab to the single-page `scripts/templates/index.html`, and two supporting library files (`lib/ingest_tool.py` for Claude tool schemas + executors, `lib/searcher.py` for vector similarity search). Chat uses the Anthropic Python SDK's streaming messages API with native `tool_use` for intent routing. Conversation history is held entirely in the browser (client-side JS array, max 20 messages / 10 turns) and sent with each request; the server is stateless per-request.

## Technical Context

**Language/Version**: Python 3.11+ (Flask server, pipeline libs); HTML/CSS/JS vanilla (single-file frontend)
**Primary Dependencies**: `anthropic` (Claude API streaming + tool_use); existing: `flask`, `chromadb`, `openai` (embedding), `sqlite3`, `tomllib`, `tomli_w`
**Storage**: `.rag-plugin.toml` (config read), `.rag-registry.db` (SQLite, read-only from chat), `.rag-store/` (ChromaDB, read-only from chat queries; written only by ingestion tool)
**Testing**: pytest (unit + integration); manual browser smoke test per acceptance scenario
**Target Platform**: Linux/macOS/Windows WSL, local developer machine
**Project Type**: Local web service feature extension (add Chat tab to existing Flask app)
**Performance Goals**: First token ≤ 3 seconds (SC-001); Claude API 30-second timeout (clarified 2026-03-18)
**Constraints**: Single user; stateless server per-request; no auth; 20-message sliding window; 4,000-char input limit; port fixed at 7842
**Scale/Scope**: Single-user local tool; up to 20 messages per request; up to 5 retrieved chunks per query (configurable via `pipeline.top_k`)

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

| Principle | Status | Notes |
|-----------|--------|-------|
| I. Standard Directory Layout | ✅ PASS | New files: `scripts/lib/ingest_tool.py`, `scripts/lib/searcher.py` (PEP 8 snake_case ✓). Chat endpoints added to existing `scripts/ui.py`. Chat tab added to existing `scripts/templates/index.html`. No new directories created. |
| II. Skill-First Design | ✅ PASS | No new skills required. Feature extends an existing script-based server component. |
| III. Test-First Development | ✅ PASS | Unit tests for `lib/ingest_tool.py` and `/api/chat` endpoints; integration tests in `tests/integration/test_chat_integration.py` covering full SSE event flow. |
| IV. Portability & Platform Parity | ✅ PASS | `anthropic` SDK + `flask` + `chromadb` run identically on Linux/macOS/WSL. No hardcoded paths; all paths from config. |
| V. Simplicity | ✅ PASS | Reuses existing SSE streaming pattern from feature 002. Vanilla JS extension of existing `index.html`. No new build pipeline. `anthropic` SDK handles streaming; no custom parser. |

**Post-design re-check**: All gates pass. No violations.

## Project Structure

### Documentation (this feature)

```text
specs/003-conversational-rag-ui/
├── plan.md              # This file
├── research.md          # Phase 0 output
├── data-model.md        # Phase 1 output
├── quickstart.md        # Phase 1 output
├── contracts/
│   └── api.md           # Phase 1 output
└── tasks.md             # Phase 2 output (/speckit.tasks)
```

### Source Code (repository root)

```text
scripts/
├── ui.py                      # Extended: /api/chat/preflight, /api/chat endpoints; _chat_stream() generator
├── templates/
│   └── index.html             # Extended: Chat tab (4th tab) with SSE EventSource, citation toggle, spinner
└── lib/
    ├── ingest_tool.py         # New: INGEST_DOCUMENTS_TOOL, QUERY_REGISTRY_TOOL,
    │                          #      SEARCH_KNOWLEDGE_BASE_TOOL schemas + execute_* functions
    ├── searcher.py            # New: search_similar(), RetrievedChunk dataclass
    ├── config.py              # Extended: LlmConfig dataclass; [llm] section parsing
    ├── pipeline.py            # Existing — no changes needed
    ├── registry.py            # Existing — no changes needed
    ├── embedder.py            # Extended: embed_query() single-vector helper
    └── store.py               # Existing — no changes needed

tests/
├── unit/
│   └── test_ui_api.py         # Extended: /api/chat/preflight and /api/chat endpoint tests
└── integration/
    └── test_chat_integration.py  # New: end-to-end chat stream tests
```

**Structure Decision**: Same single-project layout as features 001 and 002 (`scripts/` + `tests/`). Chat API is integrated directly into the existing `ui.py` module; no separate chat server process. This avoids port proliferation and keeps the tool self-contained.

## Phase 0 Research Findings

See [research.md](research.md) for full details. Key decisions:

- **Anthropic SDK streaming with tool_use**: Use `client.messages.stream()` context manager from the `anthropic` Python SDK. After the stream ends, inspect `final_msg.stop_reason`; if `"tool_use"`, extract `tool_use` blocks, execute tools, append `tool_result` messages, and call `client.messages.stream()` again. This loop repeats until `stop_reason == "end_turn"`.
- **SSE transport**: Reuse existing Flask `Response(stream_with_context(generate()), mimetype="text/event-stream")` pattern from feature 002. No additional library.
- **Intent routing**: Claude's native `tool_use` mechanism. All three tool schemas (`ingest_documents`, `query_registry`, `search_knowledge_base`) included in every API call. No separate keyword classifier.
- **History management**: Client-side JS array. Server-side safety trim to `_MAX_HISTORY_MESSAGES = 20` (10 turns × 2 messages each) before passing to Anthropic API.
- **Tool timeout**: No per-tool timeout in v1. The 30-second Claude API timeout applies to the full stream; long-running ingestion within a tool call may exceed this on very large directories.

## Phase 1 Design Artifacts

- [data-model.md](data-model.md) — entity definitions, SSE event envelope, in-memory state, LlmConfig fields
- [contracts/api.md](contracts/api.md) — full HTTP API contract (2 new endpoints)
- [quickstart.md](quickstart.md) — developer setup, architecture summary, smoke test steps

## Implementation Sequence

### Stage 1: Config + library extensions

1. Add `LlmConfig` dataclass and `[llm]` section parsing to `scripts/lib/config.py`
2. Add `embed_query()` single-vector helper to `scripts/lib/embedder.py`
3. Create `scripts/lib/searcher.py` — `RetrievedChunk` dataclass, `search_similar()` function
4. Create `scripts/lib/ingest_tool.py` — `INGEST_DOCUMENTS_TOOL`, `QUERY_REGISTRY_TOOL`, `SEARCH_KNOWLEDGE_BASE_TOOL` constants; `TOOL_SCHEMAS` list; `execute_ingest_documents()`, `execute_query_registry()`, `execute_search_knowledge_base()` functions

### Stage 2: Chat API endpoints

5. Add `_MAX_CHAT_MESSAGE_LEN = 4000` and `_MAX_HISTORY_MESSAGES = 20` constants to `scripts/ui.py`
6. Implement `GET /api/chat/preflight` — load config, check `llm_key_env` env var, return `200/412`
7. Implement `POST /api/chat` — validate message length, trim history, load config, return SSE stream
8. Implement `_chat_stream()` generator — first stream pass → tool use loop → continuation stream; yields `text_delta`, `tool_start`, `tool_result`, `citations`, `error`, `done` events
9. Write `tests/unit/test_ui_api.py` additions — `/api/chat/preflight` (200/412), `/api/chat` (400 on >4000 chars, stream event shape)

### Stage 3: Frontend

10. Add Chat tab to `scripts/templates/index.html` — 4th tab in navigation; chat message thread; `EventSource` connection to `POST /api/chat` via `fetch` + `ReadableStream`; per-message spinner during tool execution; citation toggle ("Sources (N)") collapsed by default (max 5); markdown rendering via `marked.js` or inline; 4000-char counter on input; re-enable input on `done` event

### Stage 4: Integration tests

11. Write `tests/integration/test_chat_integration.py` — mock `anthropic.Anthropic`; `POST /api/chat` with synthetic history; assert SSE event sequence (`text_delta` → `done`); assert tool invocation produces `tool_start` + `tool_result` events; assert 400 on overlong message

## Complexity Tracking

No violations to document. All constitution gates pass.
