---
artifact: Architecture Vision
artifactId: architecture-vision
engagement: {{engagement_name}}
phase: A
status: Draft
reviewStatus: Not Reviewed
version: 0.1
templateVersion: 0.9.82
lastModified: {{YYYY-MM-DD}}
taxonomy:
  admPhases: [A]
  zachmanCell: "Scope/Why"
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

## 2. Scope

<details>
<summary>📋 Guidance</summary>

Define what is IN and OUT of scope for this engagement.
Be specific about organisational units, systems, geographies, and time horizons. Reference the statement of architecture work

</details>

**Statement of Architecture Work:** [[statement-of-architecture-work]]

### In Scope
{{scope_in}}

### Out of Scope
{{scope_out}}

### Time Horizon
{{time_horizon}}

---

## 3. Stakeholders

<details>
<summary>📋 Guidance</summary>

The Stakeholder Map artifact is the authoritative record of all stakeholders, their power/interest profile, RACI, and communication preferences. This section provides a brief contextual note only — do not maintain a parallel stakeholder list here.

</details>

**Sponsor:** {{sponsor}}

Stakeholder details are maintained in the **Stakeholder Map** — see [[stakeholder-map]] · manage with `/ea-interview` (Stakeholder Map artifact).

---

## 4. Business Drivers

<details>
<summary>📋 Guidance</summary>

Business drivers are the internal or external forces that make this engagement necessary. They are
not problems or issues — they are the conditions creating pressure to act. A driver can be an
opportunity (a market shift to exploit) or a threat (a regulatory change to comply with). List
each driver separately so goals and strategy can be traced back to a specific force.

Type: Internal (inside the organisation) or External (market, regulatory, competitive).
Force: Opportunity / Threat / Mandate.

</details>

Business drivers are maintained in the **Drivers Register** — full detail (type, force, evidence, goal linkage) lives there. This section carries the executive summary only.

Summary:
{{drivers_summary}}

**Full register:** [[drivers-register]] · manage with `/ea-drivers`

---

## 5. Goals

<details>
<summary>📋 Guidance</summary>

Goals are broad, qualitative outcomes the strategy is intended to achieve. They answer "where do
we want to be?" Each goal should trace to one or more business drivers — the forces that made
this goal necessary. Goals are the primary anchor for Issues (the barriers that threaten them).

**⚠️ Two Layers check:** A goal about "Establish AI governance" or "Define architecture standards" is an **EA Goal** (EA layer), not a Business Goal. Apply the quick test: *Would this still exist if the EA team were disbanded?* If no → it belongs in the Governance Framework or Architecture Principles. See `ea-concepts.md` → **Two Layers of Intent**.

</details>

Goals are maintained in the **Goals Register** — driver/strategy linkage and rationale live there. This section carries the executive summary only.

Summary:
{{goals_summary}}

**Full register:** [[goals-register]] · manage with `/ea-goals`

---

## 6. Business Scenarios

<details>
<summary>📋 Guidance</summary>

Business Scenarios are a Phase A discovery technique (TOGAF 10 §25.3.3) that translate business problems, actors, and desired outcomes into structured narratives. Each scenario validates that the Architecture Vision addresses a real business need. Use `/ea-scenarios` to create and manage BS-NNN items; they are referenced here.

Not every engagement requires multiple formal scenarios — a single scenario may suffice.

</details>

| ID | Scenario | Problem / Opportunity | Actor(s) | Desired Outcome | Environment Required |
|---|---|---|---|---|---|
| *(none — use `/ea-scenarios` to add)* | — | — | — | — | — |

---

## 7. Issues

<details>
<summary>📋 Guidance</summary>

Issues are broader, systemic concerns that threaten the organisation's ability to achieve its
goals. An issue is not a single broken thing — it is a pattern of dysfunction, a capability gap,
or an unresolved conflict that has no single fix. Issues are linked to the goal(s) they threaten.
They are parallel to Problems, not parents of them.

</details>

Issues are maintained in the **Issues Register** — severity, threatened goals, and evidence live there. This section carries the executive summary only.

Summary:
{{issues_summary}}

**Full register:** [[issues-register]] · manage with `/ea-issues`

---

## 8. Problems

<details>
<summary>📋 Guidance</summary>

Problems are specific, observable, and fixable — concrete symptoms that are actively blocking
an objective. A problem has a clear cause-and-effect relationship and can be measured and
resolved directly. Problems are linked to the objective(s) they block. They are parallel to
Issues, not derived from them.

</details>

Problems are maintained in the **Problems Register** — observable symptom, blocked objectives, and evidence live there. This section carries the executive summary only.

Summary:
{{problems_summary}}

**Full register:** [[problems-register]] · manage with `/ea-problems`

---

## 9. Opportunities

<details>
<summary>📋 Guidance</summary>

An Opportunity is a specific, actionable possibility to exploit a favourable condition or close a capability gap in a value-generating way — something the organisation could do that it currently cannot. Opportunities are distinct from Goals (which state desired outcomes) and Drivers (which describe why the engagement is needed). Each OPP-NNN should advance at least one Goal and, in Phase E, be elaborated into one or more Work Packages (WP-NNN).

Types: **Exploit** (capitalise on existing advantage) / **Enhance** (amplify current capability) / **Emerge** (pursue something not previously in scope).

</details>

<!-- follow-up: Opportunities register (/ea-opportunities) is planned; until then OPP-NNN items are maintained in this inline table -->

Opportunities are summarised here in the Vision (there is no dedicated register yet). Each OPP-NNN should advance at least one Goal and, in Phase E, be elaborated into Work Packages (WP-NNN).

| ID | Opportunity | Driver(s) | Type | Priority | Linked Goal(s) | Rationale | Details |
|---|---|---|---|---|---|---|---|
| [[OPP-001]] | {{opportunity_1}} | DRV-00N | Exploit / Enhance / Emerge | High / Med / Low | G-00N | {{opp_rationale_1}} | [[OPP-001\|→]] |

---

## 10. Objectives

<details>
<summary>📋 Guidance</summary>

Objectives are specific, measurable, time-bound results that operationalise the goals. They
answer "how far, and by when?" Each objective must have a unit of measure, a target value, and
a deadline. Objectives are the primary anchor for Problems (the specific symptoms that block them).

</details>

Objectives are maintained in the **Objectives Register** — measure, target, deadline, and goal linkage live there. This section carries the executive summary only.

Summary:
{{objectives_summary}}

**Full register:** [[objectives-register]] · manage with `/ea-objectives`

---

## 11. Strategic Direction Summary

<details>
<summary>📋 Guidance</summary>

This section rolls up the strategic direction elements captured during the engagement. Strategies are
the chosen approaches for achieving goals — they are recorded in `engagement.json → direction.strategies[]`
and summarised here. Metrics are the measures used to track progress against objectives — they are
recorded in `engagement.json → metrics[]`. This section provides a single-page view for executive
stakeholders who need the full motivation chain without reading individual sections.

</details>

### Strategies

Strategies are maintained in the **Strategy Register** — type, horizon, supported goals/objectives, and rationale live there. This section carries the executive summary only.

Summary:
{{strategies_summary}}

**Full register:** [[strategy-register]] · manage with `/ea-strategies`

### Key Metrics

<!-- follow-up: no dedicated Metrics register/command yet — keep this lean Vision summary, sourced from engagement.json → metrics[] -->

| ID | Metric | Type | Linked Objective | Baseline | Target | Baseline Source |
|---|---|---|---|---|---|---|
| [[MET-001]] | {{metric_1}} | Performance / Outcome / Activity | OBJ-00N | {{baseline_1}} | {{target_1}} | {{baseline_source_1}} |

> *Full direction data is maintained in `engagement.json → direction` and `metrics[]`.*

---

## 12. Architecture Principles

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

## 13. Constraints

<details>
<summary>📋 Guidance</summary>

Constraints are non-negotiable restrictions that bound this engagement — regulatory, technical, financial, or organisational. Each CST-NNN has a source (the policy, regulation, or mandate that created it) and an owner. The Constraints Register is the authoritative record; this section carries the executive summary only.

Distinguish hard constraints (non-negotiable) from soft constraints (preferences that can be overridden with justification).

</details>

Constraints are maintained in the **Constraints Register** — type, source, owner, scope, and linked artifacts live there. This section carries the executive summary only.

Summary:
{{constraints_summary}}

**Full register:** [[constraints-register]] · manage with `/ea-constraints`

---

## 14. Assumptions

<details>
<summary>📋 Guidance</summary>

List the assumptions being made. These should be validated and updated throughout the engagement.

</details>

{{assumptions}}

---

## 15. High-Level Target Architecture

<details>
<summary>📋 Guidance</summary>

A high-level description of the target state, organised by architecture domain. Populate only the domains in scope; mark others ➖ Not applicable. Descriptions at Phase A are directional — principle-and-pattern statements, not system designs. Specific technology or vendor choices are premature here; capture them as PAD-NNN items instead.

</details>

### Architecture Vision Statement

{{architecture_vision_statement}}

### Business Domain

{{target_business_domain}}

### Data / Information Domain

{{target_data_domain}}

### Application Domain

{{target_application_domain}}

### Technology Domain

{{target_technology_domain}}

*Reference diagram:* `../../diagrams/{{diagram_filename}}`

---

## 16. Key Risks

<details>
<summary>📋 Guidance</summary>

Key risks are uncertain future events that could derail the engagement or undermine the target architecture. Each RIS-NNN has a likelihood, impact, mitigation approach, and owner. The Risk Register is the authoritative record; this section carries the top risks summary only.

</details>

Key risks are maintained in the **Risk Register** — likelihood, impact, mitigation, ownership, and status live there. This section carries the top risks summary only.

Summary:
{{key_risks_summary}}

**Full register:** [[risk-register]] · manage with `/ea-risks`

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

- [ ] *(Add tasks — e.g. "Populate §14 Assumptions before Phase B sign-off", "Get sponsor sign-off before proceeding to Phase B")*

*This document was created using the EA Assistant plugin.*
*Sections marked ⚠️ are unanswered. Sections marked 🤖 contain AI-suggested content requiring review.*
*Use `/ea-decisions` to generate a cross-artifact Decision Register from all A3 tables.*
*Use `/ea-concerns` to generate a cross-artifact Concerns Register from all A4 tables.*
