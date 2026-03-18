# Research: Conversational RAG UI

**Branch**: `003-conversational-rag-ui` | **Date**: 2026-03-18

## Decision 1: Anthropic SDK Streaming with Tool Use

**Decision**: Use `anthropic.Anthropic.messages.stream()` context manager with a manual tool-use loop.

**Rationale**: The Anthropic Python SDK's streaming API emits text tokens incrementally via `stream.text_stream`. When `final_msg.stop_reason == "tool_use"`, the server extracts `tool_use` blocks, executes each tool, appends `tool_result` messages, and calls `stream()` again. This loop repeats until `stop_reason == "end_turn"`. The pattern is idiomatic for the SDK, requires no third-party streaming library, and naturally supports chained tool calls.

**Alternatives considered**:
- `anthropic.Anthropic.messages.create(stream=True)` (lower-level): More control but requires manual event parsing; the `stream()` context manager provides equivalent control with less boilerplate.
- Streaming via WebSocket: Higher complexity; SSE is sufficient for server-push-only chat and is already established by feature 002.

---

## Decision 2: SSE Transport (Reuse Feature 002 Pattern)

**Decision**: Reuse `Response(stream_with_context(generator()), mimetype="text/event-stream")` from Flask, identical to the ingestion SSE endpoint in feature 002.

**Rationale**: Pattern is proven, already tested, and requires no new dependencies. The generator yields `data: <json>\n\n` lines. Chat uses `fetch` + `ReadableStream` on the frontend rather than `EventSource` because `POST` requests cannot use `EventSource` (which only supports `GET`).

**Alternatives considered**:
- WebSocket (`flask-socketio`): Bidirectional but adds a dependency and complicates the single-user local deployment model.
- Long-polling: Simpler but poor UX for progressive token streaming.

---

## Decision 3: Intent Routing via Native Tool Use

**Decision**: Include all three tool schemas (`ingest_documents`, `query_registry`, `search_knowledge_base`) in every Claude API call. Claude selects the appropriate tool; the server executes it and returns a `tool_result`.

**Rationale**: Claude's `tool_use` mechanism eliminates the need for a custom intent classifier. The model's selection generalises to varied phrasings, handles ambiguous inputs gracefully (either picks the best tool or asks a clarifying question), and requires no maintenance as phrasing evolves.

**Alternatives considered**:
- Keyword/regex heuristic: Low latency but brittle; misses paraphrases and ambiguous inputs.
- Dedicated intent classification model: Extra API call and cost; unnecessary for a local single-user tool.

---

## Decision 4: History Management (Client-Side Sliding Window)

**Decision**: Client-side JS array holds `ConversationMessage[]` (role + content). Sent in full with each `POST /api/chat`. Server safety-trims to last 20 messages before forwarding to Anthropic API.

**Rationale**: Server-stateless design simplifies deployment (no session storage, no cleanup). 20-message limit (10 turns × 2 messages) satisfies the FR-005 minimum-10-turn requirement and fits comfortably within Claude's context window even with large tool results. Server-side trim prevents oversized payloads if the client sends more than 20.

**Alternatives considered**:
- Server-side session storage: Adds state management complexity; unnecessary for a single-user local tool.
- Token-budget truncation: More accurate but requires a token-counting pass before each API call; overkill for local use.
- Summarisation: Extra API call per truncation event; significant added complexity.

---

## Decision 5: Citation Rendering

**Decision**: Collapsed by default behind a "Sources (N)" toggle. Maximum 5 citations per response (matching `pipeline.top_k` default).

**Rationale**: Keeps the chat thread readable. Users who care about sources can expand the toggle. Capping at 5 aligns with the retrieval limit — no more citations than chunks returned.

**Alternatives considered**:
- Always expanded: Clutters the conversation for users who are not verifying sources.
- No cap: Could render dozens of citations if `top_k` is raised; not bounded.

---

## Decision 6: LLM API Timeout

**Decision**: 30-second timeout applied to the Claude API call (configurable at the `httpx` transport level in the Anthropic SDK). On timeout, the generator yields an `error` event, the `done` event fires, and the frontend re-enables the input.

**Rationale**: 30 seconds is generous enough for large context calls on slow networks while still surfacing genuine failures promptly. Aligns with SC-001 (first token ≤ 3s on local network — 30s far exceeds that, so only genuine hangs hit the timeout).

**Alternatives considered**:
- 15 seconds: May cut off legitimate responses with large tool results.
- 60 seconds: Too long for a user-facing failure to be surfaced.
- No timeout: Spinner runs indefinitely on hung requests.

---

## Decision 7: `embed_query()` Single-Vector Helper

**Decision**: Add `embed_query(query: str, cfg: EmbeddingConfig) -> list[float]` to `scripts/lib/embedder.py`. This reuses the existing OpenAI-compatible embedding client already established for ingestion.

**Rationale**: Avoids duplicating the API client setup in `searcher.py`. Single function, same credentials and model as the ingestion embedder, ensuring query vectors and document vectors use the same model.

**Alternatives considered**:
- Inline embedding in `searcher.py`: Couples transport concern to search logic.
- Separate embedding client: Redundant with the existing `embedder.py` setup.
