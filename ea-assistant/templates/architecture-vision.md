---
artifactId: architecture-vision
artifact: Architecture Vision
artifactId: architecture-vision
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
  sensitivity: Internal
  tags: [vision, drivers, goals, strategy, phase-a]
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
| Linked to Statement of Architecture Work | ⚠️ Pending | |

*This section is for author guidance only. Run `/ea-grill` to validate compliance.*

</details>

<details>
<summary>📋 Guidance</summary>

**Purpose:** The Architecture Vision is the primary output of Phase A. It establishes the business case for the engagement, agrees the scope and constraints, and defines the high-level target architecture to a level sufficient for sponsor sign-off. It gates entry to Phases B–D — no domain architecture work should begin without an approved Architecture Vision.

**What to include:** Business drivers (DRV-NNN), goals (G-NNN), objectives (OBJ-NNN), issues and problems (ISS/PRB-NNN), engagement scope, stakeholder map reference, constraints (CST-NNN), assumptions, and a high-level target state description across active architecture domains. The Architecture Vision does not contain detailed architecture — detailed analysis belongs in the domain artifacts.

**Quality indicators:**
- Every element is traceable: goals trace to drivers, objectives trace to goals, assumptions are labelled as assumptions
- The target description is at the right abstraction level — principle-and-pattern statements, not system designs
- The sponsor has explicitly reviewed and signed off before Phase B begins

**Common mistakes:**
- Including technology vendor or platform decisions in Phase A — these are premature; capture them as PAD-NNN items instead
- Conflating goals (outcomes), objectives (measurable milestones), and drivers (external forces) — each has a distinct ID prefix for a reason
- Writing the target in implementation terms ("we will use microservices") rather than architectural intent ("the target must support independent release pipelines per capability")

**TOGAF reference:** TOGAF 10 Part III, Phase A (§25) — Architecture Vision. The Phase A gate artifact; required before Phase B commences.

</details>

<details>
<summary>💡 Practitioner Tip — Phase A</summary>

- **Treat the Vision as a negotiation tool**, not a static deliverable. Build multiple candidate visions and force trade-off discussions early. (Deep tactic #7)
- **Co-create the vision with business leaders** to secure ownership — the vision built by the architecture team alone rarely survives first contact with the board. (Deep tactic #9)
- **Define success metrics before moving to Phase B** — what must be true for this vision to be considered valid? (Deep tactic #10)
- **Validate the vision with real delivery constraints** — skills, vendors, legacy — before asking for funding. (Deep tactic #8)
- Use **"strategic tension"** (current vs desired state) to drive urgency — quantify the gap in economic terms. (Deep tactic #6)
- **Two Layers check** — Goals and Objectives in this artifact should describe *business outcomes* (what the organisation wants to achieve). If a goal subject is "architecture governance," "EA capability," or "standardisation process," it belongs in the EA / TOGAF layer — reclassify as an EA Goal or move to Governance Framework. See `ea-concepts.md` → **Two Layers of Intent**.

</details>

# Architecture Vision

**Engagement:** {{engagement_name}}
**Organisation:** {{organisation}}
**Sponsor:** {{sponsor}}
**Date:** {{YYYY-MM-DD}}
**Version:** {{version}}
**Status:** {{status}}

---

## 1. Executive Summary

<details>
<summary>📋 Guidance</summary>

A brief (3-5 sentence) summary of the engagement purpose, scope, and expected outcomes.
Written for an executive audience. Avoid technical jargon.

</details>

{{executive_summary}}

---

## 2. Business Drivers

<details>
<summary>📋 Guidance</summary>

Business drivers are the internal or external forces that make this engagement necessary. They are
not problems or issues — they are the conditions creating pressure to act. A driver can be an
opportunity (a market shift to exploit) or a threat (a regulatory change to comply with). List
each driver separately so goals and strategy can be traced back to a specific force.

Type: Internal (inside the organisation) or External (market, regulatory, competitive).
Force: Opportunity / Threat / Mandate.

</details>

| ID | Driver | Type | Force | Impact on Strategy | Linked Goals | Evidence / Source | Details |
|---|---|---|---|---|---|---|---|
| [DRV-001](../details/DRV-001.md) | {{driver_1}} | Internal / External | Opportunity / Threat / Mandate | {{impact_1}} | G-00N | {{evidence_1}} | [→](../details/DRV-001.md) |
| [DRV-002](../details/DRV-002.md) | {{driver_2}} | Internal / External | Opportunity / Threat / Mandate | {{impact_2}} | G-00N | {{evidence_2}} | [→](../details/DRV-002.md) |

---

## 3. Goals

<details>
<summary>📋 Guidance</summary>

Goals are broad, qualitative outcomes the strategy is intended to achieve. They answer "where do
we want to be?" Each goal should trace to one or more business drivers — the forces that made
this goal necessary. Goals are the primary anchor for Issues (the barriers that threaten them).

**⚠️ Two Layers check:** A goal about "Establish AI governance" or "Define architecture standards" is an **EA Goal** (EA layer), not a Business Goal. Apply the quick test: *Would this still exist if the EA team were disbanded?* If no → it belongs in the Governance Framework or Architecture Principles. See `ea-concepts.md` → **Two Layers of Intent**.

</details>

| ID | Goal | Business Driver(s) | Linked Strategies | Rationale | Details |
|---|---|---|---|---|---|
| [G-001](../details/G-001.md) | {{goal_1}} | DRV-00N | STR-00N | {{goal_rationale_1}} | [→](../details/G-001.md) |
| [G-002](../details/G-002.md) | {{goal_2}} | DRV-00N | STR-00N | {{goal_rationale_2}} | [→](../details/G-002.md) |

---

## 4. Objectives

<details>
<summary>📋 Guidance</summary>

Objectives are specific, measurable, time-bound results that operationalise the goals. They
answer "how far, and by when?" Each objective must have a unit of measure, a target value, and
a deadline. Objectives are the primary anchor for Problems (the specific symptoms that block them).

</details>

| ID | Objective | Measure | Target | Deadline | Linked Goal | Details |
|---|---|---|---|---|---|---|
| [OBJ-001](../details/OBJ-001.md) | {{objective_1}} | {{measure_1}} | {{target_1}} | {{deadline_1}} | G-00N | [→](../details/OBJ-001.md) |
| [OBJ-002](../details/OBJ-002.md) | {{objective_2}} | {{measure_2}} | {{target_2}} | {{deadline_2}} | G-00N | [→](../details/OBJ-002.md) |

---

## 5. Issues

<details>
<summary>📋 Guidance</summary>

Issues are broader, systemic concerns that threaten the organisation's ability to achieve its
goals. An issue is not a single broken thing — it is a pattern of dysfunction, a capability gap,
or an unresolved conflict that has no single fix. Issues are linked to the goal(s) they threaten.
They are parallel to Problems, not parents of them.

</details>

| ID | Issue | Area | Threatens Goal(s) | Evidence | Raised By | Details |
|---|---|---|---|---|---|---|
| [ISS-001](../details/ISS-001.md) | {{issue_1}} | {{area_1}} | G-00N | {{issue_evidence_1}} | {{issue_raised_by_1}} | [→](../details/ISS-001.md) |
| [ISS-002](../details/ISS-002.md) | {{issue_2}} | {{area_2}} | G-00N | {{issue_evidence_2}} | {{issue_raised_by_2}} | [→](../details/ISS-002.md) |

---

## 6. Problems

<details>
<summary>📋 Guidance</summary>

Problems are specific, observable, and fixable — concrete symptoms that are actively blocking
an objective. A problem has a clear cause-and-effect relationship and can be measured and
resolved directly. Problems are linked to the objective(s) they block. They are parallel to
Issues, not derived from them.

</details>

| ID | Problem | Observable Symptom | Blocks Objective(s) | Evidence | Raised By | Details |
|---|---|---|---|---|---|---|
| [PRB-001](../details/PRB-001.md) | {{problem_1}} | {{symptom_1}} | OBJ-00N | {{problem_evidence_1}} | {{problem_raised_by_1}} | [→](../details/PRB-001.md) |
| [PRB-002](../details/PRB-002.md) | {{problem_2}} | {{symptom_2}} | OBJ-00N | {{problem_evidence_2}} | {{problem_raised_by_2}} | [→](../details/PRB-002.md) |

---

## 7. Opportunities

<details>
<summary>📋 Guidance</summary>

An Opportunity is a specific, actionable possibility to exploit a favourable condition or close a capability gap in a value-generating way — something the organisation could do that it currently cannot. Opportunities are distinct from Goals (which state desired outcomes) and Drivers (which describe why the engagement is needed). Each OPP-NNN should advance at least one Goal and, in Phase E, be elaborated into one or more Work Packages (WP-NNN).

Types: **Exploit** (capitalise on existing advantage) / **Enhance** (amplify current capability) / **Emerge** (pursue something not previously in scope).

</details>

| ID | Opportunity | Driver(s) | Type | Priority | Linked Goal(s) | Rationale | Details |
|---|---|---|---|---|---|---|---|
| [OPP-001](../details/OPP-001.md) | {{opportunity_1}} | DRV-00N | Exploit / Enhance / Emerge | High / Med / Low | G-00N | {{opp_rationale_1}} | [→](../details/OPP-001.md) |

---

## 8. Strategic Direction Summary

<details>
<summary>📋 Guidance</summary>

This section rolls up the strategic direction elements captured during the engagement. Strategies are
the chosen approaches for achieving goals — they are recorded in `engagement.json → direction.strategies[]`
and summarised here. Metrics are the measures used to track progress against objectives — they are
recorded in `engagement.json → metrics[]`. This section provides a single-page view for executive
stakeholders who need the full motivation chain without reading individual sections.

</details>

### Strategies

| ID | Strategy | Supports Goal(s) | Details |
|---|---|---|---|
| [STR-001](../details/STR-001.md) | {{strategy_1}} | G-00N | [→](../details/STR-001.md) |

### Key Metrics

| ID | Metric | Type | Linked Objective | Baseline | Target | Baseline Source |
|---|---|---|---|---|---|---|
| [MET-001](../details/MET-001.md) | {{metric_1}} | Performance / Outcome / Activity | OBJ-00N | {{baseline_1}} | {{target_1}} | {{baseline_source_1}} |

> *Full direction data is maintained in `engagement.json → direction` and `metrics[]`.*

---

## 9. Scope

<details>
<summary>📋 Guidance</summary>

Define what is IN and OUT of scope for this engagement.
Be specific about organisational units, systems, geographies, and time horizons.

</details>

### In Scope
{{scope_in}}

### Out of Scope
{{scope_out}}

### Time Horizon
{{time_horizon}}

---

## 10. Stakeholders

<details>
<summary>📋 Guidance</summary>

List all key stakeholders, their roles, concerns, and level of engagement.
This feeds directly into the Stakeholder Map artifact.

</details>

| Stakeholder | Role | Concerns | Engagement Level |
|---|---|---|---|
| {{stakeholder_1}} | {{role_1}} | {{concerns_1}} | Informed / Consulted / Responsible |
| {{stakeholder_2}} | {{role_2}} | {{concerns_2}} | Informed / Consulted / Responsible |

---

## 11. Architecture Principles

<details>
<summary>📋 Guidance</summary>

List the governing principles that will guide architecture decisions.
These should be agreed with the sponsor and documented in the Architecture Principles artifact.
Reference the Architecture Principles artifact here rather than duplicating.

</details>

Key principles governing this engagement are defined in the **Architecture Principles** artifact.

Summary:
{{architecture_principles_summary}}

---

## 12. Constraints

<details>
<summary>📋 Guidance</summary>

List constraints that must be respected — regulatory, technical, financial, or political.
Distinguish between hard constraints (non-negotiable) and soft constraints (preferences).

</details>

| Constraint | Type | Impact |
|---|---|---|
| {{constraint_1}} | Hard / Soft | {{impact_1}} |

---

## 13. Assumptions

<details>
<summary>📋 Guidance</summary>

List the assumptions being made. These should be validated and updated throughout the engagement.

</details>

{{assumptions}}

---

## 14. High-Level Target Architecture

<details>
<summary>📋 Guidance</summary>

A high-level description of the target state architecture. This should be visual where possible.
Reference diagrams stored in the diagrams/ folder. Avoid detailed design at this stage.

</details>

{{target_architecture_description}}

*Reference diagram:* `../diagrams/{{diagram_filename}}`

---

## 15. Key Risks

<details>
<summary>📋 Guidance</summary>

Identify the top 3-5 risks to the architecture or engagement. Include mitigation approaches.

</details>

| Risk | Likelihood | Impact | Mitigation |
|---|---|---|---|
| {{risk_1}} | High/Med/Low | High/Med/Low | {{mitigation_1}} |

---

## 16. Next Steps

<details>
<summary>📋 Guidance</summary>

List the immediate next steps following approval of this document.
Typically: approve Statement of Architecture Work, proceed to Phase B/C/D.

</details>

{{next_steps}}

---

## 17. Diagrams

<details>
<summary>📋 Guidance</summary>

Standard diagrams for the Architecture Vision. Diagrams are stored in `diagrams/` relative to the engagement root and embedded in exported documents via `/ea-generate`. Use `/ea-diagram` to create or edit. See `skills/ea-artifact-templates/references/diagram-catalogue.md` for Mermaid starters.

</details>

| Diagram | File | Status |
|---|---|---|
| Motivation Map | `../../diagrams/architecture-vision-motivation-map.mmd` | ❌ Missing |
| Stakeholder Power/Interest Grid | `../../diagrams/architecture-vision-stakeholder-grid.mmd` | ❌ Missing |

*Use `/ea-diagram` to create. Run `/ea-generate png` to render for export.*

---

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
|---|---|---|---|---|---|---|---|---|---|---|---|
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


## Appendix A5 — Related Architecture Decisions

<details>
<summary>📋 Guidance</summary>

List ADRs that informed, were informed by, or are otherwise relevant to this artifact.
Reference the ADR-NNN ID so readers can navigate to the full decision record.
Use `/ea-adrs` to manage the ADR Register and surface ADR summaries.

When a significant decision is made during an interview for this artifact, the
`ea-interviewer` will suggest creating an ADR if the decision meets the threshold
criteria (technology/vendor selection, high cost/risk, hard to reverse, etc.).

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

- [ ] *(Add tasks — e.g. "Populate §3 Assumptions before Phase B sign-off")*

*This document was created using the EA Assistant plugin.*
*Sections marked ⚠️ are unanswered. Sections marked 🤖 contain AI-suggested content requiring review.*
*Use `/ea-decisions` to generate a cross-artifact Decision Register from all A3 tables.*
*Use `/ea-concerns` to generate a cross-artifact Concerns Register from all A4 tables.*
