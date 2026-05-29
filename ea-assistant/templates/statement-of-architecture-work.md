---
artifactId: statement-of-architecture-work
artifact: Statement of Architecture Work
engagement: {{engagement_name}}
phase: A
status: Draft
reviewStatus: Not Reviewed
version: 0.1
templateVersion: 0.9.55
lastModified: {{YYYY-MM-DD}}
taxonomy:
  domain: Cross-cutting
  category: Planning
  audience: Governance
  layer: Governance
  sensitivity: Confidential
  tags: [scope, commitment, deliverables, phase-a]
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

*This section is for author guidance only. Run `/ea-grill` to validate compliance.*

</details>

<details>
<summary>📋 Guidance</summary>

**Purpose:** The Statement of Architecture Work (SoAW) is the formal agreement that authorises the engagement — defining scope, approach, deliverables, schedule, and acceptance criteria. It is the engagement's mandate document. No substantive Phase B–D architecture work should begin before the SoAW is approved by the sponsor.

**What to include:** Architecture scope (in-scope and out-of-scope), engagement objectives, deliverables list (with acceptance criteria for each), schedule, resource requirements, governance arrangements (who reviews, who approves), assumptions, and constraints. The SoAW must be consistent with and traceable to the Architecture Vision.

**Quality indicators:**
- Acceptance criteria are defined per deliverable — "the Architecture Vision is accepted when..." not just "the Architecture Vision is delivered"
- Scope exclusions are explicit — unambiguous out-of-scope items prevent scope creep arguments later
- The schedule is realistic and includes governance review gates, not just delivery milestones

**Common mistakes:**
- SoAW that lists deliverables without acceptance criteria — without them, "done" is undefined and sign-off becomes subjective
- Scope described only in terms of architecture domains without reference to the specific business units, systems, or geography in scope
- Not revisiting the SoAW if the Architecture Vision changes — the SoAW must remain consistent with the Vision throughout Phase A

**TOGAF reference:** TOGAF 10 Part III, Phase A (§25.4) — Statement of Architecture Work. The formal authorisation document for the engagement; analogous to a project charter in project management terms.

</details>

<details>
<summary>💡 Practitioner Tip — SoAW</summary>

- The SoAW is a **commitment device** — it should be uncomfortable enough that stakeholders think carefully before signing. (Tip #11)
- **Timebox the architecture work** and define exit criteria — when is the architecture "good enough" to proceed? (Tip #12)
- The SoAW must trace to the Architecture Vision — if the vision changes, the SoAW must be revisited. (Tip #5)
- Define **clear decision rights and escalation paths** in the SoAW to prevent governance bottlenecks later. (Deep tactic #2)
- Treat the Architecture Board as a **decision marketplace**, not a review committee — the SoAW should reflect this operating model. (Deep tactic #1)

</details>

# Statement of Architecture Work

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

Summary of the agreed scope of architecture work, key deliverables, and timeline for this engagement phase.
Diagram: Engagement scope boundary or phase timeline diagram
Run `/ea-summary refresh` to regenerate this section from current artifact content.

</details>

{{executive_summary}}

---

## 1. Purpose

<details>
<summary>📋 Guidance</summary>

State why this architecture engagement is being undertaken. Describe the business trigger or
decision that has initiated this work. Reference the Architecture Vision if it already exists.
This should be 2-4 sentences: clear, non-technical, and focused on business value.

</details>

{{purpose}}

---

## 2. Scope

<details>
<summary>📋 Guidance</summary>

Define the architectural scope precisely. Specify which business domains, systems, organisational
units, geographies, and TOGAF phases are in scope. Clearly list what is out of scope to prevent
scope creep. Reference the Architecture Vision scope section for consistency.

</details>

### In Scope
{{scope_in}}

### Out of Scope
{{scope_out}}

### Architecture Domains
{{architecture_domains}}

### TOGAF Phases to be Executed
{{phases_in_scope}}

---

## 3. Approach

<details>
<summary>📋 Guidance</summary>

Describe the methodology and approach for conducting the engagement. Include: how stakeholder
engagement will be managed, what discovery techniques will be used (workshops, interviews, document
review), what modelling notation will be applied (ArchiMate, BPMN, etc.), and how decisions
will be documented and governed.

</details>

{{approach}}

### Key Activities
| Activity | Description | Method |
|---|---|---|
| {{activity_1}} | {{description_1}} | Workshop / Interview / Review |
| {{activity_2}} | {{description_2}} | Workshop / Interview / Review |

---

## 4. Schedule

<details>
<summary>📋 Guidance</summary>

Provide a high-level schedule with milestones. Include phase start/end dates, key review gates,
and the expected date of each deliverable. Align with any broader programme or project timeline.

</details>

| Milestone | Description | Target Date | Owner |
|---|---|---|---|
| Kick-off | {{kickoff_description}} | {{kickoff_date}} | {{owner}} |
| Phase A complete | Architecture Vision approved | {{phase_a_date}} | {{owner}} |
| {{milestone_1}} | {{description_1}} | {{date_1}} | {{owner_1}} |
| Final review | All deliverables reviewed and accepted | {{final_date}} | {{owner}} |

---

## 5. Roles and Responsibilities

<details>
<summary>📋 Guidance</summary>

List all roles involved in the engagement. Clarify who is Responsible, Accountable, Consulted,
and Informed (RACI) for key decisions and deliverables. Include both the architecture team and
client-side stakeholders who have obligations.

Role titles should align to the canonical catalogue (ROLE-NNN IDs) in
`skills/ea-engagement-lifecycle/references/role-catalogue.md`. Use `/ea-roles --generate`
to create a full Role Catalogue artifact for this engagement.

</details>

| Role | Name | Organisation | RACI for Deliverables | RACI for Decisions |
|---|---|---|---|---|
| Sponsor | {{sponsor}} | {{organisation}} | Accountable | Accountable |
| Architecture Lead | {{architecture_lead}} | {{architecture_org}} | Responsible | Responsible |
| {{role_1}} | {{name_1}} | {{org_1}} | {{raci_deliverables_1}} | {{raci_decisions_1}} |
| {{role_2}} | {{name_2}} | {{org_2}} | {{raci_deliverables_2}} | {{raci_decisions_2}} |

---

## 6. Acceptance Criteria

<details>
<summary>📋 Guidance</summary>

Define the measurable criteria that must be satisfied for each deliverable to be accepted.
Acceptance criteria should be objective and verifiable — avoid vague terms like "high quality".
Include who has authority to accept each deliverable.

</details>

| Deliverable | Acceptance Criteria | Accepted By |
|---|---|---|
| Architecture Vision | {{av_criteria}} | {{sponsor}} |
| Business Architecture | {{ba_criteria}} | {{ba_approver}} |
| {{deliverable_1}} | {{criteria_1}} | {{approver_1}} |

---

## 7. Sign-off

<details>
<summary>📋 Guidance</summary>

This section records formal approval of the Statement of Architecture Work. All named approvers
must sign before the engagement proceeds beyond Phase A. Retain a signed copy in the engagement
record.

</details>

By signing below, the named parties confirm they have read, understood, and approved this
Statement of Architecture Work.

| Role | Name | Signature | Date |
|---|---|---|---|
| Sponsor | {{sponsor}} | | |
| Architecture Lead | {{architecture_lead}} | | |
| {{approver_role_1}} | {{approver_name_1}} | | |

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
*Use `/ea-concerns` to generate a cross-artifact Concerns Register from all A4 tables.*
