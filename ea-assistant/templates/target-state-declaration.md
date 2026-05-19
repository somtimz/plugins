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
