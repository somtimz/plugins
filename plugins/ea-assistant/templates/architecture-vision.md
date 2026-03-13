---
artifact: Architecture Vision
engagement: {{engagement_name}}
phase: A
status: Draft
reviewStatus: Not Reviewed
version: 0.1
lastModified: {{YYYY-MM-DD}}
---

<!-- GUIDANCE:
  The Architecture Vision is the primary output of Phase A. It defines the scope, stakeholders,
  constraints, and high-level target architecture for the engagement. It should be approved by
  the sponsor before proceeding to Phases B-D. Guidance text (in HTML comments) is for the
  author only and will NOT appear in rendered or exported documents.
-->

# Architecture Vision

**Engagement:** {{engagement_name}}
**Organisation:** {{organisation}}
**Sponsor:** {{sponsor}}
**Date:** {{YYYY-MM-DD}}
**Version:** {{version}}
**Status:** {{status}}

---

## 1. Executive Summary

<!-- GUIDANCE:
  A brief (3-5 sentence) summary of the engagement purpose, scope, and expected outcomes.
  Written for an executive audience. Avoid technical jargon.
-->

{{executive_summary}}

---

## 2. Problem Statement

<!-- GUIDANCE:
  Describe the business problem or opportunity that this architecture engagement addresses.
  Include the business drivers and why action is needed now.
-->

{{problem_statement}}

---

## 3. Strategic Goals and Objectives

<!-- GUIDANCE:
  List the high-level goals this architecture is intended to achieve.
  Each goal should be traceable to a business driver or requirement.
  Format: Goal statement + brief rationale.
-->

| # | Goal | Business Driver |
|---|---|---|
| 1 | {{goal_1}} | {{driver_1}} |
| 2 | {{goal_2}} | {{driver_2}} |

---

## 4. Scope

<!-- GUIDANCE:
  Define what is IN and OUT of scope for this engagement.
  Be specific about organisational units, systems, geographies, and time horizons.
-->

### In Scope
{{scope_in}}

### Out of Scope
{{scope_out}}

### Time Horizon
{{time_horizon}}

---

## 5. Stakeholders

<!-- GUIDANCE:
  List all key stakeholders, their roles, concerns, and level of engagement.
  This feeds directly into the Stakeholder Map artifact.
-->

| Stakeholder | Role | Concerns | Engagement Level |
|---|---|---|---|
| {{stakeholder_1}} | {{role_1}} | {{concerns_1}} | Informed / Consulted / Responsible |
| {{stakeholder_2}} | {{role_2}} | {{concerns_2}} | Informed / Consulted / Responsible |

---

## 6. Architecture Principles

<!-- GUIDANCE:
  List the governing principles that will guide architecture decisions.
  These should be agreed with the sponsor and documented in the Architecture Principles artifact.
  Reference the Architecture Principles artifact here rather than duplicating.
-->

Key principles governing this engagement are defined in the **Architecture Principles** artifact.

Summary:
{{architecture_principles_summary}}

---

## 7. Constraints

<!-- GUIDANCE:
  List constraints that must be respected — regulatory, technical, financial, or political.
  Distinguish between hard constraints (non-negotiable) and soft constraints (preferences).
-->

| Constraint | Type | Impact |
|---|---|---|
| {{constraint_1}} | Hard / Soft | {{impact_1}} |

---

## 8. Assumptions

<!-- GUIDANCE:
  List the assumptions being made. These should be validated and updated throughout the engagement.
-->

{{assumptions}}

---

## 9. High-Level Target Architecture

<!-- GUIDANCE:
  A high-level description of the target state architecture. This should be visual where possible.
  Reference diagrams stored in the diagrams/ folder. Avoid detailed design at this stage.
-->

{{target_architecture_description}}

*Reference diagram:* `../diagrams/{{diagram_filename}}`

---

## 10. Key Risks

<!-- GUIDANCE:
  Identify the top 3-5 risks to the architecture or engagement. Include mitigation approaches.
-->

| Risk | Likelihood | Impact | Mitigation |
|---|---|---|---|
| {{risk_1}} | High/Med/Low | High/Med/Low | {{mitigation_1}} |

---

## 11. Next Steps

<!-- GUIDANCE:
  List the immediate next steps following approval of this document.
  Typically: approve Statement of Architecture Work, proceed to Phase B/C/D.
-->

{{next_steps}}

---

*This document was created using the EA Assistant plugin.*
*Sections marked ⚠️ are unanswered. Sections marked 🤖 contain AI-suggested content requiring review.*
