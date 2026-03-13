# Document Ingestion — File Format Parsing Guide

This guide describes how each supported file format is parsed by the EA Assistant document ingestion skill. For each format, it covers the parsing approach, what content is extracted, known limitations, edge cases, and how to handle problems.

---

## Supported Formats Overview

| Extension | Type | Primary Use in EA Context |
|---|---|---|
| `.md` | Markdown text | Architecture documents, requirement lists, interview templates |
| `.docx` | Word document | Formal architecture deliverables, interview forms, stakeholder documents |
| `.pdf` | PDF document | Read-only reference documents, regulatory texts, vendor specs |
| `.xlsx` | Excel workbook | Requirement registers, capability matrices, application portfolios |
| `.csv` | Comma-separated values | Tabular data exports from other tools, bulk requirement imports |
| `.mmd` | Mermaid diagram | Architecture diagrams as code (sequence, flowchart, C4, ER) |
| `.dot` | Graphviz DOT | Dependency graphs, integration maps |
| `.drawio` | Draw.io XML | Architecture diagrams (ArchiMate, block diagrams, network diagrams) |

---

## `.md` — Markdown

### Parsing Approach
Markdown files are parsed as plain text with structural interpretation:
- Headings (`#`, `##`, `###`, etc.) are extracted as structural anchors.
- Tables are parsed as structured data: the header row defines column names; subsequent rows are data rows.
- Bullet lists and numbered lists are parsed as item sequences under their nearest heading.
- Fenced code blocks (` ``` `) are treated as verbatim content — their language tag (if present) is noted.
- Inline markers used by the EA Assistant (e.g., `[SKIP]`, `[N/A]`, `<!-- answered -->`) are interpreted as answer state metadata (see Interview Form Structure guide).

### Content Extracted
- Document title (first `#` heading or filename if absent)
- Section hierarchy (headings and their nesting level)
- Table data (column names + rows as key-value records)
- Requirement statements (lines beginning with `REQ-`, `CON-`, `ASS-`, etc.)
- Answer state markers

### Known Limitations
- HTML embedded in Markdown (e.g., `<div>`, `<table>`) is not parsed as structured data — only the raw HTML text is preserved.
- Complex LaTeX math blocks are preserved as verbatim text, not interpreted.
- Markdown extensions (GFM task lists `- [ ]`, footnotes, custom directives) are partially supported: task list state is read; footnote definitions are extracted as plain text.

### Edge Cases
- A file with no headings is treated as a flat body of text; no structural extraction is possible.
- Tables with merged cells (which some renderers support via HTML) cannot be parsed correctly. Avoid these.
- Very long lines (>10,000 characters) may be truncated by some parsing paths; split content into multiple paragraphs.

---

## `.docx` — Microsoft Word Document

### Parsing Approach
DOCX files are ZIP archives containing XML. The parser extracts content from `word/document.xml`:
- Paragraphs with Heading styles (`Heading 1`–`Heading 9`) are treated as structural headings.
- Paragraph styles are inspected to identify lists, normal text, and custom styles.
- Tables in the document are parsed row by row; the first row is treated as the header unless the table has a defined header row style.
- Text runs including bold, italic, and highlight formatting are extracted; formatting is not retained in the structured output, only the text content.
- Comments (Word revision marks and comments) are optionally extracted as metadata.
- Tracked changes: by default, the accepted-changes view is parsed. Rejected changes are excluded.

### Content Extracted
- Full document text, structured by headings
- Table data
- Answer state markers in document text (if the document is an interview form export)
- Document properties (Author, Last Modified Date) from `docProps/core.xml`

### Known Limitations
- Complex embedded objects (Excel spreadsheets embedded as OLE objects within Word) are not extracted — only the placeholder text or icon label is captured.
- Text in headers, footers, and text boxes may not be extracted depending on the parser implementation; verify these sections do not contain critical content.
- Heavily formatted documents with custom styles may not map correctly to structural headings if headings are styled manually (font size + bold) rather than using Word's Heading styles.
- Password-protected documents cannot be parsed; remove protection before ingestion.
- DOCX files saved from Google Docs may have slightly different XML structures; test before ingestion at scale.

### Edge Cases
- A document with no Heading styles is parsed as a flat text blob.
- Tables with merged cells: the merged cell content is attributed to the first logical cell in the merge; subsequent cells in the merge range are empty.
- Very large documents (>100MB) may be slow to parse; consider splitting by section.

---

## `.pdf` — PDF Document

### Parsing Approach
PDF parsing extracts text using a text-layer extraction approach:
- Text is extracted in reading order (top-to-bottom, left-to-right per page).
- Headings are inferred from font size and weight differences relative to body text.
- Tables in PDF are notoriously difficult to parse: the parser uses whitespace alignment heuristics to reconstruct tabular structure.

### Content Extracted
- Raw text content per page
- Inferred section headings (heuristic — not guaranteed)
- Document metadata (Title, Author, CreationDate) from PDF metadata dictionary

### Known Limitations
- **Scanned PDFs** (images of pages with no text layer) cannot be parsed without OCR. If OCR is not available, the parser returns empty content.
- Tables in PDF are approximate: complex multi-column layouts, merged cells, or tables spanning page breaks are frequently mis-parsed. Always verify extracted table data.
- Footnotes and endnotes are often extracted inline with the body text at the point where the footnote marker appears.
- Multi-column layouts (e.g., two-column academic papers) may produce garbled text as columns are interleaved.
- Encrypted or access-restricted PDFs cannot be parsed without the password.

### Edge Cases
- PDFs with embedded fonts that are subsetted (common in professionally typeset documents) may produce garbled characters for uncommon Unicode glyphs.
- PDFs produced by scanning software with poor OCR quality will contain spelling errors in extracted text.
- Page numbers and headers/footers are extracted as text and may appear inline; post-processing is needed to remove them if clean body text is required.

### Recommended Pre-processing
- For table-heavy PDFs, export the tables to Excel before ingestion.
- For scanned PDFs, run OCR (e.g., Adobe Acrobat, ABBYY, or Tesseract) to embed a text layer before ingestion.

---

## `.xlsx` — Microsoft Excel Workbook

### Parsing Approach
XLSX files are ZIP archives containing XML. The parser processes each worksheet:
- The first non-empty row of each sheet is treated as the header row, defining column names.
- Subsequent rows are data rows, keyed by the column headers.
- Named ranges and defined tables (Excel Tables created with Ctrl+T) are detected and extracted as named datasets.
- Merged cells: the value of the merge is attributed to the top-left cell; all other cells in the merge range are empty.

### Content Extracted
- Sheet names and their data tables
- Column headers and row data
- Excel Table names and their data
- Cell notes/comments (if present, extracted as metadata attached to the cell)

### Known Limitations
- Formulas: only the computed value at the time of last save is extracted, not the formula itself. If the workbook has not been recalculated, values may be stale.
- Charts and embedded images are not extracted.
- Pivot tables: only the underlying data range is accessible; the pivot table view is not reconstructed.
- Worksheets hidden by the workbook author are not extracted by default; specify `include_hidden=true` in ingestion configuration if required.
- Password-protected sheets cannot be parsed.

### Edge Cases
- A worksheet with no header row (all data, no labels) is parsed as data with auto-generated column names (Column1, Column2, …). This produces poor structured output; always ensure a header row is present.
- Multi-line cell values (Alt+Enter within a cell) are extracted with the line break preserved as `\n`.
- Very wide worksheets (>100 columns) may have performance implications; consider splitting into multiple sheets.

---

## `.csv` — Comma-Separated Values

### Parsing Approach
CSV files are parsed as plain text with delimiter detection:
- The first row is treated as the header row.
- Delimiter is auto-detected: comma (`,`) is tried first, then semicolon (`;`), then tab (`\t`).
- Text enclosed in double quotes handles embedded delimiters and newlines.
- Encoding: UTF-8 is assumed; if parsing fails, UTF-8-BOM and Windows-1252 are tried.

### Content Extracted
- Column headers (row 1)
- Row data as key-value records

### Known Limitations
- No native support for multiple sheets — each CSV file represents one table.
- No formula support; values only.
- Mixed encoding in a single file (e.g., some rows UTF-8, some Latin-1) causes garbled output.
- Files exported from Excel with a BOM character at the start may include the BOM in the first column header. This manifests as a column named `﻿ID` instead of `ID`. Strip the BOM or re-save as UTF-8 without BOM.

### Edge Cases
- CSV files with inconsistent column counts per row: rows with fewer columns than the header are padded with empty values; rows with more columns than the header generate a parse warning and the extra values are discarded.
- Quoted fields containing newlines produce multi-line cells — these are valid CSV but may be mishandled by simple line-by-line parsers.

---

## `.mmd` — Mermaid Diagram

### Parsing Approach
Mermaid files contain diagram-as-code syntax. The parser:
1. Reads the file as plain text.
2. Identifies the diagram type from the first line (`graph`, `sequenceDiagram`, `classDiagram`, `erDiagram`, `C4Context`, etc.).
3. Extracts nodes, edges, and labels based on the diagram type's grammar.
4. Produces a structured representation: node list with IDs and labels; edge list with source, target, and relationship label.

### Content Extracted
- Diagram type
- Node/participant list with labels
- Edge/relationship list with direction and label
- Subgraph/group names (for graph diagrams)

### Known Limitations
- Mermaid syntax is version-sensitive. Features added in Mermaid v10+ (e.g., `architecture-beta` diagrams) may not be parseable by older parser versions.
- Rendering is not performed by the ingestion parser — only the structural data is extracted. To produce a rendered image, pass the `.mmd` content to a Mermaid rendering service.
- Complex flowchart styles and `style` directives are extracted but not interpreted semantically.

### Edge Cases
- A `.mmd` file with a Mermaid code block fence (` ```mermaid `) rather than raw Mermaid syntax is handled by stripping the fence before parsing.
- Syntax errors in the Mermaid source cause a parse failure for the entire diagram; partial extraction is not supported.

---

## `.dot` — Graphviz DOT

### Parsing Approach
DOT files are parsed using the Graphviz DOT grammar:
- `graph` (undirected) and `digraph` (directed) are both supported.
- Nodes and edges are extracted with their attribute maps (label, shape, color, etc.).
- Subgraphs (including `cluster_` subgraphs) are extracted as groups.
- The `label` attribute on nodes and edges is the primary human-readable identifier.

### Content Extracted
- Graph name
- Node list with label and attribute map
- Edge list with source, target, and label
- Cluster/subgraph names

### Known Limitations
- DOT `record` shape node labels (pipe-delimited field definitions) require special parsing to extract individual field labels.
- HTML-like labels (`<TABLE>` syntax inside DOT) are extracted as raw HTML strings, not as structured table data.
- Nested `subgraph` definitions beyond two levels of nesting may not preserve grouping correctly.

### Edge Cases
- Files with Windows line endings (CRLF) are handled transparently.
- DOT files that `include` other files (using C preprocessor directives) are not resolved — only the top-level file is parsed.

---

## `.drawio` — Draw.io XML

### Parsing Approach
Draw.io files are XML documents. The parser:
1. Reads the XML structure.
2. For each diagram page, extracts all `mxCell` elements.
3. Each cell has a `style` attribute (describing shape type), a `value` attribute (the label), and optional `vertex`/`edge` indicators.
4. Connections between cells are extracted as edges using the `source` and `target` attributes.
5. ArchiMate element types are inferred from the `shape=mxgraph.archimate3.*` style string.

### Content Extracted
- Page names
- Element list per page: label, shape type (inferred from style), position/size
- Edge list per page: source element, target element, label
- ArchiMate element type (where the style identifies an ArchiMate shape)
- Grouping/container relationships (cells inside container cells)

### Known Limitations
- Shape type inference is style-string pattern matching. Elements styled manually without the standard ArchiMate style name are not identified as ArchiMate elements.
- Compressed `.drawio` files (draw.io can save in a deflate-compressed XML format) must be decompressed before parsing. Standard files are uncompressed XML.
- Layer visibility (hidden layers in draw.io) is not honoured — all elements on all layers are extracted regardless of visibility.
- Element metadata added via draw.io's "Edit Data" feature (custom properties) is extracted as a property map if present in the XML.

### Edge Cases
- `.drawio` files exported from Confluence Draw.io plugin may have slight schema differences. Test ingestion before bulk processing.
- Very large diagrams (hundreds of elements per page) may produce a large structured output; consider filtering by page name if only specific views are needed.
