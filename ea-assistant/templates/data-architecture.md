---
artifact: Data Architecture
engagement: {{engagement_name}}
phase: C
status: Draft
reviewStatus: Not Reviewed
version: 0.1
lastModified: {{YYYY-MM-DD}}
---

<!-- GUIDANCE:
  The Data Architecture is a Phase C artifact describing how the organisation manages, stores,
  and moves data to meet business needs. It complements the Application Architecture and must
  be consistent with the Business Architecture (information objects) and Technology Architecture
  (storage and platform decisions). Data Architecture drives data governance, integration patterns,
  and master data management decisions.
-->

# Data Architecture

**Engagement:** {{engagement_name}}
**Organisation:** {{organisation}}
**Date:** {{YYYY-MM-DD}}

---

## 1. Data Context

<!-- GUIDANCE:
  Describe the business context driving data architecture decisions. Include: key business
  capabilities that depend on data, current data pain points (silos, quality issues, duplication),
  regulatory or compliance obligations affecting data (GDPR, sector-specific), and strategic
  data ambitions (becoming data-driven, analytics, AI/ML).
-->

{{data_context}}

---

## 2. Conceptual Data Model

<!-- GUIDANCE:
  A high-level view of the major subject areas and their relationships. Subject areas correspond
  roughly to business domains (e.g. Customer, Product, Order, Finance). This model should be
  understandable by business stakeholders without technical knowledge. Include a diagram reference.
-->

*Reference diagram:* `../diagrams/{{conceptual_data_diagram}}`

| Subject Area | Description | Primary Owner |
|---|---|---|
| {{subject_area_1}} | {{description_1}} | {{owner_1}} |
| {{subject_area_2}} | {{description_2}} | {{owner_2}} |

---

## 3. Logical Data Model

<!-- GUIDANCE:
  A normalised, technology-agnostic model of key entities and their relationships. Capture the
  main entities, their key attributes, and cardinality of relationships. This feeds into physical
  design but should not itself contain platform-specific detail. Include a diagram reference.
-->

*Reference diagram:* `../diagrams/{{logical_data_diagram}}`

{{logical_data_model_description}}

---

## 4. Data Entities

<!-- GUIDANCE:
  Describe each significant data entity. Focus on entities that are shared across systems,
  subject to governance, or represent master/reference data. For each entity, capture its
  definition, authoritative source, and key attributes.
-->

### {{entity_name_1}}

| Field | Value |
|---|---|
| **Definition** | {{definition}} |
| **Authoritative Source** | {{source_system}} |
| **Key Attributes** | {{key_attributes}} |
| **Sensitivity** | Public / Internal / Confidential / Restricted |
| **Retention Period** | {{retention}} |
| **Consuming Systems** | {{consuming_systems}} |

### {{entity_name_2}}

| Field | Value |
|---|---|
| **Definition** | {{definition}} |
| **Authoritative Source** | {{source_system}} |
| **Key Attributes** | {{key_attributes}} |
| **Sensitivity** | Public / Internal / Confidential / Restricted |
| **Retention Period** | {{retention}} |
| **Consuming Systems** | {{consuming_systems}} |

---

## 5. Data Flows

<!-- GUIDANCE:
  Describe how data moves between systems, domains, and external parties. Capture source,
  destination, frequency, volume (where significant), and transformation or enrichment that
  occurs in transit. Highlight cross-boundary flows that have governance or compliance implications.
  Include a data flow diagram reference.
-->

*Reference diagram:* `../diagrams/{{data_flow_diagram}}`

| Flow ID | Description | Source | Destination | Frequency | Classification |
|---|---|---|---|---|---|
| DF-001 | {{description}} | {{source}} | {{destination}} | Real-time / Batch / On-demand | {{classification}} |
| DF-002 | {{description}} | {{source}} | {{destination}} | Real-time / Batch / On-demand | {{classification}} |

---

## 6. Data Governance

<!-- GUIDANCE:
  Describe the data governance arrangements relevant to this architecture. Include: data ownership
  model (who is accountable for each subject area), data quality standards and how they are
  enforced, master data management approach, data lineage requirements, and any regulatory
  obligations (retention, right-to-erasure, cross-border transfer restrictions).
-->

### Data Ownership

| Subject Area | Data Owner | Steward |
|---|---|---|
| {{subject_area_1}} | {{owner_1}} | {{steward_1}} |

### Data Quality Standards
{{data_quality_standards}}

### Master Data Management Approach
{{mdm_approach}}

### Regulatory Obligations
{{regulatory_obligations}}

---

## 7. Gap Analysis

<!-- GUIDANCE:
  Summarise the key gaps between the current (baseline) data architecture and the target.
  Reference the full Gap Analysis artifact for detail. Focus here on the gaps most significant
  to data: missing authoritative sources, duplicated master data, ungoverned flows, quality deficits.
-->

*See Gap Analysis artifact for full detail:* `gap-analysis.md`

| Gap ID | Description | Priority | Impact |
|---|---|---|---|
| GAP-001 | {{description}} | High / Med / Low | {{impact}} |

---

## 8. Requirements Addressed

<!-- GUIDANCE:
  Trace this artifact back to requirements from the Requirements Register. Demonstrate that the
  data architecture decisions are driven by stated requirements, not just technical preference.
-->

| Req ID | Requirement | How Addressed |
|---|---|---|
| {{req_id}} | {{requirement}} | {{how}} |

---

*This document was created using the EA Assistant plugin.*
