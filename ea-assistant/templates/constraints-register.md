---
artifactId: constraints-register
artifact: Architecture Constraints Register
artifactId: constraints-register
engagement: {{engagement_name}}
phase: All
status: Draft
reviewStatus: Not Reviewed
version: 0.1
templateVersion: 0.9.55
lastModified: {{YYYY-MM-DD}}
taxonomy:
  domain: Cross-cutting
  category: Register
  audience: All
  layer: Reference
  sensitivity: Internal
  tags: [constraints, traceability, governance]
relatedArtifacts: []
diagrams: []
links: []
---

<details>
<summary>🔒 TOGAF/ADM Compliance Status (author only — collapses on export)</summary>

## Compliance Checklist

| Requirement | Status | Notes |
|---|---|---|
| T3-CON | ⚠️ Pending | Type column present |
| T3-CON-OWNER | ⚠️ Pending | Every Active constraint has a named owner |

*This section is for author guidance only. Run `/ea-grill` to validate compliance.*

</details>

<details>
<summary>📋 Guidance</summary>

The Architecture Constraints Register captures all non-negotiable restrictions on the solution space for this engagement.

Constraints are distinct from requirements (which define outcomes) and from risks (which are uncertain). Every constraint must have:
  - a **Source** (POL-NNN policy ID preferred, or policy/regulation/contract/mandate free-text)
  - an **Owner** (person or role accountable for upholding it)

Constraints are grouped by Type: Technology, Regulatory, Budget, Timeline, Organisational, Interoperability.

**Source field guidance:**
- Preferred: link to a `POL-NNN` policy ID in the Policies Register (e.g. `POL-003`)
- Acceptable: free-text if the policy is not yet catalogued (e.g. "Capital Expenditure Policy v3.1")
- If a constraint's Source is a policy name that matches an existing POL-NNN, update the Source to the POL-NNN ID for traceability.

**Scope:**
  - Enterprise 🔒: organisation-wide standards, principles, or regulatory mandates synced from the shared repo. Content fields (statement, type, source, owner) are read-only — only status, linked artifacts, waiver justification, and impact assessment may be updated locally.
  - Program: engagement-specific constraints captured during this program. Fully editable.

**Traceability:**
  - Every SBB should reference the CST-NNN constraints that bound its selection.
  - Use `/ea-constraints trace` to verify artifact and SBB linkage.
  - Use `/ea-constraints impact` to assess which capabilities or work packages are affected.

**⚠️ Two Layers check:** Distinguish `Business Constraints` (what the business must respect, e.g. "Must comply with GDPR") from `Architecture Constraints` (how the EA function governs solution design, e.g. "Must use approved cloud regions"). Both belong in the Constraints Register; the distinction is in Type and Source.

**Quality indicators:**
- Every active constraint has a named owner — a constraint without an owner is unenforceable
- Enterprise-scope constraints reference POL-NNN IDs — free-text source is acceptable only when the policy has not yet been catalogued
- Use `/ea-constraints trace` to verify that SBB selections reference the constraints that bound them; untraceable constraints are not actively governing design decisions

**Common mistakes:**
- Capturing requirements as constraints — a constraint is non-negotiable (if violated, the solution is not acceptable); a requirement is a stated need (can be prioritised and traded). "The system must respond within 2 seconds" is a requirement; "Must comply with GDPR" is a constraint
- Constraints without expiry or review dates — regulatory and contractual constraints change; an undated constraint may be obsolete
- Missing enterprise-scope constraints because they were not synced from the shared repository — always check for enterprise constraints before starting Phase B

**TOGAF reference:** TOGAF 10 §23 (Preliminary Phase) and §26 (Phase B) — Architecture Constraints are identified progressively from the Preliminary Phase onward. The Constraints Register is a cross-cutting artifact maintained throughout the ADM cycle.

</details>

# Architecture Constraints Register

**Engagement:** {{engagement_name}}
**Organisation:** {{organisation}}
**Last Synced from Repo:** {{last_sync_date}}
**Version:** {{version}}

---

## Executive Summary

<details>
<summary>📋 Guidance</summary>

Summary of the constraint landscape: total count, type distribution, and key enterprise constraints driving this engagement.
Diagram: Constraints summary chart (count by type/priority)
Run `/ea-summary refresh` to regenerate this section from current artifact content.

</details>

{{executive_summary}}

---

## Constraints Summary

| Total | Enterprise 🔒 | Program | Active | Waived | Proposed | High Priority | Untraced |
|---|---|---|---|---|---|---|---|
| {{N}} | {{N}} | {{N}} | {{N}} | {{N}} | {{N}} | {{N}} | {{N}} |

---

## Technology Constraints

| ID | Statement | Source | Owner | Priority | Status | Linked Artifacts |
|---|---|---|---|---|---|---|
| CST-NNN | {{statement}} | {{source}} | {{owner}} | {{priority}} | {{status}} | {{artifacts}} |

---

## Regulatory Constraints

| ID | Statement | Source | Owner | Priority | Status | Linked Artifacts |
|---|---|---|---|---|---|---|
| CST-NNN | {{statement}} | {{source}} | {{owner}} | {{priority}} | {{status}} | {{artifacts}} |

---

## Budget Constraints

| ID | Statement | Source | Owner | Priority | Status | Linked Artifacts |
|---|---|---|---|---|---|---|
| CST-NNN | {{statement}} | {{source}} | {{owner}} | {{priority}} | {{status}} | {{artifacts}} |

---

## Timeline Constraints

| ID | Statement | Source | Owner | Priority | Status | Linked Artifacts |
|---|---|---|---|---|---|---|
| CST-NNN | {{statement}} | {{source}} | {{owner}} | {{priority}} | {{status}} | {{artifacts}} |

---

## Organisational Constraints

| ID | Statement | Source | Owner | Priority | Status | Linked Artifacts |
|---|---|---|---|---|---|---|
| CST-NNN | {{statement}} | {{source}} | {{owner}} | {{priority}} | {{status}} | {{artifacts}} |

---

## Interoperability Constraints

| ID | Statement | Source | Owner | Priority | Status | Linked Artifacts |
|---|---|---|---|---|---|---|
| CST-NNN | {{statement}} | {{source}} | {{owner}} | {{priority}} | {{status}} | {{artifacts}} |

---

## Untraced Constraints

⚠️ The following constraints have no linked artifacts or SBB references:

| ID | Statement | Type | Owner | Action |
|---|---|---|---|---|
| CST-NNN | {{statement}} | {{type}} | {{owner}} | Link to artifact or SBB |

---

## Appendix A3 — Decision Log

| # | Decision | Rationale | Authority | Date | Verified |
|---|---|---|---|---|---|
| 1 | | | | | |

---

## Appendix A5 — Related Architecture Decisions

| ADR ID | Title | Status |
|---|---|---|
| | | |

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
