# Quickstart: Transparent RAG Search

**Branch**: `001-rag-search-transparency` | **Date**: 2026-03-18

## Prerequisites

Feature 001 builds on the existing Chat tab (feature 003). Complete features 001–003 setup first.

## Setup

```bash
# From plugins/RAG-assistant/

# 1. Ensure dependencies are installed (no new deps for this feature)
.venv/bin/pip install -r requirements.txt

# 2. Set API keys
export ANTHROPIC_API_KEY=sk-ant-...
export OPENAI_API_KEY=sk-...      # or whichever embedding key is configured

# 3. Ensure documents are ingested
python3 scripts/ingest.py --source ./docs/

# 4. Start the server
python3 scripts/ui.py
# → http://localhost:7842
```

## Architecture Summary

```
Browser (Chat tab)
    │
    │  POST /api/chat  {message, history[]}
    │  ← SSE stream (enhanced):
    │     tool_start → tool_result → citations → chunks → augmented_prompt → text_delta* → done
    │
scripts/ui.py  ─  _chat_stream() generator
    │
    ├── Empty KB check: collection.count() == 0 → error + done (no API calls)
    │
    ├── execute_search_knowledge_base()
    │       ├── embed_query() → vector
    │       ├── search_similar() → list[RetrievedChunk]
    │       └── build_augmented_prompt() → (summary_str, chunks, prompt_str)
    │
    ├── Emit SSE: chunks (full metadata for panel)
    ├── Emit SSE: augmented_prompt (exact prompt text)
    │
    └── anthropic.Anthropic.messages.stream()
            system = RAG_SYSTEM_INSTRUCTION
            messages = [context + question]
            → text_delta events (answer with [1], [2] citations)
```

## Running Tests

```bash
# From plugins/RAG-assistant/
python3 -m pytest tests/
python3 -m pytest tests/unit/test_ingest_tool.py    # Augmented prompt tests
python3 -m pytest tests/unit/test_ui_api.py          # SSE event tests
python3 -m pytest tests/integration/test_chat_integration.py  # End-to-end
```

## Smoke Test (Manual)

### US1: Search, Retrieve, and Answer

1. Ensure at least one document is ingested.
2. Open the Chat tab at `http://localhost:7842`.
3. Type a question related to ingested content, e.g., `What does the onboarding policy say about remote work?`
4. **Verify**:
   - A numbered chunk panel appears **before** the answer, showing up to 5 chunks
   - Each chunk shows: source name, file path, similarity score (3 decimal places), and a 300-char excerpt
   - Click "Show full text" on a chunk — full text expands inline
   - The streamed answer uses numbered citations like [1], [2]
   - Chunk panel remains visible after the answer completes

### US2: Inspect the Augmented Prompt

1. After receiving an answer (from US1 above), look below the answer text.
2. **Verify**:
   - An "Inspect prompt" collapsible panel is visible
   - Expanding it shows the system instruction, all chunk texts with numbered labels, and the original question
   - The chunk text in the panel matches the full text from the chunk panel
   - Selecting and copying the prompt text yields clean plain text (no HTML artifacts)

### Edge Cases

- **Empty knowledge base**: Delete `.rag-store/` and `.rag-registry.db`, restart server. Ask a question → verify "No documents in knowledge base" message appears. No API calls made (check network tab).
- **No relevant chunks**: Ask an unrelated question (e.g., "What is the speed of light?") → verify "No relevant content found" message, no answer generated.
- **Fewer than 5 chunks**: Ingest a single short document. Ask a question → verify the panel shows however many chunks exist with a note about the count.
- **Deleted source file**: Ingest a file, then delete it from disk. Ask a question that retrieves chunks from that file → verify chunk still displays with "(file no longer on disk)" note.
