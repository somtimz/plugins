---
artifact: Requirements Traceability Matrix
engagement: {{engagement_name}}
phase: Requirements
status: Draft
reviewStatus: Not Reviewed
version: 0.1
templateVersion: 0.9.5
lastModified: {{YYYY-MM-DD}}
taxonomy:
  domain: Cross-cutting
  category: Analysis
  audience: Architecture
  layer: Reference
  sensitivity: Internal
  tags: [traceability, requirements, goals, cross-cutting]
---

<details>
<summary>📋 Guidance</summary>

The Requirements Traceability Matrix maps each architecture requirement to the artifacts
that address it. Requirements are grouped by scope — Corporate first, Project second.
Corporate requirements with status Waived are shown with 🚫 in all artifact cells;
the waiver itself is the coverage action and they are excluded from the untraced count.
This matrix is generated or updated by /ea-requirements trace.

</details>

# Requirements Traceability Matrix

**Engagement:** {{engagement_name}}
**Organisation:** {{organisation}}
**Date:** {{YYYY-MM-DD}}
**Version:** {{version}}

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

| Req ID | Requirement | Priority | Arch Vision | Biz Arch | Data | App | Tech | Roadmap |
|---|---|---|---|---|---|---|---|---|
| 🔒REQ-001 | {{requirement}} | High | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ |

---

## Traceability Matrix — Project Requirements

<details>
<summary>📋 Guidance</summary>

Project-specific requirements. The Derives From column shows which Corporate requirement
this project requirement responds to, if applicable (— if none).

</details>

| Req ID | Requirement | Priority | Derives From | Arch Vision | Biz Arch | Data | App | Tech | Roadmap |
|---|---|---|---|---|---|---|---|---|---|
| REQ-00N | {{requirement}} | Medium | — | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ |

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

*This document was created using the EA Assistant plugin.*
*Use `/ea-requirements trace` to regenerate this matrix from current artifact data.*
*🚫 = Requirement formally waived — see Waiver Justification in the Requirements Register.*
