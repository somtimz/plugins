# SABSA to TOGAF ADM Mapping

## 1. SABSA Layer Overview

SABSA (Sherwood Applied Business Security Architecture) is a risk-driven security architecture framework structured in six layers that mirror the business concerns from contextual motivation down to operational execution. Each layer answers a different question about the security architecture.

| SABSA Layer | Interrogative | Focus | Security Architect Role |
|---|---|---|---|
| Contextual (Why) | Why? | Business context, risk drivers, regulatory obligations | Elicit business security requirements from executive stakeholders; define security vision |
| Conceptual (What) | What? | Security policies, principles, business security attributes | Define security policies and attribute model; establish measurable security properties |
| Logical (How) | How? | Security services, identity and access management, data classification | Design the logical security model; specify auth/authz, audit, and data protection services |
| Physical (With What) | With What? | Security mechanisms, technologies, network controls, cryptography | Select security technologies; specify PKI, segmentation, encryption, and endpoint standards |
| Component (Which) | Which? | Specific products, versions, configurations, implementation packages | Identify and sequence security work packages; select certified products and configurations |
| Operational (When/Who) | When? Who? | Security operations, governance, monitoring, incident response | Define the operating model; establish SOC, compliance monitoring, and ISMS governance |

## 2. SABSA to ADM Phase Mapping

| SABSA Layer | ADM Phase | Security Architecture Deliverable | Key Questions |
|---|---|---|---|
| Contextual (Why) | Prelim / Phase A | Security vision, business security attributes, security drivers (DRV-NNN type:security) | Why does security matter to this business? What are the regulatory drivers? |
| Conceptual (What) | Phase B | Security policies, security principles, business security architecture, business security attributes model | What are the security policies? What security standards apply? |
| Logical (How) | Phase C (Data + App) | Security services, data classification scheme, auth/authz model, audit logging requirements | How will identity and access be managed? How is data classified and protected? |
| Physical (With What) | Phase D | Security mechanisms, PKI, network segmentation, endpoint hardening, encryption at rest/in transit | What security products/technologies implement the logical model? |
| Component (Which) | Phase E–F | Security product/tool selection, implementation sequence, security work packages (WP-NNN) | Which specific products, versions, and configurations? |
| Operational (When/Who) | Phase G | Security operations model, monitoring, incident response, security governance, compliance assessment | Who operates security? When are controls verified? |

## 3. Business Security Attributes

Business Security Attributes (BSAs) are the core of SABSA's requirement methodology. A BSA is a measurable property that the business requires its security architecture to deliver. BSAs are derived from business risk analysis and form the traceability chain from business need to security mechanism: business risk → BSA → security service → security mechanism.

BSAs are not generic security goals — they are specific, measurable, and agreed with business stakeholders. Each BSA should have a metric (how it is measured) and a target level.

| Business Security Attribute | Definition |
|---|---|
| Confidentiality | Information is accessible only to those authorised to access it |
| Integrity | Information and system states are protected from unauthorised modification |
| Availability | Systems and information are accessible when required by authorised users |
| Auditability | All security-relevant actions are logged, attributable, and reviewable |
| Accountability | Individuals and systems can be held responsible for their actions |
| Non-repudiation | Actions or transactions cannot be denied after the fact by any party |
| Privacy | Personal data is collected, processed, and retained in accordance with regulatory obligations |
| Authenticity | The identity of users, systems, and data can be verified and trusted |
| Reliability | Security controls perform consistently under normal and adverse conditions |
| Resilience | The organisation can withstand, adapt to, and recover from security events |

## 4. Using SABSA with TOGAF

- **TOGAF provides process; SABSA provides content.** TOGAF's ADM defines when to do security architecture work (which phase, which artifacts). SABSA defines what the content of that work should be at each layer of abstraction.
- **Requirements traceability is the integration point.** SABSA's BSA model maps directly to TOGAF's Requirements Register: each BSA becomes one or more REQ-NNN entries (type:security), with the BSA as the source and the security service as the logical solution.
- **SABSA layers anchor artifact depth.** When producing a TOGAF artifact (e.g., Data Architecture), the SABSA layer (Logical) signals what level of detail is expected — security services and classification schemes, not product names or operational procedures.
- **Operational layer closes the TOGAF loop.** SABSA's Operational layer (Phase G) is the point at which the security architecture becomes a live ISMS. TOGAF's Compliance Assessment and Implementation Governance Plan are the primary vehicles for this handover.
