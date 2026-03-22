---
artifact: Requirements Traceability Matrix
engagement: {{engagement_name}}
phase: Requirements
status: Draft
reviewStatus: Not Reviewed
version: 0.1
lastModified: {{YYYY-MM-DD}}
---

<!-- GUIDANCE:
  The Requirements Traceability Matrix maps each architecture requirement to the artifacts
  that address it. It ensures every approved requirement has coverage in at least one artifact,
  and provides a single view of requirement-to-artifact linkage across all phases.
  This matrix is generated or updated by /ea-requirements trace.
-->

# Requirements Traceability Matrix

**Engagement:** {{engagement_name}}
**Organisation:** {{organisation}}
**Date:** {{YYYY-MM-DD}}
**Version:** {{version}}

---

## Coverage Summary

| Total Requirements | Fully Traced | Partially Traced | Not Traced |
|---|---|---|---|
| {{total}} | {{fully_traced}} | {{partial}} | {{not_traced}} |

---

## Traceability Matrix

<!-- GUIDANCE:
  One row per requirement. Add a column for each artifact created in the engagement.
  Use ✅ (addressed), ⚠️ (partial), ⬜ (not addressed).
  Populate using /ea-requirements trace — do not fill manually.
-->

| Req ID | Requirement | Priority | Arch Vision | Biz Arch | Data | App | Tech | Roadmap |
|---|---|---|---|---|---|---|---|---|
| REQ-001 | {{requirement}} | High | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ |

Legend: ✅ Addressed | ⚠️ Partially addressed | ⬜ Not addressed

---

## Untraced Requirements

<!-- GUIDANCE:
  List all requirements with no artifact coverage. These must be addressed before
  any artifact is submitted for approval.
-->

| Req ID | Requirement | Status | Action Required |
|---|---|---|---|
| {{req_id}} | {{requirement}} | {{status}} | {{action}} |

---

## Traceability Notes

{{traceability_notes}}

---

*This document was created using the EA Assistant plugin.*
*Use `/ea-requirements trace` to regenerate this matrix from current artifact data.*
