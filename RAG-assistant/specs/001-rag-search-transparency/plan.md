# Implementation Plan: Transparent RAG Search

**Branch**: `001-rag-search-transparency` | **Date**: 2026-03-18 | **Spec**: [spec.md](spec.md)
**Input**: Feature specification from `/specs/001-rag-search-transparency/spec.md`

## Summary

Enhance the existing Chat tab (feature 003) to display retrieved document chunks with full metadata (source name, file path, similarity score, expandable text) before the LLM answer, add numbered inline citations to answers, and provide an "Inspect prompt" panel showing the exact augmented prompt sent to the LLM. This makes the RAG pipeline fully transparent to the user.

## Technical Context

**Language/Version**: Python 3.11+
**Primary Dependencies**: Flask, anthropic, chromadb, openai (embedding client)
**Storage**: ChromaDB (vector store), SQLite (registry)
**Testing**: pytest (unit + integration)
**Target Platform**: Local developer machine (localhost:7842)
**Project Type**: Web application (Flask + vanilla JS single-page)
**Performance Goals**: Retrieved chunks displayed within 3 seconds (SC-001)
**Constraints**: Single-user, local-only; enhances existing Chat tab (feature 003)
**Scale/Scope**: Single user, 5 fixed chunks per query

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

Constitution is not yet instantiated (template placeholders only). No binding gates to enforce. Proceeding.

## Project Structure

### Documentation (this feature)

```text
specs/001-rag-search-transparency/
├── plan.md              # This file
├── research.md          # Phase 0 output
├── data-model.md        # Phase 1 output
├── quickstart.md        # Phase 1 output
├── contracts/           # Phase 1 output
│   └── api.md           # SSE event contract changes
└── tasks.md             # Phase 2 output (/speckit.tasks)
```

### Source Code (repository root)

```text
plugins/RAG-assistant/
├── scripts/
│   ├── ui.py                      # Modify: _chat_stream() — build augmented prompt, emit new SSE events
│   ├── lib/
│   │   ├── searcher.py            # No changes needed (RetrievedChunk already has all required fields)
│   │   ├── ingest_tool.py         # Modify: execute_search_knowledge_base() — return full chunk text + augmented prompt
│   │   ├── embedder.py            # No changes needed (embed_query() already exists)
│   │   └── config.py              # No changes needed (LlmConfig already exists)
│   └── templates/
│       └── index.html             # Modify: chunk detail panel, expand/collapse, inspect prompt panel, citation styling
└── tests/
    ├── unit/
    │   ├── test_ui_api.py         # Add: tests for new SSE events (chunks, augmented_prompt)
    │   └── test_ingest_tool.py    # Add: tests for augmented prompt construction
    └── integration/
        └── test_chat_integration.py  # Add: end-to-end tests for transparency features
```

**Structure Decision**: No new files needed. All changes modify existing files in the established feature 003 structure. The key change is enriching the `search_knowledge_base` flow with chunk detail display and prompt inspection.

## Implementation Stages

### Stage 1: Backend — Augmented Prompt Construction

**Goal**: Build the explicit augmented prompt string and return it alongside search results.

**Changes**:
- `scripts/lib/ingest_tool.py`: Modify `execute_search_knowledge_base()` to also construct and return the full augmented prompt string (system instruction + numbered context entries + user question). Add a hardcoded `RAG_SYSTEM_INSTRUCTION` constant that instructs the LLM to use numbered inline citations [1], [2], etc.
- `scripts/ui.py`: Modify the `search_knowledge_base` branch in `_chat_stream()` to:
  - Emit a new `chunks` SSE event with full chunk metadata (source_name, origin_path, similarity_score to 3 decimal places, text excerpt ≤300 chars, full_text)
  - Emit a new `augmented_prompt` SSE event with the exact prompt text
  - Pass the augmented prompt as the system message to Claude instead of relying on Claude's tool-use loop for grounding

### Stage 2: Frontend — Chunk Display Panel

**Goal**: Show retrieved chunks with expandable text before the answer.

**Changes**:
- `scripts/templates/index.html`:
  - On `chunks` event: render a numbered list of chunk cards, each showing source name, file path, similarity score (3 decimal places), and a 300-char excerpt with "Show full text" toggle
  - Chunk cards appear before the answer text in the message flow
  - Cards remain visible after answer generation (FR-009)

### Stage 3: Frontend — Inspect Prompt Panel

**Goal**: Let users see the exact text sent to the LLM.

**Changes**:
- `scripts/templates/index.html`:
  - On `augmented_prompt` event: store the prompt text
  - After `done` event: render a collapsible `<details>` element with summary "Inspect prompt" beneath the answer
  - Content is plain text (preformatted), copyable without rendering artefacts

### Stage 4: Edge Cases & Polish

**Goal**: Handle empty KB, no results, deleted source files, query truncation.

**Changes**:
- `scripts/ui.py`: Before embedding, check if collection is empty → emit error event with guidance message, skip embedding/LLM calls (FR-008)
- `scripts/ui.py`: When chunks list is empty after search → emit `chunks` event with empty array, do not call LLM (FR-007)
- `scripts/templates/index.html`: Handle edge states in the chunk display (0 chunks → "No relevant content found" message; fewer than 5 → note the count)
