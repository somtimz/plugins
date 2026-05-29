---
artifactId: stakeholder-action-plan
artifact: Stakeholder Action Plan
engagement: {{engagement_name}}
phase: All
status: Draft
reviewStatus: Not Reviewed
version: 0.1
templateVersion: 0.9.55
lastModified: {{YYYY-MM-DD}}
taxonomy:
  domain: Cross-cutting
  category: Governance
  audience: Governance
  layer: Governance
  sensitivity: Confidential
  tags: [stakeholders, approvals, actions, governance, arb]
relatedArtifacts: []
diagrams: []
links: []
---
<details>
<summary>📋 Guidance</summary>

**Purpose:** The Stakeholder Action Plan provides a consolidated, per-approver view of what each stakeholder with approval authority must do to progress this engagement. It is seeded from the SAoW acceptance criteria (§6) and sign-off table (§7), enriched with success criteria from the Target State Declaration, and suitable for distribution to a governance forum or ARB.

**What to include:** A summary of the target state, an approval authority register (one row per approver), per-approver action detail sections (listing each approval with acceptance criteria, due date, and status), and a governance schedule of key approval gates.

**Lifecycle:** Generate once from SAoW + Target State Declaration using `/ea-actions generate`. Refine with `/ea-actions update`. Regenerate after significant SAoW changes.

**Quality indicators:**
- Every deliverable requiring sign-off has a named approver
- Every action has a due date traceable to the SAoW schedule
- Status is kept current — stale action plans erode stakeholder trust

**Common mistakes:**
- Action plan that lists deliverables but no acceptance criteria — approvers need to know what "approved" means
- Not distributing the plan to approvers — an action plan no one has seen is not an action plan
- Regenerating the plan without preserving manual updates to status — use `/ea-actions update` to update individual rows

</details>

# Stakeholder Action Plan

**Engagement:** {{engagement_name}}
**Organisation:** {{organisation}}
**Date:** {{YYYY-MM-DD}}
**Version:** {{version}}
**Status:** {{status}}

---

## Executive Summary

<details>
<summary>📋 Guidance</summary>

One paragraph: the target state in plain language, the total number of approvers, pending/complete/overdue action counts. Generated automatically by `/ea-actions generate` — update when regenerating.

</details>

{{executive_summary}}

**Target State:** {{target_state_summary}}

**Action Summary:**
| Total Approvers | Pending | In Review | Approved | Deferred | Overdue |
|---|---|---|---|---|---|
| {{total_approvers}} | {{pending}} | {{in_review}} | {{approved}} | {{deferred}} | {{overdue}} |

---

## Approval Authority Register

<details>
<summary>📋 Guidance</summary>

One row per stakeholder with approval authority. Derived from SAoW §6 (`Accepted By`) and §7 (sign-off). Used as the navigation index for the per-approver sections below.

</details>

| Name | Role | Organisation | Pending Actions | Next Due | Overall Status |
|---|---|---|---|---|---|
| {{approver_name}} | {{role}} | {{organisation}} | {{pending_count}} | {{next_due_date}} | Pending |

---

## Per-Approver Action Detail

<details>
<summary>📋 Guidance</summary>

One H3 section per approver. Each section contains an action table listing all approvals this stakeholder owns. Status values: Pending | In Review | Approved | Deferred.

</details>

### {{approver_name_1}} — {{role_1}}

**Organisation:** {{organisation_1}}
**Role reference:** {{ROLE-NNN}}

| # | Action | Deliverable | Acceptance Criteria | Due Date | Status |
|---|---|---|---|---|---|
| 1 | Review and approve | {{deliverable_1}} | {{acceptance_criteria_1}} | {{due_date_1}} | Pending |

---

## Governance Schedule

<details>
<summary>📋 Guidance</summary>

Key approval gates in sequence. Derived from the SAoW schedule (§4). Add ARB sessions, sponsor reviews, and formal sign-off meetings.

</details>

| Gate | Description | Required Approvers | Target Date | Status |
|---|---|---|---|---|
| {{gate_1}} | {{description_1}} | {{approvers_1}} | {{date_1}} | Pending |

---

## Artifact Working Notes

> Working-layer: persists across reviews. Never exported to Word/PPTX — stripped by `/ea-generate`.

### Comments

| Date | Author | Note |
|---|---|---|
| — | — | — |

### Outstanding Tasks

- [ ] *(Add tasks — e.g. "Distribute to approvers before next ARB session")*

*This document was created using the EA Assistant plugin.*
*Use `/ea-actions status` for a summary of pending and overdue actions.*
