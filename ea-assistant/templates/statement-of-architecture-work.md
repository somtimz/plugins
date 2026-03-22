---
artifact: Statement of Architecture Work
engagement: {{engagement_name}}
phase: A
status: Draft
reviewStatus: Not Reviewed
version: 0.1
lastModified: {{YYYY-MM-DD}}
---

<!-- GUIDANCE:
  The Statement of Architecture Work (SoAW) is the formal agreement that defines the scope and
  approach for an architecture engagement. It is produced in Phase A and approved by the sponsor
  before substantive architecture work begins. It is analogous to a project charter and establishes
  the mandate, schedule, and acceptance criteria for the engagement.
-->

# Statement of Architecture Work

**Engagement:** {{engagement_name}}
**Organisation:** {{organisation}}
**Sponsor:** {{sponsor}}
**Architecture Lead:** {{architecture_lead}}
**Date:** {{YYYY-MM-DD}}
**Version:** {{version}}
**Status:** {{status}}

---

## 1. Purpose

<!-- GUIDANCE:
  State why this architecture engagement is being undertaken. Describe the business trigger or
  decision that has initiated this work. Reference the Architecture Vision if it already exists.
  This should be 2-4 sentences: clear, non-technical, and focused on business value.
-->

{{purpose}}

---

## 2. Scope

<!-- GUIDANCE:
  Define the architectural scope precisely. Specify which business domains, systems, organisational
  units, geographies, and TOGAF phases are in scope. Clearly list what is out of scope to prevent
  scope creep. Reference the Architecture Vision scope section for consistency.
-->

### In Scope
{{scope_in}}

### Out of Scope
{{scope_out}}

### Architecture Domains
{{architecture_domains}}

### TOGAF Phases to be Executed
{{phases_in_scope}}

---

## 3. Approach

<!-- GUIDANCE:
  Describe the methodology and approach for conducting the engagement. Include: how stakeholder
  engagement will be managed, what discovery techniques will be used (workshops, interviews, document
  review), what modelling notation will be applied (ArchiMate, BPMN, etc.), and how decisions
  will be documented and governed.
-->

{{approach}}

### Key Activities
| Activity | Description | Method |
|---|---|---|
| {{activity_1}} | {{description_1}} | Workshop / Interview / Review |
| {{activity_2}} | {{description_2}} | Workshop / Interview / Review |

---

## 4. Schedule

<!-- GUIDANCE:
  Provide a high-level schedule with milestones. Include phase start/end dates, key review gates,
  and the expected date of each deliverable. Align with any broader programme or project timeline.
-->

| Milestone | Description | Target Date | Owner |
|---|---|---|---|
| Kick-off | {{kickoff_description}} | {{kickoff_date}} | {{owner}} |
| Phase A complete | Architecture Vision approved | {{phase_a_date}} | {{owner}} |
| {{milestone_1}} | {{description_1}} | {{date_1}} | {{owner_1}} |
| Final review | All deliverables reviewed and accepted | {{final_date}} | {{owner}} |

---

## 5. Roles and Responsibilities

<!-- GUIDANCE:
  List all roles involved in the engagement. Clarify who is Responsible, Accountable, Consulted,
  and Informed (RACI) for key decisions and deliverables. Include both the architecture team and
  client-side stakeholders who have obligations.
-->

| Role | Name | Organisation | RACI for Deliverables | RACI for Decisions |
|---|---|---|---|---|
| Sponsor | {{sponsor}} | {{organisation}} | Accountable | Accountable |
| Architecture Lead | {{architecture_lead}} | {{architecture_org}} | Responsible | Responsible |
| {{role_1}} | {{name_1}} | {{org_1}} | {{raci_deliverables_1}} | {{raci_decisions_1}} |
| {{role_2}} | {{name_2}} | {{org_2}} | {{raci_deliverables_2}} | {{raci_decisions_2}} |

---

## 6. Acceptance Criteria

<!-- GUIDANCE:
  Define the measurable criteria that must be satisfied for each deliverable to be accepted.
  Acceptance criteria should be objective and verifiable — avoid vague terms like "high quality".
  Include who has authority to accept each deliverable.
-->

| Deliverable | Acceptance Criteria | Accepted By |
|---|---|---|
| Architecture Vision | {{av_criteria}} | {{sponsor}} |
| Business Architecture | {{ba_criteria}} | {{ba_approver}} |
| {{deliverable_1}} | {{criteria_1}} | {{approver_1}} |

---

## 7. Sign-off

<!-- GUIDANCE:
  This section records formal approval of the Statement of Architecture Work. All named approvers
  must sign before the engagement proceeds beyond Phase A. Retain a signed copy in the engagement
  record.
-->

By signing below, the named parties confirm they have read, understood, and approved this
Statement of Architecture Work.

| Role | Name | Signature | Date |
|---|---|---|---|
| Sponsor | {{sponsor}} | | |
| Architecture Lead | {{architecture_lead}} | | |
| {{approver_role_1}} | {{approver_name_1}} | | |

---

*This document was created using the EA Assistant plugin.*
