# Feature Specification: Document Ingestion Pipeline Skill

**Feature Branch**: `001-doc-ingestion-pipeline`
**Created**: 2026-03-15
**Status**: Draft
**Input**: User description: "Add a skill that enables the user to create a data pipeline that reads one or more documents, creates an embedding and stores the documents in a vector based repository"

## User Scenarios & Testing *(mandatory)*

### User Story 1 - Ingest Documents into Vector Store (Priority: P1)

A developer using the RAG-plugin wants to make a set of documents searchable via semantic
retrieval. They activate the skill, point it at their documents, and the pipeline runs
end-to-end: each document is read, converted into an embedding, and stored in the vector
repository so it can later be retrieved by a query.

**Why this priority**: This is the core value proposition — without ingestion, no
retrieval is possible. All other stories depend on this working first.

**Independent Test**: Can be fully tested by pointing the skill at two or three sample
documents, running the pipeline, and confirming the documents are retrievable from the
vector store with a semantic query.

**Acceptance Scenarios**:

1. **Given** a user has one or more documents available, **When** they activate the
   ingestion skill and specify the document sources, **Then** the pipeline reads each
   document, generates an embedding for its content, and stores both the content and
   embedding in the vector store with confirmation of success.
2. **Given** a document cannot be read (e.g., file not found, unreadable format),
   **When** the pipeline encounters it, **Then** the pipeline reports the failure clearly,
   skips that document, and continues processing the remaining documents without aborting.
3. **Given** the vector store is unavailable, **When** the pipeline attempts to store
   embeddings, **Then** the pipeline stops, reports the connection failure, and leaves no
   partial data in an inconsistent state.

---

### User Story 2 - Batch Ingest a Directory of Documents (Priority: P2)

A developer has a folder containing many documents and wants to ingest them all in one
operation without listing each file individually. They specify the directory as the source
and the pipeline discovers and processes all supported documents within it.

**Why this priority**: Individually listing files is impractical at scale. Batch ingestion
from a directory is the most common real-world ingestion pattern and significantly reduces
friction for users with existing document collections.

**Independent Test**: Can be fully tested by pointing the skill at a directory containing
at least five documents of mixed formats, running the pipeline, and confirming all
supported documents appear in the vector store.

**Acceptance Scenarios**:

1. **Given** a directory containing multiple documents, **When** the user specifies that
   directory as the source, **Then** the pipeline discovers all supported documents within
   it, processes each one, and reports how many were successfully ingested and how many
   were skipped or failed.
2. **Given** a directory containing unsupported file types alongside supported ones,
   **When** the pipeline runs, **Then** it processes only supported formats, clearly lists
   which files were skipped and why, and does not fail the entire batch.
3. **Given** an empty directory, **When** the user specifies it as the source, **Then**
   the pipeline reports that no documents were found rather than completing silently.

---

### User Story 3 - Incremental Ingestion of New or Updated Documents (Priority: P3)

A developer has already ingested a document set and now wants to add new documents or
replace previously ingested ones. They run the pipeline again and only new or changed
documents are processed; already-ingested, unchanged documents are skipped.

**Why this priority**: Re-processing an entire corpus to add a few documents is wasteful.
Incremental ingestion makes the pipeline practical for growing document collections.

**Independent Test**: Can be fully tested by ingesting an initial set of documents,
adding one new document and modifying one existing document, re-running the pipeline,
and confirming only the new and modified documents were processed.

**Acceptance Scenarios**:

1. **Given** documents already exist in the vector store, **When** the user runs the
   pipeline on the same source with no changes, **Then** the pipeline detects no new or
   changed documents and reports that the store is already up to date.
2. **Given** a new document is added to the source, **When** the pipeline runs,
   **Then** only the new document is processed and added to the store; existing entries
   are untouched.
3. **Given** an existing document has been modified, **When** the pipeline runs,
   **Then** the old embedding is replaced with a fresh one reflecting the updated content.

---

### Edge Cases

- What happens when a document exceeds the maximum embeddable size? The pipeline MUST
  split it into chunks and store each chunk as a separate retrievable unit with source
  attribution preserved.
- What happens when two documents share the same filename but live in different paths?
  Each MUST be treated as a distinct document identified by its full path.
- What happens when the embedding service is rate-limited mid-pipeline? The pipeline MUST
  retry up to 5 times with exponential backoff and jitter (maximum cumulative wait: 30s).
  If all retries are exhausted, the document MUST be marked as failed and reported in the
  summary; already-stored documents in the same run MUST NOT be re-processed.
- What happens when a document is empty? The pipeline MUST skip it with a clear report
  and not store an empty embedding.
- What happens when a document exceeds the maximum file size? The pipeline MUST skip it,
  report it as a failure with a clear message, and continue processing remaining documents.
  The default limit is 100 MB; it MUST be configurable via `pipeline.max_file_size_mb`
  in the config file.
- What happens when the exact same document is submitted twice in the same pipeline run
  (e.g., two sources pointing to the same file)? The pipeline MUST ingest it only once
  and report the duplicate as skipped.
- What happens when the registry database is corrupted or missing? The pipeline MUST
  treat all documents as new (re-ingest everything) and rebuild the registry from scratch.
- What happens when the configured embedding model changes but the vector store already
  holds embeddings from a prior model (potentially a different vector dimension)? The
  pipeline MUST detect this mismatch on startup by comparing the model stored in the
  collection metadata against the config value, abort immediately with exit code 1, and
  print a clear error message instructing the user to delete the vector store and
  registry and re-run to perform a full re-ingestion with the new model.
- What happens when a PDF is password-protected or encrypted? The pipeline MUST skip it
  and report that the file could not be decrypted, without aborting the batch.
- What happens when a PDF contains only scanned images (no selectable text)? The pipeline
  MUST skip it with a message that the file contains no extractable text.
- What happens when a `.doc` (legacy binary Word) file is encountered? The pipeline MUST
  skip it and report that only `.docx` is supported.
- What happens when a SharePoint source is unreachable (network error)? The pipeline MUST
  report the failure for that source and continue processing remaining sources.
- What happens when SharePoint authentication fails or expires mid-run? The pipeline MUST
  stop processing that source, report the auth failure with remediation guidance, and
  continue with other sources.
- What happens when the user lacks permission to a SharePoint folder? The pipeline MUST
  report a permission error for the affected folder and skip it without aborting.

## Requirements *(mandatory)*

### Functional Requirements

- **FR-001**: The skill MUST guide the user to define one or more named data sources in
  the project configuration file. Sources MAY be local filesystem paths or SharePoint
  document libraries. The pipeline MUST process all configured sources in a single run.
- **FR-001a**: A `--source PATH` CLI argument MAY be provided to override configured
  sources for a one-off local ingestion without modifying the config file.
- **FR-002**: The pipeline MUST read each specified document and extract its text content
  for embedding.
- **FR-003**: The pipeline MUST split documents that exceed the maximum embeddable size
  into smaller chunks, preserving source attribution for each chunk.
- **FR-004**: The pipeline MUST generate a semantic embedding for each document or chunk
  using an embedding provider defined in the project configuration file. The provider
  MUST NOT require selection at runtime; changing the provider requires editing the
  config file and re-running the pipeline.
- **FR-005**: The pipeline MUST store each document's content, its embedding, and its
  source metadata (origin path, ingestion timestamp) in the vector store.
- **FR-006**: The pipeline MUST support plain text (.txt), Markdown (.md), PDF (.pdf),
  and Word (.docx) document formats.
- **FR-006a**: For PDF files, the pipeline MUST extract all selectable text content.
  Scanned PDFs with no embedded text MUST be skipped with a clear explanation.
- **FR-006b**: For Word files, only the `.docx` format (Office Open XML) is supported.
  Legacy `.doc` binary files are out of scope and MUST be skipped with a clear
  explanation.
- **FR-007**: The pipeline MUST report a completion summary: total documents processed,
  number succeeded, number skipped, number failed, and reasons for each failure.
- **FR-017**: The pipeline MUST reject any document whose file size exceeds
  `pipeline.max_file_size_mb` (default: 100 MB), skipping it with a clear error message
  and continuing the batch. The limit MUST be configurable in the config file.
- **FR-008**: The pipeline MUST detect already-ingested documents whose content has not
  changed (via content hash) and skip them entirely — no re-embedding, no store update.
  A document MUST NOT be ingested more than once if its content is identical.
- **FR-008a**: When a previously ingested document has changed, the pipeline MUST delete
  ALL embeddings associated with the previous version of that document from the vector
  store BEFORE storing the new embeddings. No stale chunks from the old version MUST
  remain after re-ingestion.
- **FR-014**: The pipeline MUST maintain a persistent document registry that records, for
  each ingested document: its origin path or URL, source name, content hash, file size,
  ingestion timestamp (first and most recent), version count (how many times re-ingested),
  and chunk count. The registry MUST be a SQLite file readable by any sqlite3 client.
  No dedicated query command is provided in v1; the quickstart documents example sqlite3
  CLI queries.
- **FR-015**: The document registry MUST be updated atomically with the vector store
  operation — if the vector store write fails, the registry MUST NOT record the document
  as successfully ingested.
- **FR-016**: The pipeline MUST write log entries to a dedicated log file for every
  pipeline operation (source discovery, document read, chunk, embed, store, skip, fail).
  Each entry MUST follow the format `YYYY-MM-DD HH:MM:SS [LEVEL] message` (Python
  `logging` module format). The log file path MUST be configurable via `pipeline.log_path`
  in the config file (default: `.rag-pipeline.log`). Log output MUST be separate from
  the stdout summary and MUST NOT be suppressed on success.
- **FR-009**: The skill MUST auto-activate within a Claude Code session when the user
  expresses intent to ingest documents — explicit slash command invocation MUST NOT be
  the only way to trigger it.
- **FR-010**: The pipeline MUST store documents in a vector store defined in the
  project configuration file. The target store MUST NOT require selection at runtime;
  changing the store requires editing the config file.
- **FR-011**: The configuration file MUST support multiple named data sources of mixed
  types (local and SharePoint) defined as an array. All sources are processed per run
  unless `--source` overrides them.
- **FR-012**: The pipeline MUST support SharePoint Online document libraries as a source
  type. It MUST recursively list all supported file types in the configured folder and
  its sub-folders. Each SharePoint source MAY define an optional `max_depth` integer in
  the config (default: unlimited) to cap traversal depth; `max_depth = 1` means the
  configured folder only with no sub-folder recursion.
- **FR-013**: SharePoint sources MUST support two authentication modes configurable per
  source: (a) device code flow — user authenticates interactively via browser, suitable
  for interactive Claude Code sessions; (b) client credentials — service principal with
  client secret, suitable for unattended/automated runs. Credentials MUST be read from
  environment variables named in the config; they MUST NOT be stored in the config file.

### Key Entities

- **Document**: A source file to be ingested. Key attributes: source path, raw text
  content, file format, last-modified timestamp.
- **Chunk**: A sub-section of a document created when the document exceeds the maximum
  embeddable size. Attributes: parent document reference, chunk index, text content.
- **Embedding**: A numerical vector representation of a chunk's semantic content.
  Attributes: vector values, chunk reference, creation timestamp.
- **Vector Store Entry**: The persisted record combining chunk text and its embedding
  for retrieval. Attributes: embedding, source metadata, ingestion timestamp.
- **Pipeline Run**: A single execution of the ingestion process. Attributes: start time,
  end time, documents processed, success count, failure count, skip count.

## Success Criteria *(mandatory)*

### Measurable Outcomes

- **SC-001**: A user can ingest 10 documents end-to-end (read, embed, store) in under
  2 minutes on a standard development machine.
- **SC-002**: 100% of documents that fail to ingest produce a clear, actionable error
  message — zero silent failures.
- **SC-003**: Re-running the pipeline on an unchanged document set completes in under
  10% of the time taken by the initial ingestion run (incremental skip working).
- **SC-004**: A user with no prior experience of the plugin can successfully complete
  their first document ingestion within 5 minutes of activating the skill, guided solely
  by the skill's instructions.
- **SC-005**: Documents ingested via the pipeline are retrievable by a semantic query
  with a relevance match rate of at least 80% on a representative test set of 20 queries.

## Clarifications

### Session 2026-03-15

- Q: What logging approach should the pipeline use? → A: Dedicated log file (`.rag-pipeline.log`), path configurable via `pipeline.log_path` in config
- Q: How deep should SharePoint subfolder traversal go? → A: Recursive with a configurable max depth (`max_depth` per source in config, default unlimited)
- Q: Should the SharePoint device flow OAuth2 token be cached between runs? → A: No caching in v1; document as a known limitation (user must re-authenticate on every run)
- Q: How should users query the document registry? → A: sqlite3 CLI only — document example queries in quickstart; no dedicated command in v1
- Q: What retry policy should the pipeline use for embedding API failures? → A: 5 retries with exponential backoff and jitter (up to 30s total), then fail the document
- Q: What should happen when the configured embedding model changes but the vector store already has embeddings from a different model? → A: Detect model mismatch on startup, abort with a clear error and remediation instructions (delete store and re-ingest)
- Q: What format should log entries use? → A: Timestamped human-readable text — `YYYY-MM-DD HH:MM:SS [LEVEL] message` (Python logging module format)
- Q: Is there a maximum file size limit for individual documents? → A: 100 MB hard limit — files exceeding the limit are skipped with a clear error; configurable via `pipeline.max_file_size_mb`

## Assumptions

- SharePoint Online is the only supported remote source type in this version; other
  cloud storage (OneDrive personal, Google Drive, S3, etc.) is out of scope.
- SharePoint device flow tokens are NOT cached between runs in v1. The user must
  re-authenticate interactively on each pipeline run that uses a `device_flow` source.
  Token caching is a known limitation; `client_credentials` sources are unaffected.
- SharePoint on-premises (non-Online) is out of scope.
- The user is responsible for registering an Azure AD application and granting it the
  necessary SharePoint permissions before using a SharePoint source.
- The pipeline runs synchronously within the Claude Code session; background or async
  execution is out of scope.
- PDF and Word (.docx) support are included in this version. Legacy `.doc` format and
  scanned (image-only) PDFs are out of scope.
- Chunking uses a fixed-size character window with overlap as the default strategy;
  advanced strategies (semantic, sentence-boundary) are out of scope.
- The user has already configured their embedding provider credentials before invoking
  the skill; credential setup is out of scope for this feature.
