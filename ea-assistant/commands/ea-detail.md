---
name: ea-detail
description: Create, view, or list item detail files — extended narrative, rationale, risks, costs, issues, concerns, impact, and alternatives for individual engagement items
argument-hint: "new <ID> [artifact-id] | view <ID> | list [phase] [--type] | sync <ID> | link <ID1> <ID2> [rel] | check [ID] | note resolve <ID> | index"
allowed-tools: [Read, Write, Glob, Bash]
---

Create, view, or list detail files for individual engagement items.

## Overview

Detail files are optional companion documents for table rows in EA artifacts. They live at `artifacts/details/{ID}.md` and are linked from the `Details` column in artifact tables. See `skills/ea-artifact-templates/references/detail-file-convention.md` for the full convention.

**Link style:** all detail-link forms written or parsed by this command follow the engagement's `linkStyle` per `skills/ea-artifact-templates/references/link-conventions.md`. With `linkStyle: wikilink` (default for new engagements), write `[[{ID}\|→]]` (table cells — alias pipe escaped) instead of `[→](../details/{ID}.md)` and `[[{ID}]]` instead of `[{ID}](../details/{ID}.md)`; when parsing, recognise all forms regardless of setting.

## Instructions

If no engagement is active in context, prompt the user to run `/ea-open` first.

Read `engagement.json` to get the engagement `slug` and `name`.

---

## Mode: `new <ID> [artifact-id]`

Create a detail file for a specific engagement item.

### Step 1 — Validate the ID

Parse the prefix from `{ID}` (e.g. `G-001` → prefix `G`, `CAP-003` → prefix `CAP`). Verify the prefix is a recognised ID type from the ID Scheme table in `ea-assistant/CLAUDE.md`. If not recognised, warn: "Unrecognised ID prefix — continuing with type 'Unknown'."

Determine the `item_type` label from the prefix:

| Prefix | Type |
|---|---|
| `DRV` | Business Driver |
| `G` | Goal |
| `OBJ` | Objective |
| `STR` | Strategy |
| `ISS` | Issue |
| `PRB` | Problem |
| `OPP` | Opportunity |
| `MET` | Metric |
| `CAP` | Capability |
| `VS` | Value Stream |
| `UC` | Use Case |
| `GAP` | Gap |
| `WP` | Work Package |
| `REQ` | Requirement |
| `RIS` | Risk |
| `CON` | Stakeholder Concern |
| `ADR` | Architecture Decision Record |
| `PAD` | Pending Architecture Decision |
| `CST` | Constraint |

### Step 2 — Check for Existing File

Check whether `EA-projects/{slug}/artifacts/details/{ID}.md` already exists.

- If it exists: display its current content and ask: "A detail file for {ID} already exists. Open it for editing, or cancel?"
  - If editing: proceed as if `view` mode — show content with edit instructions.
  - If cancel: stop.
- If it does not exist: continue to Step 3.

### Step 3 — Locate the Parent Artifact

If `artifact-id` was provided as an argument, locate `EA-projects/{slug}/artifacts/**/{artifact-id}.md` using Glob.

If not provided, use the ID type to determine the likely parent artifact using the mapping table in `skills/ea-artifact-templates/references/detail-file-convention.md`. Search for the ID in each candidate artifact:
- Glob for the candidate file path(s)
- Grep the file content for the exact ID token (e.g. `G-001`)
- Report the first match as the parent artifact

If multiple matches are found (e.g. `GAP-NNN` appears in more than one gap-analysis), list them and ask the user to select the canonical parent.

If no match is found in the expected artifact, scan all `artifacts/**/*.md` for the ID.

If still not found, proceed with `parentArtifact: unknown` and note: "Could not locate {ID} in any artifact — you can fill in the parent artifact path manually."

### Step 4 — Extract Row Data and Related IDs

Read the located parent artifact. Find the table row whose first cell contains `{ID}` (or `[{ID}](...)`). Extract:
- The title or description from the second column (typically the item label or statement)
- The artifact file path relative to `EA-projects/{slug}/`

**Cross-link extraction:** Scan every cell in that table row for ID references (any `PREFIX-NNN` token where PREFIX is a recognised ID scheme prefix). Build a `relatedItems` list:

| Detected pattern | Relationship label | Example |
|---|---|---|
| ID in column header contains "Goal" or "Linked Goal" | `drives` / `achieves` | `G-001` in a Goal column → `{id: "G-001", rel: "achieves"}` |
| ID in column header contains "Objective" | `operationalizes` | `OBJ-001` in an Objective column → `{id: "OBJ-001", rel: "operationalizes"}` |
| ID in column header contains "Strategy" | `executes` / `supports` | `STR-001` in a Strategy column → `{id: "STR-001", rel: "supports"}` |
| ID in column header contains "Driver" | `driven by` | `DRV-001` in a Driver column → `{id: "DRV-001", rel: "driven by"}` |
| ID in column header contains "Issue" | `threatens` | `ISS-001` in an Issue column → `{id: "ISS-001", rel: "threatens"}` |
| ID in column header contains "Problem" | `blocks` | `PRB-001` in a Problem column → `{id: "PRB-001", rel: "blocks"}` |
| ID in column header contains "Capability" or "CAP" | `exercises` / `requires` | `CAP-001` in a Capability column → `{id: "CAP-001", rel: "requires"}` |
| ID in column header contains "Requirement" | `generates` / `satisfies` | `REQ-001` in a Requirement column → `{id: "REQ-001", rel: "satisfies"}` |
| ID in column header contains "Risk" | `threatened by` | `RIS-001` in a Risk column → `{id: "RIS-001", rel: "threatened by"}` |
| ID in column header contains "Constraint" | `bound by` | `CST-001` in a Constraint column → `{id: "CST-001", rel: "bound by"}` |
| Any other ID found in the row | `relates to` | Generic fallback |

**Rules:**
- Do not add the item's own ID to `relatedItems`
- Do not add duplicate IDs
- Extract IDs from comma-separated lists (e.g., `G-001, G-002`)
- Extract IDs from linked markdown (e.g., `[G-001](../details/G-001.md)`)
- If the column header does not match any pattern above, use `relates to`

### Step 5 — Create the Detail File

Ensure the directory exists: `EA-projects/{slug}/artifacts/details/`

Copy the detail file template from `templates/cross-cutting/item-detail.md`. Replace all placeholders:
- `{{ID}}` → the ID argument (e.g. `G-001`)
- `{{item_type}}` → the type label from Step 1
- `{{item_title}}` → the extracted title from Step 4 (or `⚠️ Not answered` if not found)
- `{{engagement_name}}` → from `engagement.json`
- `{{parent_artifact_path}}` → relative path to parent artifact (e.g. `phase-a/architecture-vision.md`)
- `{{parent_artifact_file}}` → parent artifact file name without extension (e.g. `architecture-vision`); if `linkStyle: markdown`, rewrite the Parent Artifact line as `[{{parent_artifact_name}}](../{{parent_artifact_path}})` instead
- `{{parent_artifact_name}}` → display name derived from artifact frontmatter `artifact:` field
- `{{YYYY-MM-DD}}` → today's date
- `{{related_items}}` → YAML list from Step 4 cross-link extraction; if empty, keep `[]`
- `{{related_items_table}}` → markdown table rows from Step 4 extraction; if empty, keep the header only

Write to `EA-projects/{slug}/artifacts/details/{ID}.md`.

### Step 6 — Link the Source Table Row

After creating the file, offer to update the parent artifact's table:

```
Detail file created at artifacts/details/{ID}.md

Link it in the source table now?

The {ID} row in {Parent Artifact} §{section} currently has no Details column (or has "—").
I can update it to [→](../details/{ID}.md).

Update the source table? (y/n)
```

If yes:
- Read the parent artifact
- Find the table row containing `{ID}` in the first cell
- If a `Details` column exists in the table header: replace `—` with `[→](../details/{ID}.md)` in the matching row
- If no `Details` column exists in the table: append `| Details |` to the header row, `|---|` to the separator row, and `| [→](../details/{ID}.md) |` to the matching row; set `| — |` for all other rows in that table
- Update `lastModified` in the artifact frontmatter to today's date
- Confirm: "Updated {Parent Artifact} — {ID} row now links to its detail file."

### Step 7 — Confirm

```
✅ Created artifacts/details/{ID}.md

Type | {item_type}
Title | {item_title}
Parent | {parent_artifact_path}
Related Items | {N} auto-detected from parent artifact table row

Edit the file now to add narrative, rationale, risks, costs, issues, concerns, impact, and alternatives.
Run /ea-detail view {ID} to open it again at any time.
```

---

## Mode: `view <ID>`

Open and display a detail file.

1. Check whether `EA-projects/{slug}/artifacts/details/{ID}.md` exists.
   - If not found: offer to create it — "No detail file found for {ID}. Create one now with `/ea-detail new {ID}`?"
2. Read the file and display its full content.
   After displaying the content, if `relatedItems[]` in frontmatter is non-empty, show a navigation line:
   ```
   Related: {ID1} ({type1}), {ID2} ({type2}) — /ea-detail view {ID} to navigate
   ```
3. Offer actions:
   ```
   Detail file: {ID} — {title}

   1. Edit a section
   2. Update lastModified to today
   3. Check integrity (link validity, back-link symmetry, table sync, open notes)
   4. Resolve a note
   5. Delete this detail file
   Enter a number or press Enter to close.
   ```
4. Handle selected action:
   - **Edit a section:** prompt "Which section? (Notes / Related Items / Summary / Narrative / Rationale / Risks / Costs / Issues / Concerns / Impact / Alternatives)". Show current content and accept replacement text.
   - **Update lastModified:** set `lastModified` in frontmatter to today's date. Confirm.
   - **Check integrity:** run all four checks from the `check` mode against this single file (link integrity, back-link symmetry, table/frontmatter sync, open notes). Offer interactive fixes for any issues found.
   - **Resolve a note:** run the `note resolve {ID}` mode for this file.
   - **Delete:** confirm — "This will permanently delete `artifacts/details/{ID}.md`. Continue? (y/n)". If yes, delete the file, remove the `[→](../details/{ID}.md)` link from the parent artifact's table (replace with `—`), and remove this file's ID from `relatedItems[]` in any other detail files that reference it.

---

## Mode: `sync <ID>`

Bidirectionally sync a detail file's Concerns and Issues sections with the parent artifact's Appendix A4 table.

### Step 1 — Locate the detail file

Check whether `EA-projects/{slug}/artifacts/details/{ID}.md` exists. If not: "No detail file found for {ID}. Create one first with `/ea-detail new {ID}`." — stop.

### Step 2 — Extract references from detail file

Read the detail file. Scan the **Concerns** section for `CON-NNN` references. Scan the **Issues** section for `ISS-NNN` and `PRB-NNN` references. Build two lists:
- `detail_concerns` — all CON-NNN IDs found in the Concerns section
- `detail_issues` — all ISS-NNN and PRB-NNN IDs found in the Issues section

### Step 3 — Read parent artifact A4 table

Read the parent artifact (from `parentArtifact` frontmatter field). Scan `## Appendix A4 — Stakeholder Concerns & Objections` for table rows whose ID or text can be associated with the current item's ID. Build:
- `a4_concerns` — CON-NNN rows in A4 whose concern text, subject, or Raised By field references `{ID}`

### Step 4 — Report sync gaps

Compare the two sets and report:

```
Sync report — {ID} ({title})
─────────────────────────────────────────────
Detail file → A4 (concerns in detail file not in A4):
  ⚠️ CON-002 referenced in detail file but not found in parent A4 table
  ⚠️ CON-005 referenced in detail file but not found in parent A4 table

A4 → Detail file (A4 concerns associated with this item but not in detail file):
  ⚠️ CON-007 is in A4 and relates to {ID} — not referenced in detail file Concerns section

✅ Issues section: no sync gaps found
```

If no gaps: "✅ {ID} is fully in sync — detail file and A4 are consistent."

### Step 5 — Offer resolution

```
How would you like to resolve these gaps?

  1. Push all (detail → A4) — add missing concerns from detail file to parent artifact A4
  2. Pull all (A4 → detail) — add missing A4 concerns to detail file Concerns section
  3. Both directions
  4. Select individual items
  5. Skip
```

Apply selected syncs:
- **Push (detail → A4):** append new rows to the A4 table in the parent artifact using the concern text from the detail file entry; assign the next available CON-NNN if none exists; set `Raised By` to `detail file`, `Status` to `Requires Attention`.
- **Pull (A4 → detail):** append `- CON-NNN: {concern text} — {Raised By}, {date}` to the detail file Concerns section.
- Update `lastModified` in both the detail file and the parent artifact frontmatter.

---

## Mode: `list [phase] [--type {type}]`

List all detail files in the engagement, grouped by type.

1. Glob `EA-projects/{slug}/artifacts/details/*.md`. Exclude `_index.md`.
2. For each file, read frontmatter: `item`, `type`, `title`, `parentArtifact`, `lastModified`, `relatedItems`. Count open notes by scanning `## Notes` for lines matching `— **Open**`.
3. If `phase` argument is provided, filter by phase: include only items whose `parentArtifact` path starts with the matching phase folder (e.g. `phase-a/`, `requirements/`).
4. If `--type {type}` argument is provided, filter to items whose `type` matches (case-insensitive, e.g. `--type goal`, `--type requirement`).
5. Group remaining items by `type`. Sort groups alphabetically. Within each group sort by ID.
6. Display with one type section per group:

```
Detail Files — {Engagement Name}
─────────────────────────────────────────────────────────────

### Goals
| ID | Title | Open Notes | Parent Artifact | Last Modified |
|---|---|---|---|---|
| [G-001](artifacts/details/G-001.md) | Reduce operational costs | — | [Architecture Vision](artifacts/phase-a/architecture-vision.md) | 2026-05-01 |

### Requirements
| ID | Title | Open Notes | Parent Artifact | Last Modified |
|---|---|---|---|---|
| [REQ-003](artifacts/details/REQ-003.md) | Reduce licensing spend | 📌 1 open | [Requirements Register](artifacts/requirements/requirements-register.md) | 2026-05-03 |

3 detail file(s) · 2 cross-links · 1 open note
```

Column rules:
- ID: `[{ID}](artifacts/details/{ID}.md)` — path from engagement root.
- Open Notes: `—` if zero; `📌 {N} open` if any.
- Parent Artifact: `[{display name}](artifacts/{parentArtifact})` — prefix `parentArtifact` frontmatter value with `artifacts/`.
- Cross-link count in footer: total entries across all `relatedItems[]` arrays ÷ 2.

If no detail files match:
```
No detail files found in this engagement.
Create one with: /ea-detail new {ID}
```

---

## Mode: `link {ID1} {ID2} [relationship]`

Create a bidirectional cross-link between two detail files.

### Step 1 — Validate both files

Check whether both `EA-projects/{slug}/artifacts/details/{ID1}.md` and `EA-projects/{slug}/artifacts/details/{ID2}.md` exist. If either is missing, stop with: "Detail file not found: `{missing-ID}`. Create it first with `/ea-detail new {missing-ID}`."

### Step 2 — Check for existing link

Read `{ID1}.md` frontmatter `relatedItems[]`. If `{ID2}` is already present, stop with: "`{ID1}` already links to `{ID2}`. Run `/ea-detail view {ID1}` to see existing links."

### Step 3 — Determine relationship labels

`relationship` defaults to `related` if not provided. Derive the inverse label:

| Forward | Inverse |
|---|---|
| `supports` | `supported by` |
| `implements` | `implemented by` |
| `constrains` | `constrained by` |
| `derived from` | `source of` |
| `related` | `related` |

If the provided label is not in this table, set inverse to `related`.

### Step 4 — Update ID1

Read `EA-projects/{slug}/artifacts/details/{ID1}.md`:
1. Add `{ID2}` to `relatedItems[]` frontmatter array.
2. Locate the `## Related Items` table. If the section does not exist in the file (legacy detail file created before this feature), append the following block before the next `##` heading or at end of file: `\n## Related Items\n\n| ID | Type | Title | Relationship |\n|---|---|---|---|\n`. Then append the new row: `| [{ID2}]({ID2}.md) | {ID2-type} | {ID2-title} | {relationship} |` — read `type` and `title` from `{ID2}.md` frontmatter.
3. Set `lastModified` to today's date.
4. Write the file.

### Step 5 — Update ID2

Read `EA-projects/{slug}/artifacts/details/{ID2}.md`:
1. Add `{ID1}` to `relatedItems[]` frontmatter array.
2. Locate the `## Related Items` table. If the section does not exist in the file (legacy detail file), append the section header and empty table before the next `##` heading or at end of file (same as Step 4). Then append the new row: `| [{ID1}]({ID1}.md) | {ID1-type} | {ID1-title} | {inverse-relationship} |`
3. Set `lastModified` to today's date.
4. Write the file.

### Step 6 — Confirm

```
✅ Linked {ID1} ↔ {ID2}
   {ID1} → {ID2}: {relationship}
   {ID2} → {ID1}: {inverse-relationship}
```

---

## Mode: `check [ID]`

Run link integrity and consistency checks on detail files.

- With no argument: scan all `EA-projects/{slug}/artifacts/details/*.md`, excluding `_index.md`.
- With `{ID}`: check only `EA-projects/{slug}/artifacts/details/{ID}.md`.

### Four checks per file

**Check 1 — Link integrity:** For every ID in `relatedItems[]`, verify `artifacts/details/{ID}.md` exists. Record missing files as broken links.

**Check 2 — Back-link symmetry:** For every ID in `relatedItems[]` whose file exists, read that file's `relatedItems[]`. Verify the current file's ID is present. Record one-way links.

**Check 3 — Table/frontmatter sync:** Compare IDs in `relatedItems[]` against link targets appearing as `[{ID}]({ID}.md)` in the `## Related Items` table. Use exact full-token matching — `G-001` must match `G-001` only, not `G-0010` or `G-001-alt`. Record IDs in frontmatter but missing from the table, and IDs in the table but missing from frontmatter.

**Check 4 — Open notes:** Scan `## Notes` for lines matching `— **Open**`. Count unresolved notes.

### Report format

```
/ea-detail check — {Engagement Name}
────────────────────────────────────────
{ID}    ✅ {N} links · 0 open notes
{ID}    ⚠️ broken link: {missing-ID} (file not found)
{ID}    ⚠️ one-way link: {linked-ID} does not link back
{ID}    ⚠️ table/frontmatter mismatch: {ID2} in relatedItems but missing from ## Related Items table
{ID}    ⚠️ {N} open note(s) — earliest: {YYYY-MM-DD}

{N} issue(s) found. Run /ea-detail check {ID} to fix interactively.
```

If no issues: `✅ All {N} detail file(s) passed integrity checks.`

### Interactive fix (single-file mode only)

After the report, offer to fix each issue:

- **Broken link:** "Remove `{missing-ID}` from `{ID}`'s relatedItems? (y/n)" — If yes: remove from `relatedItems[]` and remove the matching row from `## Related Items` table.
- **One-way link:** "Add back-link from `{linked-ID}` to `{ID}`? (y/n)" — If yes: add `{ID}` to `{linked-ID}`'s `relatedItems[]` and append a row to its `## Related Items` table with relationship `related`.
- **Table/frontmatter mismatch:** "Sync `## Related Items` table to match frontmatter? (y/n)" — If yes: regenerate table rows from `relatedItems[]`, preserving existing relationship labels where present and defaulting to `related` for new entries.
- **Open note:** "Navigate: `/ea-detail note resolve {ID}`"

---

## Mode: `note resolve {ID}`

Resolve an open inline note in a detail file.

### Step 1 — Locate the file

Check whether `EA-projects/{slug}/artifacts/details/{ID}.md` exists. If not: "No detail file found for `{ID}`." — stop.

### Step 2 — Find open notes

Read the file. Scan the `## Notes` section for blockquote lines matching `> 📌 **{date}:** {text} — **Open**`. Build a numbered list.

If none found: "No open notes in `{ID}`." — stop.

### Step 3 — Select a note

Display the numbered list:

```
Open notes in {ID}:
  1. {YYYY-MM-DD}: {note text}
  2. {YYYY-MM-DD}: {note text}
Select a note to resolve (1–N):
```

### Step 4 — Collect resolution text

Prompt: "Resolution: (describe what was done or decided)"

### Step 5 — Update the file

In the selected blockquote line, replace `— **Open**` with `— ~~**Open**~~ ✅ **Resolved {today}:** {resolution text}`.

Set `lastModified` to today's date in frontmatter. Write the file.

### Step 6 — Confirm

```
✅ Note resolved — artifacts/details/{ID}.md
```

---

## Mode: `index`

Generate `EA-projects/{slug}/artifacts/details/_index.md`. Overwrites any previous version.

### Step 1 — Collect detail files

Glob `EA-projects/{slug}/artifacts/details/*.md`. Exclude `_index.md`.

For each file, read frontmatter: `item`, `type`, `title`, `parentArtifact`, `relatedItems`. Count open notes by scanning `## Notes` for lines matching `— **Open**`. Derive parent artifact display name by reading the `artifact:` frontmatter field of the parent artifact file; fall back to filename without extension.

### Step 2 — Group by type

Group items by `type`. Sort groups alphabetically by type name. Within each group sort by ID.

### Step 3 — Write the index

Write `EA-projects/{slug}/artifacts/details/_index.md` with this structure:

```markdown
# Detail File Index — {Engagement Name}
_Generated: {YYYY-MM-DD} · {N} detail files · {M} cross-links · {K} open notes_

---

## {Type Group}

| ID | Title | Related Items | Open Notes | Parent Artifact |
|---|---|---|---|---|
| [{ID}]({ID}.md) | {title} | [{related-ID}]({related-ID}.md), ... | — | [{artifact-name}](../{parentArtifact}) |
| [{ID}]({ID}.md) | {title} | — | 📌 1 open | [{artifact-name}](../{parentArtifact}) |
```

Rules:
- One `## {Type Group}` section per type with at least one detail file.
- Related Items: comma-separated `[{ID}]({ID}.md)` links; `—` if `relatedItems` is empty.
- Open Notes: `—` if none; `📌 {N} open` if count > 0.
- Parent Artifact path from `details/` to `artifacts/{parentArtifact}`: use `../{parentArtifact}` (e.g. `../phase-a/architecture-vision.md`).
- Cross-link count M = total entries across all `relatedItems[]` arrays ÷ 2 (each link counted once).
- `_index.md` is excluded from all `check` operations — it is derived, not authoritative.

### Step 4 — Confirm

```
✅ Index written — artifacts/details/_index.md
   {N} detail files · {M} cross-links · {K} open notes
```
