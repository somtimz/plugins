# Constraint Types Taxonomy

This reference defines the taxonomy of constraint types used by the EA Assistant constraints management skill. For each type it describes the definition, characteristics, how it maps to TOGAF and Zachman, and provides worked examples.

---

## Overview

Architecture constraints are non-negotiable restrictions on the solution space. They are distinct from requirements (which define what the architecture must achieve) and from risks (which are uncertain). Every constraint must have a **Source** (the policy, regulation, contract, or mandate that created it) and an **Owner** (the person or role accountable for upholding it).

| Type | Code | Primary Concern |
|---|---|---|
| Technology Constraint | TEC | Mandated or prohibited technology choices |
| Regulatory Constraint | REG | Legal or regulatory obligation |
| Budget Constraint | BUD | Financial ceiling |
| Timeline Constraint | TIM | Hard deadlines |
| Organisational Constraint | ORG | Internal policy or governance |
| Interoperability Constraint | INT | Must interface with specific systems |

---

## Technology Constraint (TEC)

### Definition
A restriction on the technology choices available to the architecture. This includes mandated platforms, prohibited vendors, required standards, or existing infrastructure that must be reused.

### Characteristics
- Certain and binding — not a preference
- Often driven by existing contracts, enterprise standards, or vendor relationships
- May create lock-in if not balanced with optionality
- Must be documented with the source policy or contract reference

### TOGAF Mapping
- Identified in Phase A and refined in Phase D (Technology Architecture).
- Key input to Technology Architecture SBB selection.
- Captured in the Constraints Register and referenced in SBB records.

### Zachman Mapping
- Primarily: Row 4, Column 3 (Physical / Where) — technology placement and selection.

### Examples

**CST-001 (Technology):** All solution components must be deployed within the organisation's existing Microsoft Azure tenancy in the Australia East and Australia Southeast regions.

**CST-002 (Technology):** The solution must use the organisation's standard API gateway (Apigee) for all external-facing interfaces.

---

## Regulatory Constraint (REG)

### Definition
A legal or regulatory obligation that the architecture must comply with. These are externally imposed and non-negotiable.

### Characteristics
- Derived from legislation, regulation, or industry standards
- Cannot be waived without legal review
- Often drives data residency, privacy, and security architecture decisions
- Must reference the specific regulation and article/section

### TOGAF Mapping
- Identified in Preliminary Phase and Phase A.
- Influences all architecture domains (Business, Data, Application, Technology).
- Captured in the Constraints Register and referenced in Compliance Assessments.

### Zachman Mapping
- Primarily: Row 1, Column 6 (Contextual / Why) — strategic motivational limits.

### Examples

**CST-003 (Regulatory):** Personal data of EU-resident customers must not be stored or processed outside the European Economic Area. *(Source: GDPR Article 44)*

**CST-004 (Regulatory):** All financial transaction records must be retained for a minimum of seven years in an immutable, auditable format. *(Source: SOX Section 802)*

---

## Budget Constraint (BUD)

### Definition
A financial ceiling or cost boundary that limits what the architecture can include or procure.

### Characteristics
- Certain — the budget envelope is fixed (though it may be renegotiated at a governance level)
- Affects work package scoping and SBB selection
- Must be documented with the approving authority and budget line reference

### TOGAF Mapping
- Identified in Preliminary Phase and Phase A (Architecture Vision, Engagement Charter).
- Drives Phase E (Opportunities and Solutions) prioritisation.
- Captured in the Constraints Register and referenced in the Architecture Roadmap.

### Zachman Mapping
- Primarily: Row 1, Column 6 (Contextual / Why) — financial motivation and limits.

### Examples

**CST-005 (Budget):** Total implementation cost for the target architecture must not exceed $5M AUD over the three-year programme horizon. *(Source: FY26 Capital Budget, Board Resolution B-2025-17)*

---

## Timeline Constraint (TIM)

### Definition
A hard deadline or fixed date by which some or all of the architecture must be operational.

### Characteristics
- Certain — the date is non-negotiable (though it may be renegotiated at a governance level)
- Often regulatory-driven (compliance deadlines) or contract-driven (vendor end-of-support)
- Affects migration sequencing and work package scheduling

### TOGAF Mapping
- Identified in Preliminary Phase and Phase A.
- Drives Phase F (Migration Planning) sequencing.
- Captured in the Constraints Register and referenced in the Migration Plan.

### Zachman Mapping
- Primarily: Row 1, Column 6 (Contextual / Why) — temporal motivation.

### Examples

**CST-006 (Timeline):** The new customer onboarding platform must be operational before 1 January 2026 due to the regulatory deadline for open banking compliance. *(Source: CDR Compliance Roadmap, ACCC Notice 2025-03)*

---

## Organisational Constraint (ORG)

### Definition
An internal policy, governance rule, or organisational reality that restricts architecture choices.

### Characteristics
- Derived from internal governance, headcount limits, or political realities
- May be softer than regulatory constraints but still binding within the organisation
- Must be documented with the policy owner and governance forum

### TOGAF Mapping
- Identified in Preliminary Phase (Architecture Principles, Governance Framework).
- Influences all phases.
- Captured in the Constraints Register and referenced in the Governance Framework.

### Zachman Mapping
- Primarily: Row 1, Column 4 (Contextual / Who) — organisational actor limits.

### Examples

**CST-007 (Organisational):** The architecture must not require hiring of net-new FTEs in the infrastructure operations team. *(Source: HR Freeze Directive, CFO Memo 2025-08)*

**CST-008 (Organisational):** All vendor procurement must route through the approved vendor panel; no new vendor agreements may be initiated during FY26. *(Source: Procurement Policy v4.2)*

---

## Interoperability Constraint (INT)

### Definition
A requirement to integrate with or remain compatible with specific existing systems, data formats, or protocols.

### Characteristics
- Often the most expensive constraints to satisfy
- May create technical debt if the target system is itself being retired
- Must be documented with the system owner and integration interface specification

### TOGAF Mapping
- Identified in Phase B (Business Architecture) and refined in Phases C and D.
- Drives Application and Data Architecture interface design.
- Captured in the Constraints Register and referenced in the Interface Catalog.

### Zachman Mapping
- Primarily: Row 3, Column 2 (Logical / How) — integration logic.
- Also: Row 4, Column 2 (Physical / How) — physical integration implementation.

### Examples

**CST-009 (Interoperability):** The new claims processing platform must integrate with the existing SAP S/4HANA instance for policyholder master data without requiring SAP replacement before the planned ECC end-of-life in 2027.

**CST-010 (Interoperability):** All outbound data feeds to the regulatory reporting hub must use the existing FIX 5.0 protocol; no alternative protocols are permitted.

---

## Cross-Type Mapping Summary

| Type | TOGAF Phase Focus | TOGAF Artifact | Zachman Primary Cell |
|---|---|---|---|
| Technology (TEC) | D | Technology Architecture; SBB Register | R4, C3 |
| Regulatory (REG) | Prelim, A | Architecture Vision; Compliance Assessment | R1, C6 |
| Budget (BUD) | Prelim, A, E | Engagement Charter; Architecture Roadmap | R1, C6 |
| Timeline (TIM) | Prelim, A, F | Architecture Vision; Migration Plan | R1, C6 |
| Organisational (ORG) | Prelim | Governance Framework; Architecture Principles | R1, C4 |
| Interoperability (INT) | B, C, D | Business Architecture; Interface Catalog | R3, C2 |

---

## Distinguishing Constraints from Requirements

| Question | Constraint | Requirement |
|---|---|---|
| What does it do? | Restricts *how* something may be built | Defines *what* must be achieved |
| Is it certain? | Yes — binding regardless of belief | Yes — must be satisfied |
| Can it be traded off? | No — non-negotiable | Yes — may be de-scoped or reprioritised |
| Does it have a source? | Yes — policy, regulation, contract, mandate | Optional — may be derived from a goal |
| Does it have a measurable target? | No — it is a boundary, not a target | Yes — must be verifiable |
| Example | "Must use existing Azure tenancy" | "API must respond within 200ms" |
| ID prefix | CST-NNN | REQ-NNN |

---

## Legacy Compatibility

The Requirements Register previously captured constraints as `category: Constraint` with local IDs `CON-001`, `CON-002`, etc. These remain valid for backward compatibility but are **deprecated** for new capture. Use `/ea-constraints add` to create new constraints with canonical `CST-NNN` IDs.
