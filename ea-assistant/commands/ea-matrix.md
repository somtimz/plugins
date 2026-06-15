---
name: ea-matrix
description: Manage TOGAF relationship matrices — create, list, show, edit, and check grid artifacts (Actor/Role, Application/Data CRUD, Capability/Application, System/Technology, and 10 more) per ADM phase, with axis seeding from existing artifacts
argument-hint: "[list|new|show|edit|check] [key]"
allowed-tools: [Read, Write, Bash, Glob, Grep]
---

# /ea-matrix — TOGAF Relationship Matrices

Uses skill: `ea-artifact-templates` → `references/matrix-catalogue.md` (the catalogue) and `templates/seeds/matrix-template.md` (the template).

The catalogue is the single source of truth for axes, seed sources, marker vocabularies, grill checks, and elicitation questions. Never restate them here.

---

## Resolve context

Before executing any mode:
1. Resolve the active engagement: check context for slug; if none, scan `EA-projects/*/engagement.json` and ask the user to select. If no engagement exists, error: "No engagement is active. Run `/ea-open` or `/ea-new` first."
2. Load `engagement.json` — extract `slug`, `currentPhase`.
3. Read the catalogue: `skills/ea-artifact-templates/references/matrix-catalogue.md`.
4. If a `key` argument was given, look it up in the catalogue:
   - Unknown key → error listing the 14 valid keys.
   - Managed-elsewhere entry (Stakeholder Map, Requirements Traceability, Work Package/Gap, Requirement/Work Package) → print its **Managed by:** pointer and stop.
5. Matrix file path for a key: `EA-projects/{slug}/artifacts/{folder}/{key}-matrix.md` where `{folder}` is the catalogue entry's Folder.

Mode defaults to `list` when no arguments are given.

---

## Mode: `list`

1. For each of the 18 catalogue entries, determine status:
   - **➡️ managed elsewhere** — the 4 pointer entries; show the pointer.
   - **✅ exists** — the matrix file exists. Compute cell fill %: count non-empty body cells in the `## Matrix` table (cells after the first column, excluding the header and separator rows) divided by total body cells. Show `({pct}% filled, {status})` from frontmatter.
   - **⬜ recommended** — file does not exist.
2. Render grouped by phase (use the catalogue's Phase Index ordering). Mark the group matching `currentPhase` with `← current phase`.
3. Footer: `Create one with /ea-matrix new <key> · Validate with /ea-matrix check`

---

## Mode: `new <key>`

1. Resolve the key (see Resolve context). If the matrix file already exists, error: "{key}-matrix.md already exists — use `/ea-matrix edit {key}`."
2. **Seed axes.** Read the catalogue entry's Seed sources. For each axis, scan the listed engagement files for candidate entities (ID tokens like `CAP-\d{3}` where the axis is ID-based; otherwise table rows / list items naming the entity type). Present the candidates:
   ```
   Proposed rows ({rowEntityLabel}): {list}
   Proposed columns ({columnEntityLabel}): {list}
   Confirm, edit (add/remove), or enter axes manually:
   ```
   If a seed source file does not exist, say so and ask the user to provide that axis manually. Harvest any `[Matrix]`-relevant thoughts from `artifacts/{folder}/notes/brainstorm/brainstorm-notes.md` (category `relationships`) and offer them as additional candidates.
3. **Elicit cells (optional).** Ask: "Fill cells now, row by row? (y = guided / n = leave empty)". If yes: for each row, ask the catalogue's elicitation questions adapted to that row entity, and record markers using only the catalogue's Markers vocabulary for this key.
4. Create the phase folder if it does not exist. Write the matrix file from `templates/seeds/matrix-template.md`, substituting per the template's substitution notes. Set `lastModified` to today.
5. Register the artifact in `engagement.json → artifacts` (same shape as other artifacts: `id` `{key}-matrix`, `name`, `phase`, `file` `artifacts/{folder}/{key}-matrix.md`, `status` Draft, `version` 0.1.0) and update the engagement's `lastModified`.
6. Report: file path, axis sizes, fill %, and a reminder: "Run `/ea-matrix check {key}` after filling cells."

---

## Mode: `show <key>`

1. Resolve the key; if the file does not exist, error: "{key}-matrix.md not found — create it with `/ea-matrix new {key}`."
2. Render the full file: frontmatter summary line (name, phase, status, version, lastModified), then `## Matrix`, `## Legend`, `## Observations`, `## Open Questions`.
3. Footer: cell fill % and `Edit with /ea-matrix edit {key} · Validate with /ea-matrix check {key}`.

---

## Mode: `edit <key>`

1. Resolve the key; if the file does not exist, error and point to `new`.
2. **Stale-axis check first.** Re-scan the catalogue entry's Seed sources. List entities present in the sources but missing from the matrix axes (e.g. "CAP-009 exists in the Capability Model but has no row"), and axis entries no longer found in any source. Offer to add/remove each.
3. Guided edit menu:
   ```
   1. Add/remove rows or columns
   2. Update cells (pick a row, walk its cells)
   3. Edit Observations
   4. Edit Open Questions
   D. Done
   ```
   Cell values must use only the catalogue's Markers vocabulary for this key — reject others, showing the legal set.
4. On Done: bump the patch version in frontmatter, set `lastModified` to today, write the file, update `engagement.json → lastModified`.

---

## Mode: `check [<key>]`

1. If a key is given, check that one matrix; otherwise check every existing matrix file for the engagement (glob `EA-projects/{slug}/artifacts/*/[a-z]*-matrix.md`). Skip any file whose frontmatter has no `matrixKey` field or whose key is not a managed catalogue entry (e.g. `traceability-matrix.md`), printing `➡️ {filename} — managed elsewhere, skipped`.
2. For each matrix, run:
   - **Axes check:** row/column entity types match the catalogue entry's Axes.
   - **Marker check:** every non-empty cell uses only the catalogue's Markers vocabulary for this key.
   - **Orphan check:** the stale-axis comparison from `edit` step 2 (seed-source entities missing from axes, and vice versa).
   - **Catalogue grill checks:** each numbered item in the entry's Grill checks, evaluated against the matrix content (and `## Observations` where the check requires a note).
   - **Approval check:** if frontmatter `status: Approved` and `## Observations` is empty or `*(none yet)*`, flag: "Approved matrix with no observations — a filled matrix always exposes findings."
3. Report per matrix: `✅ passed / ⚠ failed / ❓ unverifiable` per check, then a one-line summary. This is the same check logic `/ea-grill` runs when grilling a matrix artifact — defined once, in the catalogue.
