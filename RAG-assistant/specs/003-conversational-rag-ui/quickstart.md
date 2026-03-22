# Quickstart: Conversational RAG UI

**Branch**: `003-conversational-rag-ui` | **Date**: 2026-03-18

## Prerequisites

Feature 003 builds on the existing web UI (feature 002). Complete feature 002 setup first.

## Setup

```bash
# From plugins/RAG-assistant/

# 1. Install the Anthropic SDK (added by feature 003)
.venv/bin/pip install anthropic

# 2. Set your Anthropic API key
export ANTHROPIC_API_KEY=sk-ant-...

# 3. Start the server (same command as before)
python3 scripts/ui.py
# → http://localhost:7842
```

The `[llm]` section in `.rag-plugin.toml` is optional. Defaults apply:
```toml
[llm]
model = "claude-sonnet-4-6"
llm_key_env = "ANTHROPIC_API_KEY"
```

## Architecture Summary

```
Browser (Chat tab)
    │
    │  POST /api/chat  {message, history[]}
    │  ← SSE stream: text_delta | tool_start | tool_result | citations | error | done
    │
scripts/ui.py  ─  _chat_stream() generator
    │
    ├── anthropic.Anthropic.messages.stream()   ← Claude API (streaming)
    │       tools: [ingest_documents, query_registry, search_knowledge_base]
    │
    └── tool execution (synchronous, within generator)
            ├── execute_search_knowledge_base()  ← ChromaDB + embed_query()
            ├── execute_ingest_documents()       ← lib.pipeline.run_ingestion()
            └── execute_query_registry()         ← SQLite registry
```

**Key design choices**:
- Server is **stateless per-request**. Full conversation history sent by client each time.
- **Sliding window**: server trims to last 20 messages (10 turns) server-side.
- **Tool loop**: if Claude returns `tool_use`, server executes, appends `tool_result`, resumes stream. Repeats until `stop_reason == "end_turn"`.
- **Shared `_run_lock`**: ingestion from chat and ingestion from the Ingestion tab compete for the same lock, preventing concurrent runs.

## Running Tests

```bash
# From plugins/RAG-assistant/
python3 -m pytest tests/
python3 -m pytest tests/unit/test_ui_api.py          # Chat API unit tests
python3 -m pytest tests/integration/test_chat_integration.py  # End-to-end chat tests
```

## Smoke Test (Manual — per acceptance scenarios)

### US1: Ask a question and get a cited answer

1. Ingest at least one document (use the Ingestion tab or type `ingest ./docs` in chat).
2. Open the Chat tab at `http://localhost:7842`.
3. Type a question related to ingested content, e.g. `What does the onboarding policy say about remote work?`
4. **Verify**: Response streams progressively (tokens appear); a "Sources (N)" toggle appears beneath the answer; expanding it shows 1–5 source documents.
5. Ask a follow-up referencing "it" — **verify** the system understands the prior context.

### US2: Trigger ingestion via natural language

1. Type `ingest ./docs` in the chat input.
2. **Verify**: `tool_start` spinner appears, then disappears; response includes discovered/succeeded counts.
3. Type `add ./docs/report.pdf to the knowledge base` — **verify** same behaviour for a file path.

### US3: Explore knowledge base via natural language

1. Type `what documents do you know about?`
2. **Verify**: Response lists source names and paths from the registry.

### Error states (SC-005)

- **Empty knowledge base**: Ask a question with no documents ingested → response says no documents found, suggests running ingestion.
- **Missing API key**: Unset `ANTHROPIC_API_KEY`, reload page → preflight check shows "API key not set" error in the Chat tab before the first message.
- **Concurrent ingestion block**: Start an ingestion run from the Ingestion tab, then type `ingest ./docs` in chat → chat response says run already in progress.

## Preflight Check

On Chat tab activation the frontend calls `GET /api/chat/preflight`. If the response is `412`, an inline error is shown in the chat area with the reason. The user cannot send messages until the key is configured.
