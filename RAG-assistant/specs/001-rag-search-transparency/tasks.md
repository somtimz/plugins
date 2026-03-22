# Tasks: Transparent RAG Search

**Input**: Design documents from `/specs/001-rag-search-transparency/`
**Prerequisites**: plan.md ✓, spec.md ✓, research.md ✓, data-model.md ✓, contracts/api.md ✓, quickstart.md ✓
**Branch**: `001-rag-search-transparency`

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (US1, US2)
- Exact file paths included in all descriptions

---

## Phase 1: Setup

**Purpose**: No new dependencies or files required. This feature modifies existing files only.

*(No setup tasks — feature 003 infrastructure is already in place.)*

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Backend augmented prompt construction — blocks both user stories

**⚠️ CRITICAL**: No user story work can begin until this phase is complete

- [X] T001 Add `RAG_SYSTEM_INSTRUCTION` constant (hardcoded grounding prompt with numbered citation rules per research.md Decision 2) and `build_augmented_prompt(query: str, chunks: list[RetrievedChunk]) -> str` helper function to `scripts/lib/ingest_tool.py`; the helper assembles system instruction + numbered context entries `[N] (source — path):\n{text}` + `Question: {query}` per research.md Decision 6
- [X] T002 Modify `execute_search_knowledge_base()` return type in `scripts/lib/ingest_tool.py` from `tuple[str, list]` to `tuple[str, list[RetrievedChunk], str]` — call `build_augmented_prompt(query, chunks)` after search and return the prompt string as the third tuple element; update all callers (depends on T001)
- [X] T003 [P] Add CSS styles for `.chunk-panel`, `.chunk-card`, `.chunk-card-header`, `.chunk-expand`, `.chunk-score`, and `.inspect-prompt` in `scripts/templates/index.html` — chunk cards with bordered layout, score badge, expand/collapse styling, and preformatted inspect prompt panel

**Checkpoint**: `build_augmented_prompt()` returns correct string format; existing tests still pass after return type change

---

## Phase 3: User Story 1 — Search, Retrieve, and Answer (Priority: P1) 🎯 MVP

**Goal**: User submits a question, sees numbered chunk cards with metadata before the answer, and receives a grounded answer with [1], [2] inline citations.

**Independent Test**: With at least one document ingested, submit a question in the Chat tab. Verify numbered chunk cards appear (source name, file path, score to 3dp, excerpt, "Show full text" toggle) before the streamed answer. Verify the answer uses [1]-style citations.

### Implementation for User Story 1

- [X] T004 [US1] Modify `search_knowledge_base` branch in `_chat_stream()` in `scripts/ui.py` — handle 3-tuple return `(result_str, chunks, augmented_prompt)` from `execute_search_knowledge_base()`; emit `chunks` SSE event with payload: list of `{number, source_name, origin_path, similarity_score (rounded 3dp), excerpt (text[:300]), full_text, file_exists (os.path.exists check)}` for each chunk; add empty KB check before the tool-use loop via `collection.count() == 0` → yield error event with "No documents in knowledge base" message + done, skip all API calls (FR-008)
- [X] T005 [US1] Add `chunks` case to `_dispatchEvent()` in `scripts/templates/index.html` — render a `.chunk-panel` div with numbered `.chunk-card` elements; each card shows: chunk number badge, source name (bold), origin path (with "(file no longer on disk)" if `file_exists` is false), similarity score to 3 decimal places, 300-char excerpt, and a `<details class="chunk-expand"><summary>Show full text</summary><p>` with full_text; if chunks array is empty, show "No relevant content found — try rephrasing your question or ingesting more documents"; if fewer than 5 chunks, append "(N of 5 chunks available)" note; chunk panel is inserted before the assistant answer bubble and remains visible after answer (FR-009) (depends on T003, T004)

**Checkpoint**: User Story 1 fully functional — chunk panel with expandable text, inline citations in answer, empty KB handled

---

## Phase 4: User Story 2 — Inspect the Augmented Prompt (Priority: P2)

**Goal**: User can expand an "Inspect prompt" panel beneath each answer to see the exact text submitted to the LLM.

**Independent Test**: Submit a question, receive an answer, then expand the "Inspect prompt" panel. Verify it contains the system instruction, all chunk texts with numbered labels, and the original question verbatim. Copy the text and verify no HTML artifacts.

### Implementation for User Story 2

- [X] T006 [US2] Emit `augmented_prompt` SSE event in `search_knowledge_base` branch of `_chat_stream()` in `scripts/ui.py` — yield `_sse({"event": "augmented_prompt", "prompt": augmented_prompt})` after the `chunks` event and before the continuation stream (depends on T004)
- [X] T007 [US2] Add `augmented_prompt` case to `_dispatchEvent()` in `scripts/templates/index.html` — store `payload.prompt` in a module-level `_currentAugmentedPrompt` variable (reset to `""` at stream start)
- [X] T008 [US2] In `_finaliseStream()` in `scripts/templates/index.html`, if `_currentAugmentedPrompt` is non-empty, create and append a `<details class="inspect-prompt"><summary>Inspect prompt</summary><pre>` element beneath `_currentAssistantBubble` containing the stored prompt text verbatim; reset `_currentAugmentedPrompt` to `""`; the `<pre>` ensures plain-text copy without rendering artifacts (FR-006, SC-002) (depends on T007)

**Checkpoint**: User Stories 1 AND 2 both work — chunk panel + inspect prompt panel visible, copyable

---

## Phase 5: Polish & Cross-Cutting Concerns

**Purpose**: Documentation update

- [X] T009 [P] Update `README.md` with Transparent Search section — describe chunk panel (numbered cards with source, score, expandable text), inspect prompt panel, and inline citation format; note the feature enhances the existing Chat tab

---

## Dependencies

```
Phase 2 (Foundational)
        T001 → T002 (build_augmented_prompt → modify return type)
        T003 [P]  ← parallel with T001–T002 (different file: index.html)

        ├── Phase 3 (US1)  ← needs T002 + T003
        │       T004 (ui.py: backend SSE changes)
        │       └── T005 (index.html: chunk display — needs T003 CSS + T004 events)
        │
        └── Phase 4 (US2)  ← needs T004
                T006 (ui.py: emit augmented_prompt — same function as T004)
                T007 (index.html: store prompt — needs T006)
                └── T008 (index.html: render panel — needs T007)

Phase 5 (Polish)  ← depends on all stories complete
    T009 [P]
```

---

## Parallel Execution Examples

### Phase 2 — CSS and backend can run in parallel

```
Task T001: scripts/lib/ingest_tool.py  (RAG_SYSTEM_INSTRUCTION + build_augmented_prompt)
Task T003: scripts/templates/index.html  (CSS styles)
(two different files, no dependencies between them)
```

### After Phase 2 — US1 backend and frontend are sequential

```
Task T004: scripts/ui.py  (emit chunks event — needs T002)
Task T005: scripts/templates/index.html  (render chunks — needs T003 + T004)
(T005 depends on T004's SSE events being emitted)
```

---

## Implementation Strategy

### MVP First (User Story 1 Only)

1. Complete Phase 2: Foundational (T001–T003) — **CRITICAL blocker**
2. Complete Phase 3: User Story 1 (T004–T005)
3. **STOP and VALIDATE**: Open Chat tab, ask a question, verify chunk panel with expandable text and [1]-style citations
4. Demo-ready at this point

### Incremental Delivery

1. Foundational → augmented prompt construction works; CSS ready
2. US1 → chunk panel + cited answers (MVP)
3. US2 → inspect prompt panel
4. Polish → README update

---

## Notes

- T001 and T003 are `[P]` — different files, safe to run concurrently
- T004, T006 both modify `_chat_stream()` in `scripts/ui.py` — complete T004 first (chunks event), then T006 (adds one yield for augmented_prompt)
- T005, T007, T008 all modify `scripts/templates/index.html` — sequential within their respective phases
- T002 changes `execute_search_knowledge_base()` return type from 2-tuple to 3-tuple — update the single caller in `ui.py` (T004 handles this)
- No new Python files are created — all changes are modifications to existing feature 003 code
- The `file_exists` field in the chunks event payload enables the "(file no longer on disk)" edge case display without a separate task
