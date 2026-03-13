# Requirements Sync — Format Parsing Rules

This reference defines the parsing rules for reading and synchronising requirements from external sources: Word (.docx), Excel (.xlsx), CSV, and Markdown. It specifies the expected structure, supported column and field name variations, merge/update behaviour, and how to handle malformed inputs.

---

## Overview

The EA Assistant can ingest requirements from four source formats. The goal of each parser is to extract a consistent **Requirement Record** regardless of format. The canonical fields of a Requirement Record are:

| Field | Type | Required | Description |
|---|---|---|---|
| `id` | String | Yes | Unique identifier (e.g., FR-001, NFR-023) |
| `category` | Enum | Yes | FR / NFR / CON / PRI / ASS |
| `title` | String | Yes | Short title (one line) |
| `statement` | String | Yes | The full requirement statement |
| `rationale` | String | No | Why this requirement exists |
| `source` | String | No | Origin of the requirement (document, workshop, person) |
| `priority` | Enum | No | Must / Should / Could / Won't (MoSCoW) |
| `status` | Enum | No | Draft / Agreed / Rejected / Superseded |
| `owner` | String | No | Person or role responsible for the requirement |
| `adm_phase` | String | No | TOGAF ADM phase this requirement primarily relates to |
| `notes` | String | No | Free-text notes |
| `tags` | List[String] | No | User-defined tags for filtering |

---

## Word (.docx) Format

### Expected Document Structure

The parser supports two Word document layouts for requirements:

#### Layout A — Table-based

The document contains one or more tables where each row is a requirement. The first row of each table is the header row.

Expected column header names (case-insensitive, leading/trailing spaces stripped):

| Canonical Field | Accepted Header Variations |
|---|---|
| `id` | `ID`, `Req ID`, `Requirement ID`, `Reference`, `Ref`, `No.`, `Number` |
| `category` | `Category`, `Type`, `Req Type`, `Requirement Type`, `Kind` |
| `title` | `Title`, `Name`, `Short Description`, `Summary` |
| `statement` | `Statement`, `Description`, `Requirement`, `Requirement Text`, `Detail`, `Full Text` |
| `rationale` | `Rationale`, `Justification`, `Reason`, `Why` |
| `priority` | `Priority`, `MoSCoW`, `Importance`, `Urgency` |
| `status` | `Status`, `State` |
| `owner` | `Owner`, `Responsible`, `Accountable`, `Lead` |
| `source` | `Source`, `Origin`, `Raised By` |
| `notes` | `Notes`, `Comments`, `Remarks` |

**Minimum required columns:** `id` (or an auto-assigned ID will be generated) and `statement`. All other columns are optional.

#### Layout B — Heading-per-requirement

Each requirement is expressed as a section in the document:

```
### FR-001: Support multi-currency invoicing

**Statement:** The invoicing module must support generation of invoices in the customer's preferred currency.

**Rationale:** The organisation has international customers who require invoices in EUR, GBP, and USD.

**Priority:** Must

**Owner:** Finance Systems Lead
```

The parser detects this layout when it finds Heading 3 paragraphs that begin with a requirement ID pattern (`[A-Z]+-\d+`). Each heading introduces a new requirement; bold-label paragraphs beneath it populate the fields.

Accepted bold label patterns for Layout B:

| Field | Accepted Labels |
|---|---|
| `statement` | **Statement:**, **Requirement:**, **Description:** |
| `rationale` | **Rationale:**, **Justification:**, **Reason:** |
| `priority` | **Priority:**, **MoSCoW:** |
| `status` | **Status:** |
| `owner` | **Owner:**, **Responsible:** |
| `source` | **Source:**, **Origin:**, **Raised By:** |
| `notes` | **Notes:**, **Comments:** |

### Auto-ID Assignment

If a requirement row in a table has no ID value, the parser assigns an ID in the format `AUTO-<n>` where `<n>` is a zero-padded sequential number (e.g., `AUTO-001`). These should be reviewed and replaced with formal IDs before the requirement record is finalised.

### Multi-table Documents

A document may contain multiple tables (e.g., one per requirement category, one per ADM phase). Each table is parsed independently. If the same `id` appears in multiple tables, the last occurrence wins (a merge warning is logged).

---

## Excel (.xlsx) Format

### Expected Structure

- **Single-sheet workbooks:** The active sheet (first sheet) is parsed as a single requirements register.
- **Multi-sheet workbooks:** Each sheet is parsed independently. The sheet name is used as a tag on all requirements parsed from that sheet (e.g., sheet "Phase B Requirements" adds the tag `Phase B`).

### Header Row Detection

The first non-empty row is treated as the header row. If the first row does not contain recognisable column headers (none match the accepted variations in the table above), the parser attempts row 2 as the header. If neither row 1 nor row 2 contains recognisable headers, a warning is raised and column names default to `Column_1`, `Column_2`, etc.

### Column Mapping

The same column name variations as the Word table format apply (see table above).

### Special Excel Behaviours

- **Data Validation dropdowns:** Cell values from Excel data validation lists are extracted as plain text. The dropdown options themselves are not extracted.
- **Conditional formatting and colour coding:** Cell background colour is optionally extracted as a `cell_colour` metadata field if a `coloured_status_mapping` is configured. This allows documents that use red/amber/green colour coding to be interpreted semantically. Default: colour is not extracted.
- **Excel Tables (Ctrl+T defined tables):** Named Excel Tables are detected and their structured name is used as the dataset identifier. Within a table, the table's own header row is used regardless of row position.
- **Merged cells in header rows:** If the header row contains merged cells spanning multiple columns, the merged header value is applied to all spanned columns. This is treated as a warning condition — column naming may be ambiguous.

### Handling Blank Rows

Blank rows (all cells empty) within the data range are skipped. A row where only the `id` column is blank is skipped with a warning unless other columns contain data, in which case an auto-ID is assigned.

---

## CSV Format

### Expected Structure

- Row 1: Header row.
- Rows 2+: Data rows.
- Delimiter: Auto-detected (comma, semicolon, tab — in that order of preference).
- Encoding: UTF-8 (with or without BOM). Falls back to Windows-1252 on decode error.

### Column Mapping

Same column name variations as above.

### Multi-file CSV Import

When multiple CSV files are provided in a single import operation, each file is treated as a separate sheet (analogous to Excel sheets). The filename (without extension) is used as a tag on all requirements from that file.

### Edge Cases

- **Quoted fields with embedded newlines:** Fully supported. A multi-line cell is imported as a single field value with `\n` preserved.
- **Inconsistent column counts:** Rows with fewer columns than the header are padded with empty values. Rows with more columns generate a warning; extra values are discarded.
- **BOM character in first header:** The BOM (`\uFEFF`) is stripped from the first column name.

---

## Markdown Format

### Expected Structure

Markdown requirements registers are supported in two layouts.

#### Layout A — Table

A Markdown table with a header row defining field names.

```markdown
| ID     | Category | Title                            | Statement                                           | Priority |
|--------|----------|----------------------------------|-----------------------------------------------------|----------|
| FR-001 | FR       | Multi-currency invoicing support | The invoicing module must support multiple currencies | Must    |
| NFR-001| NFR      | API response time                | 95% of API requests must complete within 200ms      | Must    |
```

Column name variations are the same as other formats. The header row separator (`|---|---|`) is ignored.

#### Layout B — Heading/paragraph

Each requirement is a section:

```markdown
## FR-001: Multi-currency invoicing support

**Statement:** The invoicing module must support generation of invoices in the customer's preferred currency.

**Priority:** Must

**Rationale:** International customers require invoices in EUR, GBP, and USD.
```

The heading level for individual requirements can be `##`, `###`, or `####`. The parser detects the heading level from the first requirement heading found and applies it consistently for the rest of the document.

Higher-level headings (`#` at level above the requirement heading level) are treated as section/category groupings. The section name is applied as a tag to all requirements within the section.

#### Layout C — List

A simpler list-based format where each list item is a requirement statement. This layout does not support structured fields; requirements are imported with only the `statement` field populated.

```markdown
## Functional Requirements

- The system must allow customers to self-register.
- The system must support password reset via email.
- The system must enforce multi-factor authentication for administrative users.
```

Auto-IDs are assigned in this layout.

---

## Merge and Update Behaviour

When requirements are imported from an external source into an existing requirements register, the following merge rules apply:

| Scenario | Default Behaviour |
|---|---|
| `id` not found in existing register | New record is created |
| `id` found; all fields identical | No change; record is marked as `confirmed` |
| `id` found; one or more fields differ | Fields are updated; the change is logged in the requirement's change history |
| `id` found in source but not in register (was deleted externally) | Record is NOT deleted by default; a `sync_deleted` flag is set for review |
| `id` in register but not in source | Record is retained as-is; no action taken |

### Conflict Resolution

If the same `id` exists in the register with `status: Agreed` and the incoming source attempts to change the `statement`, the update is flagged as a **conflict** rather than applied automatically. Conflicts are surfaced in the sync report for human review.

---

## Validation on Import

All imported requirements are validated against the following rules:

| Rule | Severity | Description |
|---|---|---|
| `id` must be non-empty | Error | Requirements without an ID after auto-assignment is attempted are rejected |
| `statement` must be non-empty | Error | A requirement with no statement text is rejected |
| `category` must be a valid enum value | Warning | Unknown categories are imported with category `UNKNOWN` and flagged |
| `priority` must be a valid MoSCoW value | Warning | Unknown priority values are imported as-is and flagged |
| `id` must be unique within the import batch | Warning | Duplicate IDs in the source result in only the last occurrence being imported; earlier occurrences are logged |
| `id` should follow the [CATEGORY]-[NNN] pattern | Info | IDs not matching the pattern are accepted but flagged for review |
