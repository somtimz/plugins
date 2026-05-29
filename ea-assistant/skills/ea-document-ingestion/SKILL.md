---
name: ea-document-ingestion
description: This skill should be used when the user asks to "upload a document", "import a diagram", "read this Word file", "use this PDF as input", "parse the completed interview", "import my answers from Word", "ingest an existing architecture document", or when processing uploaded files to extract EA-relevant content for use in artifacts or interviews.
version: 0.9.55
---

# EA Document Ingestion

This skill handles reading, parsing, and converting uploaded documents and diagrams into clean intermediate files before passing them to the `ea-document-analyst` for EA mapping.

## Pipeline Overview

Every uploaded document passes through three stages:

```
Upload (uploads/)
      │
      ▼
ea-document-converter          ← this skill governs this stage
  Converts to .md or .mmd
  Writes to uploads/converted/
      │
      ▼
ea-document-analyst            ← EA mapping: what to extract and where it goes
  Maps content to artifacts
  Presents confirmation summary
      │
      ▼
Artifact population            ← user-confirmed writes with 📎 source attribution
```

The converter stage produces a single canonical text representation regardless of source format. The analyst always receives either a Markdown file or a Mermaid file — never raw binary formats.

## Supported File Types

| Format | Conversion target | Use case |
|---|---|---|
| `.md` / `.txt` | `.md` (pass-through) | Requirements, notes, existing artifacts |
| `.docx` (Word) | `.md` | Architecture docs, completed interview forms |
| `.pdf` | `.md` | Strategy documents, reports |
| `.xlsx` / `.csv` | `.md` (tables) | Requirements lists, stakeholder registers |
| `.mmd` | `.mmd` (pass-through) | Mermaid diagrams |
| `.dot` | `.mmd` | Graphviz diagrams |
| `.drawio` | `.mmd` | Draw.io diagrams |
| `.excalidraw` | `.mmd` | Excalidraw diagrams |
| `.png` / `.jpg` | `.md` (description + inferred diagram) | Architecture screenshots, scanned docs |
| `.xmi` / `.uml` | `{stem}-extract.md` | Sparx Enterprise Architect model export (UML/XMI) |
| `.archimate` | `{stem}-extract.md` | Archi model export (ArchiMate 3.x XML) |
| `.json` / `.csv` (LeanIX) | `{stem}-extract.md` | LeanIX Fact Sheet export (JSON or CSV) |

All uploaded files are stored in `EA-projects/{slug}/uploads/` before processing. Converted intermediates are written to `EA-projects/{slug}/uploads/converted/`.

## EA Tool Format Detection

The following formats are structured EA modelling tool exports and require specialized parsing distinct from document formats. When an EA tool format is detected:

1. Skip the `ea-document-converter` agent — these formats are not documents
2. Invoke `ea-document-analyst` directly with a format-specific extraction prompt
3. Present an element inventory grouped by type or ArchiMate layer BEFORE any artifact population
4. Require explicit user confirmation for each element group before writing

**Detection rules:**
- `.xmi` extension, OR `.xml` with `xmi:type` attributes or `<uml:Model>` root → Sparx EA XMI
- `.archimate` extension → Archi XML model
- `.json` with `data.allFactSheets` or `lxID` keys, OR `.csv` with `lxType` or `factSheetType` column → LeanIX export

Two-pass detection: extension first; content heuristic second (handles `.xml` files that may or may not be XMI). If detection is ambiguous, ask the user to confirm the format before proceeding.

See `references/ea-tool-format-guide.md` for complete parsing notes, element mappings, and known limitations per format.

## Document Processing Workflow

### Step 1: Receive and Store

1. Confirm the file path provided by the user
2. Note the file into `uploads/` with a timestamped name: `{YYYY-MM-DD}-{original-filename}`
3. Identify the file type from the extension

### Step 2: Convert (ea-document-converter)

Invoke the `ea-document-converter` agent with the file path. The agent:

1. Converts the file to `.md` (document types) or `.mmd` (diagram types)
2. Writes the output to `uploads/converted/`
3. Reports the output path and hands off

**Conversion targets by format:**

| Format | Output | Method |
|---|---|---|
| `.docx` | `{stem}.md` | Read tool → structured Markdown; headings, tables, lists preserved |
| `.pdf` | `{stem}.md` | Read tool → extracted text; heading levels inferred from whitespace |
| `.xlsx` / `.csv` | `{stem}.md` | Rows → Markdown table(s); one table per sheet |
| `.drawio` | `{stem}.mmd` | Parse `<mxCell>` XML → Mermaid flowchart |
| `.excalidraw` | `{stem}.mmd` | Parse `elements` JSON → Mermaid flowchart |
| `.dot` | `{stem}.mmd` | Translate nodes/edges → Mermaid graph |
| `.png` / `.jpg` | `{stem}.md` | View image → description + inferred Mermaid block |
| `.md` / `.txt` / `.mmd` | Pass-through | Copied with conversion header |
| `.xmi` / `.uml` | `{stem}-extract.md` | Skip converter — parse `<uml:Model>` → grouped element inventory |
| `.archimate` | `{stem}-extract.md` | Skip converter — parse `<archimate:model>` → elements by ArchiMate layer |
| `.json` / `.csv` (LeanIX) | `{stem}-extract.md` | Skip converter — parse Fact Sheets → grouped inventory by type |

The converter adds a provenance comment to every output file:
```
<!-- Converted from: {original-filename} | Date: {YYYY-MM-DD} | Source format: {ext} -->
```

### Step 3: EA Mapping (ea-document-analyst)

After conversion, invoke the `ea-document-analyst` agent with the converted file path. The analyst:

1. Reads the `.md` or `.mmd` from `uploads/converted/`
2. Maps content to EA artifacts and ADM phases
3. Flags ambiguous or incomplete content with `⚠️ Needs clarification`
4. Presents an extraction summary for user confirmation before writing anything

### Step 4: Write to Artifacts

Only after user confirmation:
1. Update relevant artifact files in `artifacts/`
2. Mark extracted fields: `📎 Source: uploads/{original-filename}`
3. Do not overwrite existing answered fields without explicit user approval

## Interview Form Special Case

When the uploaded document is a **completed interview Word form**:
- `ea-document-converter` converts the `.docx` to `.md` preserving the Q&A structure
- `ea-document-analyst` detects the interview form structure and applies the interview parsing workflow: maps each answer to its artifact field, applies answer state markers (`⚠️`, `➖`, etc.)

## Content Policy

- Never overwrite `Approved` artifacts from uploaded content without explicit user confirmation
- Always show the user what was extracted before writing it anywhere
- Mark all content sourced from uploads with `📎 Source: uploads/{filename}`
- Do not infer or generate content — only extract what is explicitly present in the source

## Additional Resources

- **`agents/ea-document-converter.md`** — Full conversion logic and format-specific methods
- **`references/file-format-guide.md`** — Detailed parsing notes per file format
- **`references/interview-form-structure.md`** — Interview Word export/import format specification
- **`references/ea-tool-format-guide.md`** — Parsing notes for EA tool export formats (Sparx XMI, Archi .archimate, LeanIX CSV/JSON)
