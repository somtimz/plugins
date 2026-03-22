# Requirement Categories Taxonomy

This reference defines the taxonomy of requirement types used by the EA Assistant requirements management skill. For each category it describes the definition, characteristics, how it maps to TOGAF and Zachman, and provides worked examples.

---

## Overview of Requirement Types

Enterprise architecture work deals with requirements at multiple levels of abstraction. Not all requirements are functional system requirements in the traditional software engineering sense. Architecture requirements include the full spectrum from strategic constraints to detailed data quality rules.

The EA Assistant classifies requirements into five primary categories:

| Category | Code Prefix | Primary Concern |
|---|---|---|
| Functional Requirement | FR | What the system or architecture must do |
| Non-Functional Requirement | NFR | How well it must do it (quality attributes) |
| Constraint | CON | What limits or restricts the solution space |
| Principle | PRI | Normative statements that govern decisions |
| Assumption | ASS | Statements accepted as true without proof |

Additionally, two derived types are used for traceability:

| Category | Code Prefix | Primary Concern |
|---|---|---|
| Architecture Decision | ADR | A decision made in response to requirements |
| Gap | GAP | A difference between current state and a requirement |

---

## Functional Requirements (FR)

### Definition
A Functional Requirement specifies a behaviour, capability, or function that a system, process, or organisational component must provide. It answers the question: "What must this do?"

### Characteristics
- Describes a specific capability or action
- Can be tested — it is either satisfied or not
- Scoped to a defined subject (a system, a process, an organisation)
- Expressed in the form: "[Subject] must [verb] [object] [qualifier]"

### TOGAF Mapping
- Primarily lives in the **Architecture Requirements Specification** produced during Phase B, C, and D.
- Functional requirements for business capabilities align to Phase B outputs.
- Functional requirements for application components align to Phase C outputs.
- Functional requirements for infrastructure align to Phase D outputs.
- All feed into the Requirements Management process (central ADM hub).

### Zachman Mapping
- **Primarily:** Row 2, Column 2 (Conceptual / How) — what the business must do.
- **Also:** Row 3, Column 2 (Logical / How) — what the system must do.
- Data-focused functional requirements also touch Row 2–3, Column 1 (What).

### Sub-types

| Sub-type | Description |
|---|---|
| Business Functional Requirement | A function the business must perform (not system-specific) |
| System Functional Requirement | A function a specific application or system must provide |
| Data Functional Requirement | A data management capability (e.g., "must support data lineage tracking") |
| Integration Requirement | How systems must exchange data or trigger each other |
| Reporting Requirement | What information must be surfaced to whom and when |

### Examples

**FR-001:** The Customer Portal must allow authenticated customers to view all invoices issued in the past 24 months.

**FR-002:** The Order Management System must send a confirmation notification to the customer within 30 seconds of order acceptance.

**FR-003:** The integration between the CRM and ERP systems must synchronise customer address changes within 15 minutes of the update occurring in either system.

**FR-004:** The data platform must support data lineage tracking from source system to report cell for all regulated reporting data.

---

## Non-Functional Requirements (NFR)

### Definition
A Non-Functional Requirement (NFR) specifies a quality attribute or operational characteristic of a system or architecture. It describes how the system must behave, not what it must do. Also known as quality attributes, cross-cutting concerns, or "-ilities."

### Characteristics
- Applies broadly across multiple functional areas
- Typically expressed as a measurable target (threshold, SLA, percentage)
- Failure to meet an NFR does not prevent functionality but degrades quality
- Often the hardest requirements to retrofit after design is complete

### TOGAF Mapping
- NFRs influence all phases but are formally captured in the **Architecture Requirements Specification**.
- Performance and availability NFRs drive Phase D (Technology Architecture) decisions.
- Security NFRs appear across all phases and are synthesised into a Security Architecture View.
- Operability and maintainability NFRs influence Phase D and Phase G (governance of implemented solutions).

### Zachman Mapping
- Performance, availability, scalability: Row 3, Column 3 (Logical / Where — distributed systems) and Row 4, Column 3 (Physical / Where — technology).
- Security and access: Row 3, Column 4 (Logical / Who) and Row 4, Column 4 (Physical / Who).
- Manageability and monitoring: Row 4, Column 2 (Physical / How).

### NFR Categories (ISO/IEC 25010 Quality Model)

| NFR Category | Examples of Attributes |
|---|---|
| Performance Efficiency | Response time, throughput, resource utilisation |
| Reliability | Availability (uptime %), MTBF, fault tolerance |
| Recoverability | RTO (Recovery Time Objective), RPO (Recovery Point Objective) |
| Security | Confidentiality, integrity, non-repudiation, authentication strength |
| Maintainability | Modularity, testability, modifiability |
| Portability | Installability, adaptability, replaceability |
| Usability | Learnability, accessibility, error tolerance |
| Compatibility | Interoperability, co-existence with existing systems |

### Examples

**NFR-001 (Availability):** The Customer Portal must achieve 99.9% availability measured monthly, excluding approved maintenance windows of no more than 4 hours per month.

**NFR-002 (Performance):** The API Gateway must respond to 95% of requests within 200ms under a load of 5,000 concurrent users.

**NFR-003 (Security):** All data at rest classified as Confidential or above must be encrypted using AES-256 or equivalent.

**NFR-004 (Recoverability):** The core banking platform must achieve an RTO of 4 hours and an RPO of 1 hour for a complete data centre failure scenario.

**NFR-005 (Accessibility):** The customer-facing web application must comply with WCAG 2.1 Level AA accessibility standards.

---

## Constraints (CON)

### Definition
A Constraint is a restriction on the solution space that is non-negotiable for the given engagement. It does not express a preference — it establishes a hard boundary that the architecture must operate within.

### Characteristics
- Not derived from a goal but imposed from outside (or internally mandated)
- Cannot be traded off against cost or time (if it can, it is a requirement, not a constraint)
- Sources: regulatory/legal, contractual, organisational policy, existing technology investment, physical reality
- Must be documented with their source and owner — constraints without a named owner can be challenged

### Distinguishing Constraints from Requirements
A requirement is something the architecture must achieve; a constraint is something the architecture must not violate. A constraint may also be thought of as a requirement with zero tolerance for deviation.

### TOGAF Mapping
- Identified in Phase A and carried through all subsequent phases.
- Constraints are a key input to the **Statement of Architecture Work** and all gap analyses.
- Technology constraints (e.g., "must use existing Azure tenancy") drive Phase D decisions directly.

### Zachman Mapping
- Technology constraints: Row 4, Column 3 (Physical / Where).
- Legal/regulatory constraints: Row 1, Column 6 (Contextual / Why) — they are strategic motivational limits.
- Organisational constraints: Row 1, Column 4 (Contextual / Who).

### Constraint Types

| Type | Description | Example |
|---|---|---|
| Technology Constraint | Mandated or prohibited technology choices | "Must deploy within the existing AWS Organisation" |
| Regulatory Constraint | Legal or regulatory obligation | "Must comply with GDPR Article 17 (right to erasure)" |
| Budget Constraint | Financial ceiling | "Total implementation cost must not exceed $5M" |
| Timeline Constraint | Hard deadlines | "Must be operational before 1 January 2026 due to regulatory deadline" |
| Organisational Constraint | Internal policy or governance | "Must use the approved vendor panel; no new vendor agreements" |
| Interoperability Constraint | Must interface with specific systems | "Must integrate with the existing SAP S/4HANA instance without replacement" |

### Examples

**CON-001:** All solution components must be deployed within the organisation's existing Microsoft Azure tenancy in the Australia East and Australia Southeast regions.

**CON-002:** The solution must not require replacement of the existing SAP ECC instance until the planned ECC end-of-life date in 2027.

**CON-003:** Personal data of EU-resident customers must not be stored or processed outside the European Economic Area.

---

## Principles (PRI)

### Definition
A Principle is a normative, declarative statement that provides a rule or guideline governing architecture decisions. Principles are not requirements (they do not mandate specific outcomes) but rather filters applied when making architecture choices.

### Characteristics
- Written as an affirmative, present-tense statement of intent
- Has three parts: **Statement** (what), **Rationale** (why), **Implications** (so what)
- Applies broadly across the architecture, not to a single requirement
- Owned and endorsed at the enterprise level (or architecture board)

### TOGAF Mapping
- Defined in the **Preliminary Phase** and recorded in the **Architecture Principles Catalogue**.
- Applied throughout all ADM phases to filter design options.
- Violations of principles are surfaced in **Compliance Assessments** (Phase G).

### Zachman Mapping
- Primarily: Row 1, Column 6 (Contextual / Why) — scope-level motivation.
- Also: Row 2, Column 6 (Conceptual / Why) — business strategy level.

### Examples

**PRI-001 — Open Standards Preferred**
*Statement:* The architecture will prefer open standards over proprietary solutions where functional equivalence exists.
*Rationale:* Open standards reduce vendor lock-in, improve interoperability, and lower long-term total cost of ownership.
*Implications:* Procurement evaluation must include a standards-alignment criterion. Exceptions require architecture board approval and a documented exit strategy.

**PRI-002 — Data is an Asset**
*Statement:* Data will be managed as a shared enterprise asset, not owned by individual systems or teams.
*Rationale:* Siloed data ownership leads to duplication, inconsistency, and barriers to analytics and reporting.
*Implications:* All new systems must expose data via approved integration interfaces. A data custodian must be assigned to each canonical data entity.

**PRI-003 — Design for Change**
*Statement:* Architecture components will be designed with modularity and loose coupling to facilitate future change.
*Rationale:* Business requirements evolve; architectures that assume stability become expensive to modify.
*Implications:* All services must define clear boundaries and contracts. Tight coupling between components requires architectural justification.

---

## Assumptions (ASS)

### Definition
An Assumption is a statement that is accepted as true for the purposes of the architecture work, without formal proof or verification. Assumptions fill gaps in known facts at the time of architecture development.

### Characteristics
- Explicitly documented so that they can be validated or challenged
- Each assumption carries a risk: if the assumption is wrong, the architecture may be invalidated
- Should include the consequence if the assumption proves false
- Must be owned — someone is responsible for verifying or monitoring the assumption

### TOGAF Mapping
- Identified and recorded throughout the ADM, particularly in Phase A and Requirements Management.
- An **Architecture Requirements Specification** typically includes a dedicated assumptions section.
- Unvalidated assumptions are a key risk input to Phase E (Opportunities and Solutions).

### Zachman Mapping
- Primarily: Row 1, Column 6 (Contextual / Why) — they represent the contextual understanding of the enterprise scope.

### Examples

**ASS-001:** It is assumed that the organisation's current Azure tenancy has sufficient capacity quota to accommodate the target workloads without requiring a quota increase request. *(Consequence if false: deployment timeline is extended by 4–8 weeks for quota approval.)*

**ASS-002:** It is assumed that the existing integration middleware (MuleSoft) will be retained and is capable of supporting the additional integration load in the target state. *(Consequence if false: a middleware capacity assessment is required before Phase D is finalised.)*

**ASS-003:** It is assumed that business stakeholders can commit 4 hours per week per workstream for architecture engagement activities. *(Consequence if false: discovery and validation activities will be delayed, extending the engagement timeline.)*

---

## Cross-Category Mapping Summary

| Category | TOGAF Phase Focus | TOGAF Artefact | Zachman Primary Cell | Zachman Secondary |
|---|---|---|---|---|
| Functional (FR) | B, C, D | Architecture Requirements Specification | R2,C2 | R3,C2 |
| Non-Functional (NFR) | C, D | Architecture Requirements Specification | R3,C3 | R4,C3, R4,C2 |
| Constraint (CON) | Prelim, A | Statement of Architecture Work | R1,C6 | R4,C3 |
| Principle (PRI) | Prelim | Architecture Principles Catalogue | R1,C6 | R2,C6 |
| Assumption (ASS) | A, Req. Mgmt | Architecture Requirements Specification | R1,C6 | — |
