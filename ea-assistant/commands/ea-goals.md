---
name: ea-goals
description: Manage goals — list, add, update, trace to drivers and objectives, and generate a Goals Register
argument-hint: "[list|add|update|trace|generate] [G-NNN] [--domain Business|Technology|Data|Application|Cross-cutting] [--type Strategic|Operational|Capability|Compliance] [--priority High|Medium|Low]"
allowed-tools: [Read, Write, Bash]
---

You are executing the `/ea-goals` command.

## Overview

Goals are **qualitative statements of a desired future state** — where the organisation wants to be. They sit in the middle of the motivation chain (DRV → **G** → OBJ → WP). Every goal must trace to at least one Business Driver; every goal should be operationalised by at least one Objective.

Goals are distinct from:
- **Business Drivers** — the external/internal forces that make change necessary; Goals are the desired response to those forces
- **Objectives** — the measurable, time-bound operationalisation of a goal; an Objective is the "how far and by when" child of a Goal
- **Strategies** — the chosen approach to *achieve* a goal; Strategies are how, Goals are where
- **EA Goals** — Goals about EA team capability (e.g. "Establish AI governance") belong in the Governance Framework, not the Architecture Vision. Apply the Two-Layers test: *Would this still exist if the EA team were disbanded?*

Goals are stored in `engagement.json → direction.goals[]`. They also appear in Architecture Vision §3 — the register is the management interface; Architecture Vision is the primary display view.

**Modes:**
- `list` (default) — read goals from `engagement.json`, render a table grouped by Domain
- `add` — interactively capture a new goal and write it to `engagement.json`
- `update` — update a single field on an existing goal (`/ea-goals update G-NNN <field> <value>`)
- `trace` — show the upstream (Drivers) and downstream (Objectives, Strategies, Work Packages) motivation chain
- `generate` — produce a printable Goals Register artifact

**Filters:**
- `--domain` — filter by architecture domain
- `--type` — filter by goal type
- `--priority` — filter by priority

---

## Step 1 — Resolve Active Engagement

1. Check the conversation context for an active engagement slug.
2. If none found, scan `EA-projects/*/engagement.json` and ask the user to select one.
3. Load `engagement.json` — extract: name, slug, currentPhase, direction.

---

## Mode: `list` (default)

1. Read `engagement.json → direction.goals[]`.
2. If no goals exist, report and stop (see Edge Cases).
3. Apply any `--domain`, `--type`, or `--priority` filters.
4. Render a summary header and table grouped by Domain:

```
Goals Register — {engagement name}
══════════════════════════════════════════
Total: {N}  |  Strategic: {N}  |  Operational: {N}  |  Capability: {N}  |  Compliance: {N}

Priority:   High {N}  |  Medium {N}  |  Low {N}
Status:     Active {N}  |  Achieved {N}  |  Superseded {N}
Orphans:    {N} goal(s) with no linked driver
No OBJ:     {N} goal(s) with no linked objective

| ID | Statement | Domain | Type | Priority | Status | Drivers | Objectives | Strategies |
|---|---|---|---|---|---|---|---|---|
| G-001 | {statement truncated to 60 chars} | Business | Strategic | High | Active | DRV-001 | OBJ-001 | STR-001 |
```

5. Flag orphan goals (no linked drivers): "⚠️ {N} goal(s) have no linked driver — run `/ea-drivers add` to capture drivers first."
6. Flag goals with no linked objectives: "⚠️ {N} goal(s) have no linked objective — use `/ea-objectives add` to operationalise them."
7. Flag EA-layer goals (statement contains "governance", "standards", "EA team", "architecture capability"): "⚠️ G-NNN may be an EA-layer goal — apply the Two-Layers test before proceeding."

---

## Mode: `add`

Invoked as: `/ea-goals add`

1. Read `engagement.json → direction.goals[]`. Assign the next `G-NNN` ID (increment from highest existing; start at G-001 if empty).

2. Prompt for each field in sequence:

```
Creating new goal — G-{NNN}

1. Statement (qualitative desired future state — no measures or deadlines, e.g. "Achieve highly resilient platform operations"):

2. Domain — which architecture domain does this goal primarily belong to?
   Business / Technology / Data / Application / Cross-cutting

3. Type — what kind of goal is this?
   Strategic (organisational direction) / Operational (process/efficiency) / Capability (capability development) / Compliance (regulatory/governance)

4. Priority (High / Medium / Low):

5. Status (Active / Achieved / Superseded) [default: Active]:

6. Linked Drivers (DRV-NNN IDs, comma-separated — press Enter to skip) [optional]:
   [List available DRV-NNN IDs from engagement.json]

7. Rationale (why is this a goal for this engagement? What happens if not achieved?) [optional]:
```

3. **Two-Layers disambiguation check**: If the statement contains any of ("governance", "standards", "EA team", "architecture capability", "review process", "approval", "EA function"), warn:
   ```
   ⚠️  This statement may describe an EA-layer goal, not a business goal.
   Quick test: Would this goal still exist if the EA team were disbanded?
   - If yes → proceed (it is a business goal)
   - If no → this belongs in the Governance Framework, not the Architecture Vision
   Continue as a business goal? (y/n)
   ```

4. **Objective check**: If no `linkedObjectives` and user provided a statement with a number or deadline in it, warn:
   ```
   ⚠️  Your statement contains what looks like a measure or deadline.
   Goals are qualitative; Objectives are measurable. Consider:
   - Goal: "{cleaned statement without measure}"
   - Objective: "{statement}" (linked to this goal)
   Proceed with the statement as-is? (y/n)
   ```

5. Show confirmation preview:

```
New goal — G-NNN
Statement: {statement}
Domain: {domain}  |  Type: {type}  |  Priority: {priority}  |  Status: {status}
Linked Drivers: {drivers or "—"}
Rationale: {rationale or "—"}

Add to engagement? (y/n)
```

6. On confirm: append to `engagement.json → direction.goals[]`, set `lastModified: today`.
7. Confirm: `"G-NNN added. Use '/ea-objectives add' to operationalise this goal with a measurable objective."`
8. If no drivers linked: "⚠️ No drivers linked. Run `/ea-drivers list` to see available drivers, then `/ea-goals update G-NNN drivers DRV-NNN`."

---

## Mode: `update`

Invoked as: `/ea-goals update G-NNN <field> <value>`

1. Read `engagement.json → direction.goals[]` and find the entry with `id = G-NNN`.
2. Valid fields for update:

| Field | Valid values |
|---|---|
| `statement` | any string |
| `domain` | Business / Technology / Data / Application / Cross-cutting |
| `type` | Strategic / Operational / Capability / Compliance |
| `priority` | High / Medium / Low |
| `status` | Active / Achieved / Superseded |
| `drivers` | comma-separated DRV-NNN list |
| `rationale` | any string |

3. Validation rules:
   - Setting `drivers` to empty → warn: "Removing all drivers will orphan this goal. Continue? (y/n)"
   - `drivers` values must match existing DRV-NNN IDs in `direction.drivers[]`; flag unknown IDs
   - Setting `status: Superseded` → prompt: "Superseded by which goal? (G-NNN or press Enter to skip)"
4. Show proposed change: `"G-NNN: {field} — '{old}' → '{new}'"`
5. Ask: `"Apply? (y/n)"`
6. On confirm: update `engagement.json`, set `lastModified: today`.

---

## Mode: `trace`

Invoked as: `/ea-goals trace [G-NNN]`

**Without G-NNN — traceability summary table:**

1. For every `G-NNN` in `direction.goals[]`, collect:
   - Linked drivers: `direction.drivers[]` where `linkedGoals` contains this G-NNN
   - Linked objectives: `direction.objectives[]` where `linkedGoal` = this G-NNN
   - Linked strategies: `direction.strategies[]` where `supports` contains this G-NNN
2. Output:

```
| G-NNN | Statement (first 60 chars) | Domain | Priority | Drivers | Objectives | Strategies | Orphan? |
|---|---|---|---|---|---|---|---|
```

3. Flag orphans (no drivers AND no objectives) with `⚠️ Orphan`.

**With G-NNN — full chain:**

```
Goal Chain — G-NNN: {statement}

Domain: {domain}  |  Type: {type}  |  Priority: {priority}  |  Status: {status}
Rationale: {rationale or "—"}

Upstream — Business Drivers:
  ✅ DRV-001 — {driver statement}
  ⚠️ No drivers linked — goal is an orphan

Lateral — Issues threatening this goal:
  ⚠️ ISS-001 — {issue statement}

Downstream — Objectives:
  ✅ OBJ-001 — {objective} (Measure: {measure}, Target: {target}, Deadline: {deadline})
  ⚠️ No objectives — goal is not yet operationalised

Downstream — Strategies:
  ✅ STR-001 — {strategy statement}

Downstream — Work Packages (from Architecture Roadmap):
  ✅ WP-001 — {wp name} [advances G-NNN]
  ⚠️ No work packages — goal not yet represented in roadmap

Chain status: {✅ Complete | ⚠️ Partial | 🔴 Orphan}
```

4. Flag any referenced IDs that do not exist in `engagement.json` as broken links.

---

## Mode: `generate`

Invoked as: `/ea-goals generate`

1. Read `engagement.json → direction.goals[]`.
2. Produce `EA-projects/{slug}/artifacts/cross-cutting/goals-register-{YYYY-MM-DD}.md`:

```markdown
---
artifact: Goals Register
artifactId: goals-register
engagement: {name}
phase: cross-cutting
status: Draft
generated: {YYYY-MM-DD}
relatedArtifacts: ["architecture-vision"]
diagrams: []
links: []
---

# Goals Register

**Engagement:** {name}
**Generated:** {YYYY-MM-DD}
**Total Goals:** {N} ({N} Business, {N} Technology, {N} Data, {N} Application, {N} Cross-cutting)

---

## Summary

| Metric | Count |
|---|---|
| Total | {N} |
| Active | {N} |
| Achieved | {N} |
| Superseded | {N} |
| Orphans (no driver) | {N} |
| Not operationalised (no objective) | {N} |

---

## Goals by Domain

### Business Goals ({N})

#### G-NNN: {statement truncated}

| Field | Value |
|---|---|
| **ID** | G-NNN |
| **Statement** | {full statement} |
| **Domain** | Business |
| **Type** | {type} |
| **Priority** | {priority} |
| **Status** | {status} |
| **Linked Drivers** | {DRV-NNN list or —} |
| **Linked Objectives** | {OBJ-NNN list or —} |
| **Linked Strategies** | {STR-NNN list or —} |
| **Rationale** | {rationale or —} |

{Repeat for all goals, grouped by Domain}
```

3. Register artifact in `engagement.json → artifacts[]`.
4. Confirm: `"Goals Register written to artifacts/cross-cutting/goals-register-{YYYY-MM-DD}.md — {N} goals."`

---

## Edge Cases

| Scenario | Handling |
|---|---|
| No goals found | "No goals found. Capture goals during Phase A interviews (`/ea-interview start phase A`) or `/ea-brainstorm`, then add them with `/ea-goals add`." |
| Goal with no drivers | Flag as orphan in `list` and `trace`; suggest `/ea-goals update G-NNN drivers DRV-NNN` |
| Goal with no objectives | Flag in `list`; suggest `/ea-objectives add` |
| `drivers` references unknown DRV-NNN | Flag as broken link; suggest verifying with `/ea-drivers list` |
| Duplicate G-NNN in `engagement.json` | Report duplication; offer to renumber: "G-NNN appears twice — renumber second entry to G-{N+1}? (y/n)" |
| Possible EA-layer goal | Trigger Two-Layers check during `add`; flag in `list` with `⚠️ EA-layer?` |
| Statement with measure/deadline | Trigger Objective disambiguation during `add` |
