# Feature Specification: Transparent RAG Search

**Feature Branch**: `001-rag-search-transparency`
**Created**: 2026-03-18
**Status**: Draft
**Input**: User description: "create a feature to transform a user query into an embedded vector and then query the vector database in order to retrieve the five closest chunks. Get the retrieved chunks into the context and then use it to answer the user's query. Show the user what has been retrieved and what query is being submitted to the LLM"

## User Scenarios & Testing *(mandatory)*

### User Story 1 — Search, Retrieve, and Answer (Priority: P1)

A user types a natural language question. The system embeds the question, searches the vector database for the five most semantically similar document chunks, shows those five chunks to the user (with source, excerpt, and relevance score), constructs a prompt from them, and returns a grounded answer. The user can see exactly which content the answer is based on before the answer appears.

**Why this priority**: This is the complete core loop — embedding, retrieval, context injection, and answer generation. It delivers the entire RAG pipeline value in a single interaction. Everything else is supplementary.

**Independent Test**: With at least one document ingested, submit a question related to that document. Verify that five chunks are displayed with their source and relevance score, then verify the answer references content visible in those chunks.

**Acceptance Scenarios**:

1. **Given** documents are ingested in the knowledge base, **When** the user submits a question, **Then** the system displays exactly five retrieved chunks — each showing the source document name, file path, similarity score, and a text excerpt — before generating any answer.
2. **Given** the five chunks are visible, **When** the LLM generates its answer, **Then** the answer is grounded in the displayed chunks and does not introduce information absent from them.
3. **Given** the user submits a question, **When** the system finds fewer than five relevant chunks (e.g., knowledge base has only three documents), **Then** all available chunks are displayed and the shortfall is noted.
4. **Given** the user submits a question, **When** no semantically relevant chunks are found, **Then** the system clearly states no relevant content was found and does not generate a fabricated answer.

---

### User Story 2 — Inspect the Augmented Prompt (Priority: P2)

A user wants to see the exact prompt — system instructions, retrieved chunks formatted as context, and the original question — that was sent to the LLM. They can expand an "Inspect prompt" panel beneath each answer to read the full augmented query verbatim.

**Why this priority**: Transparency about what the LLM receives allows users to diagnose poor answers, verify source coverage, and build trust in the system. High value for power users and debugging, but the core retrieval and answer (US1) must work first.

**Independent Test**: Submit a question, receive an answer, then expand the "Inspect prompt" panel. Verify the panel contains all five retrieved chunk texts and the original question exactly as submitted, formatted as they were sent to the LLM.

**Acceptance Scenarios**:

1. **Given** an answer has been generated, **When** the user opens the "Inspect prompt" panel, **Then** the full text sent to the LLM is visible — including the system instruction, each chunk's text and citation label, and the user's original question.
2. **Given** the prompt panel is open, **When** the user reads the chunk text in the panel, **Then** it matches exactly the excerpts shown in the retrieved chunks display (no truncation or modification introduced for display purposes).
3. **Given** the panel is open, **When** the user copies the content, **Then** the copied text is the plain-text representation of the prompt with no rendering artefacts.

---

### Edge Cases

- What happens if the query is very long (exceeds embedding model input limit)? The query is truncated to the model's maximum input length before embedding; the user is notified of the truncation.
- What if all five retrieved chunks come from the same source document? All five are shown regardless; source diversity is not enforced in v1.
- What if a retrieved chunk's source file has been deleted from disk since ingestion? The chunk is still shown using metadata stored in the registry; no crash occurs and a "(file no longer on disk)" note is appended to the path display.
- What if the LLM is unavailable when the answer is requested? The retrieved chunks are still displayed; only the answer section shows an error. The user does not lose the retrieval results.
- What if the knowledge base has never been populated? An informational message is shown before any embedding or retrieval is attempted, directing the user to ingest documents first.

## Requirements *(mandatory)*

### Functional Requirements

- **FR-001**: The system MUST accept a natural language query from the user and convert it to a vector representation using the same embedding model used during document ingestion, ensuring query and document vectors are comparable.
- **FR-002**: The system MUST query the vector database for the five most semantically similar document chunks to the embedded query and return them ranked by descending similarity score.
- **FR-003**: The system MUST display each of the five retrieved chunks to the user before generating an answer, showing: source document name, file path, similarity score (to three decimal places), and a text excerpt of up to 300 characters with a "Show full text" toggle to expand the complete chunk text inline.
- **FR-004**: The system MUST construct a prompt that includes the retrieved chunks as numbered context entries and the user's original question, then submit this to the LLM to generate the answer.
- **FR-005**: The system MUST instruct the LLM to base its answer solely on the provided context, use numbered inline citations (e.g., [1], [2]) matching the chunk display order, and indicate when the context does not contain sufficient information to answer.
- **FR-006**: The system MUST provide an "Inspect prompt" view that shows the exact, unmodified text submitted to the LLM — system instruction, context block, and user question — in a collapsible panel beneath each answer.
- **FR-007**: The system MUST display a clear, actionable message when no relevant chunks are found and MUST NOT generate a speculative answer in this case.
- **FR-008**: If the knowledge base is empty (no documents ingested), the system MUST detect this before embedding the query and show a message directing the user to ingest documents, without making any embedding or LLM API call.
- **FR-009**: The retrieved chunks panel and the "Inspect prompt" panel MUST remain visible after the answer is generated so the user can compare the answer against the source material.

### Key Entities

- **QueryEmbedding**: The vector representation of the user's natural language question, produced by the same embedding model used for document ingestion.
- **RetrievedChunk**: A single result from the vector similarity search — containing the chunk text, source document name, file path, and similarity score.
- **RetrievalResult**: The ordered set of up to five RetrievedChunks returned for a given query, displayed to the user before answer generation.
- **AugmentedPrompt**: The full text submitted to the LLM — a system instruction, the five chunks formatted as numbered context entries with citation labels, and the user's original question.
- **GroundedAnswer**: The LLM response to the AugmentedPrompt, ideally citing the specific chunks it drew from.

## Success Criteria *(mandatory)*

### Measurable Outcomes

- **SC-001**: Retrieved chunks are displayed to the user within 3 seconds of submitting a query on a local developer machine with a populated knowledge base.
- **SC-002**: The "Inspect prompt" panel contains all five retrieved chunk texts verbatim and the original user question — verifiable by string comparison against the displayed chunk excerpts.
- **SC-003**: For queries where relevant content exists, the generated answer references at least one of the five displayed chunks (verifiable by checking for source name mentions or content overlap).
- **SC-004**: When the knowledge base is empty, no embedding API call and no LLM API call is made — only the informational message is shown. Verifiable by network monitoring or log inspection.
- **SC-005**: A user unfamiliar with RAG systems can identify which source document an answer came from within 30 seconds of receiving a response, using only the retrieved chunks panel.

## Clarifications

### Session 2026-03-18

- Q: Does this feature extend the existing Chat tab (feature 003) or create a separate search interface? → A: Enhance existing Chat tab — add chunk display and prompt inspection to feature 003's flow.
- Q: Should the system enforce a minimum similarity threshold, excluding chunks below it? → A: No threshold in v1 — always return up to 5 results regardless of score; the user judges relevance via the displayed similarity scores.
- Q: How should the LLM's answer cite retrieved chunks? → A: Numbered inline citations (e.g., [1], [2]) matching the numbered chunk display order.
- Q: Can users expand individual chunk excerpts inline to see the full text? → A: Yes — each chunk has a "Show full text" toggle to expand beyond the 300-character excerpt.
- Q: Is the system instruction in the augmented prompt hardcoded or user-configurable? → A: Hardcoded in v1 — fixed system instruction optimized for grounded RAG answers with numbered citations.

## Assumptions

- A single user accesses the system at a time; multi-user scenarios and authentication are out of scope.
- The knowledge base has already been populated via a separate ingestion step before this feature is used.
- The embedding model used for query embedding is the same model used during ingestion — no cross-model mismatch handling is required.
- Five chunks is the fixed retrieval count for v1; configurability is deferred to a future iteration.
- Chunk text excerpts default to 300 characters for initial display; each chunk has an inline "Show full text" toggle for the complete text. Full chunk text is also available in the "Inspect prompt" panel.
- The LLM call uses the same API credentials already configured for the system.
- Answer streaming is desirable if supported, but not required for v1.
- This feature enhances the existing Chat tab (feature 003) rather than creating a separate interface; chunk display and prompt inspection are additions to the current conversational flow.
- The system instruction used in the augmented prompt is hardcoded (not user-configurable); configurability is deferred to a future iteration.
