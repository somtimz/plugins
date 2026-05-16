---
name: ea-scenarios
description: Manage TOGAF Business Scenarios — list, create, interview, trace, and generate Phase A scenario artifacts (BS-NNN)
argument-hint: "[list|new|view|interview|trace|generate] [BS-NNN]"
allowed-tools: [Read, Write, Bash]
---

You are executing the `/ea-scenarios` command.

## Overview

A Business Scenario is a **TOGAF Phase A technique** that bridges business stakeholders and architects by framing architecture needs as a narrative. It captures the six TOGAF elements (Problem Statement, Objectives, Environment, Stakeholders, Actors, Requirements) plus Current State / Target State narratives to validate the Architecture Vision and produce concrete, traceable requirements.

Business Scenarios are distinct from:
- **Issues (ISS-NNN)** — broad, systemic concerns; a scenario may be *triggered by* one or more issues
- **Problems (PRB-NNN)** — specific fixable symptoms; a scenario may *address* one or more problems
- **Requirements (REQ-NNN)** — a scenario *generates* requirements; the scenario is the narrative context
- **Architecture Vision** — the Vision is the agreed-upon target state; a scenario is one story that *justifies* or *tests* the Vision
- **Use Cases (UC-NNN)** — use cases are functional flows; scenarios are business narratives that may contain multiple use cases

Business Scenarios are stored as full artifact files in `artifacts/phase-a/` and indexed in `engagement.json → scenarios[]`.

**Modes:**
- `list` (default) — show all BS-NNN scenarios and their status
- `new` — guided creation through all six TOGAF elements and both state narratives
- `view BS-NNN` — display a scenario artifact
- `interview BS-NNN` — guided Q&A to complete or review an existing scenario
- `trace BS-NNN` — show the full motivation chain this scenario connects
- `generate` — produce a Scenarios Summary Register artifact

---

## Step 1 — Resolve Active Engagement

1. Check the conversation context for an active engagement slug.
2. If none found, scan `EA-projects/*/engagement.json` and ask the user to select one.
3. Load `engagement.json` — extract: name, slug, currentPhase, scenarios (if present), direction.

---

## Mode: `list` (default)

1. Read `engagement.json → scenarios[]`. If the `scenarios` key is absent or empty, report and stop (see Edge Cases).
2. Render summary header and table:

```
Business Scenarios — {engagement name}
══════════════════════════════════════════
Total: {N}  |  Draft: {N}  |  In Review: {N}  |  Approved: {N}

| ID | Title | Status | Linked Drivers | Linked Goals | Requirements | Last Modified |
|---|---|---|---|---|---|---|
| BS-001 | {title} | Draft | DRV-001 | G-001, G-002 | REQ-001–REQ-003 | {date} |
```

3. Flag any scenario with no linked goals: "⚠️ {N} scenario(s) not linked to any goal — run `/ea-scenarios trace BS-NNN` to review."
4. Flag any scenario in Draft status that has been open > 30 days: "⚠️ BS-NNN has been in Draft for {N} days — consider advancing to In Review."

---

## Mode: `new`

Invoked as: `/ea-scenarios new`

Assign the next `BS-NNN` ID (increment from highest existing N in `engagement.json → scenarios[]`; start at BS-001 if none exist).

Work through the six TOGAF elements in sequence. Show progress indicator: `[BS-NNN — Step {N}/9]`.

---

### Step 1/9 — Title and Problem Statement

```
[BS-NNN — Step 1/9] Problem Statement

Give this scenario a short title that names the problem domain (e.g. "Customer Onboarding Delays",
"Regulatory Reporting Gap", "Legacy ERP Integration Failure"):
Title:

Now describe the business problem in 2–4 sentences. Answer: "What is broken, and why does it matter?"
A good problem statement names: the actors affected, the business consequence, and the scale or frequency.
Problem Statement:
```

After capturing title and problem:
```
Does this scenario relate to any existing Issues or Problems?
Linked Issues (ISS-NNN, comma-separated — or press Enter to skip):
Linked Problems (PRB-NNN, comma-separated — or press Enter to skip):
Linked Drivers (DRV-NNN, comma-separated — or press Enter to skip):
```
Display the available ISS-NNN, PRB-NNN, and DRV-NNN IDs from `direction` for reference.

---

### Step 2/9 — Objectives

```
[BS-NNN — Step 2/9] Objectives

Define at least one SMART objective the architecture must achieve to resolve this scenario.
Each objective needs a measure, target, and deadline.

SMART check: Specific · Measurable · Achievable · Relevant · Time-bound

Objective 1:
  Statement (e.g. "Reduce customer onboarding time from 5 days to 1 day"):
  Measure (unit, e.g. "Days to onboard"):
  Target (e.g. "≤ 1 day"):
  Deadline (YYYY-MM-DD):
  Priority (High / Medium / Low):

Add another objective? (y/n)
```

> If the user states a destination without a measure (e.g. "improve customer satisfaction"), prompt: "This looks like a Goal rather than an Objective — objectives need a numeric measure and deadline. Can you add a metric and target date?"

---

### Step 3/9 — Environment and Context

```
[BS-NNN — Step 3/9] Environment and Context

3.1 Internal Environment
Describe the organisational factors that bound this scenario — structure, capabilities, platforms,
budget constraints, regulatory mandate relevant to this problem:

3.2 External Environment
Describe external factors — market pressures, regulatory changes, partner/customer expectations,
competitive landscape relevant to this scenario:

3.3 Technology Context — Current State
Which specific systems, platforms, and integration points are involved in this scenario today?
Focus on what constrains or enables the target state:
```

---

### Step 4/9 — Stakeholders and Concerns

```
[BS-NNN — Step 4/9] Stakeholders and Concerns

Who is directly involved in or affected by this scenario?
(These are scenario-level stakeholders — for the full engagement register, see the Stakeholder Map.)

For each stakeholder:
  Name / Role:
  Primary Concern (what they care about in this scenario):
  Engagement Level (Informed / Consulted / Responsible / Accountable):

Add another stakeholder? (y/n)
```

---

### Step 5/9 — Actors

```
[BS-NNN — Step 5/9] Actors

Actors are the specific people and systems that take actions in this scenario.
(Distinct from stakeholders — actors do things; stakeholders have interests.)

Human Actors (people or roles who initiate, approve, or receive outcomes):
  Actor name / role:
  Role in scenario (what they do):
  Add another? (y/n)

Computing Actors (systems, applications, services, or devices that process or store data):
  System name:
  Type (Application / Platform / Service / Device):
  Role in scenario (what the system does):
  Current State (Existing / To Be Built / To Be Modified):
  Add another? (y/n)
```

---

### Step 6/9 — Requirements

```
[BS-NNN — Step 6/9] Requirements

What specific capabilities must the architecture deliver to resolve this scenario?
Group by domain and assign REQ-NNN IDs (check existing REQ-NNN in engagement.json to avoid duplicates).

For each requirement:
  Statement (what must be true — e.g. "The system must process onboarding in under 1 business day"):
  Domain (Business / Data / Application / Technology):
  Priority (Must / Should / Could):
  Source (which actor or PRB-NNN / ISS-NNN surfaces this?):
  Add another? (y/n)
```

> After capture: "These requirements will be registered. Run `/ea-requirements add` to formally record each REQ-NNN in the Requirements Register with `sourceScenario: BS-NNN` for traceability."

---

### Step 7/9 — Current State Narrative

```
[BS-NNN — Step 7/9] Current State Narrative

Describe what happens today — the "before" picture. Write as a stakeholder would describe it,
not as an architect would model it. Focus on friction, delays, workarounds, and pain points.

Current State Narrative:

Key friction points (list 2–4 specific pain points observable today):
  Friction 1:
  Friction 2:
  (optional) Friction 3:
  (optional) Friction 4:
```

---

### Step 8/9 — Target State Narrative

```
[BS-NNN — Step 8/9] Target State Narrative

Describe what will happen after the architecture is delivered — the "after" picture.
Write to be verifiable: a stakeholder should be able to confirm whether the target has been reached.

Target State Narrative:

Success signals (observable indicators that confirm the target state has been achieved):
  Signal 1:
  Signal 2:
  (optional) Signal 3:
```

---

### Step 9/9 — Change Delta

```
[BS-NNN — Step 9/9] Change Delta

Complete the change delta table — what specifically must the architecture enable?

| Dimension | Current State | Target State | Architecture Action Required |
|---|---|---|---|
| Process | {current} | {target} | {what to design/build/change} |
| Data | {current} | {target} | {what to design/build/change} |
| Application | {current} | {target} | {what to design/build/change} |
| Technology | {current} | {target} | {what to design/build/change} |

Fill in each row — press Enter to skip a dimension that does not apply.
```

---

### Confirmation and Write

Show a full preview summary of the scenario, then:

```
Create Business Scenario BS-NNN: "{title}"?
This will write artifacts/phase-a/business-scenario-BS-NNN.md and index it in engagement.json.
(y/n)
```

On confirm:
1. Read `ea-assistant/templates/business-scenario.md` (the template).
2. Substitute all `{{placeholder}}` tokens with captured answers.
3. Write to `EA-projects/{slug}/artifacts/phase-a/business-scenario-BS-NNN.md`.
4. Append to `engagement.json → scenarios[]`:
   ```json
   {
     "id": "BS-NNN",
     "title": "{title}",
     "status": "Draft",
     "phase": "A",
     "path": "artifacts/phase-a/business-scenario-BS-NNN.md",
     "linkedDrivers": ["DRV-NNN"],
     "linkedIssues": ["ISS-NNN"],
     "linkedProblems": ["PRB-NNN"],
     "linkedGoals": ["G-NNN"],
     "linkedObjectives": ["OBJ-NNN"],
     "requirements": ["REQ-NNN"],
     "lastModified": "YYYY-MM-DD"
   }
   ```
5. Set `engagement.json → lastModified: today`.
6. Confirm:
   ```
   ✅ BS-NNN created — artifacts/phase-a/business-scenario-BS-NNN.md
   
   Next steps:
   • Run `/ea-scenarios trace BS-NNN` to verify motivation chain linkage.
   • Run `/ea-requirements add` to formally register each REQ-NNN with sourceScenario: BS-NNN.
   • Run `/ea-grill business-scenario-BS-NNN` to check TOGAF completeness.
   ```

---

## Mode: `view`

Invoked as: `/ea-scenarios view BS-NNN`

1. Resolve `BS-NNN` from `engagement.json → scenarios[]` and get the `path`.
2. Read and display the full artifact file.
3. Show compliance checklist status from the `<details>` block.

---

## Mode: `interview`

Invoked as: `/ea-scenarios interview BS-NNN`

Used to complete or enrich an existing scenario, section by section.

1. Read the artifact at the resolved path.
2. Scan for unfilled `{{placeholder}}` tokens and `⚠️ Pending` compliance items.
3. Report:
   ```
   Business Scenario BS-NNN — {title}
   Completeness check:

   ✅ Problem Statement
   ⚠️ Pending — Objectives (no SMART objectives defined)
   ✅ Environment documented
   ⚠️ Pending — Stakeholders (no named stakeholders)
   ✅ Actors defined
   ⚠️ Pending — Requirements (no requirements captured)
   ✅ Current State narrative
   ✅ Target State narrative

   3 sections need attention. Work through them now? (y/n/[section number to jump to])
   ```
4. For each pending section, run the corresponding guided prompt from `new` mode (steps 2–8 above).
5. After each section: ask "Section complete? (y/n — n to re-answer)".
6. On completion: update the artifact file and `engagement.json → scenarios[BS-NNN].lastModified`.
7. Update compliance checklist items to `✅ Done` where sections are now complete.

---

## Mode: `trace`

Invoked as: `/ea-scenarios trace [BS-NNN]`

**Without BS-NNN — traceability summary for all scenarios:**

```
| BS-NNN | Title | Status | ← ISS/PRB/DRV | → G/OBJ | → REQ | Chain Status |
|---|---|---|---|---|---|---|
| BS-001 | {title} | Draft | ISS-001, DRV-002 | G-001, OBJ-002 | REQ-001–003 | ✅ |
```

**With BS-NNN — full motivation chain:**

```
Scenario Chain — BS-NNN: {title}

Status: {status}  |  Phase: A  |  Last Modified: {date}

── Upstream — What triggered this scenario ─────────────────────────────────
 Drivers feeding this scenario:
   → DRV-001 — {driver statement} [External / High]

 Issues this scenario addresses:
   → ISS-001 — {issue statement} [Domain: {domain} / Severity: {severity}]

 Problems this scenario addresses:
   → PRB-001 — {problem statement} [Severity: {severity}]

── Scenario Scope ──────────────────────────────────────────────────────────
 Objectives operationalised by this scenario:
   → OBJ-001 — {objective} [Measure: {measure}, Target: {target}, Deadline: {date}]

 Goals this scenario advances:
   → G-001 — {goal statement} [Domain: {domain} / Priority: {priority}]

── Downstream — What this scenario generates ──────────────────────────────
 Requirements generated:
   → REQ-001 — {statement} [Domain: {domain} / Priority: {priority}]
   → REQ-002 — {statement} [Domain: {domain} / Priority: {priority}]

 Architecture Vision section:
   → Architecture Vision §1 (Problem Summary) / §14 (Scenario Reference)

Chain status: {✅ Complete | ⚠️ Partial (list missing links) | 🔴 Orphan (no goals linked)}
```

Flag any upstream or downstream links that reference IDs not found in `engagement.json`.

---

## Mode: `generate`

Invoked as: `/ea-scenarios generate`

Produces a **Scenarios Summary Register** — a cross-cutting artifact that lists all scenarios, their completeness, and the aggregate requirements they generate.

1. Read all scenario files from `engagement.json → scenarios[]`.
2. Write `EA-projects/{slug}/artifacts/cross-cutting/scenarios-register-{YYYY-MM-DD}.md`:

```markdown
---
artifact: Business Scenarios Register
artifactId: scenarios-register
engagement: {name}
phase: cross-cutting
status: Draft
generated: {YYYY-MM-DD}
relatedArtifacts: ["architecture-vision", "requirements-register"]
diagrams: []
links: []
---

# Business Scenarios Register

**Engagement:** {name}
**Generated:** {YYYY-MM-DD}
**TOGAF Reference:** Phase A — Business Scenarios (§25.3.3)

---

## Summary

| Metric | Count |
|---|---|
| Total Scenarios | {N} |
| Draft | {N} |
| In Review | {N} |
| Approved | {N} |
| Total Requirements Generated | {N} |
| Orphaned (no goal link) | {N} |

---

## Scenarios by Status

### {Status} Scenarios

#### BS-NNN: {title}

**Problem Statement:** {brief}

| Element | Status | Detail |
|---|---|---|
| Problem Statement | ✅ / ⚠️ | {brief} |
| Objectives | ✅ {N} defined / ⚠️ None | {first objective} |
| Environment | ✅ / ⚠️ | — |
| Stakeholders | ✅ {N} named / ⚠️ None | — |
| Actors | ✅ {N} human, {N} computing / ⚠️ | — |
| Requirements | ✅ {N} generated / ⚠️ None | REQ-NNN, REQ-NNN |

**Linked Drivers:** {DRV-NNN list or —}
**Linked Goals:** {G-NNN list or —}
**Linked Issues/Problems:** {ISS-NNN / PRB-NNN list or —}

**Requirements generated by this scenario:**
{REQ-NNN table subset}

---
{Repeat for each scenario}
```

3. Register in `engagement.json → artifacts[]`.
4. Confirm: `"Scenarios Register written to artifacts/cross-cutting/scenarios-register-{YYYY-MM-DD}.md — {N} scenarios."`

---

## Edge Cases

| Scenario | Handling |
|---|---|
| No scenarios found | "No business scenarios found. Start with `/ea-scenarios new` to create your first scenario." |
| `view` / `interview` / `trace` with unknown BS-NNN | "BS-NNN not found in engagement.json. Run `/ea-scenarios list` to see available scenarios." |
| Scenario file exists but not in engagement.json index | "Found artifact file but no index entry — run `/ea-scenarios interview BS-NNN` to re-index." |
| Objective without measure or deadline | Warn during `new` / `interview`: "This objective is missing a {measure/deadline} — without it, it cannot be verified as SMART." |
| Requirement overlaps with existing REQ-NNN | "REQ-NNN with similar statement exists — confirm this is a new, distinct requirement (y/n)." |
| Scenario with no linked goals after `new` | "⚠️ No goals linked to BS-NNN. Architecture Vision requires that each scenario advances at least one goal. Use `/ea-goals list` to review, then link via the Traceability Appendix or `/ea-scenarios interview BS-NNN`." |
| `interview` on Approved scenario | "BS-NNN is Approved — editing requires setting status to Draft first. Change status? (y/n)" |
