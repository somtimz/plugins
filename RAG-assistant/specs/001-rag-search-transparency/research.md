# Research: Transparent RAG Search

**Branch**: `001-rag-search-transparency` | **Date**: 2026-03-18

## Decision 1: Augmented Prompt Construction Location

**Decision**: Build the augmented prompt in `execute_search_knowledge_base()` in `ingest_tool.py`, returning it as a third element in the tuple alongside the summary string and chunk list.

**Rationale**: The function already has access to the query, chunks, and embedding config. Constructing the prompt here keeps the grounding logic co-located with the retrieval logic. The `_chat_stream()` generator in `ui.py` then simply emits it as an SSE event and passes it as the system message.

**Alternatives considered**:
- Build prompt in `_chat_stream()` directly — rejected because it mixes presentation concerns with retrieval logic
- Create a separate `prompt_builder.py` module — rejected as overengineering for a single function

## Decision 2: System Instruction Content

**Decision**: Hardcoded `RAG_SYSTEM_INSTRUCTION` constant in `ingest_tool.py`:

```
You are a knowledge base assistant. Answer questions using ONLY the provided context chunks below.
Rules:
- Cite your sources using numbered inline citations like [1], [2] that match the chunk numbers.
- If the context does not contain enough information to answer, say so explicitly.
- Do not fabricate information not present in the context.
```

**Rationale**: Clear, minimal instruction that enforces grounding and numbered citations per FR-005 and the clarification. Hardcoded per clarification Q5.

**Alternatives considered**:
- TOML-configurable system prompt — deferred to future iteration per clarification
- Include chunk metadata in system instruction — unnecessary, chunks are already in the context block

## Decision 3: New SSE Event Types

**Decision**: Add two new SSE events to the `/api/chat` stream:

1. `chunks` — emitted after `search_knowledge_base` completes, before answer generation:
   ```json
   {
     "event": "chunks",
     "chunks": [
       {
         "number": 1,
         "source_name": "hr-docs",
         "origin_path": "./docs/onboarding.pdf",
         "similarity_score": 0.892,
         "excerpt": "First 300 chars...",
         "full_text": "Complete chunk text..."
       }
     ]
   }
   ```

2. `augmented_prompt` — emitted once, after chunks, before the LLM answer stream begins:
   ```json
   {
     "event": "augmented_prompt",
     "prompt": "You are a knowledge base assistant...\n\n[1] (hr-docs — ./docs/onboarding.pdf):\n..."
   }
   ```

**Rationale**: Separating chunk metadata from the existing `citations` event allows the frontend to render the detailed chunk panel independently. The `augmented_prompt` event provides the exact text for the Inspect Prompt panel. Existing `citations` event is retained for backward compatibility.

**Alternatives considered**:
- Overload the existing `citations` event with chunk details — rejected because it changes the contract for existing consumers
- Send chunks as part of `tool_result` — rejected because `tool_result` is a string summary, not structured metadata

## Decision 4: Chunk Display vs Existing Citations

**Decision**: The new `chunks` event replaces the visual role of the existing `citations` event for transparency purposes. The `citations` event continues to be emitted for backward compatibility but the chunk panel (from `chunks` event) is the primary display. The old "Sources (N)" toggle is superseded by the richer chunk panel.

**Rationale**: The chunk panel shows everything the citations toggle showed (source_name, origin_path) plus similarity score, excerpt, and full text toggle. Keeping both events avoids breaking the existing SSE contract.

**Alternatives considered**:
- Remove `citations` event entirely — rejected to avoid breaking existing clients
- Merge into a single event — rejected for clarity of concerns

## Decision 5: Empty Knowledge Base Detection

**Decision**: Check `collection.count() == 0` before calling `embed_query()`. If empty, yield an SSE `error` event with message directing user to ingest documents, then yield `done`. No embedding or LLM API call is made.

**Rationale**: ChromaDB's `count()` is O(1) and avoids unnecessary API calls (FR-008, SC-004). The check happens in `_chat_stream()` before the tool-use loop.

**Alternatives considered**:
- Check in `execute_search_knowledge_base()` — possible but the check is more naturally a pre-condition in the stream generator
- Check during preflight — rejected because KB state can change between preflight and query

## Decision 6: Prompt Construction Format

**Decision**: The augmented prompt is assembled as a single string with this structure:

```
{RAG_SYSTEM_INSTRUCTION}

Context:

[1] (source_name — origin_path):
{full chunk text}

[2] (source_name — origin_path):
{full chunk text}

...

Question: {user's original question}
```

**Rationale**: Numbered entries with source metadata enable the LLM to produce `[1]`-style citations naturally. The format is human-readable in the Inspect Prompt panel (FR-006). Source info in each entry helps the LLM reference documents by name if helpful.

**Alternatives considered**:
- XML-tagged context blocks — more structured but harder for users to read in the Inspect panel
- JSON context — rejected for readability in the plain-text panel
