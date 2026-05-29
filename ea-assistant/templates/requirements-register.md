---
artifactId: requirements-register
artifact: Architecture Requirements Register
artifactId: requirements-register
engagement: {{engagement_name}}
phase: Requirements
status: Draft
reviewStatus: Not Reviewed
version: 0.1
templateVersion: 0.9.55
lastModified: {{YYYY-MM-DD}}
taxonomy:
  domain: Cross-cutting
  category: Analysis
  audience: All
  layer: Reference
  sensitivity: Internal
  tags: [requirements, nfr, constraints, traceability]
relatedArtifacts: []
diagrams: []
links: []
---
<details>
<summary>🔒 TOGAF/ADM Compliance Status (author only — collapses on export)</summary>

## Compliance Checklist

| Requirement | Status | Notes |
|---|---|---|
| T3-ADR | ⚠️ Pending | |
| T3-REQ | ⚠️ Pending | |
| Scope column present (Enterprise / Program) | ⚠️ Pending | |

*This section is for author guidance only. Run `/ea-grill` to validate compliance.*

</details>

<details>
<summary>📋 Guidance</summary>

The Architecture Requirements Register captures all architecture requirements for this engagement.
Requirements are grouped by scope:
  - Enterprise: organisation-wide standards, principles, or regulatory mandates synced from the
    shared repo. Content fields (statement, category, priority) are read-only — only status,
    linked artifacts, and waiver justification may be updated locally.
  - Program: engagement-specific requirements captured during this program. Fully editable.
Sync from the shared requirements repository using /ea-requirements sync.
Enterprise requirements are prefixed with 🔒 to indicate read-only content.
Non-functional requirements (NFRs) should have a populated NFR Sub-Type and Measurable Target.
Use /ea-interview start phase requirements to run a guided NFR discovery session.

**⚠️ Two Layers check:** Distinguish `Business Requirements` (what the business needs to achieve, e.g., "Reduce case-handling time by 40%") from `Architecture Requirements` (how the EA function governs solution design, e.g., "All AI models must pass bias audit"). The Requirements Register primarily holds **Business Requirements**; Architecture Requirements belong in the Governance Framework or Architecture Principles. See `ea-concepts.md` → **Two Layers of Intent**.

**Quality indicators:**
- Non-functional requirements (NFRs) have a populated Measurable Target — "the system must be fast" is not an NFR; "95th-percentile response time under 2 seconds under peak load" is
- Every requirement traces to an architecture domain artifact where it is addressed — orphan requirements are either not addressed or not tracked
- Enterprise requirements are synced and current — run `/ea-requirements sync` before final review

**Common mistakes:**
- Requirements written as solutions ("the system must use a REST API") rather than needs ("the system must allow third-party applications to access customer data") — solution choices belong in ADRs, not requirements
- NFRs without measurable targets — these cannot be verified in a Compliance Assessment
- Missing scope classification (Enterprise / Program) — requirements without scope cannot be appropriately governed or waived

**TOGAF reference:** TOGAF 10 Part III, Requirements Management (§24.7) — the Requirements Register is a continuous artifact maintained throughout the ADM cycle, feeding into each domain architecture phase and the Gap Analysis.

</details>

# Architecture Requirements Register

**Engagement:** {{engagement_name}}
**Organisation:** {{organisation}}
**Last Synced from Repo:** {{last_sync_date}}
**Version:** {{version}}

---

## Executive Summary

<details>
<summary>📋 Guidance</summary>

Summary of the requirement landscape: total count, priority distribution, and key corporate requirements driving this engagement.
Diagram: Requirements summary chart (count by priority/status)
Run `/ea-summary refresh` to regenerate this section from current artifact content.

</details>

{{executive_summary}}

---

## Requirements Summary

| Total | Enterprise 🔒 | Program | Approved | Draft | Deferred | Waived | Rejected | Sample Tests |
|---|---|---|---|---|---|---|---|---|
| {{total}} | {{enterprise}} | {{program}} | {{approved}} | {{draft}} | {{deferred}} | {{waived}} | {{rejected}} | ✅ {{N}} / ⬜ {{M}} |

<!-- GUIDANCE: Sample Tests column — ✅ N = number of requirements with at least one sample test captured; ⬜ M = number with no tests. Regenerate via `/ea-requirements trace`. -->

---

> **NFR Coverage Checklist** — before marking this register complete, confirm at least one entry exists for each applicable NFR category:
> ☐ Availability &nbsp; ☐ Reliability &nbsp; ☐ Performance &nbsp; ☐ Security &nbsp; ☐ Usability &nbsp; ☐ Maintainability &nbsp; ☐ Portability &nbsp; ☐ Compatibility &nbsp; ☐ Recoverability
> Run `/ea-grill requirements-register --skill requirements` for a full NFR coverage review.

---

## Enterprise Requirements

<details>
<summary>📋 Guidance</summary>

Enterprise requirements are synced from the shared requirements repository.
Content fields are read-only — only Status, Linked Artifacts, and Waiver Justification
may be changed locally. Prefix each ID with 🔒 in headings and tables.
To formally waive an Enterprise requirement, set Status to Waived and provide a justification.

</details>

---

### 🔒REQ-001: {{requirement_title}}

| Field | Value |
|---|---|
| **ID** | [REQ-001](../details/REQ-001.md) |
| **Scope** | Enterprise 🔒 |
| **Statement** | {{requirement_statement}} |
| **Category** | Functional / Non-Functional / Constraint / Principle |
| **NFR Sub-Type** | Performance / Reliability / Availability / Usability / Security / Maintainability / Portability / Compatibility / Recoverability / Compliance / Quality / Process / Technical / Operational / Monitoring / Governance / Ethical / Legal / Resilience — or ➖ Not applicable |
| **Measurable Target** | {{sla_or_threshold — e.g. 99.9% uptime, <200ms p95, RTO 4h}} — or ➖ Not applicable |
| **Priority** | High / Medium / Low |
| **Source** | {{source_document}} |
| **Motivation** | DRV-NNN / ISS-NNN / PRB-NNN / G-NNN / OBJ-NNN (link to the driver, issue, problem, goal, or objective in Architecture Vision that makes this requirement necessary) |
| **Status** | Draft / Approved / Deferred / Waived / Rejected |
| **Waiver Justification** | {{required_if_status_is_Waived — leave blank otherwise}} |
| **ADM Phase** | {{phase}} |
| **Zachman Cell** | Row {{N}} / Column {{N}} ({{description}}) |
| **Linked Artifacts** | {{artifact_ids}} |
| **Details** | [→](../details/REQ-001.md) |

### Sample Tests

<!-- GUIDANCE: Optional. List verification tests that confirm this requirement is met.
     Each test should be independently executable and produce a clear pass/fail result.
     Format: bullet list. Example: "Submit 1,000 decisions and verify all appear in audit log." -->

*(no sample tests captured)*

### Stories

<!-- GUIDANCE: Optional. List user stories that implement the capability or component needed
     to satisfy this requirement. Format: "As a {actor}, I want {goal} so that {benefit}."
     Assign STY-NNN IDs for stories that need to be tracked formally.
     Tasks (step-level implementation items) are captured under stories, not here. -->

| STY-NNN | Story | Implements (SBB-NNN) | Tasks |
|---|---|---|---|

---

## Program Requirements

<details>
<summary>📋 Guidance</summary>

Program requirements are captured during this engagement and are fully editable.
Use the Derived From field to link a Program requirement to the Enterprise requirement
it responds to or refines — this maintains governance traceability.

</details>

---

### REQ-00N: {{requirement_title}}

| Field | Value |
|---|---|
| **ID** | REQ-00N |
| **Scope** | Program |
| **Statement** | {{requirement_statement}} |
| **Category** | Functional / Non-Functional / Constraint / Principle |
| **NFR Sub-Type** | Performance / Reliability / Availability / Usability / Security / Maintainability / Portability / Compatibility / Recoverability / Compliance / Quality / Process / Technical / Operational / Monitoring / Governance / Ethical / Legal / Resilience — or ➖ Not applicable |
| **Measurable Target** | {{sla_or_threshold — e.g. 99.9% uptime, <200ms p95, RTO 4h}} — or ➖ Not applicable |
| **Priority** | High / Medium / Low |
| **Source** | {{source_stakeholder_or_document}} |
| **Motivation** | DRV-NNN / ISS-NNN / PRB-NNN / G-NNN / OBJ-NNN (link to the driver, issue, problem, goal, or objective in Architecture Vision that makes this requirement necessary) |
| **Status** | Draft / Approved / Deferred / Rejected |
| **Derived From** | {{enterprise_req_id — leave blank if not derived from an Enterprise requirement}} |
| **ADM Phase** | {{phase}} |
| **Zachman Cell** | Row {{N}} / Column {{N}} ({{description}}) |
| **Linked Artifacts** | {{artifact_ids}} |
| **Details** | — |

### Sample Tests

<!-- GUIDANCE: Optional. List verification tests that confirm this requirement is met.
     Each test should be independently executable and produce a clear pass/fail result.
     Format: bullet list. Example: "Submit 1,000 decisions and verify all appear in audit log." -->

*(no sample tests captured)*

### Stories

<!-- GUIDANCE: Optional. List user stories that implement the capability or component needed
     to satisfy this requirement. Format: "As a {actor}, I want {goal} so that {benefit}."
     Assign STY-NNN IDs for stories that need to be tracked formally.
     Tasks (step-level implementation items) are captured under stories, not here. -->

| STY-NNN | Story | Implements (SBB-NNN) | Tasks |
|---|---|---|---|

---

## Traceability Summary

<details>
<summary>📋 Guidance</summary>

This section is auto-generated by /ea-requirements trace.
It shows which artifacts address each requirement, grouped by scope.

</details>

| Req ID | Scope | Requirement | Arch Vision | Biz Arch | Data | App | Tech |
|---|---|---|---|---|---|---|---|
| 🔒REQ-001 | Enterprise | {{title}} | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ |
| REQ-00N | Program | {{title}} | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ |

Legend: ✅ Addressed | ⚠️ Partial | ⬜ Not addressed | 🚫 Waived

---
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
*Requirements synced from: {{requirementsRepoPath}}*
