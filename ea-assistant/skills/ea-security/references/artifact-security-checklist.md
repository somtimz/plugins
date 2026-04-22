# Artifact Security Checklist

Per-artifact security control checklist for use by ea-security-auditor, /ea-security-review, and /ea-grill with a security focus. Use checkbox format for review output. Severity hints: **(Critical)** = blocking gap; **(Warning)** = should be addressed before approval.

---

## Architecture Vision

- [ ] Security drivers are identified and recorded as DRV-NNN (type:security) **(Critical)**
- [ ] Security stakeholders are named — at minimum CISO or equivalent and DPO where personal data is in scope **(Critical)**
- [ ] Top-level security risks are summarised with references to RIS-NNN entries **(Warning)**
- [ ] Security principles are referenced or a placeholder confirms they will be defined in the Preliminary phase **(Warning)**
- [ ] Regulatory and compliance obligations are listed (e.g., GDPR, PCI-DSS, ISO 27001, sector-specific) **(Critical)**
- [ ] Security constraints on the architecture scope are documented (e.g., must not process data outside jurisdiction X) **(Warning)**

---

## Stakeholder Map

- [ ] CISO (or equivalent security authority) is present with a named individual or role **(Critical)**
- [ ] DPO is present where the engagement involves personal data processing **(Warning)**
- [ ] Security architect role is defined (internal or external) **(Warning)**
- [ ] Security authority level is mapped — who can approve security exceptions? **(Warning)**
- [ ] Compliance officer or risk committee is referenced where ISO 27001 or regulated frameworks apply **(Warning)**

---

## Architecture Principles

- [ ] A dedicated security principles section is present **(Critical)**
- [ ] At least one principle addresses the Contextual SABSA layer (business security vision or governance) **(Warning)**
- [ ] At least one principle addresses the Conceptual SABSA layer (security policy or access control philosophy) **(Warning)**
- [ ] Principles are testable — each has a statement, rationale, and implication **(Warning)**
- [ ] Privacy by design is referenced as a principle where personal data is in scope **(Warning)**
- [ ] Principle conflicts with other architectural concerns are noted (e.g., security vs. usability) **(Warning)**

---

## Business Architecture

- [ ] Security roles and responsibilities are defined (RACI or equivalent) **(Warning)**
- [ ] Security policy references are present — policies that govern this business domain **(Warning)**
- [ ] Business security attributes (BSAs) are identified from the SABSA model **(Warning)**
- [ ] Security-sensitive business processes are flagged **(Warning)**
- [ ] HR security obligations (A.6 people controls) are addressed — screening, awareness, termination **(Warning)**
- [ ] Supply chain or third-party security obligations are identified where relevant **(Warning)**

---

## Data Architecture

- [ ] Data classification scheme is defined with at least two sensitivity levels **(Critical)**
- [ ] Encryption at rest is specified for each classification level that requires it **(Critical)**
- [ ] Encryption in transit is specified (TLS version, certificate requirements) **(Critical)**
- [ ] Data retention and deletion policy is documented with obligation source **(Warning)**
- [ ] Privacy requirements are captured as REQ-NNN (type:security, category:data-protection) **(Critical)** where personal data is in scope
- [ ] Data residency or jurisdiction constraints are documented **(Warning)**

---

## Application Architecture

- [ ] Authentication model is defined (e.g., SSO, MFA, federated identity, protocol) **(Critical)**
- [ ] Authorisation model is defined (RBAC, ABAC, policy-based) with a rationale **(Critical)**
- [ ] API security controls are specified (OAuth 2.0, mTLS, API gateway policy) **(Warning)**
- [ ] Audit logging requirements are captured as REQ-NNN (type:security) with retention period **(Warning)**
- [ ] Vulnerability management approach is referenced (SSDLC, DAST/SAST, penetration testing) **(Warning)**
- [ ] Secure coding standards are referenced (e.g., OWASP, A.8.28) **(Warning)**

---

## Technology Architecture

- [ ] Network segmentation model is defined (zones, DMZ, micro-segmentation approach) **(Critical)**
- [ ] PKI and certificate management approach is documented **(Warning)**
- [ ] Endpoint hardening standards are referenced (CIS Benchmarks or equivalent) **(Warning)**
- [ ] Security monitoring and SIEM are specified (tools, log sources, alerting) **(Warning)**
- [ ] Backup and recovery controls are documented with RTO/RPO targets **(Warning)**
- [ ] Physical security controls are referenced for infrastructure components **(Warning)**

---

## Requirements Register

- [ ] At least one security REQ-NNN is present **(Critical)**
- [ ] All security requirements are tagged type:security **(Critical)**
- [ ] ISO 27001 and/or NIST CSF source references are present on security REQs **(Warning)**
- [ ] Security requirements are traceable to a DRV-NNN or RIS-NNN **(Warning)**
- [ ] No security requirements are captured only in artifact body text (must be in the register) **(Warning)**

---

## Risk Register

- [ ] Security risks are classified with a security category label **(Critical)**
- [ ] Each security risk has a RIS-NNN entry with likelihood, impact, and risk rating **(Critical)**
- [ ] Mitigation owners are assigned for all Critical-rated security risks **(Critical)**
- [ ] Accepted risks have a documented rationale and an approval authority named **(Warning)**
- [ ] Risks are reviewed for NIST CSF function coverage (ID, PR, DE, RS, RC) **(Warning)**

---

## Architecture Roadmap

- [ ] Security work packages (WP-NNN) are present and clearly labelled **(Warning)**
- [ ] Security milestones are sequenced before dependent business capabilities where security is an enabler **(Warning)**
- [ ] Foundational security controls (IAM, network segmentation) appear in early iterations **(Warning)**
- [ ] Security debt items from Gap Analysis are reflected as roadmap entries **(Warning)**
- [ ] Security work packages reference the ISO 27001 controls or NIST CSF functions they address **(Warning)**

---

## Compliance Assessment (Phase G)

- [ ] All four ISO 27001:2022 domains (A.5–A.8) are addressed **(Critical)**
- [ ] All six NIST CSF 2.0 functions (GV, ID, PR, DE, RS, RC) are addressed **(Critical)**
- [ ] SABSA Operational layer deliverables are present (SOC model, incident response, security governance) **(Warning)**
- [ ] Statement of Applicability (SoA) is referenced or produced as an output **(Critical)** where ISO 27001 certification is in scope
- [ ] Compliance gaps are documented with remediation owners and target dates **(Critical)**
- [ ] Security architecture sign-off authority is identified **(Warning)**
