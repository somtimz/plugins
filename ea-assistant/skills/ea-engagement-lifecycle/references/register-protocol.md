# Register Protocol — Shared Mode Mechanics for Direction Registers

Single source of truth for the mechanics of the direction-register commands: `/ea-drivers`, `/ea-goals`, `/ea-objectives`, `/ea-strategies`, `/ea-issues`, `/ea-problems`, `/ea-gaps`. Each command file declares a **Register Spec** (identity, fields, links, trace chain, groupings) plus any register-specific checks; everything else — the mode flows below — comes from this protocol and is **never restated in the command file**.

## Register Spec (declared per command)

Each command declares:

| Spec element | Meaning |
|---|---|
| **Prefix / concept** | ID prefix (e.g. `G`) and concept name; concept definition lives in `ea-concepts.md` — never inline |
| **Storage** | The `engagement.json → direction.{array}` that is the single source of truth |
| **Register file** | Stable output path for `generate` (e.g. `artifacts/cross-cutting/goals-register.md`) |
| **Display view** *(optional)* | The artifact section that renders this register for stakeholders (e.g. Architecture Vision `§3 Goals`), with a column → field mapping. `add`/`update` mirror changes into it (see Display View Sync below) |
| **Fields** | Table of: field, add-prompt text, valid values, required/optional |
| **Link fields** | Fields holding cross-references (target prefix + orphan semantics) |
| **Trace chain** | Upstream and downstream walks for `trace` |
| **Groupings** | How `list` and `generate` group items, and which counts appear in the summary header |
| **Checks** | Register-specific add/update checks (disambiguation, escalation, etc.) |
| **Status transitions** | Status values that require an extra prompt (e.g. Superseded → "by which?", Accepted → rationale required) |

## Step 0 — Resolve Active Engagement (all modes)

1. Check the conversation context for an active engagement slug.
2. If none found, scan `EA-projects/*/engagement.json` (excluding `.archive/`) and ask the user to select one.
3. Load `engagement.json` — extract: name, slug, currentPhase, direction.

## ID Assignment

1. Read the spec's storage array. If empty or missing, assign `{PREFIX}-001`.
2. Otherwise extract all IDs matching `{PREFIX}-\d{3}`, find the maximum numeric suffix N, assign `{PREFIX}-{N+1}` zero-padded to 3 digits.
3. IDs are permanent — never reused or reassigned, even if the item is removed. A removed/superseded item keeps its ID as a placeholder where the spec defines a closed status.
4. If a spec defines multiple series (e.g. `GAP` vs `GAP-M`), assign within the series selected by the spec's series rule.

## Mode: `list` (default)

1. Read the storage array. If empty, show the spec's empty-state message and stop.
2. Apply any filter flags from the command's argument-hint.
3. Render a summary header: total + counts per the spec's groupings, status counts, and a line per orphan/missing-data condition the spec defines (e.g. "Orphans: {N} with no linked driver", "No evidence: {N}").
4. Render the table grouped per the spec, statements truncated to 60 chars, link fields shown as comma-separated IDs or `—`.
5. After the table, emit the spec's flag lines (orphans, missing evidence, Critical/High unresolved, etc.) with the suggested follow-up command.

## Mode: `add`

1. Assign the next ID (above).
2. Run the spec's **pre-add checks** (e.g. Issue-vs-Problem disambiguation) — these may re-route to a sibling command and stop.
3. Prompt for each field in the spec's field order, showing valid values, defaults, and available link-target IDs from `engagement.json` where the field is a link field.
4. Run the spec's **post-prompt checks** (e.g. Two-Layers test, specificity/systemic warnings) — each asks "Proceed? (y/n)".
5. Show a confirmation preview (all captured fields; recommended-but-empty fields shown as `⚠️ None — recommended`). Ask "Add to engagement? (y/n)".
6. On confirm: append to the storage array, set `engagement.json → lastModified: today`.
7. Run **Display View Sync** (below) if the spec declares a display view.
8. Confirm with the spec's success message; if a link field is empty, emit the spec's orphan nudge (suggested `update` command).

## Mode: `update {ID} <field> <value>`

1. Find the entry by ID in the storage array. If not found, list valid IDs and stop.
2. Validate the field against the spec's field table; reject unknown fields with the valid list.
3. Generic validation (always applies):
   - Emptying a link field → warn "Removing all links will orphan this item. Continue? (y/n)"
   - Link values must match existing IDs in their target array/artifact; flag unknown IDs as broken references
4. Apply the spec's **status transitions** (extra prompts) and any field-specific rules.
5. Show the proposed change — `"{ID}: {field} — '{old}' → '{new}'"` — and ask "Apply? (y/n)".
6. On confirm: update `engagement.json`, set `lastModified: today`, run **Display View Sync** (below) if the spec declares one, confirm.

## Display View Sync (`add` and `update`)

`engagement.json` is the single source of truth; the display view is a rendered projection of it. After a confirmed `add` or `update`, mirror the change into the spec's display view so the stakeholder-facing artifact never drifts from the data:

1. Resolve the display artifact file (e.g. `artifacts/phase-a/architecture-vision.md`). If the file does not exist, skip silently — the section is rendered when the artifact is created.
2. Find the spec's section heading and its table. If the heading or table is missing, skip and note: "ℹ️ {artifact} has no {section} table — display view not updated."
3. **Add:** append a row using the spec's column → field mapping, following the table's existing row conventions (`—` for unmapped columns; ID and Details links per the engagement's `linkStyle` — see `skills/ea-artifact-templates/references/link-conventions.md`). Remove any remaining `{{placeholder}}` template rows when adding the first real row.
4. **Update:** find the row whose first cell contains the item's ID and rewrite only the mapped cells; preserve unmapped cells. If no row matches, append as in step 3.
5. Update the artifact's `lastModified` frontmatter field. Do not change `status`, `reviewStatus`, or `version`.

Never edit the display view in the other direction — content found in artifact tables but absent from `engagement.json` is drift, surfaced by `/ea-status --direction`, and resolved by importing into the register (`add`) or correcting the artifact.

## Mode: `trace [{ID}]`

**Without ID** — matrix: one row per item with statement (60 chars), key classification columns, each chain link column, and an `Orphan?` flag per the spec's orphan rule.

**With ID** — full chain block: item header (classification fields + evidence/rationale), then one section per spec chain hop (upstream first, then lateral, then downstream), each entry as `{✅|⚠️|🔴} {ID} — {statement}`. Close with `Chain status: {✅ Complete | ⚠️ Partial | 🔴 Orphan}`.

Always flag referenced IDs that do not exist in `engagement.json` (or the named artifact for WP/REQ hops) as broken links.

## Mode: `generate`

1. Read the storage array.
2. If the spec's register file already exists, archive it to `snapshots/` per `skills/ea-artifact-templates/references/register-snapshot-convention.md`.
3. Write the register to the spec's stable path with frontmatter:
   ```yaml
   ---
   artifact: {Concept} Register
   artifactId: {register-id}
   engagement: {name}
   phase: cross-cutting
   status: Draft
   generated: {YYYY-MM-DD}
   relatedArtifacts: {per spec}
   diagrams: []
   links: []
   ---
   ```
   Body: title, engagement/date/total header, `## Summary` count table (totals, statuses, orphan/missing-data counts), then one `###`-grouped section per the spec's grouping with a `#### {ID}: {statement truncated}` field table per item (all spec fields plus link fields).
4. Register the artifact in `engagement.json → artifacts[]` (single entry at the stable path; update a legacy dated entry rather than adding).
5. Confirm: `"{Concept} Register written to {path} — {N} items."`

## Common Edge Cases (all registers)

| Scenario | Handling |
|---|---|
| Empty storage array | Spec's empty-state message: where to capture items first |
| Duplicate ID in array | Report; offer to renumber the second entry to next free ID (y/n) |
| Link references unknown ID | Flag as broken link; suggest the target register's `list` command |
| Orphan item | Flag in `list` and `trace` per the spec's orphan rule; suggest the linking `update` command |
| Unknown field in `update` | Reject; show the spec's valid field list |
| Display artifact missing or section absent | Skip Display View Sync silently (file) or with an ℹ️ note (section); never create the artifact |
| ID found in display table but not in storage array | Drift — do not delete from the table; suggest `add` to import it into the register |
