# 12 Architecture Principles for Government

A reference catalogue of the 12 Architecture Principles for Government. Use these as a starting point when creating a new EA engagement for a government or public-sector organisation.

**How to use:**
- Run `/ea-requirements add` and choose category `Principle` for each entry you wish to adopt
- Set scope to `Corporate` if your organisation has formally adopted the principle enterprise-wide; `Project` if you are applying it only to this engagement
- Adapt the Statement, Rationale, and Implications to your organisation's specific context before approving

---

## GP-001 — Reuse before Buy, Buy before Build

| Field | Value |
|---|---|
| **Statement** | Check for existing government-wide shared services or open-source government solutions before procuring SaaS or building custom. |
| **Rationale** | Reduces procurement overhead and ensures consistency across citizen-facing services. |
| **Implications** | All new capability requests must demonstrate that no reusable government shared service or approved open-source solution exists. A build option requires documented justification. Procurement of net-new SaaS is the second option, not the first. |

---

## GP-002 — Interoperability by Mandate

| Field | Value |
|---|---|
| **Statement** | All new systems must support open standards (REST, JSON, OAuth 2.0) for data exchange. |
| **Rationale** | Government data is often needed by multiple agencies; proprietary interfaces prevent cross-agency integration and create vendor lock-in. |
| **Implications** | No point-to-point or proprietary integrations are approved without ARB exception. All APIs must be documented and versioned. Systems that cannot expose or consume open-standard interfaces are not approved for procurement. |

---

## GP-003 — Security as a Shared Responsibility

| Field | Value |
|---|---|
| **Statement** | Use standardised, pre-approved security patterns and identity providers rather than custom security implementations. |
| **Rationale** | Security audits are the primary cause of delivery delays; pre-vetted patterns accelerate the Authority to Operate (ATO) process and reduce risk. |
| **Implications** | Identity and authentication must use the approved government identity provider. Custom authentication implementations require explicit security team sign-off. Security review is required at architecture design time, not at deployment. |

---

## GP-004 — Data Sovereignty & Privacy by Design

| Field | Value |
|---|---|
| **Statement** | Data must be classified at source and privacy controls must be automated, not applied manually after the fact. |
| **Rationale** | Compliance with privacy legislation is non-negotiable; automation eliminates manual review cycles and reduces the risk of human error. |
| **Implications** | All new data collections require a Privacy Impact Assessment before build begins. Data classification tags must be applied at ingestion. Citizen PII must remain within jurisdiction-approved storage boundaries. Manual privacy review gates are replaced by automated policy checks in the build pipeline. |

---

## GP-005 — The "Golden Path" Developer Experience

| Field | Value |
|---|---|
| **Statement** | The architecture team provides a standard, pre-approved technology stack that is eligible for fast-track delivery approval. |
| **Rationale** | Small delivery teams cannot afford to evaluate and support multiple deployment methods; standardisation allows teams to focus on features, not infrastructure. |
| **Implications** | A Golden Path stack is maintained and published by the architecture team. Teams that adopt it receive fast-track approval. Teams that deviate must seek ARB review and accept full ownership of their non-standard stack. The Golden Path is updated at a regular cadence to reflect current approved tooling. |

---

## GP-006 — Modular & Decoupled Services

| Field | Value |
|---|---|
| **Statement** | Large programmes must be decomposed into smaller, independently deployable modules with well-defined boundaries and interfaces. |
| **Rationale** | Smaller modules are easier to test, approve, and deploy; modularity enables incremental delivery of value rather than a single high-risk release. |
| **Implications** | Monolithic system designs require explicit ARB justification. Each module must have a defined API contract. Inter-module dependencies must be declared and reviewed. Modules must be independently deployable without co-ordinated releases. |

---

## GP-007 — Automated Compliance (Policy as Code)

| Field | Value |
|---|---|
| **Statement** | Architectural and security policies are encoded as automated checks in the build and deployment pipeline. |
| **Rationale** | Replacing manual architecture reviews with automated pipeline gates provides instant feedback to developers and removes the architecture team as a delivery bottleneck. |
| **Implications** | All approved policies must have a corresponding automated check. Build pipelines that lack policy-as-code gates are not approved for production deployment. The architecture team is responsible for maintaining and publishing the policy check library. |

---

## GP-008 — Public-First Transparency

| Field | Value |
|---|---|
| **Statement** | Code and documentation are open-source by default unless a documented security or sensitivity reason requires otherwise. |
| **Rationale** | Open-source encourages higher quality code, simplifies vendor collaboration, and builds public trust in government digital services. |
| **Implications** | All new repositories default to public. Requests to make a repository private must be approved and recorded with a stated reason. Sensitive configuration and secrets must never be committed to any repository, public or private. |

---

## GP-009 — Design for Disruption (Resilience)

| Field | Value |
|---|---|
| **Statement** | Systems must handle failure gracefully, with defined recovery objectives, especially for services that are essential to citizens. |
| **Rationale** | System downtime means loss of essential services for citizens who may have no alternative means of access. |
| **Implications** | All citizen-facing systems must define and test Recovery Time Objectives (RTO) and Recovery Point Objectives (RPO). Graceful degradation must be designed for all critical paths. Regular failure and recovery exercises are required for Tier 1 services. |

---

## GP-010 — Evidence-Based Decision Making

| Field | Value |
|---|---|
| **Statement** | Architecture decisions are based on user research, usage data, and measured outcomes — not technical preference or assumption. |
| **Rationale** | Building features citizens do not use wastes public funds and delays genuinely needed capability. |
| **Implications** | All significant architecture decisions must reference supporting evidence (user research, analytics, pilot results). New capability proposals without evidence of user need are returned for validation before design work begins. Metrics are defined at the start of delivery and reviewed at each phase gate. |

---

## GP-011 — Cloud-First, Not Cloud-Only

| Field | Value |
|---|---|
| **Statement** | Managed cloud services are the default choice; on-premises or hybrid hosting requires documented justification and an assured data portability strategy. |
| **Rationale** | Cloud hosting reduces capital expenditure and operational overhead, while a data portability requirement protects the long-term interests of government data custodianship. |
| **Implications** | New infrastructure provisioning must evaluate cloud-native options first. On-premises exceptions require a cost-benefit analysis and exit strategy. All cloud-hosted data must be exportable in an open format. Vendor lock-in risk must be assessed and mitigated for Tier 1 services. |

---

## GP-012 — Continuous Architecture

| Field | Value |
|---|---|
| **Statement** | Architecture is a living, iterative process; architects are embedded in delivery teams rather than operating in a separate review layer. |
| **Rationale** | Small delivery teams cannot maintain quality without real-time architecture guidance; an ivory-tower model creates delays, rework, and adversarial dynamics. |
| **Implications** | Architecture reviews occur in sprint cycles, not as pre/post-delivery gates. Architects are accountable for delivery outcomes, not just design documents. The Architecture Decision Record (ADR) is the primary artefact, maintained by the team with architect support. |
