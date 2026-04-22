# ISO 27001:2022 Control Reference

## 1. Overview

ISO 27001:2022 is the international standard for Information Security Management Systems (ISMS). Annex A contains 93 controls organised into 4 themes (domains). The 2022 revision reduced the control count from 114 (2013 edition) and introduced 11 new controls covering cloud security, threat intelligence, data masking, and ICT readiness for business continuity.

The standard requires organisations to select applicable controls, document exclusions, and maintain a Statement of Applicability (SoA). In TOGAF terms, this maps to Phase G compliance work. Controls in Annex A are not prescriptive on implementation — the ISMS determines how each control is realised, which is where security architecture decisions live.

## 2. Control Domain Mapping

| Domain | Controls | TOGAF Artifact | SABSA Layer | Representative Controls |
|---|---|---|---|---|
| A.5 Organisational controls | 37 | Architecture Principles, Governance Framework | Contextual / Conceptual | A.5.1 (Policies for information security), A.5.9 (Inventory of information and other assets), A.5.15 (Access control), A.5.23 (Information security for use of cloud services) |
| A.6 People controls | 8 | Business Architecture (roles), Statement of Architecture Work | Contextual | A.6.1 (Screening), A.6.2 (Terms and conditions of employment), A.6.3 (Information security awareness, education and training), A.6.5 (Responsibilities after termination or change of employment) |
| A.7 Physical controls | 14 | Technology Architecture | Physical | A.7.1 (Physical security perimeters), A.7.4 (Physical security monitoring), A.7.8 (Equipment siting and protection), A.7.14 (Secure disposal or re-use of equipment) |
| A.8 Technological controls | 34 | Application Architecture, Data Architecture, Technology Architecture | Logical / Physical | A.8.2 (Privileged access rights), A.8.5 (Secure authentication), A.8.10 (Information deletion), A.8.24 (Use of cryptography), A.8.28 (Secure coding) |

### A.5 Organisational Controls (37 controls)

Covers governance, policy, roles, asset management, supplier relationships, incident management, and cloud security. This is the broadest domain and primarily informs Architecture Principles (security governance policies) and the Governance Framework (security roles, incident management process, supplier security obligations).

Key controls for architecture work:
- **A.5.1** — Policies for information security: drives Architecture Principles (security section)
- **A.5.9** — Inventory of information and other assets: drives Business Architecture (asset register) and Data Architecture (data inventory)
- **A.5.10** — Acceptable use of information and other assets: informs Application Architecture (user policy enforcement)
- **A.5.15** — Access control: drives Application Architecture (auth/authz model) and Data Architecture (classification-based access)
- **A.5.23** — Information security for use of cloud services: drives Technology Architecture (cloud security controls)
- **A.5.24** — Information security incident management planning and preparation: drives Phase G Implementation Governance Plan

### A.6 People Controls (8 controls)

Covers pre-employment screening, employment terms, awareness training, disciplinary process, remote working, and termination. Primarily informs Business Architecture (HR security roles and responsibilities) and the Statement of Architecture Work (people-related security obligations).

### A.7 Physical Controls (14 controls)

Covers physical perimeters, entry controls, office security, clear desk/screen, equipment siting, cabling, maintenance, disposal, and unattended equipment. Primarily informs Technology Architecture (data centre and infrastructure physical security).

### A.8 Technological Controls (34 controls)

The largest technological domain. Covers privileged access, least privilege, secure authentication, malware protection, backup, logging, network security, web filtering, cryptography, secure development, and vulnerability management. Informs Application Architecture, Data Architecture, and Technology Architecture with specific technical control requirements.

Key controls for architecture work:
- **A.8.2** — Privileged access rights: drives Application Architecture (PAM model)
- **A.8.5** — Secure authentication: drives Application Architecture (MFA, SSO, federated identity)
- **A.8.8** — Management of technical vulnerabilities: drives Technology Architecture (patch management, vulnerability scanning)
- **A.8.10** — Information deletion: drives Data Architecture (retention and deletion policy)
- **A.8.15** — Logging: drives Application and Technology Architecture (audit logging requirements)
- **A.8.24** — Use of cryptography: drives Data Architecture (encryption at rest/in transit) and Technology Architecture (PKI)
- **A.8.28** — Secure coding: drives Application Architecture (SSDLC requirements)

## 3. REQ-NNN Tagging Guidance

Security requirements derived from ISO 27001 controls should be captured in the Requirements Register with consistent tagging to enable traceability from control to architecture decision:

- `type: security`
- `source: ISO27001`
- `control: A.X.Y` (the specific Annex A control number)

**Examples:**

| REQ-NNN | Description | type | source | control |
|---|---|---|---|---|
| REQ-042 | All data at rest in the customer data store must be encrypted using AES-256 | security | ISO27001 | A.8.24 |
| REQ-043 | All privileged access to production systems must use MFA and be logged with a 90-day retention period | security | ISO27001 | A.8.2, A.8.5, A.8.15 |
| REQ-044 | Personal data must be deleted within 30 days of the retention period expiry, with deletion confirmed in audit logs | security | ISO27001 | A.8.10 |

Multiple controls may apply to a single requirement — list all in the `control` field as a comma-separated list.

## 4. Statement of Applicability

ISO 27001 requires every certified organisation to maintain a Statement of Applicability (SoA) — a document that lists all 93 Annex A controls, states whether each is applicable or excluded, provides justification for exclusions, and describes how applicable controls are implemented.

In TOGAF terms, the SoA maps to the **Compliance Assessment** artifact produced in Phase G. The Compliance Assessment should:

- Reference the SoA directly if one exists (upload to `ResearchAndReferences/`)
- For each ISO 27001 domain, confirm which TOGAF artifacts address the relevant controls
- Flag any controls marked "not applicable" that the security architect believes should be included (raise as RIS-NNN)
- Record the implementation status of each control as a Phase G compliance checkpoint

Where no formal ISMS exists, the architecture team should produce a draft SoA as part of the Architecture Roadmap, with full SoA completion as a security work package (WP-NNN).
