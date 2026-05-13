---
artifact: Architecture Constraints Register
engagement: {{engagement_name}}
phase: All
status: Draft
reviewStatus: Not Reviewed
version: 0.1
templateVersion: 0.9.5
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
