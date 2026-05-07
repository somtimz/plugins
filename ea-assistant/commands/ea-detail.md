---
name: ea-detail
description: Create, view, or list item detail files — extended narrative, rationale, risks, costs, issues, concerns, impact, and alternatives for individual engagement items
argument-hint: "new <ID> [artifact-id] | view <ID> | list [phase]"
allowed-tools: [Read, Write, Glob, Bash]
---

Create, view, or list detail files for individual engagement items.

## Overview

Detail files are optional companion documents for table rows in EA artifacts. They live at `artifacts/details/{ID}.md` and are linked from the `Details` column in artifact tables. See `skills/ea-artifact-templates/references/detail-file-convention.md` for the full convention.

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

### Step 4 — Extract Row Data

Read the located parent artifact. Find the table row whose first cell contains `{ID}` (or `[{ID}](...)`). Extract:
- The title or description from the second column (typically the item label or statement)
- The artifact file path relative to `EA-projects/{slug}/`

### Step 5 — Create the Detail File

Ensure the directory exists: `EA-projects/{slug}/artifacts/details/`

Copy the detail file template from `templates/item-detail.md`. Replace all placeholders:
- `{{ID}}` → the ID argument (e.g. `G-001`)
- `{{item_type}}` → the type label from Step 1
- `{{item_title}}` → the extracted title from Step 4 (or `⚠️ Not answered` if not found)
- `{{engagement_name}}` → from `engagement.json`
- `{{parent_artifact_path}}` → relative path to parent artifact (e.g. `phase-a/architecture-vision.md`)
- `{{parent_artifact_name}}` → display name derived from artifact frontmatter `artifact:` field
- `{{YYYY-MM-DD}}` → today's date

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

Edit the file now to add narrative, rationale, risks, costs, issues, concerns, impact, and alternatives.
Run /ea-detail view {ID} to open it again at any time.
```

---

## Mode: `view <ID>`

Open and display a detail file.

1. Check whether `EA-projects/{slug}/artifacts/details/{ID}.md` exists.
   - If not found: offer to create it — "No detail file found for {ID}. Create one now with `/ea-detail new {ID}`?"
2. Read the file and display its full content.
3. Offer actions:
   ```
   Detail file: {ID} — {title}

   1. Edit a section
   2. Update lastModified to today
   3. Check consistency (verify parent artifact still references this file)
   4. Delete this detail file
   Enter a number or press Enter to close.
   ```
4. Handle selected action:
   - **Edit a section:** prompt "Which section? (Summary / Narrative / Rationale / Risks / Costs / Issues / Concerns / Impact / Alternatives)". Show current content and accept replacement text.
   - **Update lastModified:** set `lastModified` in frontmatter to today's date. Confirm.
   - **Check consistency:** read the parent artifact; verify the `../details/{ID}.md` link exists in the expected table row. Report whether it is present or missing. If missing, offer to add it.
   - **Delete:** confirm — "This will permanently delete `artifacts/details/{ID}.md`. Continue? (y/n)". If yes, delete the file and remove the `[→](../details/{ID}.md)` link from the parent artifact's table (replace with `—`).

---

## Mode: `list [phase]`

List all detail files in the engagement.

1. Glob `EA-projects/{slug}/artifacts/details/*.md`
2. For each file, read the frontmatter to extract: `item`, `type`, `title`, `parentArtifact`, `lastModified`
3. If `phase` argument is provided, filter by phase:
   - Determine which phase folder the `parentArtifact` belongs to (e.g. `phase-a/`, `phase-b/`)
   - Include only items whose parent artifact is in that phase folder
4. Display as a table:

```
Detail Files — {Engagement Name}
─────────────────────────────────────────────────────────────
| ID | Type | Title | Parent Artifact | Last Modified |
|---|---|---|---|---|
| G-001 | Goal | Reduce operational costs | Architecture Vision | 2026-05-01 |
| CAP-003 | Capability | Customer Data Management | Business Architecture | 2026-05-03 |
| WP-007 | Work Package | CRM Platform Replacement | Architecture Roadmap | 2026-05-05 |

3 detail file(s) · Run /ea-detail view {ID} to open any file.
```

If no detail files exist:
```
No detail files found in this engagement.
Create one with: /ea-detail new {ID}
```
