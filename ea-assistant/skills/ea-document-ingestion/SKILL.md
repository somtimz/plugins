---
name: EA Document Ingestion
description: This skill should be used when the user asks to "upload a document", "import a diagram", "read this Word file", "use this PDF as input", "parse the completed interview", "import my answers from Word", "ingest an existing architecture document", or when processing uploaded files to extract EA-relevant content for use in artifacts or interviews.
version: 0.1.0
---

# EA Document Ingestion

This skill handles reading, parsing, and extracting EA-relevant content from uploaded documents and diagrams. Extracted content is used to pre-populate artifact fields, guide interviews, or provide context for the EA engagement.

## Supported File Types

| Format | Use Case | Extraction Method |
|---|---|---|
| `.md` / `.txt` | Requirements, notes, existing artifacts | Read directly |
| `.docx` (Word) | Existing architecture docs, completed interview forms | Parse with pandoc or Read |
| `.pdf` | Strategy documents, reports | Read tool (if text-based) |
| `.xlsx` / `.csv` | Requirements lists, stakeholder registers | Parse rows/columns |
| `.mmd` | Mermaid diagrams | Read and display |
| `.dot` | Graphviz diagrams | Read and display |
| `.drawio` | Draw.io diagrams | Read XML and interpret |
| `.excalidraw` | Excalidraw diagrams | Read JSON and interpret |
| `.png` / `.jpg` | Architecture screenshots, scanned docs | View with image support |

All uploaded files are stored in `EA-projects/{slug}/uploads/` before processing.

## Document Processing Workflow

### Step 1: Receive and Store

1. Confirm the file path provided by the user
2. Copy or note the file into `uploads/` with a timestamped name: `{YYYY-MM-DD}-{original-filename}`
3. Identify the file type from the extension

### Step 2: Extract Content

**For Markdown / text files:**
- Read the file directly
- Identify headings, sections, and key content

**For Word documents (.docx):**
- Use the Read tool to read the file (Claude Code supports .docx reading)
- If the document is an **interview form** (contains Q&A structure), apply the interview parsing workflow below
- Otherwise, extract sections relevant to EA artifacts

**For Excel / CSV:**
- Parse rows as records
- Map columns to known fields (requirements ID, description, priority, status)

**For diagram files (.mmd, .dot, .drawio):**
- Read the file content
- Summarise the diagram structure and elements
- Identify ArchiMate elements, layers, and relationships where applicable

**For PDFs and images:**
- Use the Read tool with image/PDF support
- Extract visible text, tables, and diagram descriptions

### Step 3: Map to EA Context

After extraction, map content to the engagement:

1. Identify which **artifact** or **ADM phase** the content relates to
2. Extract individual field values where possible
3. Flag ambiguous or incomplete content with `⚠️ Needs clarification`
4. Present extracted content to the user for confirmation before writing to any artifact

### Step 4: Write to Artifacts

Only write to artifacts after user confirmation:
1. Update the relevant artifact file in `artifacts/`
2. Mark extracted fields as sourced from the uploaded document: `📎 Source: uploads/{filename}`
3. Do not overwrite existing answered fields without explicit user approval

## Interview Form Parsing

When a user imports a completed interview Word document:

### Expected Structure

Interview Word exports use a structured format:
```
## Question 1: [Question text]
**Answer:** [user's answer or SKIP or N/A]

## Question 2: [Question text]
**Answer:** [user's answer]
```

### Parsing Workflow

1. Read the document
2. Extract each Q&A pair
3. Map answers to the corresponding artifact fields
4. Preserve answer states:
   - Written answer → use as artifact field value
   - `SKIP` → mark as `⚠️ Not answered`
   - `N/A` → mark as `➖ Not applicable`
   - Empty → treat as skipped, not overriding existing values
5. Present a summary of extracted answers to the user before applying
6. Apply answers to the artifact and save a dated interview note

## Content Policy

- Never overwrite `Approved` artifacts from uploaded content without explicit user confirmation
- Always show the user what was extracted before writing it anywhere
- Mark all content sourced from uploads with `📎 Source: uploads/{filename}`
- Do not infer or generate content from uploads — only extract what is explicitly present

## Additional Resources

- **`references/file-format-guide.md`** — Detailed parsing notes per file format
- **`references/interview-form-structure.md`** — Full interview Word export/import format specification
