# EA Target State + Stakeholder Action Plan — Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Add a Target State Declaration artifact (`/ea-target`) and a Stakeholder Action Plan artifact (`/ea-actions`) to the ea-assistant plugin.

**Architecture:** Two new commands + two new templates. The Target State Declaration is a Phase A artifact capturing where the engagement is going; the Stakeholder Action Plan is a cross-cutting governance artifact seeded from the SAoW and Target State Declaration, providing a per-approver action view for governance forums.

**Tech Stack:** Markdown + YAML frontmatter (Claude Code plugin framework); validation via `~/.bun/bin/bun .github/scripts/validate-frontmatter.ts`.

---

## File Map

| Action | Path |
|---|---|
| Create | `ea-assistant/templates/target-state-declaration.md` |
| Create | `ea-assistant/commands/ea-target.md` |
| Create | `ea-assistant/templates/stakeholder-action-plan.md` |
| Create | `ea-assistant/commands/ea-actions.md` |
| Modify | `ea-assistant/skills/ea-artifact-templates/SKILL.md` |
| Modify | `ea-assistant/commands/ea-help.md` |
| Modify | `ea-assistant/CLAUDE.md` |

All paths are relative to the repo root `/mnt/d/dev/claude-sandbox/plugins/`.

---

## Task 1: Create the Target State Declaration template

**Files:**
- Create: `ea-assistant/templates/target-state-declaration.md`

- [ ] **Step 1: Write the template file**

Write the following content exactly to `ea-assistant/templates/target-state-declaration.md`:

```markdown
---
artifact: Target State Declaration
engagement: {{engagement_name}}
phase: A
status: Draft
reviewStatus: Not Reviewed
version: 0.1
templateVersion: 0.9.55
lastModified: {{YYYY-MM-DD}}
taxonomy:
  domain: Cross-cutting
  category: Strategy
  audience: Executive
  layer: Motivation
  sensitivity: Confidential
  tags: [target-state, goals, success-criteria, phase-a]
relatedArtifacts: []
diagrams: []
links: []
---
<details>
<summary>🔒 TOGAF/ADM Compliance Status (author only — collapses on export)</summary>

## Compliance Checklist

| Requirement | Status | Notes |
|---|---|---|
| T3-A3 | ⚠️ Pending | |
| T3-A4 | ⚠️ Pending | |
| T3-ADR | ⚠️ Pending | |
| T3-RATIONALE | ⚠️ Pending | |
| Linked to Architecture Vision | ⚠️ Pending | |
| Linked to Statement of Architecture Work | ⚠️ Pending | |

*This section is for author guidance only. Run `/ea-grill` to validate compliance.*

</details>

<details>
<summary>📋 Guidance</summary>

**Purpose:** The Target State Declaration is the engagement's authoritative statement of where the organisation is going — what will be true when this architecture work succeeds. It translates the Architecture Vision into a concrete, domain-by-domain description of the desired end state, and defines the success criteria by which the engagement will be judged complete.

**What to include:** An overall target state summary, per-domain descriptions of the desired future state, explicit success criteria (with measurable conditions and named approvers), key assumptions underpinning the target state, and traceability to goals (G-NNN), objectives (OBJ-NNN), and strategies (STR-NNN).

**Relationship to other artifacts:**
- **Architecture Vision** — sets direction and justifies the engagement; Target State Declaration operationalises it
- **SAoW** — defines scope, deliverables, and schedule; Target State Declaration defines what success looks like
- **Stakeholder Action Plan** — seeded from this artifact's success criteria and the SAoW's acceptance criteria

**Quality indicators:**
- Each domain target state is specific enough that an architect reviewing the final architecture would know whether it has been achieved
- Success criteria have measurable conditions — "all critical data flows are documented in ArchiMate" not "data architecture is complete"
- Every success criterion has a named approver
- The traceability table links every domain target state to at least one G-NNN goal

**Common mistakes:**
- Target state written as a vision statement — aspirational language without testable conditions
- Domains not in scope left blank rather than marked ➖ Not applicable
- Success criteria that duplicate the SAoW acceptance criteria word-for-word without adding architectural specificity

**TOGAF reference:** Informed by TOGAF 10 Phase A §25 — Architecture Vision and Statement of Architecture Work. The Target State Declaration is a practitioner-level supplement that bridges the Vision's qualitative direction and the SAoW's contractual commitments.

</details>

<details>
<summary>💡 Practitioner Tip — Target State</summary>

- Write the target state **before** the domain architecture work, not after — it is the compass, not the summary. (Tip #5)
- **Use strategic tension** — the target state should make visible the gap between current and desired state. Quantify where possible. (Deep tactic #50)
- Test every success criterion against the question: "Would two senior architects agree on whether this is met?" If not, it is too vague. (Tip #12)
- The target state is a **commitment device** — if stakeholders won't sign off on it, find out why before proceeding. (Tip #11)

</details>

# Target State Declaration

**Engagement:** {{engagement_name}}
**Organisation:** {{organisation}}
**Sponsor:** {{sponsor}}
**Architecture Lead:** {{architecture_lead}}
**Date:** {{YYYY-MM-DD}}
**Version:** {{version}}
**Status:** {{status}}

---

## Executive Summary

<details>
<summary>📋 Guidance</summary>

One paragraph summarising what success looks like for this engagement — the end state in plain language for an executive audience. Reference the Architecture Vision for strategic context.
Run `/ea-summary refresh` to regenerate this section from current artifact content.

</details>

{{executive_summary}}

---

## 1. Overall Target State

<details>
<summary>📋 Guidance</summary>

A concise statement (1–3 sentences) of what will be true when this engagement succeeds. This is not a vision statement — it is a testable description of the desired future state. A reader should be able to use this statement to evaluate whether a proposed architecture achieves the target.

</details>

{{overall_target_state}}

---

## 2. Per-Domain Target States

<details>
<summary>📋 Guidance</summary>

Describe the target state in each architecture domain in scope for this engagement. Be specific — describe what the architecture will look like, not just what it will enable. If a domain is not in scope, mark it ➖ Not applicable.

</details>

### Business Domain

{{target_state_business}}

### Data Domain

{{target_state_data}}

### Application Domain

{{target_state_application}}

### Technology Domain

{{target_state_technology}}

---

## 3. Success Criteria

<details>
<summary>📋 Guidance</summary>

Define the measurable conditions that must be satisfied for this engagement to be considered complete. Each criterion must be testable — two architects reviewing the final deliverables should reach the same conclusion about whether it is met. The `Accepted By` column names the individual with authority to confirm that criterion is satisfied. Pre-populate from the SAoW §6 Acceptance Criteria table where a SAoW exists.

</details>

| # | Criterion | Measurable Condition | Linked Deliverable | Accepted By | Status |
|---|---|---|---|---|---|
| 1 | {{criterion_1}} | {{condition_1}} | {{deliverable_1}} | {{approver_1}} | Pending |
| 2 | {{criterion_2}} | {{condition_2}} | {{deliverable_2}} | {{approver_2}} | Pending |

Status values: `Pending | Met | Not Met | Deferred`

---

## 4. Key Assumptions

<details>
<summary>📋 Guidance</summary>

List the assumptions on which this target state depends. An assumption that proves false may invalidate the target state. Flag high-risk assumptions — consider converting them to PAD-NNN entries or RIS-NNN risks.

</details>

- {{assumption_1}}
- {{assumption_2}}

---

## 5. Traceability

<details>
<summary>📋 Guidance</summary>

Link each domain target state to the goals (G-NNN), objectives (OBJ-NNN), and strategies (STR-NNN) in engagement.json that it realises. Every domain target state should trace to at least one goal. Use `/ea-trace` to verify the full DRV→G→OBJ→STR→WP chain.

</details>

| Domain Target State | Goals | Objectives | Strategies |
|---|---|---|---|
| Business | {{G-NNN}} | {{OBJ-NNN}} | {{STR-NNN}} |
| Data | {{G-NNN}} | {{OBJ-NNN}} | {{STR-NNN}} |
| Application | {{G-NNN}} | {{OBJ-NNN}} | {{STR-NNN}} |
| Technology | {{G-NNN}} | {{OBJ-NNN}} | {{STR-NNN}} |

---

## Appendix A3 — Decision Log

<details>
<summary>📋 Guidance</summary>

Record all decisions made during the development of this artifact.
Each row captures the decision item, agreed value, governance state, who captured it,
who owns or must verify it, and classification fields used by /ea-decisions.
Use /ea-decisions to aggregate this table across all artifacts into a Decision Register.

</details>

| Item | Value | State | Captured By | Owner | Authority | Domain | Cost | Impact | Risk | Subject | Date |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| *(no decisions recorded)* | — | — | — | — | — | — | — | — | — | — | — |

---

## Appendix A4 — Stakeholder Concerns & Objections

<details>
<summary>📋 Guidance</summary>

Record all stakeholder concerns, objections, and tough questions raised about this artifact.
Sources include grill-me sessions, Architecture Review Board feedback, executive challenge
sessions, and sponsor meetings. For each concern, record whether it is addressed in existing
documentation (Addressed / Partially Addressed) or requires further action (Requires Attention).
Use `/ea-concerns` to aggregate unresolved items across all artifacts. Concerns that represent
a material risk should also be raised as RIS-NNN entries via `/ea-risks`.

</details>

| ID | Concern | Raised By | Category | Status | Response | Action / Owner |
|---|---|---|---|---|---|---|
| *(no concerns recorded)* | — | — | — | — | — | — |

---

## Appendix A5 — Related Architecture Decisions

<details>
<summary>📋 Guidance</summary>

List ADRs that informed, were informed by, or are otherwise relevant to this artifact.
Reference the ADR-NNN ID so readers can navigate to the full decision record.

</details>

| ADR ID | Title | Status | Summary |
|---|---|---|---|
| *(no related ADRs recorded)* | — | — | — |

---

## Artifact Working Notes

> Working-layer: persists across reviews. Populated by `/ea-grill` (Critiques), `/ea-review` (Comments), and manually. Never exported to Word/PPTX — stripped by `/ea-generate`.

### Comments

*Ad-hoc notes from architects, reviewers, or stakeholders.*

| Date | Author | Note |
|---|---|---|
| — | — | — |

### Critiques

*Formal findings from `/ea-grill` or `/ea-review` that require a response before this artifact can be approved.*

| # | Section | Finding | Source | Date | Status |
|---|---|---|---|---|---|
| — | — | — | — | — | Open |

### Exceptions

*Formal exceptions granted to a standard, principle, or compliance rule — each must have a rationale and approver.*

| # | Rule / Principle Waived | Rationale | Approver | Date |
|---|---|---|---|---|
| — | — | — | — | — |

### Outstanding Tasks

*Things that must be completed before this artifact can move to Approved status.*

- [ ] *(Add tasks — e.g. "Populate per-domain target states before Phase B kick-off")*

*This document was created using the EA Assistant plugin.*
*Use `/ea-concerns` to generate a cross-artifact Concerns Register from all A4 tables.*
```

- [ ] **Step 2: Verify the file was created**

```bash
ls -la /mnt/d/dev/claude-sandbox/plugins/ea-assistant/templates/target-state-declaration.md
```

Expected: file exists, non-zero size.

- [ ] **Step 3: Run frontmatter validator**

```bash
cd /mnt/d/dev/claude-sandbox/plugins && ~/.bun/bin/bun .github/scripts/validate-frontmatter.ts ea-assistant/
```

Expected: passes with no errors for the new template. (Other errors in the repo are pre-existing and can be ignored.)

- [ ] **Step 4: Commit**

```bash
cd /mnt/d/dev/claude-sandbox/plugins
git add ea-assistant/templates/target-state-declaration.md
git commit -m "feat(ea-assistant): add Target State Declaration template"
```

---

## Task 2: Create the `/ea-target` command

**Files:**
- Create: `ea-assistant/commands/ea-target.md`

- [ ] **Step 1: Write the command file**

Write the following content exactly to `ea-assistant/commands/ea-target.md`:

```markdown
---
name: ea-target
description: Create and manage the Target State Declaration — captures per-domain target states, success criteria, and traceability to goals and objectives
argument-hint: "[new|view|update <section> <value>]"
allowed-tools: [Read, Write, Bash]
---

You are executing the `/ea-target` command.

## Overview

The Target State Declaration is the engagement's authoritative statement of the desired end state — what will be true when this architecture work succeeds. It translates the Architecture Vision into a concrete, domain-by-domain description of the future state and defines the success criteria by which the engagement will be judged complete.

The Target State Declaration is defined by and must be consistent with:
1. The Statement of Architecture Work (SAoW) — scope, deliverables, and acceptance criteria
2. The Architecture Vision — strategic direction and justification

It feeds the Stakeholder Action Plan (`/ea-actions`) which surfaces per-approver actions for governance forums.

**Modes:**
- `new` (default if no artifact exists) — interview-driven creation
- `view` — display the current Target State Declaration
- `update <section> <value>` — update a specific section

---

## Step 1 — Resolve Active Engagement

1. Check the conversation context for an active engagement slug.
2. If none found, scan `EA-projects/*/engagement.json` and ask the user to select one.
3. Load `engagement.json` — extract: name, slug, organisation, sponsor, currentPhase, architectureDomains, direction (goals, objectives, strategies).

---

## Mode: `new`

Invoked as: `/ea-target new` or `/ea-target` when no Target State Declaration artifact exists.

### Pre-check

Check whether `artifacts/phase-a/target-state-declaration.md` already exists in the engagement folder.

- If it exists: "A Target State Declaration already exists. Open it for editing (`/ea-target view`) or overwrite it? (edit/overwrite)" — stop unless user selects overwrite.
- If SAoW exists at `artifacts/phase-a/statement-of-architecture-work.md`: read §6 acceptance criteria table — extract all rows into a buffer for use in Step 4.

### Interview

Conduct the following questions in sequence. Apply standard interview shortcuts (s = skip, n/a = not applicable, opt-out, a: = decision log). Use the template at `templates/target-state-declaration.md` for placeholder keys.

**Q1 — Overall target state:**
```
What will be true when this engagement succeeds?
(1–3 sentences — a testable description of the desired future state, not an aspiration)
```

**Q2 — Per-domain target states** (one question per domain in `engagement.json → architectureDomains`; skip domains not in scope):

For each domain in [Business, Data, Application, Technology]:
```
In the {domain} domain, what does the target state look like?
(Describe the future architecture — what will exist, what will be different, what will be possible)
```

If a domain is not in `architectureDomains`, pre-fill with `➖ Not applicable`.

**Q3 — Success criteria:**

If SAoW acceptance criteria were found in the pre-check buffer:
```
I found {N} acceptance criteria in the SAoW (§6). Here they are:

{table of SAoW acceptance criteria rows}

Do these cover all success criteria for this engagement, or are there additional architectural success criteria to add?
(Enter additional criteria one at a time, or press Enter to accept the SAoW criteria as-is)
```

If no SAoW exists:
```
What specific conditions must be met for this engagement to be considered complete?
(Enter each criterion as: [Condition] | [Measurable test] | [Deliverable] | [Accepted By])
```

Collect all criteria. For each criterion without an `Accepted By` value, prompt: "Who has authority to confirm this criterion is met?"

**Q4 — Key assumptions:**
```
What key assumptions does this target state depend on?
(List each assumption — flag any that could invalidate the target state if proven false)
```

**Q5 — Traceability:**
```
Which goals (G-NNN) does this target state realise?
```
Display available G-NNN entries from `engagement.json → direction.goals[]`. Allow multi-select.

If no goals exist: "No goals found — you can add goals later via `/ea-goals add` and link them with `/ea-target update traceability`."

### Writing the artifact

1. Substitute all collected answers into `templates/target-state-declaration.md`.
2. Pre-populate `engagement_name`, `organisation`, `sponsor` from `engagement.json`.
3. Set `lastModified` to today's date.
4. Write to `EA-projects/{slug}/artifacts/phase-a/target-state-declaration.md`.
5. Register in `engagement.json → artifacts[]`:
```json
{
  "id": "target-state-declaration",
  "name": "Target State Declaration",
  "phase": "A",
  "file": "artifacts/phase-a/target-state-declaration.md",
  "reviewFile": "artifacts/phase-a/target-state-declaration.review.md",
  "status": "Draft",
  "createdAt": "{ISO 8601 timestamp}",
  "lastModified": "{ISO 8601 timestamp}",
  "reviewStatus": "Not Reviewed"
}
```
6. Update `engagement.json → lastModified`.
7. Confirm: "Target State Declaration written to `artifacts/phase-a/target-state-declaration.md`. Use `/ea-actions generate` to produce a Stakeholder Action Plan from this artifact."

---

## Mode: `view`

Invoked as: `/ea-target view`

1. Read `EA-projects/{slug}/artifacts/phase-a/target-state-declaration.md`.
2. If the file does not exist: "No Target State Declaration found. Run `/ea-target new` to create one."
3. Display the full artifact content inline.

---

## Mode: `update`

Invoked as: `/ea-target update <section> <value>`

Valid section names and what they update:

| Section name | Updates |
|---|---|
| `summary` | §1 Overall Target State (`{{overall_target_state}}`) |
| `business` | §2 Business Domain (`{{target_state_business}}`) |
| `data` | §2 Data Domain (`{{target_state_data}}`) |
| `application` | §2 Application Domain (`{{target_state_application}}`) |
| `technology` | §2 Technology Domain (`{{target_state_technology}}`) |
| `assumptions` | §4 Key Assumptions (replace full list) |
| `traceability` | §5 Traceability table |

1. Read the current artifact.
2. Show the current value of the named section.
3. Ask: "Replace with: `{value}`? (y/n)"
4. On confirm: replace the placeholder/current value, update `lastModified`, write back.

---

## Edge Cases

| Scenario | Handling |
|---|---|
| Artifact already exists on `new` | Prompt: edit or overwrite |
| No SAoW found | Skip SAoW pre-population; prompt for success criteria directly |
| SAoW §6 is empty/placeholder | Warn: "SAoW §6 Acceptance Criteria is unpopulated — fill it in first via `/ea-interview` or enter success criteria directly" |
| No goals in direction | Skip traceability Q5; note in artifact; suggest `/ea-goals add` |
| Domain not in architectureDomains | Pre-fill that domain section with `➖ Not applicable` |
| Unknown section name in `update` | List valid section names and stop |
```

- [ ] **Step 2: Verify the file was created**

```bash
ls -la /mnt/d/dev/claude-sandbox/plugins/ea-assistant/commands/ea-target.md
```

Expected: file exists, non-zero size.

- [ ] **Step 3: Run frontmatter validator**

```bash
cd /mnt/d/dev/claude-sandbox/plugins && ~/.bun/bin/bun .github/scripts/validate-frontmatter.ts ea-assistant/
```

Expected: passes with no new errors.

- [ ] **Step 4: Commit**

```bash
cd /mnt/d/dev/claude-sandbox/plugins
git add ea-assistant/commands/ea-target.md
git commit -m "feat(ea-assistant): add /ea-target command"
```

---

## Task 3: Create the Stakeholder Action Plan template

**Files:**
- Create: `ea-assistant/templates/stakeholder-action-plan.md`

- [ ] **Step 1: Write the template file**

Write the following content exactly to `ea-assistant/templates/stakeholder-action-plan.md`:

```markdown
---
artifact: Stakeholder Action Plan
engagement: {{engagement_name}}
phase: All
status: Draft
reviewStatus: Not Reviewed
version: 0.1
templateVersion: 0.9.55
lastModified: {{YYYY-MM-DD}}
taxonomy:
  domain: Cross-cutting
  category: Governance
  audience: Governance
  layer: Governance
  sensitivity: Confidential
  tags: [stakeholders, approvals, actions, governance, arb]
relatedArtifacts: []
diagrams: []
links: []
---
<details>
<summary>📋 Guidance</summary>

**Purpose:** The Stakeholder Action Plan provides a consolidated, per-approver view of what each stakeholder with approval authority must do to progress this engagement. It is seeded from the SAoW acceptance criteria (§6) and sign-off table (§7), enriched with success criteria from the Target State Declaration, and suitable for distribution to a governance forum or ARB.

**What to include:** A summary of the target state, an approval authority register (one row per approver), per-approver action detail sections (listing each approval with acceptance criteria, due date, and status), and a governance schedule of key approval gates.

**Lifecycle:** Generate once from SAoW + Target State Declaration using `/ea-actions generate`. Refine with `/ea-actions update`. Regenerate after significant SAoW changes.

**Quality indicators:**
- Every deliverable requiring sign-off has a named approver
- Every action has a due date traceable to the SAoW schedule
- Status is kept current — stale action plans erode stakeholder trust

**Common mistakes:**
- Action plan that lists deliverables but no acceptance criteria — approvers need to know what "approved" means
- Not distributing the plan to approvers — an action plan no one has seen is not an action plan
- Regenerating the plan without preserving manual updates to status — use `/ea-actions update` to update individual rows

</details>

# Stakeholder Action Plan

**Engagement:** {{engagement_name}}
**Organisation:** {{organisation}}
**Date:** {{YYYY-MM-DD}}
**Version:** {{version}}
**Status:** {{status}}

---

## Executive Summary

<details>
<summary>📋 Guidance</summary>

One paragraph: the target state in plain language, the total number of approvers, pending/complete/overdue action counts. Generated automatically by `/ea-actions generate` — update when regenerating.

</details>

{{executive_summary}}

**Target State:** {{target_state_summary}}

**Action Summary:**
| Total Approvers | Pending | In Review | Approved | Deferred | Overdue |
|---|---|---|---|---|---|
| {{total_approvers}} | {{pending}} | {{in_review}} | {{approved}} | {{deferred}} | {{overdue}} |

---

## Approval Authority Register

<details>
<summary>📋 Guidance</summary>

One row per stakeholder with approval authority. Derived from SAoW §6 (`Accepted By`) and §7 (sign-off). Used as the navigation index for the per-approver sections below.

</details>

| Name | Role | Organisation | Pending Actions | Next Due | Overall Status |
|---|---|---|---|---|---|
| {{approver_name}} | {{role}} | {{organisation}} | {{pending_count}} | {{next_due_date}} | Pending |

---

## Per-Approver Action Detail

<details>
<summary>📋 Guidance</summary>

One H3 section per approver. Each section contains an action table listing all approvals this stakeholder owns. Status values: Pending | In Review | Approved | Deferred.

</details>

### {{approver_name_1}} — {{role_1}}

**Organisation:** {{organisation_1}}
**Role reference:** {{ROLE-NNN}}

| # | Action | Deliverable | Acceptance Criteria | Due Date | Status |
|---|---|---|---|---|---|
| 1 | Review and approve | {{deliverable_1}} | {{acceptance_criteria_1}} | {{due_date_1}} | Pending |

---

## Governance Schedule

<details>
<summary>📋 Guidance</summary>

Key approval gates in sequence. Derived from the SAoW schedule (§4). Add ARB sessions, sponsor reviews, and formal sign-off meetings.

</details>

| Gate | Description | Required Approvers | Target Date | Status |
|---|---|---|---|---|
| {{gate_1}} | {{description_1}} | {{approvers_1}} | {{date_1}} | Pending |

---

## Artifact Working Notes

> Working-layer: persists across reviews. Never exported to Word/PPTX — stripped by `/ea-generate`.

### Comments

| Date | Author | Note |
|---|---|---|
| — | — | — |

### Outstanding Tasks

- [ ] *(Add tasks — e.g. "Distribute to approvers before next ARB session")*

*This document was created using the EA Assistant plugin.*
*Use `/ea-actions status` for a summary of pending and overdue actions.*
```

- [ ] **Step 2: Verify the file was created**

```bash
ls -la /mnt/d/dev/claude-sandbox/plugins/ea-assistant/templates/stakeholder-action-plan.md
```

Expected: file exists, non-zero size.

- [ ] **Step 3: Run frontmatter validator**

```bash
cd /mnt/d/dev/claude-sandbox/plugins && ~/.bun/bin/bun .github/scripts/validate-frontmatter.ts ea-assistant/
```

Expected: passes with no new errors.

- [ ] **Step 4: Commit**

```bash
cd /mnt/d/dev/claude-sandbox/plugins
git add ea-assistant/templates/stakeholder-action-plan.md
git commit -m "feat(ea-assistant): add Stakeholder Action Plan template"
```

---

## Task 4: Create the `/ea-actions` command

**Files:**
- Create: `ea-assistant/commands/ea-actions.md`

- [ ] **Step 1: Write the command file**

Write the following content exactly to `ea-assistant/commands/ea-actions.md`:

```markdown
---
name: ea-actions
description: Generate and manage the Stakeholder Action Plan — a consolidated per-approver action view seeded from the SAoW and Target State Declaration, suitable for governance forums and ARB
argument-hint: "[generate|view|update <approver> <row#> <field> <value>|status]"
allowed-tools: [Read, Write, Bash]
---

You are executing the `/ea-actions` command.

## Overview

The Stakeholder Action Plan provides a consolidated, per-approver view of what each stakeholder with approval authority must do to progress this engagement. It is seeded from the SAoW acceptance criteria and sign-off table, enriched with success criteria from the Target State Declaration, and suitable for distribution to a governance forum or ARB.

**Modes:**
- `generate` — seed from SAoW + Target State Declaration; show draft for confirmation before writing
- `view` — display the current Stakeholder Action Plan
- `update <approver> <row#> <field> <value>` — update a single action row
- `status` — summary of pending, complete, and overdue actions

---

## Step 1 — Resolve Active Engagement

1. Check the conversation context for an active engagement slug.
2. If none found, scan `EA-projects/*/engagement.json` and ask the user to select one.
3. Load `engagement.json` — extract: name, slug, organisation, currentPhase, direction, artifacts list.

---

## Mode: `generate`

Invoked as: `/ea-actions generate`

### Pre-check

Check whether `artifacts/cross-cutting/governance/stakeholder-action-plan.md` already exists.

- If it exists: "Stakeholder Action Plan already exists. Regenerate (replaces content) or view existing? (regenerate/view)" — stop unless user selects regenerate.

### Data Collection

**Step A — Read SAoW:**

Check for `artifacts/phase-a/statement-of-architecture-work.md` in the engagement folder.

- If not found: "No SAoW found. Create one via `/ea-interview start phase A` before generating the action plan." Stop.
- If found, read and extract:
  - §6 Acceptance Criteria table rows: `Deliverable | Acceptance Criteria | Accepted By`
  - §7 Sign-off table rows: `Role | Name`
  - §4 Schedule table rows: `Milestone | Description | Target Date | Owner`

Flag if §6 or §7 are empty/placeholder-only: "⚠️ SAoW §6 or §7 is unpopulated — the action plan will be a stub. Continue? (y/n)"

**Step B — Read Target State Declaration:**

Check for `artifacts/phase-a/target-state-declaration.md`.

- If found: extract §3 Success Criteria table rows (`Criterion | Measurable Condition | Linked Deliverable | Accepted By`) and §1 Overall Target State summary.
- If not found: warn "No Target State Declaration found — success criteria will come from the SAoW only. Run `/ea-target new` to create one." Continue.

**Step C — Build approver map:**

1. Extract all unique names from SAoW §6 `Accepted By` column.
2. Match each name against SAoW §7 `Name` column to find their `Role`.
3. For names in §6 not present in §7: include them with role `⚠️ Role not in SAoW §7 — verify`.
4. Merge Target State Declaration §3 `Accepted By` values into the approver map — deduplicate by name.

**Step D — Build per-approver action rows:**

For each approver:
1. Collect all SAoW §6 rows where `Accepted By` = this approver.
2. Collect all Target State §3 rows where `Accepted By` = this approver (skip duplicates already from SAoW).
3. For each row, find a matching milestone in SAoW §4 `Milestone` text — use `Target Date` as `Due Date`. If no match: leave `Due Date` as `{{due_date}}`.
4. Set all statuses to `Pending`.

**Step E — Build target state summary:**

- If Target State Declaration exists: use §1 Overall Target State text.
- Otherwise: use `engagement.json → direction.vision` if populated, else `{{target_state_summary}}`.

### Draft and Confirm

Present the full draft to the user:

```
Stakeholder Action Plan — {engagement name}
══════════════════════════════════════════════
Approvers: {N}
Total actions: {N}

{Per-approver summary table}

---
Per-Approver Detail:

{For each approver: name, role, action table}

---
Governance Schedule:
{SAoW §4 milestones relevant to sign-off}

Write this action plan? (y/n/edit)
```

If user selects `edit`: prompt for which approver or section to modify before writing.

### Writing the Artifact

1. Substitute all collected data into `templates/stakeholder-action-plan.md`.
2. Populate `engagement_name`, `organisation` from `engagement.json`.
3. Compute action summary counts (all Pending at generation time).
4. Set `lastModified` to today.
5. Write to `EA-projects/{slug}/artifacts/cross-cutting/governance/stakeholder-action-plan.md`.
6. Register in `engagement.json → artifacts[]`:
```json
{
  "id": "stakeholder-action-plan",
  "name": "Stakeholder Action Plan",
  "phase": "All",
  "file": "artifacts/cross-cutting/governance/stakeholder-action-plan.md",
  "reviewFile": "artifacts/cross-cutting/governance/stakeholder-action-plan.review.md",
  "status": "Draft",
  "createdAt": "{ISO 8601 timestamp}",
  "lastModified": "{ISO 8601 timestamp}",
  "reviewStatus": "Not Reviewed"
}
```
7. Update `engagement.json → lastModified`.
8. Confirm: "Stakeholder Action Plan written to `artifacts/cross-cutting/governance/stakeholder-action-plan.md` — {N} approvers, {N} actions. Use `/ea-actions status` for a summary."

---

## Mode: `view`

Invoked as: `/ea-actions view`

1. Read `EA-projects/{slug}/artifacts/cross-cutting/governance/stakeholder-action-plan.md`.
2. If the file does not exist: "No Stakeholder Action Plan found. Run `/ea-actions generate` to create one."
3. Display the full artifact content inline.

---

## Mode: `update`

Invoked as: `/ea-actions update <approver> <row#> <field> <value>`

`<approver>` — partial name match (case-insensitive) against the H3 section headers.
`<row#>` — 1-based row number in that approver's action table.
`<field>` — one of: `action`, `deliverable`, `acceptance-criteria`, `due-date`, `status`
`<value>` — new value. For `status`: must be one of `Pending | In Review | Approved | Deferred`.

1. Read the artifact.
2. Find the approver section (H3 matching `<approver>`). If ambiguous (multiple matches): list matches and ask user to be more specific.
3. Find row `<row#>` in that approver's action table.
4. Show: `"Row {N} — {field}: '{current}' → '{new}'"`
5. Ask: `"Apply? (y/n)"`
6. On confirm: update the cell, update `lastModified`, write back.
7. Recompute action summary counts in the Executive Summary table and update them.

---

## Mode: `status`

Invoked as: `/ea-actions status`

1. Read `EA-projects/{slug}/artifacts/cross-cutting/governance/stakeholder-action-plan.md`.
2. If not found: "No Stakeholder Action Plan found. Run `/ea-actions generate` to create one."
3. Parse all action table rows across all per-approver sections.
4. Compute counts: Total | Pending | In Review | Approved | Deferred | Overdue (Due Date < today and status ≠ Approved).
5. Output:

```
Stakeholder Action Plan — {engagement name}
══════════════════════════════════════════════
Total: {N}  |  Pending: {N}  |  In Review: {N}  |  Approved: {N}  |  Deferred: {N}
Overdue: {N}

| Approver | Role | Pending | Approved | Overdue | Next Due |
|---|---|---|---|---|---|
| {name} | {role} | {N} | {N} | {N} | {date or —} |
```

6. Flag overdue items: "⚠️ {N} overdue action(s) — update status with `/ea-actions update <approver> <row#> status <value>`."

---

## Edge Cases

| Scenario | Handling |
|---|---|
| No SAoW found | Abort with message directing to `/ea-interview start phase A` |
| SAoW §6/§7 empty | Warn; offer to generate stub or stop |
| Approver in §6 not in §7 | Include with flagged role; warn |
| Target State Declaration absent | Continue without it; warn |
| Artifact already exists on `generate` | Ask: regenerate or view |
| Ambiguous approver name in `update` | List matches; ask user to be specific |
| `status` value not in allowed set | List valid values and stop |
```

- [ ] **Step 2: Verify the file was created**

```bash
ls -la /mnt/d/dev/claude-sandbox/plugins/ea-assistant/commands/ea-actions.md
```

Expected: file exists, non-zero size.

- [ ] **Step 3: Run frontmatter validator**

```bash
cd /mnt/d/dev/claude-sandbox/plugins && ~/.bun/bin/bun .github/scripts/validate-frontmatter.ts ea-assistant/
```

Expected: passes with no new errors.

- [ ] **Step 4: Commit**

```bash
cd /mnt/d/dev/claude-sandbox/plugins
git add ea-assistant/commands/ea-actions.md
git commit -m "feat(ea-assistant): add /ea-actions command"
```

---

## Task 5: Register new artifacts in `ea-artifact-templates/SKILL.md`

**Files:**
- Modify: `ea-assistant/skills/ea-artifact-templates/SKILL.md`

The Artifact Catalogue table in this skill (around line 191) lists all templates. Add two rows.

- [ ] **Step 1: Read the current table**

Open `ea-assistant/skills/ea-artifact-templates/SKILL.md` and locate the Artifact Catalogue table. Find the row:

```
| `statement-of-architecture-work.md` | Statement of Architecture Work | A |
```

- [ ] **Step 2: Insert two new rows after the SAoW row**

Add these two rows immediately after the `statement-of-architecture-work.md` row:

```
| `target-state-declaration.md` | Target State Declaration | A |
```

And find the row:

```
| `adr-register.md` | ADR Register | cross-cutting/governance/ (generated by /ea-adrs) |
```

Add this row immediately before the `adr-register.md` row:

```
| `stakeholder-action-plan.md` | Stakeholder Action Plan | cross-cutting/governance/ (generated by /ea-actions) |
```

- [ ] **Step 3: Verify the table is correct**

Run:

```bash
grep -n "target-state-declaration\|stakeholder-action-plan" /mnt/d/dev/claude-sandbox/plugins/ea-assistant/skills/ea-artifact-templates/SKILL.md
```

Expected: two lines found, each containing the correct template filename.

- [ ] **Step 4: Commit**

```bash
cd /mnt/d/dev/claude-sandbox/plugins
git add ea-assistant/skills/ea-artifact-templates/SKILL.md
git commit -m "feat(ea-assistant): register Target State Declaration and Stakeholder Action Plan in artifact catalogue"
```

---

## Task 6: Update `/ea-help` command table

**Files:**
- Modify: `ea-assistant/commands/ea-help.md`

- [ ] **Step 1: Locate the insertion point**

Open `ea-assistant/commands/ea-help.md`. Find this line in the All Commands table:

```
| `/ea-goals [mode]` | Goals Register — list, add, update, trace G→OBJ→STR→WP chain, or generate register; Domain + Type classification |
```

- [ ] **Step 2: Insert two new rows after the `/ea-goals` row**

Add the following two rows immediately after the `/ea-goals` row:

```
| `/ea-target [new\|view\|update]` | Target State Declaration — capture per-domain target states, success criteria, and traceability to goals and objectives |
| `/ea-actions [generate\|view\|update\|status]` | Stakeholder Action Plan — consolidated per-approver action view seeded from SAoW and Target State Declaration; suitable for governance forums and ARB |
```

- [ ] **Step 3: Verify**

```bash
grep -n "ea-target\|ea-actions" /mnt/d/dev/claude-sandbox/plugins/ea-assistant/commands/ea-help.md
```

Expected: two lines found.

- [ ] **Step 4: Commit**

```bash
cd /mnt/d/dev/claude-sandbox/plugins
git add ea-assistant/commands/ea-help.md
git commit -m "docs(ea-assistant): add /ea-target and /ea-actions to help command table"
```

---

## Task 7: Update `CLAUDE.md` command reference

**Files:**
- Modify: `ea-assistant/CLAUDE.md`

- [ ] **Step 1: Locate the insertion point**

Open `ea-assistant/CLAUDE.md`. Find the line in the Command Reference section:

```
Key entry points: `/ea-new` · `/ea-open` · `/ea-interview` · `/ea-grill` · `/ea-generate` · `/ea-status` · `/ea-brief` · `/ea-lens` · `/ea-git` · `/ea-goals` · `/ea-issues` · `/ea-problems` · `/ea-scenarios`
```

- [ ] **Step 2: Add the two new commands to the key entry points line**

Replace that line with:

```
Key entry points: `/ea-new` · `/ea-open` · `/ea-interview` · `/ea-grill` · `/ea-generate` · `/ea-status` · `/ea-brief` · `/ea-lens` · `/ea-git` · `/ea-goals` · `/ea-target` · `/ea-actions` · `/ea-issues` · `/ea-problems` · `/ea-scenarios`
```

- [ ] **Step 3: Also update the command count line**

Find this line in `ea-assistant/CLAUDE.md`:

```
47 commands available — run `/ea-help` for the full table with agent assignments.
```

Replace with:

```
49 commands available — run `/ea-help` for the full table with agent assignments.
```

- [ ] **Step 4: Verify**

```bash
grep -n "ea-target\|ea-actions\|49 commands" /mnt/d/dev/claude-sandbox/plugins/ea-assistant/CLAUDE.md
```

Expected: three lines found — one for the key entry points, one for ea-actions in the key entry points, and one for the count.

- [ ] **Step 5: Commit**

```bash
cd /mnt/d/dev/claude-sandbox/plugins
git add ea-assistant/CLAUDE.md
git commit -m "docs(ea-assistant): add /ea-target and /ea-actions to CLAUDE.md; update command count to 49"
```

---

## Task 8: Final validation and feature branch PR

- [ ] **Step 1: Run full frontmatter validation**

```bash
cd /mnt/d/dev/claude-sandbox/plugins && ~/.bun/bin/bun .github/scripts/validate-frontmatter.ts ea-assistant/
```

Expected: no new errors introduced by this work.

- [ ] **Step 2: Verify all 7 files were changed**

```bash
cd /mnt/d/dev/claude-sandbox/plugins && git log --oneline -8
```

Expected: see 7 commits from this work (Tasks 1–7).

- [ ] **Step 3: Verify command count in ea-help**

```bash
grep -c "^| \`/ea-" /mnt/d/dev/claude-sandbox/plugins/ea-assistant/commands/ea-help.md
```

Expected: previous count + 2 (was 47 commands, now 49).

- [ ] **Step 4: Check for CRLF issues on WSL2**

```bash
file /mnt/d/dev/claude-sandbox/plugins/ea-assistant/commands/ea-target.md /mnt/d/dev/claude-sandbox/plugins/ea-assistant/commands/ea-actions.md /mnt/d/dev/claude-sandbox/plugins/ea-assistant/templates/target-state-declaration.md /mnt/d/dev/claude-sandbox/plugins/ea-assistant/templates/stakeholder-action-plan.md
```

Expected: all four show `ASCII text` or `UTF-8 Unicode text`, NOT `CRLF line terminators`. If CRLF detected: run `dos2unix <file>` on each affected file and amend the relevant commit.
```
