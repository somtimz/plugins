---
name: ea-problems
description: Manage architecture problems — list, add, update, trace to objectives and requirements, and generate a Problems Register
argument-hint: "[list|add|update|trace|generate] [PRB-NNN] [--domain Business|Technology|Data|Application|Engagement] [--type Operational|Technical|Data|Engagement|Compliance] [--severity Critical|High|Medium|Low] [--status Open|In Progress|Resolved]"
allowed-tools: [Read, Write, Bash]
---

You are executing the `/ea-problems` command.

## Overview

Problems are **specific, observable, and fixable symptoms that are actively blocking the achievement of one or more objectives**. They have a clear cause-and-effect relationship: a root cause produces a visible symptom that degrades performance against a known objective. Because they are specific and measurable, problems can be prioritised, assigned, and resolved directly.

Problems are distinct from:
- **Issues (ISS-NNN)** — an issue is *systemic and broad*, with multiple contributing causes and no single fix. A problem is *specific, observable, and directly fixable*. "Poor data culture" is an issue; "30% of customer records have duplicates" is a problem. Multiple problems can contribute to a single issue.
- **Risks (RIS-NNN)** — a risk is *future and uncertain*; a problem is *certain and present*.
- **Gaps (GAP-NNN)** — a gap is the architectural delta between baseline and target state; a problem is a current operational failure. A problem may *evidence* a gap but is not the same as one.
- **Constraints (CST-NNN)** — a constraint is a non-negotiable boundary on implementation choices; a problem is a current dysfunction that needs resolution.

Problems are stored in `engagement.json → direction.problems[]`. They also appear in Architecture Vision §6 — the register is the management interface; Architecture Vision is the primary display view.

**Modes:**
- `list` (default) — read problems from `engagement.json`, render a table grouped by Domain
- `add` — interactively capture a new problem and write it to `engagement.json`
- `update` — update a single field on an existing problem (`/ea-problems update PRB-NNN <field> <value>`)
- `trace` — show upstream (Issues) and downstream (Objectives, Requirements) chain
- `generate` — produce a printable Problems Register artifact

**Filters:**
- `--domain` — filter by domain (Business / Technology / Data / Application / Engagement)
- `--type` — filter by problem type
- `--severity` — filter by severity
- `--status` — filter by status

---

## Step 1 — Resolve Active Engagement

1. Check the conversation context for an active engagement slug.
2. If none found, scan `EA-projects/*/engagement.json` and ask the user to select one.
3. Load `engagement.json` — extract: name, slug, currentPhase, direction.

---

## Mode: `list` (default)

1. Read `engagement.json → direction.problems[]`.
2. If no problems exist, report and stop (see Edge Cases).
3. Apply any filters.
4. Render summary header and table grouped by Domain (Engagement first, then Business, Technology, Data, Application):

```
Problems Register — {engagement name}
══════════════════════════════════════════
Total: {N}  |  Critical: {N}  |  High: {N}  |  Medium: {N}  |  Low: {N}

By Domain:  Engagement {N}  |  Business {N}  |  Technology {N}  |  Data {N}  |  Application {N}
Status:     Open {N}  |  In Progress {N}  |  Resolved {N}
No evidence: {N} problem(s) missing evidence
No objectives: {N} problem(s) with no linked objective

| ID | Statement | Domain | Type | Severity | Status | Blocks Objectives | Evidence |
|---|---|---|---|---|---|---|---|
| PRB-001 | {statement truncated to 60 chars} | Business | Operational | High | Open | OBJ-001 | ✅ |
```

5. Flag problems with no evidence: "⚠️ {N} problem(s) have no evidence — problems without a measurable symptom cannot be prioritised."
6. Flag problems with no linked objectives: "⚠️ {N} problem(s) block no objective — if they cannot be linked to an objective, they may be out of scope."
7. Flag Critical/High Open problems: "🔴 {N} critical/high problem(s) are unresolved — consider creating architecture requirements to address them."

---

## Mode: `add`

Invoked as: `/ea-problems add`

1. Read `engagement.json → direction.problems[]`. Assign the next `PRB-NNN` ID.

2. **Problem vs Issue disambiguation** — ask first:
   ```
   Is this concern specific, observable, and directly fixable?
   Or is it a broader, systemic pattern with multiple contributing causes?

   (p) Problem — specific, observable, fixable, blocks a particular objective
   (i) Issue — systemic, broad, multiple causes, sustained response needed

   Enter choice [p/i]:
   ```
   If (i): "Routing to `/ea-issues add` — use Issues for systemic, broad concerns that threaten goals." Stop.

3. Prompt for each field in sequence:

```
Creating new problem — PRB-{NNN}

1. Statement (name the specific problem — observable and fixable, e.g. "Mobile checkout page load time averages 8.2 seconds"):

2. Observable Symptom (what can be seen or measured today — ideally a number, e.g. "68% cart abandonment on mobile due to slow load"):

3. Domain — which area is primarily affected?
   Business / Technology / Data / Application / Engagement
   (Engagement = problem with the EA engagement itself: methodology, governance, team, tooling)

4. Type — what category of problem is this?
   Operational / Technical / Data / Engagement / Compliance

5. Severity (Critical / High / Medium / Low):

6. Status (Open / In Progress / Resolved) [default: Open]:

7. Blocks Objectives (OBJ-NNN IDs, comma-separated — which objectives is this problem preventing?):
   [List available OBJ-NNN IDs from engagement.json]
   If no OBJ-NNN exist yet: "No objectives captured yet — add objectives with '/ea-objectives add' after this step."

8. Evidence (data point, incident, or measurement confirming the symptom is currently active):

9. Raised By (stakeholder or source that identified this problem) [optional]:
```

4. **Systemic check**: If the statement uses plural broad terms ("architecture", "culture", "all systems", "consistently", "always"), warn:
   ```
   ⚠️  Your statement sounds systemic — it may describe a pattern rather than a specific event.
   Problems are specific and fixable. Issues are systemic and broad.
   Example of a Problem: "Payment API returns HTTP 500 errors on 3× per week on average"
   Example of an Issue: "Integration architecture lacks resilience and monitoring"
   Proceed as a Problem? (y/n)
   ```

5. **Objective check**: If no objectives exist in `direction.objectives[]`, note after add:
   ```
   ⚠️ No objectives captured yet. Problems should block specific objectives.
   After capturing objectives with '/ea-objectives add', link this problem:
   /ea-problems update PRB-NNN blocksObjectives OBJ-NNN
   ```

6. Show confirmation preview:

```
New problem — PRB-NNN
Statement: {statement}
Observable Symptom: {symptom}
Domain: {domain}  |  Type: {type}  |  Severity: {severity}  |  Status: {status}
Blocks Objectives: {objectives or "⚠️ None — recommended"}
Evidence: {evidence or "⚠️ None — recommended"}
Raised By: {raisedBy or "—"}

Add to engagement? (y/n)
```

7. On confirm: append to `engagement.json → direction.problems[]`, set `lastModified: today`.
8. Confirm: `"PRB-NNN added. Consider creating a REQ-NNN requirement to address this problem: '/ea-requirements add'."`

---

## Mode: `update`

Invoked as: `/ea-problems update PRB-NNN <field> <value>`

1. Read `engagement.json → direction.problems[]` and find the entry with `id = PRB-NNN`.
2. Valid fields for update:

| Field | Valid values |
|---|---|
| `statement` | any string |
| `symptom` | any string (ideally includes a number or measurable observation) |
| `domain` | Business / Technology / Data / Application / Engagement |
| `type` | Operational / Technical / Data / Engagement / Compliance |
| `severity` | Critical / High / Medium / Low |
| `status` | Open / In Progress / Resolved |
| `blocksObjectives` | comma-separated OBJ-NNN list |
| `evidence` | any string |
| `raisedBy` | any string |

3. Validation rules:
   - Setting `blocksObjectives` to empty → warn: "Removing all objective links makes this problem out-of-scope. Continue? (y/n)"
   - `blocksObjectives` values must match existing OBJ-NNN IDs; flag unknown IDs
   - Setting `status: Resolved` → prompt: "Resolution summary (optional):"
4. Show proposed change and ask: `"Apply? (y/n)"`
5. On confirm: update `engagement.json`, set `lastModified: today`.

---

## Mode: `trace`

Invoked as: `/ea-problems trace [PRB-NNN]`

**Without PRB-NNN — traceability summary:**

```
| PRB-NNN | Statement (first 60 chars) | Domain | Severity | Status | Blocks Objectives | Related Issues | Orphan? |
|---|---|---|---|---|---|---|---|
```

Flag orphans (no linked objectives) with `⚠️ Orphan`.

**With PRB-NNN — full chain:**

```
Problem Chain — PRB-NNN: {statement}

Domain: {domain}  |  Type: {type}  |  Severity: {severity}  |  Status: {status}
Observable Symptom: {symptom}
Evidence: {evidence or "⚠️ None"}
Raised By: {raisedBy or "—"}

Upstream — Related Issues (systemic patterns this problem contributes to):
  Scan direction.issues[] for ISS-NNN entries that share threatened goals with this problem's blocked objectives:
  → ISS-001 — {issue statement} [threatens G-001 which has OBJ-001]

Blocks — Objectives:
  🔴 OBJ-001 — {objective} (Target: {target}, Deadline: {deadline}) [Goal: G-NNN]
  🔴 OBJ-002 — {objective}
  ⚠️ No objectives linked — problem is an orphan

Upstream (via Objectives) — Goals at risk:
  → G-001 — {goal statement}

Downstream — Architecture Requirements (derived from this problem):
  Scan artifacts/**/requirements*.md for REQ-NNN rows referencing PRB-NNN:
  → REQ-001 — {requirement statement}
  ⚠️ No requirements — consider creating REQ-NNN entries to address this problem

Chain status: {✅ Addressed | ⚠️ Partial | 🔴 Orphan}
```

---

## Mode: `generate`

Invoked as: `/ea-problems generate`

1. Read `engagement.json → direction.problems[]`.
2. If `problems-register.md` already exists in the target folder, archive it to `snapshots/` per `skills/ea-artifact-templates/references/register-snapshot-convention.md`.
3. Produce `EA-projects/{slug}/artifacts/cross-cutting/problems-register.md`:

```markdown
---
artifact: Problems Register
artifactId: problems-register
engagement: {name}
phase: cross-cutting
status: Draft
generated: {YYYY-MM-DD}
relatedArtifacts: ["architecture-vision"]
diagrams: []
links: []
---

# Problems Register

**Engagement:** {name}
**Generated:** {YYYY-MM-DD}
**Total Problems:** {N}

---

## Summary

| Metric | Count |
|---|---|
| Total | {N} |
| Critical | {N} |
| High | {N} |
| Medium | {N} |
| Low | {N} |
| Open | {N} |
| In Progress | {N} |
| Resolved | {N} |
| Orphans (no objective link) | {N} |
| No evidence | {N} |

---

## Problems by Domain

### Engagement Problems ({N})

#### PRB-NNN: {statement truncated}

| Field | Value |
|---|---|
| **ID** | PRB-NNN |
| **Statement** | {full statement} |
| **Observable Symptom** | {symptom} |
| **Domain** | Engagement |
| **Type** | {type} |
| **Severity** | {severity} |
| **Status** | {status} |
| **Blocks Objectives** | {OBJ-NNN list or —} |
| **Evidence** | {evidence or ⚠️ None} |
| **Raised By** | {raisedBy or —} |

{Repeat for all problems, grouped by Domain}
```

4. Register artifact in `engagement.json → artifacts[]` (single entry at the stable path).
5. Confirm: `"Problems Register written to artifacts/cross-cutting/problems-register.md — {N} problems."`

---

## Edge Cases

| Scenario | Handling |
|---|---|
| No problems found | "No problems found. Capture problems during Phase A interviews (`/ea-interview start phase A`) or add directly with `/ea-problems add`." |
| Problem with no objectives | Flag as orphan; suggest linking via `/ea-problems update PRB-NNN blocksObjectives OBJ-NNN` or creating objectives with `/ea-objectives add` |
| Problem with no evidence | Flag inline with `⚠️ No evidence`; remind: "Problems without measurable symptoms cannot be prioritised" |
| `blocksObjectives` references unknown OBJ-NNN | Flag as broken link; suggest verifying with `/ea-objectives list` (when available) or checking Architecture Vision §4 |
| Duplicate PRB-NNN | Report duplication; offer renumbering |
| Status set to Resolved | Prompt for resolution summary before applying |
| Statement sounds systemic | Trigger disambiguation check during `add`; offer to route to `/ea-issues add` |
| No objectives in engagement.json | Note after add; provide update command for when objectives are captured |
