---
artifact: Business Architecture
engagement: {{engagement_name}}
phase: B
status: Draft
reviewStatus: Not Reviewed
version: 0.1
lastModified: {{YYYY-MM-DD}}
---

<details>
<summary>📋 Guidance</summary>

The Business Architecture describes the business strategy, governance, organisation, and
key business processes. It is the foundation for the Application and Technology architectures.
Phase B takes Architecture Vision as its primary input.

</details>

# Business Architecture

**Engagement:** {{engagement_name}}
**Organisation:** {{organisation}}
**Date:** {{YYYY-MM-DD}}

---

## 1. Business Context

<details>
<summary>📋 Guidance</summary>

Describe the business context: industry, operating model, strategic direction.
Reference the Architecture Vision for strategic goals.

</details>

{{business_context}}

---

## 2. Organisation Model

<details>
<summary>📋 Guidance</summary>

Describe the organisational structure relevant to this architecture.
Include a diagram reference if available.

</details>

{{organisation_model}}

*Reference diagram:* `../diagrams/{{org_diagram}}`

---

## 3. Business Capabilities

<details>
<summary>📋 Guidance</summary>

List the business capabilities relevant to this engagement.
A capability is an ability to achieve a business outcome, not a process or function.
Use ArchiMate Capability elements from the Strategy layer.

</details>

| Capability | Description | Current Maturity | Target Maturity |
|---|---|---|---|
| {{capability_1}} | {{description}} | Initial/Developing/Defined/Managed | {{target}} |

---

## 4. Business Processes

<details>
<summary>📋 Guidance</summary>

Describe the key business processes in scope.
Map to capabilities above. Include process diagrams in diagrams/ folder.

</details>

### {{process_name}}

- **Purpose:** {{purpose}}
- **Trigger:** {{trigger}}
- **Inputs:** {{inputs}}
- **Outputs:** {{outputs}}
- **Actors:** {{actors}}
- **Diagram:** `../diagrams/{{process_diagram}}`

---

## 5. Business Services

<details>
<summary>📋 Guidance</summary>

List the business services delivered by the organisation.
A business service is an explicitly defined exposed behaviour.

</details>

| Service | Description | Consumer | Provider |
|---|---|---|---|
| {{service_1}} | {{description}} | {{consumer}} | {{provider}} |

---

## 6. Business Information / Data Objects

<details>
<summary>📋 Guidance</summary>

Key business information objects used and produced by the business processes.
These feed into the Data Architecture in Phase C.

</details>

| Information Object | Description | Owner | Sensitivity |
|---|---|---|---|
| {{object_1}} | {{description}} | {{owner}} | Public/Internal/Confidential |

---

## 7. Gap Analysis

<details>
<summary>📋 Guidance</summary>

Compare the current state business architecture with the target state.
Identify gaps that need to be addressed in the solution architecture.

</details>

| Gap | Current State | Target State | Impact |
|---|---|---|---|
| {{gap_1}} | {{current}} | {{target}} | High/Med/Low |

---

## 8. Requirements Addressed

<details>
<summary>📋 Guidance</summary>

List requirements from the Requirements Register that this artifact addresses.

</details>

| Req ID | Requirement | How Addressed |
|---|---|---|
| {{req_id}} | {{requirement}} | {{how}} |

---

---

## Appendix A3 — Decision Log

<details>
<summary>📋 Guidance</summary>

Record all decisions made during the development of this artifact.
Use /ea-decisions to aggregate this table across all artifacts into a Decision Register.

</details>

| Item | Value | State | Captured By | Owner | Authority | Domain | Cost | Impact | Risk | Subject | Date |
|---|---|---|---|---|---|---|---|---|---|---|---|
| *(no decisions recorded)* | — | — | — | — | — | — | — | — | — | — | — |

---

## Appendix A4 — Stakeholder Concerns & Objections

<details>
<summary>📋 Guidance</summary>

Record all stakeholder concerns, objections, and tough questions raised about this artifact.
Sources include grill-me sessions, Architecture Review Board feedback, executive challenge
sessions, and sponsor meetings. For each concern, record whether it is addressed in existing
documentation (Addressed / Partially Addressed) or requires further action (Requires Attention).
Use `/ea-concerns` to aggregate unresolved items across all artifacts. Concerns that represent
a material risk should also be raised as RIS-NNN entries via `/ea-risks`.

</details>

| ID | Concern | Raised By | Category | Status | Response | Action / Owner |
|---|---|---|---|---|---|---|
| *(no concerns recorded)* | — | — | — | — | — | — |

---

*This document was created using the EA Assistant plugin.*
*Use `/ea-decisions` to generate a cross-artifact Decision Register from all A3 tables.*
*Use `/ea-concerns` to generate a cross-artifact Concerns Register from all A4 tables.*
