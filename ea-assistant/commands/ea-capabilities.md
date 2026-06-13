---
name: ea-capabilities
description: Create, edit, map, and score business capabilities (CAP-NNN) in the Business Architecture capability model. list/add/update/map render and edit the hierarchy; score assigns Completeness + Quality; adopt seeds from the Architecture Repository's canonical capability map.
argument-hint: "[list|add|update|map|score|adopt] [CAP-NNN] [field value] [--level L1|L2|L3] [--type Business|Technology] [--domain name]"
allowed-tools: [Read, Write, Bash, Glob]
---

You are executing the `/ea-capabilities` command. For the **Capability** and **Capability Model** concept — what a capability is (an ability to achieve an outcome, independent of who/how/what), its components (people/process/information/technology/resources), attributes (strategic importance/maturity/cost/risk/performance), the realization chain, the value it must articulate, and what it is *not* (process, org chart, value stream) — read `skills/ea-artifact-templates/references/ea-concepts.md` (**Capability Model**). For capability-based planning method, read `skills/ea-engagement-lifecycle/references/capability-based-planning.md`. Do not restate definitions here.

Capabilities are **mastered in the Business Architecture artifact** — the `## 3. Capability Model` table in `artifacts/phase-b/business-architecture.md` is the single source of truth (there is no `engagement.json` capabilities array). This command reads and edits that table in place. The capability matrices (`/ea-matrix` — capability×value-stream / ×application / ×organization) hold the typed relationships.

## Capability table columns

`CAP-NNN | Level | Capability Type | Domain | Capability | Value / Outcome | Description | Current Maturity | Target Maturity | Supports (STR-NNN / G-NNN) | Details`

- **Level** — L1 (domain) / L2 (capability) / L3 (sub-capability); the map is box-in-box, hierarchical, **not** flow-based
- **Capability Type** — Business (delivers stakeholder value; survives EA team) / Technology (enables/governs how the org operates)
- **Value / Outcome** — the business outcome this capability enables (the value it brings); a capability with no value and no `Supports` anchor is flagged for removal (capability inflation)
- **Current / Target Maturity** — Absent / Immature / Developing / Mature
- **Supports** — STR-NNN strategies or G-NNN goals it enables (strategy→capability traceability)

If a legacy capability table lacks the `Value / Outcome` column, add it (insert after `Capability`) before writing.

## Step 1 — Resolve Engagement & Artifact

1. Resolve the active engagement (context, else scan `EA-projects/*/engagement.json`). Load `engagement.json`.
2. Locate `artifacts/phase-b/business-architecture.md`. If it does not exist: "No Business Architecture yet — run `/ea-artifact create business-architecture` first (the capability model lives in it)." Stop unless mode is `adopt` (which can create it).
3. Read its `## 3. Capability Model` table.

## Modes

### `list` (default)
Render the capability hierarchy grouped by L1 domain, showing Type, Current→Target maturity, Value/Outcome (truncated), and Supports. Header: total caps, counts by Type and by Current Maturity. Then flag lines:
- `⚠️ No value/outcome: {CAP list}` · `⚠️ No strategic anchor (orphan): {CAP list}` · `⚠️ No target maturity: {CAP list}` · `⚠️ L2/L3 with no parent: {CAP list}`
- Possible duplication: capabilities with near-identical names → "review for capability inflation".

### `add`
1. Assign the next `CAP-NNN` (scan all `CAP-\d{3}` in the table, max + 1).
2. Prompt in order: **Level** (L1/L2/L3) → if L2/L3, **Parent** (CAP-NNN) → **Capability Type** (Business/Technology) → **Domain** (L1 group) → **Name** (a noun; reject verb-noun process names with a warning) → **Value / Outcome** (the business outcome it enables — required; "what do we gain by being able to do this?") → **Description** → **Current Maturity** → **Target Maturity** → **Supports** (list available STR-NNN/G-NNN from `engagement.json → direction`).
3. **Process-name check:** if the name reads as a process (starts with a verb, or matches "process/manage/handle X" as an action), warn: "⚠️ '{name}' looks like a process (how), not a capability (what). A capability is a noun — e.g. 'Order Management', not 'Process Orders'. Proceed? (y/n)".
4. **Value check:** if Value/Outcome is empty, warn it will be flagged as inflation; offer to add one.
5. Show a preview, confirm, then append the row in the correct domain group (keep L1→L2→L3 ordering). Update the artifact `lastModified`. Confirm: "CAP-NNN added under {domain}. Link it to a value stream with `/ea-matrix` (capability-value-stream)."

### `update CAP-NNN <field> <value>`
Validate `<field>` against the columns (level, type, domain, name, value, description, currentMaturity, targetMaturity, supports, parent). Apply the same process-name and value checks. Show old→new, confirm, write, update `lastModified`.

### `map`
Render the capability model as a hierarchical **box-in-box map** (no arrows — it is not a flow): an indented text tree (L1 → L2 → L3) annotated with Current→Target maturity, and a Mermaid `graph TD` (or `flowchart`) hierarchy. Offer to write it to `diagrams/capability-map.{mmd}` and register it. A heatmap variant: colour/annotate by maturity gap (Target − Current) to surface investment priorities.

### `score`
Score the capability model on **Completeness** and **Quality** (0–100 + band), using `skills/ea-engagement-lifecycle/references/grill-scoring-rubric.md` specialised for capabilities:
- **Completeness** — share of capabilities with: a Value/Outcome, Current and Target maturity, a `Supports` anchor, and (for L2/L3) a parent; plus whether the model covers the enterprise scope implied by the strategies/value streams.
- **Quality** — capabilities are outcome-based **nouns** (not processes); no duplication / inflation; each is value-stream traced (via `/ea-matrix`); Business vs Technology correctly classified; value statements are concrete (an outcome, not a restatement of the name); differentiating vs commodity is distinguishable; **readability** of names and value statements.
Output the two scores, a per-capability flag table (✅ / ⚠️ with the issue), and the three weakest capabilities. Note this scores the capability model specifically; `/ea-score business-architecture` scores the whole artifact.

### `adopt`
Seed capabilities from the Architecture Repository's **canonical capability map** (`Architecture-Repository/capability-library/canonical-capability-map.md`), if the engagement is linked (`engagement.json → repoPath`).
1. If no repo linked: "No Architecture Repository linked — run `/ea-repo link` first, or add capabilities manually with `/ea-capabilities add`."
2. Read the canonical map; show its L1 domains and let the user pick which domains/branches to adopt (`all`, or a domain list).
3. For each adopted capability, allocate a fresh engagement CAP-NNN, copy name + description + suggested value/outcome, set Current Maturity = Absent (to be assessed), and record `Source: canonical {canonical-id}` in the Details. Append to the Business Architecture table.
4. Confirm count adopted; suggest `/ea-capabilities list` then assess maturity and `Supports`.

## Edge Cases

| Scenario | Handling |
|---|---|
| No capability table / empty | "No capabilities yet. `/ea-capabilities add`, or `/ea-capabilities adopt` to seed from the canonical map." |
| Capability with no `Supports` | Flag as orphan in `list`/`score`; suggest linking to a strategy/goal or removing |
| Verb-noun (process) name | Warn it is a process, not a capability (see `add`) |
| Duplicate/near-duplicate names | Flag as possible capability inflation; suggest merge |
| `adopt` but no repo | Direct to `/ea-repo link` or manual `add` |
