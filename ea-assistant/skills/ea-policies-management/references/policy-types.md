# Policy Types — Reference Taxonomy

A taxonomy of policy types used in the Architecture Policies Register. Each type maps to a typical issuing authority, common examples, and the kinds of constraints it typically generates.

| Type | Code | Typical Issuing Authority | Common Examples | Typical Constraints Generated |
|---|---|---|---|---|
| **Security** | SEC | CISO / Security Board / InfoSec Committee | "All data at rest must be encrypted"; "MFA required for all remote access"; "Vulnerability scans monthly" | Technology constraints (encryption standards), Organisational constraints (access controls), Regulatory constraints (compliance deadlines) |
| **Procurement** | PRO | CFO / Procurement Board / Vendor Management | "Vendor contracts >$100K require board approval"; "Preferred vendor list"; "Open-source before commercial" | Budget constraints (spending limits), Technology constraints (approved vendor list), Organisational constraints (approval workflows) |
| **Data Governance** | DGO | CDO / DPO / Data Governance Committee | "Customer PII may not leave EU regions"; "Data retention 7 years for financial records"; "Master data must be centralised" | Regulatory constraints (GDPR, SOX), Technology constraints (data residency), Organisational constraints (data ownership) |
| **Technology** | TEC | CTO / Enterprise Architecture Board / CIO | "Cloud-first for all new systems"; "APIs must use REST/GraphQL"; "Containers for all stateless workloads" | Technology constraints (approved platforms), Interoperability constraints (standard interfaces), Organisational constraints (migration timelines) |
| **Compliance** | COM | Legal / Compliance Officer / Regulatory Affairs | "SOX requires 7-year audit trail retention"; "GDPR Article 44 — data transfer mechanisms"; "PCI-DSS for all payment systems" | Regulatory constraints (mandatory controls), Budget constraints (audit costs), Technology constraints (compliant platforms) |
| **HR** | HRM | CHRO / HR Director / People Committee | "Remote access requires MFA for all staff"; "All employees must complete security awareness training"; "BYOD permitted for non-sensitive roles" | Organisational constraints (training requirements), Technology constraints (device management), Budget constraints (training budgets) |
| **Operational** | OPS | COO / Operations Board / IT Service Management | "All production changes require CAB approval"; "RTO ≤ 4 hours for Tier-1 systems"; "Change freeze during month-end close" | Timeline constraints (change windows), Budget constraints (resourcing), Organisational constraints (approval gates) |

## Usage Notes

- **Type is mandatory** — every policy must have exactly one type.
- **Types are not exclusive** — a Security policy may generate Technology constraints; a Compliance policy may generate Security constraints. The type describes the policy's primary domain, not the domain of its derived constraints.
- **Enterprise policies** (Scope = Enterprise 🔒) are typically Security, Data Governance, Compliance, or Technology types. Divisional or Geographic policies are more commonly Procurement, HR, or Operational.
- When in doubt, use **Compliance** for externally mandated policies (regulator, law) and **Technology** for internally mandated architecture standards.
