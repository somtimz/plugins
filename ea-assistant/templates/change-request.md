---
artifact: Architecture Change Request
engagement: {{engagement_name}}
phase: H
status: Draft
reviewStatus: Not Reviewed
version: 0.1
lastModified: {{YYYY-MM-DD}}
---

<!-- GUIDANCE:
  An Architecture Change Request (ACR) is a Phase H artifact. Phase H (Architecture Change
  Management) governs the ongoing evolution of the architecture after the initial target state
  has been delivered. Change requests are raised when a business event, technology change, or
  implementation learning requires a deviation from, or update to, the agreed architecture.
  The ACR process ensures changes are assessed for architectural impact before they are approved,
  preventing uncontrolled architectural drift.
-->

# Architecture Change Request

**Engagement:** {{engagement_name}}
**Change Request ID:** {{change_request_id}}
**Organisation:** {{organisation}}
**Raised By:** {{raised_by}}
**Date Raised:** {{YYYY-MM-DD}}
**Version:** {{version}}
**Status:** Draft / Under Review / Approved / Rejected / Deferred

---

## 1. Change Description

<!-- GUIDANCE:
  Describe the proposed change clearly and concisely. State what is being changed, added, or
  removed. Be specific about the architectural element involved (a specific application, data
  entity, integration, technology component, or principle). Avoid conflating the change with
  its justification — that belongs in section 2.
-->

**Type of Change:** New capability / Technology substitution / Process change / Correction / Decommission / Other

**Summary:** {{change_summary}}

**Detailed Description:**
{{change_description}}

**Affected Architecture Domains:** Business / Data / Application / Technology (select all that apply)

---

## 2. Justification

<!-- GUIDANCE:
  Explain why this change is needed. Link to a business driver, technology trigger (e.g. a vendor
  end-of-life notice), regulatory requirement, or learning from implementation. A well-justified
  change request is much easier to assess and approve. Include the consequence of NOT making the
  change — this helps the architecture authority weigh the risk of approval against the risk of
  rejection.
-->

**Business Driver / Trigger:** {{business_driver}}

**Justification:**
{{justification}}

**Consequence of Not Changing:**
{{consequence_of_inaction}}

---

## 3. Impact Assessment

<!-- GUIDANCE:
  Assess the impact of the proposed change on the existing architecture. Consider all domains,
  even if the change appears localised — application changes often have data and technology
  implications, and vice versa. List each artifact that would need to be updated if the change
  is approved. Identify any dependencies on other work packages or change requests.
-->

### Impact on Architecture Domains

| Domain | Impact | Description |
|---|---|---|
| Business Architecture | High / Med / Low / None | {{impact_description}} |
| Data Architecture | High / Med / Low / None | {{impact_description}} |
| Application Architecture | High / Med / Low / None | {{impact_description}} |
| Technology Architecture | High / Med / Low / None | {{impact_description}} |

### Artifacts Requiring Update
| Artifact | Nature of Change |
|---|---|
| {{artifact_name}} | {{change_description}} |

### Dependencies
{{dependencies}}

### Estimated Effort
{{estimated_effort}}

---

## 4. Risk Assessment

<!-- GUIDANCE:
  Assess the risks introduced by making this change. Also consider the risk of the change
  interacting badly with work already in progress. Distinguish between architectural risks
  (the change creates technical debt, introduces an undesirable pattern, or weakens a control)
  and implementation risks (disruption to live systems, migration complexity).
-->

| Risk ID | Description | Likelihood | Impact | Mitigation |
|---|---|---|---|---|
| CR-R001 | {{description}} | High / Med / Low | High / Med / Low | {{mitigation}} |
| CR-R002 | {{description}} | High / Med / Low | High / Med / Low | {{mitigation}} |

**Overall Risk Level:** High / Medium / Low

---

## 5. Disposition

<!-- GUIDANCE:
  Record the decision made by the architecture authority. Choose Approve, Reject, or Defer,
  and document the rationale. If approved with conditions, list the conditions explicitly —
  these become conformance requirements for the implementing team. If deferred, record when
  the request should be reconsidered and what information is needed before a decision can be made.
-->

**Decision:** Approved / Rejected / Deferred / Approved with Conditions

**Decision Date:** {{decision_date}}
**Decision Authority:** {{decision_authority}}

**Rationale:**
{{decision_rationale}}

**Conditions (if Approved with Conditions):**
{{conditions}}

**Deferral Reason and Reconsideration Trigger (if Deferred):**
{{deferral_reason}}

---

## 6. Updated Artifacts

<!-- GUIDANCE:
  If the change is approved, list all artifacts that must be updated as a result, who is
  responsible for updating them, and the target date. Tracking this ensures the architecture
  repository remains current and consistent with the implemented state.
-->

| Artifact | Update Required | Owner | Target Date | Status |
|---|---|---|---|---|
| {{artifact_name}} | {{update_description}} | {{owner}} | {{target_date}} | Pending / In Progress / Complete |

---

*This document was created using the EA Assistant plugin.*
