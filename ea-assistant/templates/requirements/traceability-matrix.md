---
artifact: Requirements Traceability Matrix
artifactId: traceability-matrix
engagement: {{engagement_name}}
phase: Requirements
status: Draft
reviewStatus: Not Reviewed
version: 0.1
templateVersion: 0.9.55
lastModified: {{YYYY-MM-DD}}
taxonomy:
  admPhases: [Requirements]
  zachmanCell: ""
  domain: Cross-cutting
  category: Analysis
  audience: Architecture
  layer: Reference
  sensitivity: Internal
  tags: [traceability, requirements, goals, cross-cutting]
relatedArtifacts: []
diagrams: []
links: []
---
<details>
<summary>🔒 TOGAF/ADM Compliance Status (author only — collapses on export)</summary>

## Compliance Checklist

| Requirement | Status | Notes |
|---|---|---|
| T3-TRACE | ⚠️ Pending | |
| Two-section structure (Corporate / Project) | ⚠️ Pending | |

*This section is for author guidance only. Run `/ea-grill` to validate compliance.*

</details>

<details>
<summary>📋 Guidance</summary>

**Purpose:** The Requirements Traceability Matrix maps each architecture requirement (REQ-NNN) to the artifacts that address it, providing assurance that all requirements have been considered and either addressed or formally waived. It is the primary evidence of requirements completeness for governance reviews.

**What to include:** All requirements from the Requirements Register (Corporate scope first, Project scope second), mapped to the architecture domain artifacts (Business, Data, Application, Technology) that address each requirement. Waived requirements are shown with 🚫 in all cells. This matrix is generated and updated by `/ea-requirements trace` — do not edit it manually.

**Quality indicators:**
- Untraced requirements (no cell has an artifact reference) are highlighted and actioned — either they are addressed in an artifact that needs to be linked, or they are a gap that must be planned for
- Corporate requirements appear first — governance reviewers will check corporate requirements compliance before project-specific requirements
- The matrix is updated after each domain architecture artifact is approved — a stale matrix does not reflect the current coverage state

**Common mistakes:**
- Leaving the traceability matrix until Phase G compliance review — by then, requirements gaps discovered here are expensive to address; trace continuously
- Showing all requirements as covered without verifying the referenced artifacts actually address them — coverage must be substantive, not just a link for appearance
- Not reflecting waivers — a Corporate requirement with no artifact reference and no 🚫 waiver indicator appears as an unaddressed gap

**TOGAF reference:** TOGAF 10 Requirements Management (§24.7) — traceability is a continuous ADM activity; the Traceability Matrix provides the evidence base for confirming that architecture decisions address the stated requirements.

</details>

# Requirements Traceability Matrix

**Engagement:** {{engagement_name}}
**Organisation:** {{organisation}}
**Date:** {{YYYY-MM-DD}}
**Version:** {{version}}

---

## Executive Summary

<details>
<summary>📋 Guidance</summary>

Summary of requirements traceability: what proportion of corporate and project requirements are addressed by architecture decisions.
Diagram: Traceability coverage heat map
Run `/ea-summary refresh` to regenerate this section from current artifact content.

</details>

{{executive_summary}}

---

## Coverage Summary

| Total | Corporate 🔒 | Project | Fully Traced | Partially Traced | Not Traced |
|---|---|---|---|---|---|
| {{total}} | {{corporate}} | {{project}} | {{fully_traced}} | {{partial}} | {{not_traced}} |

**Corporate coverage:** {{corp_traced}} / {{corp_total}} requirements fully traced
**Project coverage:** {{proj_traced}} / {{proj_total}} requirements fully traced

---

## Traceability Matrix — Corporate Requirements

<details>
<summary>📋 Guidance</summary>

Corporate requirements appear first. Content fields are read-only; this matrix tracks
artifact linkage and coverage status only. Waived requirements show 🚫 in all cells.

</details>

| Req ID | Requirement | Priority | Coverage |
|---|---|---|---|
| 🔒REQ-001 | {{requirement}} | High | ArchVision ⬜ · BizArch ⬜ · Data ⬜ · App ⬜ · Tech ⬜ · Roadmap ⬜ |

---

## Traceability Matrix — Project Requirements

<details>
<summary>📋 Guidance</summary>

Project-specific requirements. The Derives From column shows which Corporate requirement
this project requirement responds to, if applicable (— if none).

</details>

| Req ID | Requirement | Priority | Derives From | Coverage |
|---|---|---|---|---|
| REQ-00N | {{requirement}} | Medium | — | ArchVision ⬜ · BizArch ⬜ · Data ⬜ · App ⬜ · Tech ⬜ · Roadmap ⬜ |

Legend: ✅ Addressed | ⚠️ Partially addressed | ⬜ Not addressed | 🚫 Waived

---

## Untraced Requirements

<details>
<summary>📋 Guidance</summary>

List all requirements with no artifact coverage. These must be addressed or formally
waived before any artifact is submitted for approval. Waived Corporate requirements
are excluded from this section.

</details>

| Req ID | Scope | Requirement | Status | Action Required |
|---|---|---|---|---|
| {{req_id}} | Corporate / Project | {{requirement}} | {{status}} | {{action}} |

---

## Traceability Notes

{{traceability_notes}}

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
*Use `/ea-requirements trace` to regenerate this matrix from current artifact data.*
*🚫 = Requirement formally waived — see Waiver Justification in the Requirements Register.*
