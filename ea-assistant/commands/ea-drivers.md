---
name: ea-drivers
description: Manage business drivers — list, add, update, trace to goals and work packages, and generate a drivers register
argument-hint: "[list|add|update|trace|generate] [DRV-NNN] [--type External|Internal] [--priority High|Medium|Low]"
allowed-tools: [Read, Write, Bash]
---

You are executing the `/ea-drivers` command. Load the `ea-drivers-management` skill for detailed logic.

## Overview

Business drivers are the **external pressures and internal imperatives** that make this engagement necessary. They sit at the top of the motivation chain (DRV → G → OBJ → STR → WP). Every goal should trace to at least one driver; every driver should have at least one linked goal.

Drivers are distinct from:
- **Goals** — where you want to be (qualitative destination statements)
- **Objectives** — measurable targets with deadlines derived from goals
- **Strategies** — how you will pursue goals

This command manages all `DRV-NNN` entries stored in `engagement.json → direction.drivers[]`, supports creating or updating individual driver records, and traces each driver through the full motivation chain to work packages.

**Modes:**
- `list` (default) — read drivers from `engagement.json`, render a table grouped by Type
- `add` — interactively capture a new driver and write it to `engagement.json`
- `update` — update a single field on an existing driver (`/ea-drivers update DRV-NNN <field> <value>`)
- `trace` — show the downstream motivation chain from a driver to goals, objectives, strategies, and work packages
- `generate` — produce a printable Drivers Register artifact

**Filters:**
- `--type` — filter by driver type (External / Internal)
- `--priority` — filter by priority (High / Medium / Low)

---

## Step 1 — Resolve Active Engagement

1. Check the conversation context for an active engagement slug.
2. If none found, scan `EA-projects/*/engagement.json` and ask the user to select one.
3. Load `engagement.json` — extract: name, slug, currentPhase, direction.

---

## Mode: `list` (default)

1. Read `engagement.json → direction.drivers[]`.
2. If no drivers exist, report and stop (see Edge Cases).
3. Render a summary header and table grouped by Type (External first, Internal second):

```
Drivers Register — {engagement name}
══════════════════════════════════════════
Total: {N}  |  External: {N}  |  Internal: {N}

Priority:      High {N}  |  Medium {N}  |  Low {N}
Orphans:       {N} driver(s) with no linked goal
No evidence:   {N} driver(s) with no evidence cited

| ID | Statement | Type | Priority | Linked Goals | Evidence |
|---|---|---|---|---|---|
| DRV-001 | {statement} | External | High | G-001, G-002 | {evidence or ⚠️ None} |
```

4. Flag orphan drivers (no linked goals): "⚠️ {N} driver(s) have no linked goal — run `/ea-drivers trace` to review."
5. Flag drivers with no evidence: note inline with `⚠️ No evidence cited`.

---

## Mode: `add`

Invoked as: `/ea-drivers add`

1. Read `engagement.json → direction.drivers[]`. Assign the next `DRV-NNN` ID (increment from the highest existing N; start at DRV-001 if empty).
2. Prompt for each field in sequence:

```
Creating new driver — DRV-{NNN}

1. Statement (the business pressure or imperative, e.g. "Regulatory mandates for data residency in the EU by 2027"):
2. Type (External / Internal):
3. Priority (High / Medium / Low):
4. Evidence (source document, metric, or external reference — press Enter to skip) [optional]:
5. Linked Goals (G-NNN IDs, comma-separated — press Enter to skip) [optional]:
```

3. Show confirmation preview:

```
New driver — DRV-NNN
Statement: {statement}
Type: {type}  |  Priority: {priority}
Evidence: {evidence or "—"}
Linked Goals: {linkedGoals or "—"}

Add to engagement? (y/n)
```

4. On confirm: append to `engagement.json → direction.drivers[]`, set `lastModified: today`.
5. Confirm: `"DRV-NNN added. Use '/ea-drivers trace DRV-NNN' to verify goal linkage."`
6. If `linkedGoals` is empty: "⚠️ No goals linked. Consider running `/ea-drivers update DRV-NNN linkedGoals G-NNN` after capturing goals."

---

## Mode: `update`

Invoked as: `/ea-drivers update DRV-NNN <field> <value>`

1. Read `engagement.json → direction.drivers[]` and find the entry with `id = DRV-NNN`.
2. Valid fields for update:

| Field | Valid values |
|---|---|
| `statement` | any string |
| `type` | External / Internal |
| `priority` | High / Medium / Low |
| `evidence` | any string or URL |
| `linkedGoals` | comma-separated G-NNN list |

3. Validation rules:
   - Setting `linkedGoals` to empty → warn: "Removing all linked goals will orphan this driver. Continue? (y/n)"
   - `linkedGoals` values must match existing G-NNN IDs in `direction.goals[]`; flag any unknown IDs
4. Show proposed change: `"DRV-NNN: {field} — '{old}' → '{new}'"`
5. Ask: `"Apply? (y/n)"`
6. On confirm: update `engagement.json`, set `lastModified: today`.
7. Confirm: `"Updated DRV-NNN: {field} set to '{new_value}'."`

---

## Mode: `trace`

Invoked as: `/ea-drivers trace [DRV-NNN]`

**Without DRV-NNN — full traceability matrix:**

1. For every `DRV-NNN` in `direction.drivers[]`, walk the downstream chain:
   - Linked goals: `direction.goals[]` where `drivers` contains this DRV-NNN
   - Linked objectives: `direction.objectives[]` where `linkedGoal` is in the goal set
2. Output traceability matrix:

```
| DRV-NNN | Statement (first 60 chars) | Priority | Linked Goals | Linked Objectives | Orphan? |
|---|---|---|---|---|---|
```

3. Flag orphan drivers (no linked goals) with `⚠️ Orphan`.

**With DRV-NNN — full downstream chain:**

1. Find the driver entry.
2. Walk the full motivation chain:
   - **Goals:** `direction.goals[]` where `drivers` array contains `DRV-NNN`
   - **Objectives:** `direction.objectives[]` where `linkedGoal` is in the goal set found above
   - **Strategies:** `direction.strategies[]` where `supports` intersects the goal or objective set
   - **Work Packages:** Scan `artifacts/phase-e/architecture-roadmap.md` (and any other roadmap files) for WP-NNN rows where `Advances Goals/Objectives` or `Executes Strategies` references the found IDs
3. Output:

```
Downstream Chain — DRV-NNN: {statement}

Type: {type}  |  Priority: {priority}
Evidence: {evidence or "—"}

Goals (G-NNN):
  ✅ G-001 — {goal statement}
  ✅ G-002 — {goal statement}

Objectives (OBJ-NNN):
  ✅ OBJ-001 — {objective} [linked to G-001]

Strategies (STR-NNN):
  ✅ STR-001 — {strategy} [supports G-001]

Work Packages (WP-NNN):
  ✅ WP-001 — {wp name} [advances G-001]
  ⚠️ WP-002 — {wp name} [not yet linked to any driver goal]

Chain status: {✅ Complete | ⚠️ Partial | 🔴 No goals linked}
```

4. Flag any referenced IDs that don't exist in `engagement.json` as broken links.

---

## Mode: `generate`

Invoked as: `/ea-drivers generate`

1. Read `engagement.json → direction.drivers[]`.
2. Produce `EA-projects/{slug}/artifacts/cross-cutting/drivers-register-{YYYY-MM-DD}.md`:

```markdown
---
artifact: Drivers Register
artifactId: drivers-register
engagement: {name}
phase: cross-cutting
status: Draft
generated: {YYYY-MM-DD}
---

# Business Drivers Register

**Engagement:** {name}
**Generated:** {YYYY-MM-DD}
**Total Drivers:** {N} ({N} External, {N} Internal)

---

## DRV-NNN: {statement truncated to 60 chars}

| Field | Value |
|---|---|
| **ID** | DRV-NNN |
| **Statement** | {full statement} |
| **Type** | External / Internal |
| **Priority** | High / Medium / Low |
| **Evidence** | {evidence or —} |
| **Linked Goals** | {G-NNN, G-NNN or —} |

### Downstream Chain
{Walk the chain for this driver — list linked G-NNN, OBJ-NNN, STR-NNN, WP-NNN}
```

3. Confirm: `"Drivers Register written to artifacts/cross-cutting/drivers-register-{YYYY-MM-DD}.md — {N} drivers."`

---

## Edge Cases

| Scenario | Handling |
|---|---|
| No drivers found | Report "No drivers found. Capture drivers during Preliminary phase interviews, engagement interview (`/ea-interview start engagement`), or `/ea-brainstorm`." |
| Driver with no linked goals | Flag as orphan in `list` and `trace`; suggest `/ea-drivers update DRV-NNN linkedGoals G-NNN` |
| `linkedGoals` references unknown G-NNN | Flag as broken link; suggest verifying or removing the reference |
| Duplicate DRV-NNN in `engagement.json` | Report duplication; offer to renumber: "DRV-NNN appears twice — renumber second entry to DRV-{N+1}? (y/n)" |
| No Architecture Roadmap found | Report "Architecture Roadmap not found — work package linkage cannot be traced. Generate one with `/ea-artifact architecture-roadmap`." |
