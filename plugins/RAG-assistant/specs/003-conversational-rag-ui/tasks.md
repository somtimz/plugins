# Tasks: Conversational RAG UI

**Input**: Design documents from `/specs/003-conversational-rag-ui/`
**Prerequisites**: plan.md ✓, spec.md ✓, research.md ✓, data-model.md ✓, contracts/api.md ✓, quickstart.md ✓
**Branch**: `003-conversational-rag-ui`

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (US1, US2, US3)
- Exact file paths included in all descriptions

---

## Phase 1: Setup

**Purpose**: Install new dependency and confirm environment

- [X] T001 Install `anthropic` into `.venv`, add to `requirements.txt`, and verify import: `python -c "import anthropic; print(anthropic.__version__)"`

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Config extension, new library modules, Flask scaffold — blocks all three user stories

**⚠️ CRITICAL**: No user story work can begin until this phase is complete

- [X] T002 [P] Add `LlmConfig` dataclass (`model: str = "claude-sonnet-4-6"`, `llm_key_env: str = "ANTHROPIC_API_KEY"`) to `scripts/lib/config.py`; extend `Config` dataclass with `llm: LlmConfig = field(default_factory=LlmConfig)`; add `[llm]` section parsing in `load_config()` (both fields optional with defaults)
- [X] T003 [P] Add `embed_query(query: str, cfg: EmbeddingConfig) -> list[float]` to `scripts/lib/embedder.py` — single-vector helper using the existing OpenAI-compatible client; reuses `embedding_key_env` and `api_base` already established for ingestion
- [X] T004 Create `scripts/lib/searcher.py` — define `RetrievedChunk` dataclass with fields `(text: str, source_name: str, origin_path: str, similarity_score: float)`; implement `search_similar(collection, query_vector: list[float], n_results: int = 5) -> list[RetrievedChunk]` (depends on T003)
- [X] T005 Create `scripts/lib/ingest_tool.py` — define `INGEST_DOCUMENTS_TOOL`, `QUERY_REGISTRY_TOOL`, `SEARCH_KNOWLEDGE_BASE_TOOL` Anthropic tool schema dicts and `TOOL_SCHEMAS` list; implement `execute_ingest_documents()`, `execute_query_registry()`, `execute_search_knowledge_base()` executor functions (imports from `lib.searcher` — depends on T004)
- [X] T006 Add `_MAX_CHAT_MESSAGE_LEN = 4000`, `_MAX_HISTORY_MESSAGES = 20` constants and `import anthropic` to `scripts/ui.py`; implement `GET /api/chat/preflight` — load config, check `os.environ.get(cfg.llm.llm_key_env)`, return `200 {"ok": true, "model": ...}` or `412 {"ok": false, "reason": ...}`; implement `POST /api/chat` — validate message length (400 if exceeded), trim history, load config, return `Response(stream_with_context(_chat_stream(...)), content_type="text/event-stream")`; implement `_chat_stream()` skeleton yielding only `{"event": "done"}` in finally (depends on T002 + T005)
- [X] T007 [P] Add Chat tab skeleton to `scripts/templates/index.html` — 4th tab button in navigation; chat message thread `<div>`; `<textarea>` input with 4000-char `maxlength`, character counter (`0 / 4000`), submit on Enter (Shift+Enter = newline); Send button; `fetch` + `ReadableStream` SSE loop that parses `data: <json>` lines and dispatches by `event` field (stub handlers for now)

**Checkpoint**: `python scripts/ui.py` starts; `GET /api/chat/preflight` responds; Chat tab visible; all existing tests still pass

---

## Phase 3: User Story 1 — Ask Questions, Get Cited Answers (Priority: P1) 🎯 MVP

**Goal**: User types a question, system performs semantic search, Claude streams a grounded cited answer. Follow-up questions use prior context.

**Independent Test**: With at least one document ingested and `ANTHROPIC_API_KEY` set, open the Chat tab, type "What does the onboarding policy say?", verify tokens stream progressively and a "Sources (N)" toggle appears beneath the answer. Ask "What else does it say about that?" — verify coherent follow-up.

### Tests for User Story 1

- [X] T008 [P] [US1] Add tests to `tests/unit/test_ui_api.py` for `GET /api/chat/preflight`: assert `200 {"ok": true}` when `ANTHROPIC_API_KEY` env var is set; assert `412 {"ok": false}` when env var unset; assert `412` when `.rag-plugin.toml` missing
- [X] T009 [P] [US1] Add tests to `tests/unit/test_ui_api.py` for `POST /api/chat`: assert `400` when `message` exceeds 4000 chars; assert `422` when config missing/invalid; assert `200` with `text/event-stream` content-type on valid request; assert history is trimmed to last 20 messages server-side when client sends 25

### Implementation for User Story 1

- [X] T010 [US1] Implement `search_knowledge_base` branch in `_chat_stream()` in `scripts/ui.py` — open `chromadb.PersistentClient`, call `execute_search_knowledge_base(query, n_results=cfg.pipeline.top_k, embedding_cfg=cfg.embedding, collection=collection)`; yield `{"event": "citations", "sources": sources[:5]}`; yield `{"event": "tool_result", "name": "search_knowledge_base", "result": result_str}`; append `tool_results_for_api` for continuation call
- [X] T011 [US1] Implement full streaming + tool-use loop in `_chat_stream()` in `scripts/ui.py` — create `anthropic.Anthropic(api_key=api_key, timeout=30.0)`; first stream pass: `client.messages.stream(model=cfg.llm.model, max_tokens=4096, tools=TOOL_SCHEMAS, messages=messages)`; yield `text_delta` events; check `final_msg.stop_reason`; while `"tool_use"`: yield `tool_start`, dispatch to tool branch (T010 + T016 + T018), yield `tool_result`, append tool result to messages, resume continuation stream; yield `done` in finally; `except Exception` yields `error` event
- [X] T012 [US1] Implement citation toggle in `scripts/templates/index.html` — on `citations` event, render collapsed `<details><summary>Sources (N)</summary>` beneath the active assistant bubble; list up to 5 `{source_name}: {origin_path}` entries; expand/collapse natively via `<details>`
- [X] T013 [US1] Implement streaming display + history management in `scripts/templates/index.html` — on `text_delta`: append token to current assistant message bubble; on `tool_start`: show spinner overlay on assistant bubble; on `tool_result`: hide spinner; on `done`: re-enable send button + textarea; on `error`: re-enable input, show inline error message; after each complete exchange: push `{role: "user", content: msg}` and `{role: "assistant", content: fullText}` to history array; trim history array to last 20 entries before next send
- [X] T014 [US1] Implement preflight check on Chat tab activation in `scripts/templates/index.html` — on tab click: `fetch GET /api/chat/preflight`; if `412`: show dismissible banner in chat area ("LLM API key not configured: {reason}"), disable Send button; if `200`: show model name as subtitle beneath tab heading, enable Send

**Checkpoint**: User Story 1 fully functional — streaming cited answers, follow-up context, spinner during search, citations toggle

---

## Phase 4: User Story 2 — Trigger Ingestion via Natural Language (Priority: P2)

**Goal**: User types "ingest ./docs" or "add ./report.pdf to the knowledge base"; system runs the ingestion pipeline and reports progress inline.

**Independent Test**: Type "ingest ./docs" in chat; verify spinner appears during tool execution, then response includes "Discovered: N, Succeeded: N, Skipped: N, Failed: N". Type during an active ingestion run from the Ingestion tab and verify "run in progress" error appears in conversation.

### Tests for User Story 2

- [X] T015 [P] [US2] Write `tests/integration/test_chat_integration.py` — mock `anthropic.Anthropic`; synthesise a `tool_use` block for `ingest_documents`; `POST /api/chat`, consume SSE stream, assert event sequence: `tool_start` (name=`ingest_documents`) → `tool_result` → `text_delta` → `done`; assert `tool_result.result` is a string (not an exception); assert second `POST /api/chat` while `_run_lock` held returns `tool_result` containing "already in progress"

### Implementation for User Story 2

- [X] T016 [US2] Implement `ingest_documents` branch in `_chat_stream()` in `scripts/ui.py` — open registry + ChromaDB, init logger; call `execute_ingest_documents(path, cfg, chroma_client, collection, reg_conn, _run_lock, logger)`; close `reg_conn` in finally; result is always a string (locked → error string, success → summary string); yield `tool_start` before call, `tool_result` after

**Checkpoint**: User Stories 1 AND 2 both work independently

---

## Phase 5: User Story 3 — Explore Knowledge Base via Natural Language (Priority: P3)

**Goal**: User asks "what documents do you have about onboarding?"; system queries the registry and Claude summarises matching records.

**Independent Test**: With several documents ingested, type "list documents from source hr-docs"; verify response names files from that source. Type "what do you know about?" with no docs ingested; verify system says no documents available.

### Tests for User Story 3

- [X] T017 [P] [US3] Add to `tests/integration/test_chat_integration.py` — mock `anthropic.Anthropic`; synthesise `tool_use` for `query_registry`; assert SSE sequence: `tool_start` (name=`query_registry`) → `tool_result` → `done`; assert `tool_result.result` is valid JSON string (list); seed a tmp SQLite registry, assert query filters correctly

### Implementation for User Story 3

- [X] T018 [US3] Implement `query_registry` branch in `_chat_stream()` in `scripts/ui.py` — open registry conn with `open_registry(cfg.pipeline.registry_path)`; call `execute_query_registry(query=tool_input.get("query"), limit=int(tool_input.get("limit", 50)), reg_conn=reg_conn)`; close conn in finally; yield `tool_start` before call, `tool_result` after; handle missing registry file with error string (no exception)

**Checkpoint**: All three user stories independently functional

---

## Phase 6: Polish & Cross-Cutting Concerns

**Purpose**: Markdown rendering, edge-case error states, documentation

- [X] T019 Implement markdown rendering in `scripts/templates/index.html` — render Claude's text responses with basic markdown support (bold `**`, lists `- / 1.`, inline code `` ` ``, fenced code blocks ` ``` `); use `marked.js` loaded from CDN or a 50-line inline renderer; apply only to assistant message bubbles (not user input)
- [X] T020 [P] Implement remaining error states in `scripts/templates/index.html` — rate-limit (`error` event with "429" in message): show "Rate limit reached — please wait and try again"; timeout (`error` event with "timeout"): show "Request timed out — please try again"; streaming interruption (fetch abort / network drop): append "[Response interrupted]" to partial message, re-enable input; all three cases re-enable send button
- [X] T021 [P] Update `README.md` with Chat UI section — add "Conversational Chat Interface" subsection under Usage: `export ANTHROPIC_API_KEY=sk-ant-...`, `python3 scripts/ui.py`, open `http://localhost:7842`, click Chat tab; show optional `[llm]` TOML config; note "ingest ./path" shortcut

---

## Dependencies

```
Phase 1 (T001: install anthropic)
    └── Phase 2 (Foundational)
            T002 [P], T003 [P]  ← parallel with each other
            └── T004 (needs T003: uses embed_query)
                    └── T005 (needs T004: imports searcher)
                            └── T006 (needs T002 + T005: uses LlmConfig + TOOL_SCHEMAS)
            T007 [P]  ← parallel with T002–T006 (different file)

            ├── Phase 3 (US1)  ← needs T006 + T007
            │       T008 [P], T009 [P]  ← test tasks, parallel with T010–T014
            │       T010 → T011 (same function, T010 implements one branch of T011's loop)
            │       T012, T013, T014  ← frontend, sequential (same file)
            │
            ├── Phase 4 (US2)  ← needs T006 + T011 scaffold
            │       T015 [P]  ← tests, parallel with T016
            │       T016  ← adds ingest_documents branch to _chat_stream
            │
            └── Phase 5 (US3)  ← needs T006 + T011 scaffold
                    T017 [P]  ← tests, parallel with T018
                    T018  ← adds query_registry branch to _chat_stream

Phase 6 (Polish)  ← depends on all stories complete
    T019, T020 [P], T021 [P]
```

---

## Parallel Execution Examples

### Phase 2 — Config and embedder can run in parallel

```
Task T002: scripts/lib/config.py  (LlmConfig + [llm] parsing)
Task T003: scripts/lib/embedder.py  (embed_query helper)
Task T007: scripts/templates/index.html  (Chat tab skeleton)
(three different files, no dependencies between them)
```

### Phase 3 (US1) — Tests run in parallel with implementation

```
Task T008: tests/unit/test_ui_api.py  (preflight tests)
Task T009: tests/unit/test_ui_api.py  (POST /api/chat tests)
(same file — run sequentially to avoid write conflicts)

Task T010: scripts/ui.py  (search_knowledge_base branch)
Task T012: scripts/templates/index.html  (citation toggle)
(different files — can run in parallel after T006+T007 complete)
```

### After Phase 2 — Stories can be worked by separate developers

```
Developer A: Phase 3 (US1) — T008–T014
Developer B: Phase 4 (US2) — T015–T016  (needs T006 scaffold only)
Developer C: Phase 5 (US3) — T017–T018  (needs T006 scaffold only)
```

Note: T010/T011/T016/T018 all modify `_chat_stream()` in `scripts/ui.py`. Single-developer sequential execution is safest; multi-developer requires branch coordination on that function.

---

## Implementation Strategy

### MVP First (User Story 1 Only)

1. Complete Phase 1: Setup (T001)
2. Complete Phase 2: Foundational (T002–T007) — **CRITICAL blocker**
3. Complete Phase 3: User Story 1 (T008–T014)
4. **STOP and VALIDATE**: Open Chat tab, ask a question about ingested content, verify streaming cited answer
5. Demo-ready at this point

### Incremental Delivery

1. Setup + Foundational → server extends cleanly; preflight works
2. US1 → streaming cited answers (MVP)
3. US2 → ingestion via chat
4. US3 → registry exploration via chat
5. Polish → markdown, error states, README

---

## Notes

- T002 and T003 are `[P]` — add to different files, safe to run concurrently
- T007 is `[P]` throughout Phase 2 — `index.html` is independent of all lib changes
- T010 and T011 edit the same `_chat_stream()` function: complete T010 first (branch body), then T011 (loop frame that calls it)
- T016 and T018 also edit `_chat_stream()` — complete after T011 establishes the loop
- Tests T008/T009 can be written before or during implementation; they do not gate task completion
- Never expose the LLM API key value in any endpoint — only `llm_key_env` (the env var name) is serialized
