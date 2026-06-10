# Security Interview Questions

Phase-by-phase optional security question bank for ea-interviewer. Load this file when an engagement has security drivers (DRV-NNN type:security) or when the user requests a security-focused interview session. Questions are supplementary to the standard phase interview questions — select the most relevant 2-4 per session rather than asking all.

---

## Preliminary Phase

**SABSA focus:** Contextual — governance, obligations, and existing security posture

**Questions:**

1. What security governance model applies to this organisation? (e.g., CISO-led, committee-based, outsourced)
2. Who holds security decision authority — who can approve exceptions, set policy, and sign off on architecture security sections?
3. What security policies already exist? Are they current and enforced?
4. What compliance obligations apply? (e.g., GDPR, PCI-DSS, ISO 27001, HIPAA, sector regulation)
5. Is there an existing ISMS or security programme this engagement must align with?
6. What is the current security maturity tier? (NIST CSF: Partial / Risk Informed / Repeatable / Adaptive)

**Output routing:**

| Output | Artifact |
|---|---|
| Governance model and decision authority | Architecture Principles (security governance section) |
| Existing policies and compliance obligations | Governance Framework (security notes), DRV-NNN (type:security) |
| Current maturity tier | Architecture Vision (security baseline section) |

---

## Phase A — Architecture Vision

**SABSA focus:** Contextual — security vision, drivers, and top-level risk

**Questions:**

1. What are the primary security drivers for this engagement? Are they regulatory, contractual, or risk-driven?
2. Who are the security stakeholders? (CISO, DPO, compliance officer, risk committee, board audit committee)
3. What are the top 3 security risks at the engagement level? What keeps the CISO awake at night?
4. What security principles should constrain all downstream architecture decisions?
5. Is there an existing security architecture or security reference model that this engagement must align with?
6. Are there any known security incidents or breaches in this organisation's recent history that should inform the architecture?

**Output routing:**

| Output | Artifact |
|---|---|
| Security drivers | DRV-NNN (type:security) in Requirements Register |
| Security stakeholders | Stakeholder Map (security authority roles) |
| Top-level security risks | RIS-NNN (type:security, category:security) in Risk Register |
| Security principles | Architecture Principles (security section) |

---

## Phase B — Business Architecture

**SABSA focus:** Conceptual — security policies, business security attributes, organisational model

**Questions:**

1. What are the business security attributes required? (confidentiality, integrity, availability, auditability, accountability, non-repudiation — which matter most and why?)
2. What security policies govern this business domain? Are they documented and enforced?
3. How are security roles and responsibilities organised? Is there a clear RACI for security decisions?
4. What are the security-sensitive business processes — processes where a failure would cause regulatory, financial, or reputational harm?
5. What third-party or supply chain relationships introduce security risk?

**Output routing:**

| Output | Artifact |
|---|---|
| Business security attributes | Business Architecture (security section), REQ-NNN (type:security, source:business policy) |
| Security roles and RACI | Business Architecture (security RACI), Governance Framework |
| Security-sensitive processes | Business Architecture (process security notes), RIS-NNN |

---

## Phase C — Data Architecture

**SABSA focus:** Logical — data classification, protection services, and privacy obligations

**Questions:**

1. What data classification levels apply? (e.g., Public / Internal / Confidential / Restricted — or organisation-specific scheme)
2. What data is most sensitive or regulated? (personal data, payment data, health data, IP, classified)
3. What are the encryption requirements — at rest and in transit? Are there approved algorithms or key lengths?
4. What data retention and deletion obligations exist? What triggers deletion?
5. What privacy requirements apply? Is GDPR Article 25 (privacy by design and by default) a relevant obligation?
6. Where does data reside — jurisdiction constraints, cross-border transfer restrictions?

**Output routing:**

| Output | Artifact |
|---|---|
| Data classification scheme | Data Architecture (classification table) |
| Encryption at rest and in transit | Data Architecture (encryption specification), REQ-NNN (type:security, category:data-protection) |
| Retention and deletion | Data Architecture (retention policy), REQ-NNN (type:security, source:ISO27001, control:A.8.10) |
| Privacy requirements | Data Architecture (privacy notes), REQ-NNN (type:security, category:privacy) |

---

## Phase C — Application Architecture

**SABSA focus:** Logical — identity, access, audit, and secure development

**Questions:**

1. What authentication model is required? (SSO, MFA, federated identity, protocol: SAML / OIDC / Kerberos)
2. What authorisation model applies? (RBAC, ABAC, policy-based — what granularity of access control is needed?)
3. What audit logging is required? Who needs to see logs, for how long, and in what format?
4. How are APIs secured? (OAuth 2.0, mTLS, API gateway, rate limiting)
5. What are the secure coding standards for this application? (OWASP, SSDLC, code review requirements)
6. What is the approach to vulnerability management — SAST, DAST, penetration testing frequency?

**Output routing:**

| Output | Artifact |
|---|---|
| Authentication model | Application Architecture (auth model section), REQ-NNN (type:security, category:access-control) |
| Authorisation model | Application Architecture (authz model), REQ-NNN (type:security, source:ISO27001, control:A.5.15) |
| Audit logging | Application Architecture (logging requirements), REQ-NNN (type:security, source:ISO27001, control:A.8.15) |
| API security | Application Architecture (API security section) |

---

## Phase D — Technology Architecture

**SABSA focus:** Physical — security mechanisms, network controls, monitoring, and infrastructure

**Questions:**

1. What network segmentation model is required? (zones, DMZ, micro-segmentation, air-gapped segments)
2. What PKI and certificate management approach is used? (internal CA, public CA, certificate lifecycle)
3. What endpoint hardening standards apply? (CIS Benchmarks, vendor hardening guides, mobile device management)
4. What security monitoring and SIEM tools are in scope? What log sources are required?
5. What physical security controls apply to infrastructure? (data centre, co-location, cloud physical security)
6. What backup and recovery controls are required? (RTO, RPO, backup encryption, offsite storage)

**Output routing:**

| Output | Artifact |
|---|---|
| Network segmentation | Technology Architecture (network security section) |
| PKI and certificate management | Technology Architecture (PKI section), REQ-NNN (type:security, source:ISO27001, control:A.8.24) |
| SIEM and monitoring | Technology Architecture (monitoring section), RIS-NNN (infrastructure security risks) |
| Backup and recovery | Technology Architecture (resilience section), REQ-NNN (type:security, source:NIST-CSF, control:RC.RP) |

---

## Phase E — Gaps and Roadmap

**SABSA focus:** Component — security gap analysis and work package sequencing

**Questions:**

1. What security gaps have been identified against the target architecture?
2. Which security work packages are highest priority — what cannot go live without being addressed?
3. Are there security dependencies that constrain the roadmap sequence? (e.g., IAM must be in place before application migration)
4. What security products or tools are being selected to implement the Physical layer controls?
5. Are any security capabilities being deferred to a later iteration, and is that risk-accepted?

**Output routing:**

| Output | Artifact |
|---|---|
| Security gaps | Gap Analysis (security gaps section) |
| Security work packages | Architecture Roadmap (WP-NNN type:security) |
| Security dependencies | Architecture Roadmap (sequencing notes) |

---

## Phase F — Migration Planning

**SABSA focus:** Physical/Operational — securing the transition itself, not just the end state

**Questions:**

1. How is data protected during migration — encryption in transit, integrity verification, and handling of copies created for cutover?
2. What is the security posture during coexistence windows when old and new systems run in parallel? (duplicated attack surface, synchronised access revocation)
3. How are credentials, keys, and secrets rotated or re-issued as workloads move?
4. What is the secure decommissioning plan for legacy systems — data sanitisation, licence/account termination, certificate revocation?
5. Do migration vendors or partners get temporary privileged access, and how is it time-boxed and audited?
6. Is there a security go/no-go checkpoint per migration wave, and who owns it?

**Output routing:**

| Output | Artifact |
|---|---|
| Migration data protection | Migration Plan (security section), REQ-NNN (type:security) |
| Coexistence/cutover risks | Migration Plan risk table, RIS-NNN |
| Secrets rotation | Migration Plan (cutover runbook), REQ-NNN (type:security, source:ISO27001, control:A.8.24) |
| Decommissioning | Migration Plan (decommissioning section), GAP-M-NNN if unplanned |
| Third-party access | Migration Plan, CON-NNN if contested |

---

## Phase G — Implementation Governance

**SABSA focus:** Operational — security operations model, compliance, and incident management

**Questions:**

1. How will security compliance be assessed during implementation? Who performs the assessment?
2. Who is responsible for security operations once the architecture is live? (internal SOC, MSSP, hybrid)
3. What security monitoring and alerting is in place — or needs to be stood up — before go-live?
4. How are security incidents managed? Is there a tested incident response plan?
5. Is an ISO 27001 Statement of Applicability required? Who is responsible for maintaining it?
6. What are the security acceptance criteria for the Implementation Governance Plan — what must be true before sign-off?

**Output routing:**

| Output | Artifact |
|---|---|
| Compliance assessment approach | Compliance Assessment (Phase G artifact) |
| Security operations model | Implementation Governance Plan (security operations section) |
| Incident response | Governance Framework (incident management), Implementation Governance Plan |
| Statement of Applicability | Compliance Assessment (SoA reference or draft) |

---

## Phase H — Architecture Change Management

**SABSA focus:** Operational — keeping the security posture current as the architecture changes

**Questions:**

1. Does every Architecture Change Request (ACR) receive a security impact assessment, and who performs it?
2. What triggers a security re-assessment outside the change process — new threats, vendor advisories, regulatory change, incident learnings?
3. How is control drift detected — are deployed controls periodically verified against the documented architecture?
4. Are security policies (POL-NNN) and constraints (CST-NNN) on a review cycle, and what happens when one expires?
5. How do post-incident learnings feed back into Architecture Principles, standards, and the threat model?
6. When a change is classified as re-architecting, is the security architecture explicitly re-entered (Phase A security context refresh), or only the affected domain?

**Output routing:**

| Output | Artifact |
|---|---|
| ACR security assessment step | Change Request (security impact field), Governance Framework |
| Re-assessment triggers | Governance Framework (security review triggers) |
| Control drift checks | Compliance Assessment (recurring), RIS-NNN if drift found |
| Policy/constraint review cycle | Policies Register (reviewCycle), Constraints Register |
| Incident-learning feedback | Architecture Principles (revision), ADR-NNN if a decision is reversed |
