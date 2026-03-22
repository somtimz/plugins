---
artifact: Business Architecture
engagement: {{engagement_name}}
phase: B
status: Draft
reviewStatus: Not Reviewed
version: 0.1
lastModified: {{YYYY-MM-DD}}
---

<!-- GUIDANCE:
  The Business Architecture describes the business strategy, governance, organisation, and
  key business processes. It is the foundation for the Application and Technology architectures.
  Phase B takes Architecture Vision as its primary input.
-->

# Business Architecture

**Engagement:** {{engagement_name}}
**Organisation:** {{organisation}}
**Date:** {{YYYY-MM-DD}}

---

## 1. Business Context

<!-- GUIDANCE:
  Describe the business context: industry, operating model, strategic direction.
  Reference the Architecture Vision for strategic goals.
-->

{{business_context}}

---

## 2. Organisation Model

<!-- GUIDANCE:
  Describe the organisational structure relevant to this architecture.
  Include a diagram reference if available.
-->

{{organisation_model}}

*Reference diagram:* `../diagrams/{{org_diagram}}`

---

## 3. Business Capabilities

<!-- GUIDANCE:
  List the business capabilities relevant to this engagement.
  A capability is an ability to achieve a business outcome, not a process or function.
  Use ArchiMate Capability elements from the Strategy layer.
-->

| Capability | Description | Current Maturity | Target Maturity |
|---|---|---|---|
| {{capability_1}} | {{description}} | Initial/Developing/Defined/Managed | {{target}} |

---

## 4. Business Processes

<!-- GUIDANCE:
  Describe the key business processes in scope.
  Map to capabilities above. Include process diagrams in diagrams/ folder.
-->

### {{process_name}}

- **Purpose:** {{purpose}}
- **Trigger:** {{trigger}}
- **Inputs:** {{inputs}}
- **Outputs:** {{outputs}}
- **Actors:** {{actors}}
- **Diagram:** `../diagrams/{{process_diagram}}`

---

## 5. Business Services

<!-- GUIDANCE:
  List the business services delivered by the organisation.
  A business service is an explicitly defined exposed behaviour.
-->

| Service | Description | Consumer | Provider |
|---|---|---|---|
| {{service_1}} | {{description}} | {{consumer}} | {{provider}} |

---

## 6. Business Information / Data Objects

<!-- GUIDANCE:
  Key business information objects used and produced by the business processes.
  These feed into the Data Architecture in Phase C.
-->

| Information Object | Description | Owner | Sensitivity |
|---|---|---|---|
| {{object_1}} | {{description}} | {{owner}} | Public/Internal/Confidential |

---

## 7. Gap Analysis

<!-- GUIDANCE:
  Compare the current state business architecture with the target state.
  Identify gaps that need to be addressed in the solution architecture.
-->

| Gap | Current State | Target State | Impact |
|---|---|---|---|
| {{gap_1}} | {{current}} | {{target}} | High/Med/Low |

---

## 8. Requirements Addressed

<!-- GUIDANCE:
  List requirements from the Requirements Register that this artifact addresses.
-->

| Req ID | Requirement | How Addressed |
|---|---|---|
| {{req_id}} | {{requirement}} | {{how}} |

---

*This document was created using the EA Assistant plugin.*
