---
artifact: Technology Architecture
engagement: {{engagement_name}}
phase: D
status: Draft
reviewStatus: Not Reviewed
version: 0.1
lastModified: {{YYYY-MM-DD}}
taxonomy:
  domain: Technology
  category: Design
  audience: Architecture
  layer: Target
  sensitivity: Internal
  tags: [infrastructure, platforms, technology, phase-d]
---

<details>
<summary>📋 Guidance</summary>

The Technology Architecture is the Phase D artifact describing the technology platforms,
infrastructure components, and standards that host and connect the application and data
layers. It translates application requirements into infrastructure and platform decisions.
Technology Architecture should be driven by the Application Architecture outputs, not by
technology preferences alone. It must address security, resilience, and operational concerns.

</details>

# Technology Architecture

**Engagement:** {{engagement_name}}
**Organisation:** {{organisation}}
**Date:** {{YYYY-MM-DD}}

---

## 1. Technology Context

<details>
<summary>📋 Guidance</summary>

Describe the current technology environment and the strategic context for technology decisions.
Include: existing infrastructure estate (on-premise, cloud, hybrid), organisational cloud
strategy and maturity, constraints from existing contracts or vendor relationships, and any
mandated technology standards from the enterprise or regulatory body.

</details>

{{technology_context}}

---

## 2. Technology Standards

<details>
<summary>📋 Guidance</summary>

Document the agreed technology standards for this engagement. Standards constrain and guide
technology choices throughout implementation. Distinguish between mandatory standards
(must be followed) and preferred standards (default choice, deviation requires justification).
Include standards for compute, storage, networking, middleware, security, and observability.

</details>

| Category | Standard | Mandatory / Preferred | Rationale |
|---|---|---|---|
| Compute | {{standard}} | Mandatory / Preferred | {{rationale}} |
| Storage | {{standard}} | Mandatory / Preferred | {{rationale}} |
| Networking | {{standard}} | Mandatory / Preferred | {{rationale}} |
| Identity & Access | {{standard}} | Mandatory / Preferred | {{rationale}} |
| Observability | {{standard}} | Mandatory / Preferred | {{rationale}} |
| {{category}} | {{standard}} | Mandatory / Preferred | {{rationale}} |

---

## 3. Infrastructure Components

<details>
<summary>📋 Guidance</summary>

Catalogue the key infrastructure components in the target state. For each component, describe
its role, the platform or product used, deployment model, and sizing considerations. Use
ArchiMate Technology layer elements (Node, Device, System Software) where applicable.
Include a target infrastructure diagram.

</details>

*Reference diagram:* `../diagrams/{{infrastructure_diagram}}`

| Component ID | Component | Role | Platform / Product | Deployment Model | Resilience |
|---|---|---|---|---|---|
| INF-001 | {{component}} | {{role}} | {{platform}} | On-premise / IaaS / PaaS / SaaS | Active-Active / Active-Passive / Single |
| INF-002 | {{component}} | {{role}} | {{platform}} | On-premise / IaaS / PaaS / SaaS | Active-Active / Active-Passive / Single |

### Hosting Model
{{hosting_model_description}}

### Disaster Recovery and Resilience
<details>
<summary>📋 Guidance</summary>

Describe the DR strategy: RTO (Recovery Time Objective), RPO (Recovery Point Objective),
and the mechanism used (warm standby, pilot light, multi-region active-active, backup/restore).

</details>

| Service Tier | RTO | RPO | DR Mechanism |
|---|---|---|---|
| {{tier_1}} | {{rto}} | {{rpo}} | {{mechanism}} |

---

## 4. Network Architecture

<details>
<summary>📋 Guidance</summary>

Describe the network topology, segmentation model, and connectivity approach. Include:
network zones (DMZ, internal, management), connectivity to cloud providers or external
parties, VPN/private connectivity, DNS, and load balancing strategy.
Include a network diagram reference.

</details>

*Reference diagram:* `../diagrams/{{network_diagram}}`

### Network Zones
| Zone | Purpose | Trust Level | Key Components |
|---|---|---|---|
| {{zone_1}} | {{purpose}} | High / Medium / Low / Untrusted | {{components}} |
| {{zone_2}} | {{purpose}} | High / Medium / Low / Untrusted | {{components}} |

### Connectivity
{{connectivity_description}}

---

## 5. Security Architecture

<details>
<summary>📋 Guidance</summary>

Describe the security controls and patterns applied in the technology architecture. Cover:
identity and access management (IAM), network security (firewalls, WAF, DDoS protection),
data protection at rest and in transit, secrets management, vulnerability management, and
compliance with relevant security standards (ISO 27001, SOC 2, NIST CSF, etc.).
Security architecture should be reviewed by a security specialist.

</details>

### Identity and Access Management
{{iam_description}}

### Network Security Controls
| Control | Implementation | Applies To |
|---|---|---|
| {{control_1}} | {{implementation_1}} | {{scope_1}} |
| {{control_2}} | {{implementation_2}} | {{scope_2}} |

### Data Protection
{{data_protection_description}}

### Security Standards and Compliance
| Standard | Applicability | Status |
|---|---|---|
| {{standard_1}} | {{applicability_1}} | Compliant / In Progress / Gap |
| {{standard_2}} | {{applicability_2}} | Compliant / In Progress / Gap |

---

## 6. Gap Analysis

<details>
<summary>📋 Guidance</summary>

Summarise technology architecture gaps between the current estate and the target state.
Common technology gaps: end-of-life platforms, missing observability, inadequate DR posture,
inconsistent security controls, unsupported or vendor lock-in risks.
Reference the full Gap Analysis artifact for detail.

</details>

*See Gap Analysis artifact for full detail:* `gap-analysis.md`

| Gap ID | Description | Priority | Impact |
|---|---|---|---|
| GAP-001 | {{description}} | High / Med / Low | {{impact}} |

---

## 7. Requirements Addressed

<details>
<summary>📋 Guidance</summary>

Trace technology decisions back to requirements from the Requirements Register.
Non-functional requirements (performance, availability, security, scalability) are especially
important to trace here, as they most directly shape technology choices.

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
