# NIST CSF 2.0 Reference

## 1. Overview

NIST Cybersecurity Framework 2.0 (CSF 2.0, released February 2024) is an outcome-based framework for managing cybersecurity risk. It is structured as 6 functions, 22 categories, and 106 subcategories. CSF 2.0 adds the Govern (GV) function — new in this version — which elevates cybersecurity governance to the top level, reflecting that cybersecurity risk is a business risk.

The framework is outcome-based and non-prescriptive: it describes what good looks like, not how to achieve it. Organisations map their existing controls and practices to the CSF to identify gaps and communicate maturity. CSF originated in US critical infrastructure sectors but is now widely adopted globally across both public and private sector organisations of all sizes.

CSF 2.0 explicitly maps to ISO 27001:2022, NIST SP 800-53, and other control frameworks, making it a useful integration layer when multiple compliance obligations apply to an engagement.

## 2. Function Mapping

| Function | Core Question | ADM Phase | TOGAF Artifact | ISO 27001 Alignment |
|---|---|---|---|---|
| GV — Govern | How is cybersecurity risk managed and communicated across the organisation? | Prelim / A | Governance Framework, Architecture Principles | A.5.1, A.5.35, A.5.36 |
| ID — Identify | What assets, vulnerabilities, and risks exist? | A–B | Architecture Vision (risks), Business Architecture (assets), Requirements Register | A.5.9, A.5.12, A.8.8 |
| PR — Protect | What safeguards are in place to limit the impact of a cybersecurity event? | C–D | Application Architecture, Data Architecture, Technology Architecture (controls) | A.8.2, A.8.5, A.8.24, A.7.1 |
| DE — Detect | How are cybersecurity events identified? | D | Technology Architecture (monitoring and SIEM), Governance Framework | A.8.15, A.8.16 |
| RS — Respond | How are detected incidents managed? | G | Implementation Governance Plan, Change Register | A.5.24, A.5.26 |
| RC — Recover | How is normal operation restored after an incident? | G–H | Migration Plan, Change Register | A.5.29, A.5.30 |

### GV — Govern (6 categories)

The Govern function is the strategic anchor. It covers: organisational context, risk management strategy, roles and responsibilities, policy, oversight, and supply chain risk. In TOGAF terms, GV deliverables live in the Governance Framework and Architecture Principles (security section). Key categories:

- **GV.OC** — Organisational Context: maps to Architecture Vision (scope, constraints, regulatory obligations)
- **GV.RM** — Risk Management Strategy: maps to Risk Register (risk tolerance, risk appetite)
- **GV.RR** — Roles, Responsibilities, and Authorities: maps to Business Architecture (security RACI)
- **GV.SC** — Cybersecurity Supply Chain Risk Management: maps to Technology Architecture (third-party risk controls)

### ID — Identify (5 categories)

Covers asset management, risk assessment, and improvement planning. Maps primarily to Phase A and Phase B. Key categories:

- **ID.AM** — Asset Management: drives Business Architecture (asset inventory) and Data Architecture (data inventory)
- **ID.RA** — Risk Assessment: drives Requirements Register (RIS-NNN security risks) and Architecture Vision (risk summary)
- **ID.IM** — Improvement: drives Phase H change management

### PR — Protect (6 categories)

Covers identity management, awareness and training, data security, platform security, and technology infrastructure resilience. Maps to Phase C and D. Key categories:

- **PR.AA** — Identity Management, Authentication, and Access Control: drives Application Architecture (auth/authz model)
- **PR.DS** — Data Security: drives Data Architecture (classification, encryption, retention)
- **PR.PS** — Platform Security: drives Technology Architecture (hardening standards, patch management)
- **PR.IR** — Technology Infrastructure Resilience: drives Technology Architecture (backup, redundancy, availability controls)

### DE — Detect (2 categories)

Covers continuous monitoring and adverse event analysis. Maps to Phase D Technology Architecture. Key categories:

- **DE.CM** — Continuous Monitoring: drives Technology Architecture (SIEM, IDS/IPS, log aggregation)
- **DE.AE** — Adverse Event Analysis: drives Governance Framework (SOC procedures, alert triage)

### RS — Respond (4 categories)

Covers incident response planning, incident analysis, incident response reporting, and mitigation. Maps to Phase G governance artifacts. Key categories:

- **RS.MA** — Incident Management: drives Implementation Governance Plan (security incident procedures)
- **RS.AN** — Incident Analysis: drives Business Architecture security review process (investigation procedures, evidence collection)
- **RS.CO** — Incident Response Reporting and Communication: drives Governance Framework (notification obligations, GDPR 72-hour breach reporting)
- **RS.MI** — Incident Mitigation: drives Architecture Roadmap / Change Register (containment and eradication actions)

### RC — Recover (2 categories)

Covers incident recovery planning and communication during recovery. Maps to Phase G and Phase H. Key categories:

- **RC.RP** — Incident Recovery Plan Execution: drives Migration Plan (DR/BCP sequence)
- **RC.CO** — Incident Recovery Communication: drives Change Register (stakeholder communication during recovery)

## 3. Maturity Tiers

NIST CSF 2.0 uses four maturity tiers to characterise the sophistication of an organisation's cybersecurity risk management practices. Tiers are not compliance levels — they describe whether practices are ad hoc or systematic.

| Tier | Name | Characteristics |
|---|---|---|
| 1 | Partial | Cybersecurity risk management is ad hoc and reactive. Limited awareness of risk at the organisational level. No formal processes. |
| 2 | Risk Informed | Risk management practices exist but are not formally approved or consistently applied across the organisation. |
| 3 | Repeatable | Risk management practices are formally approved, consistently applied, and updated regularly in response to changes. |
| 4 | Adaptive | The organisation continuously adapts its security practices based on threat intelligence, lessons learned, and real-time risk data. |

**How to use tiers in an engagement:**

In the Architecture Vision security section, record the current tier assessment alongside the target tier at the end of the roadmap period. Reference the tier when sizing security work packages — moving from Tier 1 to Tier 3 requires significant investment in governance, tooling, and process. Frame tier improvement as measurable architecture outcomes in the Requirements Register (OBJ-NNN entries in `engagement.json`).

## 4. CSF + TOGAF + SABSA Alignment

The table below shows how a single security concern traces through all three frameworks, using data breach risk as the example.

| Dimension | Entry |
|---|---|
| **Business risk** | Unauthorised access to customer personal data leading to regulatory penalties and reputational damage |
| **NIST CSF** | ID.AM-5 (sensitive data catalogued), PR.DS-1 (data at rest protected), PR.DS-2 (data in transit protected), DE.CM-3 (personnel activity monitored) |
| **ISO 27001:2022** | A.5.9 (asset inventory), A.8.10 (information deletion), A.8.24 (cryptography), A.8.15 (logging) |
| **SABSA Layer** | Logical (data classification and encryption service design) → Physical (encryption mechanisms and key management) |
| **TOGAF Artifact** | Data Architecture (classification scheme, encryption at rest/in transit spec, retention policy), Technology Architecture (KMS, TLS configuration) |
| **REQ-NNN** | REQ-NNN type:security, source:ISO27001, control:A.8.24 — encryption at rest requirement; REQ-NNN type:security, source:ISO27001, control:A.8.10 — deletion obligation |
| **RIS-NNN** | RIS-NNN category:security — data breach risk, with likelihood, impact, and mitigation owner |

Use this trace pattern when deriving security requirements from an identified risk: start with the business risk, map to CSF categories and ISO controls, anchor to a SABSA layer, then produce the TOGAF artifact and REQ/RIS entries.
