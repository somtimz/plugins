# Detail File Cross-Linking Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Add bidirectional cross-linking, inline notes with Open/Resolved lifecycle, integrity checks, and a generated index to the ea-assistant detail file system.

**Architecture:** Keep the flat `artifacts/details/` folder structure unchanged. Add `relatedItems: []` frontmatter and two new body sections (`## Notes`, `## Related Items`) to the template. Extend `ea-detail.md` with four new modes (`link`, `check`, `note resolve`, `index`) and update the existing `view` and `list` modes. Add `--detail {ID}` target to `ea-note.md`. Document everything in `detail-file-convention.md`. Bump version 0.9.45 → 0.9.46.

**Tech Stack:** Claude Code plugin framework — markdown instruction files with YAML frontmatter; no compiled code. Validation: `~/.bun/bin/bun .github/scripts/validate-frontmatter.ts ea-assistant/`. Working branch: `feat/detail-cross-linking-v0.9.46`.

---

## Pre-work: Create feature branch

- [ ] **Create and switch to feature branch**

```bash
git checkout -b feat/detail-cross-linking-v0.9.46
```

Expected: `Switched to a new branch 'feat/detail-cross-linking-v0.9.46'`

---

## Task 1: Update item-detail.md template

**Files:**
- Modify: `ea-assistant/templates/item-detail.md`

This task adds `relatedItems: []` to the frontmatter, and inserts `## Notes` and `## Related Items` sections immediately after the header metadata block (before `## Summary`). These sections appear in every new detail file from this point forward.

- [ ] **Step 1: Add `relatedItems` to frontmatter**

In `ea-assistant/templates/item-detail.md`, replace the closing frontmatter line `lastModified: {{YYYY-MM-DD}}` with:

```yaml
lastModified: {{YYYY-MM-DD}}
relatedItems: []
```

The full frontmatter block should now read:
```yaml
---
item: {{ID}}
type: {{item_type}}
title: {{item_title}}
engagement: {{engagement_name}}
parentArtifact: {{parent_artifact_path}}
created: {{YYYY-MM-DD}}
lastModified: {{YYYY-MM-DD}}
relatedItems: []
---
```

- [ ] **Step 2: Insert `## Notes` and `## Related Items` sections before `## Summary`**

In `ea-assistant/templates/item-detail.md`, find the line:

```
## Summary
```

Insert the following block immediately before it (after the `---` separator that follows the header metadata):

```markdown
## Notes

<!-- GUIDANCE: Inline notes and flags for this item.
     Add via /ea-note --detail {ID} or n: during sessions.
     Resolve via /ea-detail note resolve {ID}. -->

---

## Related Items

<!-- GUIDANCE: Cross-links to related detail files. Managed via /ea-detail link {ID1} {ID2}.
     The relatedItems frontmatter field is the source of truth; this table is derived from it. -->

| ID | Type | Title | Relationship |
|---|---|---|---|

---

```

After this edit the section order in the template body is:
`# {{ID}}` header → `**Type:**` / `**Parent Artifact:**` / `**Last Updated:**` → `---` → `## Notes` → `---` → `## Related Items` → `---` → `## Summary` → … remaining sections

- [ ] **Step 3: Validate frontmatter**

```bash
~/.bun/bin/bun .github/scripts/validate-frontmatter.ts ea-assistant/
```

Expected: `Validated 55 files: 0 errors, 0 warnings`
(The template is not a frontmatter-validated file — this just confirms no regressions elsewhere.)

- [ ] **Step 4: Commit**

```bash
git add ea-assistant/templates/item-detail.md
git commit -m "feat(ea-assistant): add relatedItems frontmatter and Notes/RelatedItems sections to detail template (v0.9.46)"
```

---

## Task 2: Add `link`, `check`, `note resolve`, and `index` modes to ea-detail.md

**Files:**
- Modify: `ea-assistant/commands/ea-detail.md`

This task appends four new mode sections to the end of `ea-detail.md`, after the existing `list` mode. Each mode is separated by `---`.

- [ ] **Step 1: Append the `link` mode**

After the last line of the `list` mode section in `ea-assistant/commands/ea-detail.md`, append:

```markdown

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
2. Locate the `## Related Items` table. Append a new row: `| [{ID2}]({ID2}.md) | {ID2-type} | {ID2-title} | {relationship} |` — read `type` and `title` from `{ID2}.md` frontmatter.
3. Set `lastModified` to today's date.
4. Write the file.

### Step 5 — Update ID2

Read `EA-projects/{slug}/artifacts/details/{ID2}.md`:
1. Add `{ID1}` to `relatedItems[]` frontmatter array.
2. Append a row to the `## Related Items` table: `| [{ID1}]({ID1}.md) | {ID1-type} | {ID1-title} | {inverse-relationship} |`
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

**Check 3 — Table/frontmatter sync:** Compare IDs in `relatedItems[]` against link targets appearing as `[{ID}]({ID}.md)` in the `## Related Items` table. Record IDs in frontmatter but missing from the table, and IDs in the table but missing from frontmatter.

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
```

- [ ] **Step 2: Validate frontmatter**

```bash
~/.bun/bin/bun .github/scripts/validate-frontmatter.ts ea-assistant/
```

Expected: `Validated 55 files: 0 errors, 0 warnings`

- [ ] **Step 3: Commit**

```bash
git add ea-assistant/commands/ea-detail.md
git commit -m "feat(ea-assistant): add link, check, note resolve, and index modes to /ea-detail (v0.9.46)"
```

---

## Task 3: Update `view` and `list` modes in ea-detail.md

**Files:**
- Modify: `ea-assistant/commands/ea-detail.md`

**`view` mode changes (lines 136–158):**

- [ ] **Step 1: Add Related Items navigation after file display**

Find the `view` mode section. After step 2 ("Read the file and display its full content"), add:

```markdown
   After displaying the content, if `relatedItems[]` in frontmatter is non-empty, show a navigation line:
   ```
   Related: {ID1} ({type1}), {ID2} ({type2}) — /ea-detail view {ID} to navigate
   ```
```

- [ ] **Step 2: Extend the actions menu**

Replace the current actions list:
```
   1. Edit a section
   2. Update lastModified to today
   3. Check consistency (verify parent artifact still references this file)
   4. Delete this detail file
   Enter a number or press Enter to close.
```

With:
```
   1. Edit a section
   2. Update lastModified to today
   3. Check integrity (link validity, back-link symmetry, table sync, open notes)
   4. Resolve a note
   5. Delete this detail file
   Enter a number or press Enter to close.
```

- [ ] **Step 3: Update action handlers**

Replace the current action handler descriptions:
```
   - **Edit a section:** prompt "Which section? (Summary / Narrative / Rationale / Risks / Costs / Issues / Concerns / Impact / Alternatives)". Show current content and accept replacement text.
   - **Update lastModified:** set `lastModified` in frontmatter to today's date. Confirm.
   - **Check consistency:** read the parent artifact; verify the `../details/{ID}.md` link exists in the expected table row. Report whether it is present or missing. If missing, offer to add it.
   - **Delete:** confirm — "This will permanently delete `artifacts/details/{ID}.md`. Continue? (y/n)". If yes, delete the file and remove the `[→](../details/{ID}.md)` link from the parent artifact's table (replace with `—`).
```

With:
```
   - **Edit a section:** prompt "Which section? (Notes / Related Items / Summary / Narrative / Rationale / Risks / Costs / Issues / Concerns / Impact / Alternatives)". Show current content and accept replacement text.
   - **Update lastModified:** set `lastModified` in frontmatter to today's date. Confirm.
   - **Check integrity:** run all four checks from the `check` mode against this single file (link integrity, back-link symmetry, table/frontmatter sync, open notes). Offer interactive fixes for any issues found.
   - **Resolve a note:** run the `note resolve {ID}` mode for this file.
   - **Delete:** confirm — "This will permanently delete `artifacts/details/{ID}.md`. Continue? (y/n)". If yes, delete the file, remove the `[→](../details/{ID}.md)` link from the parent artifact's table (replace with `—`), and remove this file's ID from `relatedItems[]` in any other detail files that reference it.
```

**`list` mode changes (lines 218–248):**

- [ ] **Step 4: Replace the list mode content**

Replace the entire `## Mode: list [phase]` section with:

```markdown
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
```

- [ ] **Step 5: Validate frontmatter**

```bash
~/.bun/bin/bun .github/scripts/validate-frontmatter.ts ea-assistant/
```

Expected: `Validated 55 files: 0 errors, 0 warnings`

- [ ] **Step 6: Commit**

```bash
git add ea-assistant/commands/ea-detail.md
git commit -m "feat(ea-assistant): update view and list modes in /ea-detail — related navigation, type grouping, open notes (v0.9.46)"
```

---

## Task 4: Add `--detail {ID}` support to ea-note.md

**Files:**
- Modify: `ea-assistant/commands/ea-note.md`

The `--detail {ID}` flag appends an inline open note to the `## Notes` section of a detail file — bypassing the separate note file creation flow.

- [ ] **Step 1: Add `--detail` to Step 3 in ea-note.md**

In `ea-note.md`, find the `### Step 3 — Determine mode` section. Before the existing `#### Artifact mode (when --artifact <id> is provided)` block, insert:

```markdown
#### Detail mode (when `--detail {ID}` is provided)

1. Check whether `EA-projects/{slug}/artifacts/details/{ID}.md` exists. If not: "No detail file found for `{ID}`. Create it first with `/ea-detail new {ID}`." — stop.
2. Read the detail file.
3. If a `## Notes` section exists, locate its end (the `---` separator or next `##` heading that follows it). If `## Notes` does not exist (legacy file), append `\n\n## Notes\n` before the next `##` heading.
4. Insert a new blockquote at the end of the `## Notes` section content (immediately before the closing `---` or next `##`):
   `> 📌 **{YYYY-MM-DD}:** {text} — **Open**`
5. Set `lastModified` in frontmatter to today's date.
6. Write the file.
7. Skip to Step 4 (confirm save), using path `artifacts/details/{ID}.md`.

The routing suggestions in Step 5 still apply after the confirm.
```

- [ ] **Step 2: Update argument-hint in frontmatter**

In `ea-note.md` frontmatter, replace:
```yaml
argument-hint: "[text] [--artifact <id>] | resolve <path>"
```
With:
```yaml
argument-hint: "[text] [--artifact <id>] [--detail <id>] | resolve <path>"
```

- [ ] **Step 3: Validate frontmatter**

```bash
~/.bun/bin/bun .github/scripts/validate-frontmatter.ts ea-assistant/
```

Expected: `Validated 55 files: 0 errors, 0 warnings`

- [ ] **Step 4: Commit**

```bash
git add ea-assistant/commands/ea-note.md
git commit -m "feat(ea-assistant): add --detail target to /ea-note for inline detail file annotations (v0.9.46)"
```

---

## Task 5: Update detail-file-convention.md

**Files:**
- Modify: `ea-assistant/skills/ea-artifact-templates/references/detail-file-convention.md`

- [ ] **Step 1: Append Cross-Linking section**

At the end of `detail-file-convention.md`, append:

```markdown

---

## Cross-Linking

Detail files can be cross-linked to each other using the `relatedItems` frontmatter field and the `## Related Items` section. This enables navigation between related items — for example, a requirement can link to the goal it supports and the capability it implements.

### Data model

Each detail file has a `relatedItems: []` frontmatter field containing the IDs of related items:

```yaml
relatedItems: ["G-001", "CAP-003"]
```

The `## Related Items` section holds a human-readable table with an optional relationship label:

```markdown
## Related Items

| ID | Type | Title | Relationship |
|---|---|---|---|
| [G-001](G-001.md) | Goal | Reduce operational costs | supports |
| [CAP-003](CAP-003.md) | Capability | Customer Data Management | implemented by |
```

Links use same-directory relative paths — all detail files share `artifacts/details/`, so `G-001.md` resolves to `artifacts/details/G-001.md`.

`relatedItems[]` frontmatter is the authoritative source. The `## Related Items` table is derived from it.

### Managing links

Use `/ea-detail link {ID1} {ID2} [relationship]` to create a bidirectional link in both files simultaneously. Default relationship: `related`.

Supported relationship labels and their automatic inverses:

| Forward | Inverse |
|---|---|
| `supports` | `supported by` |
| `implements` | `implemented by` |
| `constrains` | `constrained by` |
| `derived from` | `source of` |
| `related` | `related` |

Labels outside this table use `related` as the inverse.

### Consistency rules

- Every link must be bidirectional: if `A` lists `B` in `relatedItems[]`, `B` must list `A`.
- All IDs in `relatedItems[]` must have a corresponding detail file.
- Every ID in `relatedItems[]` must have a matching row in `## Related Items`, and vice versa.
- Run `/ea-detail check` to verify all three constraints across all detail files.
- `/ea-consistency --details` (Check D) also validates detail file link integrity.

---

## Inline Notes

Each detail file has a `## Notes` section for inline annotations with an Open/Resolved lifecycle.

### Format

**Open note:**
```markdown
> 📌 **{YYYY-MM-DD}:** {note text} — **Open**
```

**Resolved note:**
```markdown
> 📌 **{YYYY-MM-DD}:** {note text} — ~~**Open**~~ ✅ **Resolved {YYYY-MM-DD}:** {resolution text}
```

### Adding a note

- `/ea-note --detail {ID}` — appends an open note to the file's `## Notes` section
- `n: {text}` during any session where the detail file is in context — saves inline with source matching the active session type

### Resolving a note

- `/ea-detail note resolve {ID}` — lists open notes, prompts for selection and resolution text, updates the note in place
- Action 4 in `/ea-detail view {ID}` runs the same flow

### Visibility

- `/ea-detail check` flags detail files with unresolved open notes (Check 4)
- `/ea-detail list` shows an Open Notes column — `—` or `📌 N open`
- `/ea-detail index` shows open note counts in the generated `_index.md`
```

- [ ] **Step 2: Verify the file reads correctly**

Read the last 30 lines of `ea-assistant/skills/ea-artifact-templates/references/detail-file-convention.md` and confirm both new sections are present with correct headings.

- [ ] **Step 3: Commit**

```bash
git add ea-assistant/skills/ea-artifact-templates/references/detail-file-convention.md
git commit -m "docs(ea-assistant): add Cross-Linking and Inline Notes sections to detail-file-convention.md (v0.9.46)"
```

---

## Task 6: Version bump and documentation

**Files:**
- Modify: `ea-assistant/.claude-plugin/plugin.json`
- Modify: `.claude-plugin/marketplace.json`
- Modify: `ea-assistant/CLAUDE.md`
- Modify: `ea-assistant/commands/ea-help.md`
- Modify: `ea-assistant/docs/PRD.md`
- Modify: `ea-assistant/README.md`

- [ ] **Step 1: Bump plugin.json**

In `ea-assistant/.claude-plugin/plugin.json`, replace `"version": "0.9.45"` with `"version": "0.9.46"`.

- [ ] **Step 2: Bump marketplace.json**

In `.claude-plugin/marketplace.json`, find the ea-assistant entry and replace its `"version": "0.9.45"` with `"version": "0.9.46"`. The `description` field must remain identical to `plugin.json`.

- [ ] **Step 3: Bump CLAUDE.md**

In `ea-assistant/CLAUDE.md`, replace `**Current version:** 0.9.45` with `**Current version:** 0.9.46`.

- [ ] **Step 4: Update ea-help.md — /ea-detail row**

In `ea-assistant/commands/ea-help.md`, replace the `/ea-detail` row:
```
| `/ea-detail new\|view\|list\|sync` | Create, view, list, or sync optional item detail files — extended narrative, rationale, risks, costs, issues, concerns, impact, and alternatives for individual engagement items |
```
With:
```
| `/ea-detail new\|view\|list\|sync\|link\|check\|index` | Create, view, list, sync, cross-link, and check item detail files — with inline notes (Open/Resolved), bidirectional cross-links, integrity checks, and a generated type-grouped index |
```

Also update the argument-hint tip line for /ea-detail if present.

- [ ] **Step 5: Add PRD section 5.39**

In `ea-assistant/docs/PRD.md`, after the `### 5.38 Ad-hoc Note Capture with Lifecycle (v0.9.45)` section and its trailing `---`, insert:

```markdown
### 5.39 Detail File Cross-Linking and Organisation (v0.9.46)

**`/ea-detail link|check|note resolve|index`** — bidirectional cross-links, integrity checks, inline notes, and a generated index for item detail files.

- **Cross-linking:** `/ea-detail link {ID1} {ID2} [relationship]` creates a bidirectional link between two detail files, adding `relatedItems[]` frontmatter entries and `## Related Items` table rows in both files simultaneously. Relationship labels (`supports`, `implements`, `constrains`, `derived from`, `related`) are set with automatic inverses.
- **Integrity check:** `/ea-detail check [ID]` runs four checks — link file existence, back-link symmetry, table/frontmatter sync, and open notes count. Single-file mode offers interactive fixes.
- **Inline notes:** `/ea-note --detail {ID}` appends an open `📌` blockquote to a detail file's `## Notes` section. `/ea-detail note resolve {ID}` closes it in place with resolution text.
- **Generated index:** `/ea-detail index` writes `artifacts/details/_index.md` — items grouped by type, with related-item links, open note counts, and parent artifact links.
- **Improved list:** `/ea-detail list` now groups by type, adds an Open Notes column, supports `--type {type}` filtering, and shows a cross-link count in the footer.

---
```

- [ ] **Step 6: Update README.md**

In `ea-assistant/README.md`, find the section listing detail file capabilities and add:

```
- **Detail file cross-linking** — `/ea-detail link {ID1} {ID2}` creates bidirectional links between detail files with relationship labels; `/ea-detail check` verifies integrity; `/ea-detail index` generates a type-grouped navigation index; inline notes via `/ea-note --detail {ID}`
```

Add `link|check|index` to the `/ea-detail` entry in the commands table.

- [ ] **Step 7: Validate frontmatter**

```bash
~/.bun/bin/bun .github/scripts/validate-frontmatter.ts ea-assistant/
```

Expected: `Validated 55 files: 0 errors, 0 warnings`

- [ ] **Step 8: Commit**

```bash
git add ea-assistant/.claude-plugin/plugin.json .claude-plugin/marketplace.json ea-assistant/CLAUDE.md ea-assistant/commands/ea-help.md ea-assistant/docs/PRD.md ea-assistant/README.md
git commit -m "feat(ea-assistant): bump version to 0.9.46 — detail file cross-linking and organisation"
```

---

## Final validation

- [ ] **Run frontmatter validation one last time**

```bash
~/.bun/bin/bun .github/scripts/validate-frontmatter.ts ea-assistant/
```

Expected: `Validated 55 files: 0 errors, 0 warnings`

- [ ] **Spot-check ea-detail.md structure**

Read `ea-assistant/commands/ea-detail.md` and verify these mode headings exist in order:
- `## Mode: new <ID> [artifact-id]`
- `## Mode: view <ID>`
- `## Mode: sync <ID>`
- `## Mode: list [phase] [--type {type}]`
- `## Mode: link {ID1} {ID2} [relationship]`
- `## Mode: check [ID]`
- `## Mode: note resolve {ID}`
- `## Mode: index`

- [ ] **Spot-check item-detail.md section order**

Read `ea-assistant/templates/item-detail.md` and verify the body section order: `## Notes` → `## Related Items` → `## Summary` → `## Narrative` → `## Rationale` → `## Risks` → `## Costs` → `## Issues` → `## Concerns` → `## Impact` → `## Alternatives`

- [ ] **Check git log**

```bash
git log --oneline main..HEAD
```

Expected: 6 commits ahead of main (pre-work branch + 5 feature commits).
