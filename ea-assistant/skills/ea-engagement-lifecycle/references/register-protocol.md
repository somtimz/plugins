# Register Protocol — Shared Mode Mechanics for Direction Registers

Single source of truth for the mechanics of the direction-register commands: `/ea-drivers`, `/ea-goals`, `/ea-issues`, `/ea-problems`, `/ea-gaps`. Each command file declares a **Register Spec** (identity, fields, links, trace chain, groupings) plus any register-specific checks; everything else — the mode flows below — comes from this protocol and is **never restated in the command file**.

## Register Spec (declared per command)

Each command declares:

| Spec element | Meaning |
|---|---|
| **Prefix / concept** | ID prefix (e.g. `G`) and concept name; concept definition lives in `ea-concepts.md` — never inline |
| **Storage** | The `engagement.json → direction.{array}` that is the single source of truth |
| **Register file** | Stable output path for `generate` (e.g. `artifacts/cross-cutting/goals-register.md`) |
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
7. Confirm with the spec's success message; if a link field is empty, emit the spec's orphan nudge (suggested `update` command).

## Mode: `update {ID} <field> <value>`

1. Find the entry by ID in the storage array. If not found, list valid IDs and stop.
2. Validate the field against the spec's field table; reject unknown fields with the valid list.
3. Generic validation (always applies):
   - Emptying a link field → warn "Removing all links will orphan this item. Continue? (y/n)"
   - Link values must match existing IDs in their target array/artifact; flag unknown IDs as broken references
4. Apply the spec's **status transitions** (extra prompts) and any field-specific rules.
5. Show the proposed change — `"{ID}: {field} — '{old}' → '{new}'"` — and ask "Apply? (y/n)".
6. On confirm: update `engagement.json`, set `lastModified: today`, confirm.

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
