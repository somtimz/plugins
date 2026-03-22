---
artifact: Technology Architecture
engagement: {{engagement_name}}
phase: D
status: Draft
reviewStatus: Not Reviewed
version: 0.1
lastModified: {{YYYY-MM-DD}}
---

<!-- GUIDANCE:
  The Technology Architecture is the Phase D artifact describing the technology platforms,
  infrastructure components, and standards that host and connect the application and data
  layers. It translates application requirements into infrastructure and platform decisions.
  Technology Architecture should be driven by the Application Architecture outputs, not by
  technology preferences alone. It must address security, resilience, and operational concerns.
-->

# Technology Architecture

**Engagement:** {{engagement_name}}
**Organisation:** {{organisation}}
**Date:** {{YYYY-MM-DD}}

---

## 1. Technology Context

<!-- GUIDANCE:
  Describe the current technology environment and the strategic context for technology decisions.
  Include: existing infrastructure estate (on-premise, cloud, hybrid), organisational cloud
  strategy and maturity, constraints from existing contracts or vendor relationships, and any
  mandated technology standards from the enterprise or regulatory body.
-->

{{technology_context}}

---

## 2. Technology Standards

<!-- GUIDANCE:
  Document the agreed technology standards for this engagement. Standards constrain and guide
  technology choices throughout implementation. Distinguish between mandatory standards
  (must be followed) and preferred standards (default choice, deviation requires justification).
  Include standards for compute, storage, networking, middleware, security, and observability.
-->

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

<!-- GUIDANCE:
  Catalogue the key infrastructure components in the target state. For each component, describe
  its role, the platform or product used, deployment model, and sizing considerations. Use
  ArchiMate Technology layer elements (Node, Device, System Software) where applicable.
  Include a target infrastructure diagram.
-->

*Reference diagram:* `../diagrams/{{infrastructure_diagram}}`

| Component ID | Component | Role | Platform / Product | Deployment Model | Resilience |
|---|---|---|---|---|---|
| INF-001 | {{component}} | {{role}} | {{platform}} | On-premise / IaaS / PaaS / SaaS | Active-Active / Active-Passive / Single |
| INF-002 | {{component}} | {{role}} | {{platform}} | On-premise / IaaS / PaaS / SaaS | Active-Active / Active-Passive / Single |

### Hosting Model
{{hosting_model_description}}

### Disaster Recovery and Resilience
<!-- GUIDANCE:
  Describe the DR strategy: RTO (Recovery Time Objective), RPO (Recovery Point Objective),
  and the mechanism used (warm standby, pilot light, multi-region active-active, backup/restore).
-->

| Service Tier | RTO | RPO | DR Mechanism |
|---|---|---|---|
| {{tier_1}} | {{rto}} | {{rpo}} | {{mechanism}} |

---

## 4. Network Architecture

<!-- GUIDANCE:
  Describe the network topology, segmentation model, and connectivity approach. Include:
  network zones (DMZ, internal, management), connectivity to cloud providers or external
  parties, VPN/private connectivity, DNS, and load balancing strategy.
  Include a network diagram reference.
-->

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

<!-- GUIDANCE:
  Describe the security controls and patterns applied in the technology architecture. Cover:
  identity and access management (IAM), network security (firewalls, WAF, DDoS protection),
  data protection at rest and in transit, secrets management, vulnerability management, and
  compliance with relevant security standards (ISO 27001, SOC 2, NIST CSF, etc.).
  Security architecture should be reviewed by a security specialist.
-->

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

<!-- GUIDANCE:
  Summarise technology architecture gaps between the current estate and the target state.
  Common technology gaps: end-of-life platforms, missing observability, inadequate DR posture,
  inconsistent security controls, unsupported or vendor lock-in risks.
  Reference the full Gap Analysis artifact for detail.
-->

*See Gap Analysis artifact for full detail:* `gap-analysis.md`

| Gap ID | Description | Priority | Impact |
|---|---|---|---|
| GAP-001 | {{description}} | High / Med / Low | {{impact}} |

---

## 7. Requirements Addressed

<!-- GUIDANCE:
  Trace technology decisions back to requirements from the Requirements Register.
  Non-functional requirements (performance, availability, security, scalability) are especially
  important to trace here, as they most directly shape technology choices.
-->

| Req ID | Requirement | How Addressed |
|---|---|---|
| {{req_id}} | {{requirement}} | {{how}} |

---

*This document was created using the EA Assistant plugin.*
