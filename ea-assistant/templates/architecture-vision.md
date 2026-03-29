---
artifact: Architecture Vision
engagement: {{engagement_name}}
phase: A
status: Draft
reviewStatus: Not Reviewed
version: 0.1
templateVersion: 0.9.5
lastModified: {{YYYY-MM-DD}}
taxonomy:
  domain: Cross-cutting
  category: Strategy
  audience: Executive
  layer: Motivation
  sensitivity: Internal
  tags: [vision, drivers, goals, strategy, phase-a]
---

<details>
<summary>📋 Guidance</summary>

The Architecture Vision is the primary output of Phase A. It defines the business drivers, goals,
objectives, issues, problems, scope, stakeholders, constraints, and high-level target architecture
for the engagement. It should be approved by the sponsor before proceeding to Phases B-D.
Collapsible guidance blocks (📋 Guidance) are for the author only and collapse when exported.

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

| ID | Driver | Type | Force | Impact on Strategy |
|---|---|---|---|---|
| DRV-001 | {{driver_1}} | Internal / External | Opportunity / Threat / Mandate | {{impact_1}} |
| DRV-002 | {{driver_2}} | Internal / External | Opportunity / Threat / Mandate | {{impact_2}} |

---

## 3. Goals

<details>
<summary>📋 Guidance</summary>

Goals are broad, qualitative outcomes the strategy is intended to achieve. They answer "where do
we want to be?" Each goal should trace to one or more business drivers — the forces that made
this goal necessary. Goals are the primary anchor for Issues (the barriers that threaten them).

</details>

| ID | Goal | Business Driver(s) |
|---|---|---|
| G-001 | {{goal_1}} | DRV-00N |
| G-002 | {{goal_2}} | DRV-00N |

---

## 4. Objectives

<details>
<summary>📋 Guidance</summary>

Objectives are specific, measurable, time-bound results that operationalise the goals. They
answer "how far, and by when?" Each objective must have a unit of measure, a target value, and
a deadline. Objectives are the primary anchor for Problems (the specific symptoms that block them).

</details>

| ID | Objective | Measure | Target | Deadline | Linked Goal |
|---|---|---|---|---|---|
| OBJ-001 | {{objective_1}} | {{measure_1}} | {{target_1}} | {{deadline_1}} | G-00N |
| OBJ-002 | {{objective_2}} | {{measure_2}} | {{target_2}} | {{deadline_2}} | G-00N |

---

## 5. Issues

<details>
<summary>📋 Guidance</summary>

Issues are broader, systemic concerns that threaten the organisation's ability to achieve its
goals. An issue is not a single broken thing — it is a pattern of dysfunction, a capability gap,
or an unresolved conflict that has no single fix. Issues are linked to the goal(s) they threaten.
They are parallel to Problems, not parents of them.

</details>

| ID | Issue | Area | Threatens Goal(s) |
|---|---|---|---|
| ISS-001 | {{issue_1}} | {{area_1}} | G-00N |
| ISS-002 | {{issue_2}} | {{area_2}} | G-00N |

---

## 6. Problems

<details>
<summary>📋 Guidance</summary>

Problems are specific, observable, and fixable — concrete symptoms that are actively blocking
an objective. A problem has a clear cause-and-effect relationship and can be measured and
resolved directly. Problems are linked to the objective(s) they block. They are parallel to
Issues, not derived from them.

</details>

| ID | Problem | Observable Symptom | Blocks Objective(s) |
|---|---|---|---|
| PRB-001 | {{problem_1}} | {{symptom_1}} | OBJ-00N |
| PRB-002 | {{problem_2}} | {{symptom_2}} | OBJ-00N |

---

## 7. Strategic Direction Summary

<details>
<summary>📋 Guidance</summary>

This section rolls up the strategic direction elements captured during the engagement. Strategies are
the chosen approaches for achieving goals — they are recorded in `engagement.json → direction.strategies[]`
and summarised here. Metrics are the measures used to track progress against objectives — they are
recorded in `engagement.json → metrics[]`. This section provides a single-page view for executive
stakeholders who need the full motivation chain without reading individual sections.

</details>

### Strategies

| ID | Strategy | Supports Goal(s) |
|---|---|---|
| STR-001 | {{strategy_1}} | G-00N |

### Key Metrics

| ID | Metric | Type | Linked Objective | Baseline | Target |
|---|---|---|---|---|---|
| MET-001 | {{metric_1}} | Performance / Outcome / Activity | OBJ-00N | {{baseline_1}} | {{target_1}} |

> *Full direction data is maintained in `engagement.json → direction` and `metrics[]`.*

---

## 8. Scope

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

## 9. Stakeholders

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

## 10. Architecture Principles

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

## 11. Constraints

<details>
<summary>📋 Guidance</summary>

List constraints that must be respected — regulatory, technical, financial, or political.
Distinguish between hard constraints (non-negotiable) and soft constraints (preferences).

</details>

| Constraint | Type | Impact |
|---|---|---|
| {{constraint_1}} | Hard / Soft | {{impact_1}} |

---

## 12. Assumptions

<details>
<summary>📋 Guidance</summary>

List the assumptions being made. These should be validated and updated throughout the engagement.

</details>

{{assumptions}}

---

## 13. High-Level Target Architecture

<details>
<summary>📋 Guidance</summary>

A high-level description of the target state architecture. This should be visual where possible.
Reference diagrams stored in the diagrams/ folder. Avoid detailed design at this stage.

</details>

{{target_architecture_description}}

*Reference diagram:* `../diagrams/{{diagram_filename}}`

---

## 14. Key Risks

<details>
<summary>📋 Guidance</summary>

Identify the top 3-5 risks to the architecture or engagement. Include mitigation approaches.

</details>

| Risk | Likelihood | Impact | Mitigation |
|---|---|---|---|
| {{risk_1}} | High/Med/Low | High/Med/Low | {{mitigation_1}} |

---

## 15. Next Steps

<details>
<summary>📋 Guidance</summary>

List the immediate next steps following approval of this document.
Typically: approve Statement of Architecture Work, proceed to Phase B/C/D.

</details>

{{next_steps}}

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

---

*This document was created using the EA Assistant plugin.*
*Sections marked ⚠️ are unanswered. Sections marked 🤖 contain AI-suggested content requiring review.*
*Use `/ea-decisions` to generate a cross-artifact Decision Register from all A3 tables.*
*Use `/ea-concerns` to generate a cross-artifact Concerns Register from all A4 tables.*
