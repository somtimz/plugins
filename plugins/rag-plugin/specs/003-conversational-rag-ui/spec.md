# Feature Specification: Conversational RAG UI

**Feature Branch**: `003-conversational-rag-ui`
**Created**: 2026-03-16
**Status**: Draft
**Input**: User description: "Create a conversational web UI that accepts natural language from the user for managing data ingestion, data retrieval and conversational response"

## User Scenarios & Testing *(mandatory)*

### User Story 1 — Ask Questions, Get Cited Answers (Priority: P1)

A user types a question in natural language — "What does our onboarding policy say about remote work?" — and the system searches the knowledge base for relevant document chunks, then produces a grounded, cited answer. The conversation continues naturally, with context from prior turns retained within the session.

**Why this priority**: This is the core value of a RAG system. Without retrieval-augmented answers, the feature has no reason to exist. Everything else supports this capability.

**Independent Test**: With at least one source ingested, open the chat UI, type a question related to ingested content, and verify the answer references specific content from the knowledge base with source citations. Ask a follow-up question referencing "it" and verify the system understands the prior context.

**Acceptance Scenarios**:

1. **Given** documents have been ingested into the knowledge base, **When** the user types a question, **Then** the system returns an answer grounded in retrieved content, with citations indicating which source documents were used.
2. **Given** a question has been answered, **When** the user asks a follow-up referencing the same topic, **Then** the system maintains conversational context and gives a coherent continuation.
3. **Given** the user asks about a topic not covered by any ingested document, **When** the system finds no relevant content, **Then** the response clearly states that no relevant information was found rather than fabricating an answer.
4. **Given** the user sends a message, **When** the system is generating a response, **Then** the response streams progressively rather than appearing all at once after a delay.

---

### User Story 2 — Trigger Ingestion via Natural Language (Priority: P2)

A user types "ingest the docs/ folder" or "add ./reports/q1.pdf to the knowledge base" and the system interprets the intent, triggers the ingestion pipeline for the specified path, and reports progress and results inline in the conversation.

**Why this priority**: Unifying ingestion management into the chat interface removes the need to switch to a separate UI tab or run CLI commands. High value once retrieval is working.

**Independent Test**: Type "ingest ./docs" in the chat, verify the system recognises the ingestion intent, triggers a pipeline run, and reports discovered/succeeded/failed counts in the conversation.

**Acceptance Scenarios**:

1. **Given** a valid local path, **When** the user types a message such as "ingest [path]" or "add [path] to the knowledge base", **Then** the system triggers ingestion for that path and streams progress updates in the conversation.
2. **Given** ingestion completes, **When** the run finishes, **Then** the system reports a summary (discovered, succeeded, skipped, failed) as a conversational message.
3. **Given** an invalid or non-existent path, **When** the user requests ingestion, **Then** the system responds with a clear error message rather than silently failing.
4. **Given** an ingestion run is already in progress, **When** the user requests another, **Then** the system informs the user and declines to start a second concurrent run.

---

### User Story 3 — Explore the Knowledge Base via Natural Language (Priority: P3)

A user types "what documents do I have about onboarding?" or "show me files ingested from the HR folder" and the system queries the document registry and responds with a human-readable summary of matching documents.

**Why this priority**: Natural language registry exploration removes the need to switch to the Registry tab. Lower priority than retrieval and ingestion but completes the conversational experience.

**Independent Test**: With several documents ingested, type "list documents from source X" in the chat and verify the response lists matching registry records with source name, path, and last-ingested date.

**Acceptance Scenarios**:

1. **Given** documents have been ingested, **When** the user asks what content is available (e.g., "what do you know about?", "list my documents"), **Then** the system returns a readable summary of registry records relevant to the query.
2. **Given** the user asks about a specific source or path, **When** the system queries the registry, **Then** only records matching the query are returned.
3. **Given** no documents have been ingested yet, **When** the user asks about the knowledge base, **Then** the system responds that no documents are available and suggests running ingestion.

---

### Edge Cases

- What happens when the user's message is ambiguous between retrieval and ingestion intent? Claude, via tool_use reasoning, either selects the most appropriate tool or responds with a clarifying question before invoking any tool.
- What if the knowledge base is empty when the user asks a question? Return an informative message with a suggestion to ingest documents first.
- What if the LLM API is unreachable or returns an error? Display a clear error message; do not lose the conversation history.
- What if the user sends an extremely long message or pastes a large block of text? Messages exceeding 4,000 characters are rejected with a clear error; the input is not submitted.
- What if a cited source document has been deleted from disk since ingestion? The citation still references the registry record; no crash occurs.
- What happens if streaming is interrupted mid-response? The partial response is marked as incomplete and the input box re-enables.

## Requirements *(mandatory)*

### Functional Requirements

- **FR-001**: The UI MUST provide a persistent chat input where users can type natural language messages and submit them with a button or keyboard shortcut. Messages exceeding 4,000 characters MUST be rejected with an inline error before submission.
- **FR-002**: The system MUST perform vector similarity search over the ingested knowledge base to retrieve relevant document chunks for each retrieval-intent message.
- **FR-003**: Answers MUST cite the source documents used, including at minimum the source name and file path, displayed as collapsible references beneath each response.
- **FR-004**: The system MUST stream responses progressively so the user sees content as it is generated.
- **FR-005**: The system MUST maintain conversation context within a session so follow-up questions are understood in relation to prior turns (minimum last 10 turns).
- **FR-006**: The system MUST expose an `ingest_documents` tool schema (defined in `lib/ingest_tool.py`) in each Claude API call. When Claude returns a `tool_use` block invoking `ingest_documents`, the server MUST execute the ingestion pipeline for the specified path and return results as a `tool_result` message, without requiring the user to navigate to a separate tab.
- **FR-007**: Ingestion progress and completion summary triggered via chat MUST appear inline in the conversation thread.
- **FR-008**: The system MUST expose a `query_registry` tool schema (defined in `lib/ingest_tool.py`) in each Claude API call. When Claude returns a `tool_use` block invoking `query_registry`, the server MUST query the document registry and return a `tool_result` containing matching records, which Claude then summarises for the user.
- **FR-009**: The system MUST respond with a clear, actionable message when no relevant documents are found rather than generating an unsupported answer.
- **FR-010**: The system MUST prevent concurrent ingestion runs triggered from chat, consistent with the existing single-run concurrency model.
- **FR-011**: The chat interface MUST be accessible as a new tab within the existing web UI at `http://localhost:7842`, requiring no additional server process or port.
- **FR-012**: The LLM used for conversational responses MUST be Anthropic Claude API. The default model is `claude-sonnet-4-6`. The model name and API key environment variable name MUST be configurable via a `[llm]` section in `.rag-plugin.toml`. The API key is read from the environment variable named in that config field.
- **FR-013**: Conversation history MUST be maintained in the browser (client-side JS array) and sent with each new request. The server is stateless — it does not store conversation history between requests. History is lost on page reload, which is the intended session boundary.
- **FR-014**: The number of document chunks retrieved per query MUST default to 5 and MUST be configurable in `.rag-plugin.toml`.
- **FR-015**: Intent routing MUST use Claude's native `tool_use` mechanism. The server MUST include `ingest_documents`, `query_registry`, and `search_knowledge_base` tool schemas in every Claude API call, allowing Claude to select the appropriate action. A lightweight keyword pre-filter MAY be applied before the API call to avoid unnecessary round-trips for clearly general messages, but MUST NOT override a tool invocation returned by Claude.

### Key Entities

- **ConversationTurn**: A single exchange — user message, tool invocations (if any), retrieved context (chunks + sources), and assistant response text.
- **ConversationSession**: The ordered list of turns for the current browser session; passed as context to each new LLM call.
- **RetrievedChunk**: A document chunk returned by vector search — text content, source name, file path, similarity score.
- **IngestDocumentsTool**: Claude tool schema that accepts a `path` parameter and triggers the ingestion pipeline; defined in `lib/ingest_tool.py`.
- **QueryRegistryTool**: Claude tool schema that accepts an optional `query` parameter and returns matching document registry records; defined in `lib/ingest_tool.py`.
- **SearchKnowledgeBaseTool**: Claude tool schema that accepts a `query` parameter, performs vector similarity search, and returns relevant chunks with source citations; defined in `lib/ingest_tool.py`.

## Success Criteria *(mandatory)*

### Measurable Outcomes

- **SC-001**: A user can ask a question about ingested content and receive a cited, streaming answer — first token appears within 3 seconds of pressing send on a local network.
- **SC-002**: Claude correctly invokes the `ingest_documents` tool for ingestion-intent messages (e.g., "ingest X", "add X to knowledge base") with no false negatives on the 10 canonical phrasings defined in the acceptance test suite.
- **SC-003**: Conversation context is maintained for at least the last 10 turns within a session without degradation in answer coherence.
- **SC-004**: A user with no prior experience can ask a question and receive a grounded, cited answer within 3 minutes of opening the UI for the first time.
- **SC-005**: The chat UI correctly handles an empty knowledge base, an unreachable LLM, and a concurrent ingestion block — all three error states produce a visible, actionable message rather than a silent failure or crash.

## Clarifications

### Session 2026-03-16

- Q: Which LLM provider should be the default for conversational responses? → A: Anthropic Claude API — model and API key env var name configurable via `[llm]` section in `.rag-plugin.toml`.
- Q: Where is conversation history stored between turns? → A: Browser — the JS client maintains the turn array and sends the full prior context with each new request. The server is stateless per-request.
- Q: What is the default Claude model? → A: `claude-sonnet-4-6` — configurable via `[llm]` section in `.rag-plugin.toml`.
- Q: How should intent classification work? → A: Keyword/pattern heuristic first; fall back to a single LLM call only when the heuristic confidence is low.
- Q: Should intent routing use a custom classifier or the LLM's native tool_use mechanism? → A: LLM tool_use — the server exposes `ingest_documents`, `query_registry`, and `search_knowledge_base` tool schemas in every Claude API call; Claude selects the appropriate tool. A keyword pre-filter may short-circuit clearly general messages to avoid unnecessary API calls. The custom heuristic classifier (original FR-015) is replaced by this approach.
- Q: What is the maximum chat input length? → A: 4,000 characters.

## Assumptions

- A single user accesses the UI at a time; multi-user sessions and authentication are out of scope.
- The chat tab integrates into the existing web UI served at port 7842; no new server process is required.
- The LLM API key is set as an environment variable before the server starts, analogous to the embedding API key.
- Conversation history is held in the browser (client-side JS array, tab lifetime). The server receives the full prior turns with each new message and does not maintain per-session state. No persistence to disk is required in v1.
- Intent routing uses Claude's native `tool_use` mechanism. The server includes `ingest_documents`, `query_registry`, and `search_knowledge_base` tool schemas in every API call; Claude decides which tool to invoke. A lightweight keyword pre-filter may skip the API call for clearly general conversational messages. A dedicated intent-classification model is out of scope. Tool schemas are defined in `lib/ingest_tool.py`, created as part of this feature.
- The UI displays citations as collapsible source references beneath each answer.
- Markdown formatting in LLM responses is rendered in the chat (bold, lists, code blocks).
