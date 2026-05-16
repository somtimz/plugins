---
name: ea-issues
description: Manage architecture issues — list, add, update, trace to goals and gaps, and generate an Issues Register
argument-hint: "[list|add|update|trace|generate] [ISS-NNN] [--domain Business|Technology|Data|Application|Engagement] [--type Organisational|Process|Technology|Regulatory|Capability] [--severity Critical|High|Medium|Low] [--status Open|Under Mitigation|Resolved|Accepted]"
allowed-tools: [Read, Write, Bash]
---

You are executing the `/ea-issues` command.

## Overview

Issues are **broader, systemic concerns that threaten the organisation's ability to achieve one or more goals**. They represent patterns of dysfunction, capability gaps, unresolved conflicts, or sustained exposure to a driver that has no single fix. Issues have multiple contributing causes, affect a domain broadly, and require sustained organisational response rather than a technical patch.

Issues are distinct from:
- **Problems (PRB-NNN)** — a problem is a *specific, observable, directly fixable* symptom. An issue is *systemic and broad*. Multiple problems can contribute to a single issue. "Poor data culture" is an issue; "30% of customer records have duplicates" is a problem.
- **Risks (RIS-NNN)** — a risk is *future and uncertain*. An issue is *present and ongoing*. When a risk materialises, it becomes an issue.
- **Drivers (DRV-NNN)** — a driver is the external/internal force; an issue is the *organisational consequence* of inadequately responding to a driver.
- **Gaps (GAP-NNN)** — a gap is the delta between baseline and target architecture state; an issue is a current operational concern that may *cause* or be *evidenced by* gaps.

Issues are stored in `engagement.json → direction.issues[]`. They also appear in Architecture Vision §5 — the register is the management interface; Architecture Vision is the primary display view.

**Modes:**
- `list` (default) — read issues from `engagement.json`, render a table grouped by Domain
- `add` — interactively capture a new issue and write it to `engagement.json`
- `update` — update a single field on an existing issue (`/ea-issues update ISS-NNN <field> <value>`)
- `trace` — show upstream (Drivers) and downstream (Goals, Gaps) motivation chain
- `generate` — produce a printable Issues Register artifact

**Filters:**
- `--domain` — filter by domain (Business / Technology / Data / Application / Engagement)
- `--type` — filter by issue type
- `--severity` — filter by severity
- `--status` — filter by status

---

## Step 1 — Resolve Active Engagement

1. Check the conversation context for an active engagement slug.
2. If none found, scan `EA-projects/*/engagement.json` and ask the user to select one.
3. Load `engagement.json` — extract: name, slug, currentPhase, direction.

---

## Mode: `list` (default)

1. Read `engagement.json → direction.issues[]`.
2. If no issues exist, report and stop (see Edge Cases).
3. Apply any filters.
4. Render summary header and table grouped by Domain (Engagement first, then Business, Technology, Data, Application):

```
Issues Register — {engagement name}
══════════════════════════════════════════
Total: {N}  |  Critical: {N}  |  High: {N}  |  Medium: {N}  |  Low: {N}

By Domain:  Engagement {N}  |  Business {N}  |  Technology {N}  |  Data {N}  |  Application {N}
Status:     Open {N}  |  Under Mitigation {N}  |  Resolved {N}  |  Accepted {N}
No evidence: {N} issue(s) missing evidence
No goals:    {N} issue(s) with no linked goal

| ID | Statement | Domain | Type | Severity | Status | Threatens Goals | Evidence |
|---|---|---|---|---|---|---|---|
| ISS-001 | {statement truncated to 60 chars} | Business | Organisational | High | Open | G-001, G-002 | ✅ |
```

5. Flag issues with no evidence: "⚠️ {N} issue(s) have no evidence — unverified issues are assumptions, not confirmed concerns."
6. Flag issues with no linked goals: "⚠️ {N} issue(s) threaten no goal — link to a G-NNN or consider whether this is in scope."
7. Flag Critical/High unresolved issues: "🔴 {N} critical/high issue(s) are Open or Under Mitigation — review for escalation."

---

## Mode: `add`

Invoked as: `/ea-issues add`

1. Read `engagement.json → direction.issues[]`. Assign the next `ISS-NNN` ID.

2. **Issue vs Problem disambiguation** — ask first:
   ```
   Is this concern systemic and broad (affecting a domain or goal generally, with multiple contributing causes)?
   Or is it specific, observable, and directly fixable (blocking a particular objective)?

   (i) Issue — systemic, broad, multiple causes, sustained response needed
   (p) Problem — specific, observable, directly fixable, blocks an objective

   Enter choice [i/p]:
   ```
   If (p): "Routing to `/ea-problems add` — use Problems for specific, fixable symptoms that block objectives." Stop.

3. Prompt for each field in sequence:

```
Creating new issue — ISS-{NNN}

1. Statement (name the systemic concern — what pattern of dysfunction, what capability gap, or what sustained barrier?):

2. Domain — which area is primarily affected?
   Business / Technology / Data / Application / Engagement
   (Engagement = concern about the EA engagement itself: methodology, governance, team, tooling)

3. Type — what category of issue is this?
   Organisational / Process / Technology / Regulatory / Capability

4. Severity (Critical / High / Medium / Low):

5. Status (Open / Under Mitigation / Resolved / Accepted) [default: Open]:

6. Threatens Goals (G-NNN IDs, comma-separated — which goals does this issue put at risk?):
   [List available G-NNN IDs from engagement.json]

7. Evidence (observable signal, data point, or event that confirms this issue is real, e.g. "Incident log: 12 P1 outages in 90 days"):

8. Raised By (stakeholder or source that surfaced this issue) [optional]:
```

4. **Specificity check**: If the statement contains a number, file name, or individual system name, warn:
   ```
   ⚠️  Your statement looks specific and measurable.
   Issues are systemic — they describe a broad pattern, not a single event.
   Example of an Issue: "Integration architecture lacks resilience and monitoring"
   Example of a Problem: "The payment API returns 500 errors 3× per week"
   Proceed as an Issue? (y/n)
   ```

5. Show confirmation preview:

```
New issue — ISS-NNN
Statement: {statement}
Domain: {domain}  |  Type: {type}  |  Severity: {severity}  |  Status: {status}
Threatens Goals: {goals or "—"}
Evidence: {evidence or "⚠️ None — recommended"}
Raised By: {raisedBy or "—"}

Add to engagement? (y/n)
```

6. On confirm: append to `engagement.json → direction.issues[]`, set `lastModified: today`.
7. Confirm: `"ISS-NNN added. Run '/ea-issues trace ISS-NNN' to verify goal linkage and check for related gaps."`
8. If no goals linked: "⚠️ No goals linked. Use `/ea-goals list` to review goals, then `/ea-issues update ISS-NNN threatensGoals G-NNN`."

---

## Mode: `update`

Invoked as: `/ea-issues update ISS-NNN <field> <value>`

1. Read `engagement.json → direction.issues[]` and find the entry with `id = ISS-NNN`.
2. Valid fields for update:

| Field | Valid values |
|---|---|
| `statement` | any string |
| `domain` | Business / Technology / Data / Application / Engagement |
| `type` | Organisational / Process / Technology / Regulatory / Capability |
| `severity` | Critical / High / Medium / Low |
| `status` | Open / Under Mitigation / Resolved / Accepted |
| `threatensGoals` | comma-separated G-NNN list |
| `evidence` | any string |
| `raisedBy` | any string |

3. Validation rules:
   - Setting `threatensGoals` to empty → warn: "Removing all goal links will orphan this issue. Continue? (y/n)"
   - `threatensGoals` values must match existing G-NNN IDs; flag unknown IDs
   - Setting `status: Resolved` → prompt: "Resolution notes (optional):"
   - Setting `status: Accepted` → prompt: "Acceptance rationale (required):" — do not proceed without rationale
4. Show proposed change and ask: `"Apply? (y/n)"`
5. On confirm: update `engagement.json`, set `lastModified: today`.

---

## Mode: `trace`

Invoked as: `/ea-issues trace [ISS-NNN]`

**Without ISS-NNN — traceability summary:**

```
| ISS-NNN | Statement (first 60 chars) | Domain | Severity | Status | Threatens Goals | Related Gaps | Orphan? |
|---|---|---|---|---|---|---|---|
```

Flag orphans (no linked goals) with `⚠️ Orphan`.

**With ISS-NNN — full chain:**

```
Issue Chain — ISS-NNN: {statement}

Domain: {domain}  |  Type: {type}  |  Severity: {severity}  |  Status: {status}
Evidence: {evidence or "⚠️ None"}
Raised By: {raisedBy or "—"}

Upstream — Related Drivers (contextual):
  Drivers linked to the goals this issue threatens:
  → DRV-001 — {driver statement}

Threatens — Goals:
  ⚠️ G-001 — {goal statement} [Priority: High]
  ⚠️ G-002 — {goal statement} [Priority: Medium]
  ⚠️ No goals linked — issue is an orphan

Related — Problems (specific symptoms that contribute to this issue):
  Run `/ea-problems list` and look for PRB-NNN entries that block objectives under the threatened goals.

Downstream — Architecture Gaps (gaps this issue may feed):
  Scan artifacts/phase-e/ and cross-cutting/ for GAP-NNN entries referencing this issue or its threatened goals:
  → GAP-001 — {gap statement} [Domain: {domain}]

Chain status: {✅ Complete | ⚠️ Partial | 🔴 Orphan}
```

---

## Mode: `generate`

Invoked as: `/ea-issues generate`

1. Read `engagement.json → direction.issues[]`.
2. Produce `EA-projects/{slug}/artifacts/cross-cutting/issues-register-{YYYY-MM-DD}.md`:

```markdown
---
artifact: Issues Register
artifactId: issues-register
engagement: {name}
phase: cross-cutting
status: Draft
generated: {YYYY-MM-DD}
relatedArtifacts: ["architecture-vision"]
diagrams: []
links: []
---

# Issues Register

**Engagement:** {name}
**Generated:** {YYYY-MM-DD}
**Total Issues:** {N}

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
| Under Mitigation | {N} |
| Resolved | {N} |
| Accepted | {N} |
| Orphans (no goal link) | {N} |
| No evidence | {N} |

---

## Issues by Domain

### Engagement Issues ({N})

#### ISS-NNN: {statement truncated}

| Field | Value |
|---|---|
| **ID** | ISS-NNN |
| **Statement** | {full statement} |
| **Domain** | Engagement |
| **Type** | {type} |
| **Severity** | {severity} |
| **Status** | {status} |
| **Threatens Goals** | {G-NNN list or —} |
| **Evidence** | {evidence or ⚠️ None} |
| **Raised By** | {raisedBy or —} |

{Repeat for all issues, grouped by Domain}
```

3. Register artifact in `engagement.json → artifacts[]`.
4. Confirm: `"Issues Register written to artifacts/cross-cutting/issues-register-{YYYY-MM-DD}.md — {N} issues."`

---

## Edge Cases

| Scenario | Handling |
|---|---|
| No issues found | "No issues found. Capture issues during Phase A interviews (`/ea-interview start phase A`) or add directly with `/ea-issues add`." |
| Issue with no goals | Flag as orphan; suggest linking via `/ea-issues update ISS-NNN threatensGoals G-NNN` |
| Issue with no evidence | Flag inline with `⚠️ No evidence`; remind: "Unverified issues are assumptions — add evidence before publishing" |
| `threatensGoals` references unknown G-NNN | Flag as broken link; suggest verifying with `/ea-goals list` |
| Duplicate ISS-NNN | Report duplication; offer renumbering |
| Status set to Accepted without rationale | Block update until rationale is provided |
| Statement looks like a Problem | Trigger disambiguation check during `add`; offer to route to `/ea-problems add` |
