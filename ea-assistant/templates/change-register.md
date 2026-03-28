---
artifact: Change Register
engagement: {{engagement_name}}
phase: H
status: Draft
reviewStatus: Not Reviewed
version: 0.1
lastModified: {{YYYY-MM-DD}}
generated: {{YYYY-MM-DD}}
filters: {{applied_filters_or_None}}
---

<details>
<summary>📋 Guidance</summary>

The Change Register aggregates all Architecture Change Request (ACR) artifacts from this
engagement into a single cross-artifact view. It is generated on demand via `/ea-changes`
and provides a consolidated picture of proposed, approved, rejected, and deferred changes
to the architecture.

Do not edit this document directly — regenerate it with `/ea-changes` whenever the source
ACR artifacts are updated. Use `/ea-changes status` for a quick inline summary.

</details>

# Change Register

**Engagement:** {{engagement_name}}
**Organisation:** {{organisation}}
**Generated:** {{YYYY-MM-DD}}
**Filters applied:** {{applied_filters_or_None}}
**Total Change Requests:** {{total_count}}

---

## Summary

| Status | Count |
|---|---|
| Under Review | {{count}} |
| Approved | {{count}} |
| Approved with Conditions | {{count}} |
| Rejected | {{count}} |
| Deferred | {{count}} |
| **Total** | **{{total_count}}** |

| Type | Count |
|---|---|
| New Capability | {{count}} |
| Technology Substitution | {{count}} |
| Process Change | {{count}} |
| Correction | {{count}} |
| Decommission | {{count}} |
| Other | {{count}} |

---

## Open — Under Review

| ID | Summary | Type | Domains Affected | Raised By | Date Raised | Overall Risk | Assigned To |
|---|---|---|---|---|---|---|---|
| {{acr_id}} | {{summary}} | {{type}} | {{domains}} | {{raised_by}} | {{date}} | High / Med / Low | {{assigned_to}} |

*(no open change requests)*

---

## Approved

| ID | Summary | Type | Decision Date | Decision Authority | Conditions |
|---|---|---|---|---|---|
| {{acr_id}} | {{summary}} | {{type}} | {{decision_date}} | {{authority}} | {{conditions_or_None}} |

*(no approved change requests)*

---

## Approved with Conditions

| ID | Summary | Conditions | Conditions Met? | Owner |
|---|---|---|---|---|
| {{acr_id}} | {{summary}} | {{conditions}} | Yes / No / Partial | {{owner}} |

*(no conditionally approved change requests)*

---

## Rejected

| ID | Summary | Date Rejected | Decision Authority | Rationale |
|---|---|---|---|---|
| {{acr_id}} | {{summary}} | {{date}} | {{authority}} | {{rationale}} |

*(no rejected change requests)*

---

## Deferred

| ID | Summary | Deferred Until / Trigger | Owner | Review Date |
|---|---|---|---|---|
| {{acr_id}} | {{summary}} | {{trigger}} | {{owner}} | {{review_date}} |

*(no deferred change requests)*

---

## Change Impact Summary

*Artifacts most frequently affected by approved or pending changes:*

| Artifact | Change Requests Referencing It | Net Impact |
|---|---|---|
| {{artifact_name}} | {{count}} | {{impact_description}} |

*(generated from approved and under-review ACRs only)*

---

## Source Cross-Reference

| Change Request File | ID | Status | Last Modified |
|---|---|---|---|
| {{acr_filename}} | {{acr_id}} | {{status}} | {{YYYY-MM-DD}} |

---

*Use `/ea-changes` to regenerate this register. Use `/ea-changes status` for an inline summary.*
