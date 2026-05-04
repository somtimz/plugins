---
artifact: Data Architecture
engagement: {{engagement_name}}
phase: C-Data
status: Draft
reviewStatus: Not Reviewed
version: 0.1
templateVersion: 0.9.5
lastModified: {{YYYY-MM-DD}}
taxonomy:
  domain: Data
  category: Design
  audience: Architecture
  layer: Target
  sensitivity: Internal
  tags: [data-model, information, data-flow, phase-c-data]
relatedArtifacts: []
diagrams: []
links: []
---

<details>
<summary>📋 Guidance</summary>

The Data Architecture is a Phase C artifact describing how the organisation manages, stores,
and moves data to meet business needs. It complements the Application Architecture and must
be consistent with the Business Architecture (information objects) and Technology Architecture
(storage and platform decisions). Data Architecture drives data governance, integration patterns,
and master data management decisions.

</details>

# Data Architecture

**Engagement:** {{engagement_name}}
**Organisation:** {{organisation}}
**Date:** {{YYYY-MM-DD}}

---

## Executive Summary

<details>
<summary>📋 Guidance</summary>

Summary of key data assets, how they flow through the organisation, and what governance changes are required.
Diagram: Conceptual data flow diagram or data domain map
Run `/ea-summary refresh` to regenerate this section from current artifact content.

</details>

{{executive_summary}}

---

## 1. Data Context

<details>
<summary>📋 Guidance</summary>

Describe the business context driving data architecture decisions. Include: key business
capabilities that depend on data, current data pain points (silos, quality issues, duplication),
regulatory or compliance obligations affecting data (GDPR, sector-specific), and strategic
data ambitions (becoming data-driven, analytics, AI/ML).

</details>

{{data_context}}

---

## 2. Conceptual Data Model

<details>
<summary>📋 Guidance</summary>

A high-level view of the major subject areas and their relationships. Subject areas correspond
roughly to business domains (e.g. Customer, Product, Order, Finance). This model should be
understandable by business stakeholders without technical knowledge. Include a diagram reference.

</details>

*Reference diagram:* `../diagrams/{{conceptual_data_diagram}}`

| Subject Area | Description | Primary Owner |
|---|---|---|
| {{subject_area_1}} | {{description_1}} | {{owner_1}} |
| {{subject_area_2}} | {{description_2}} | {{owner_2}} |

---

## 3. Logical Data Model

<details>
<summary>📋 Guidance</summary>

A normalised, technology-agnostic model of key entities and their relationships. Capture the
main entities, their key attributes, and cardinality of relationships. This feeds into physical
design but should not itself contain platform-specific detail. Include a diagram reference.

</details>

*Reference diagram:* `../diagrams/{{logical_data_diagram}}`

{{logical_data_model_description}}

---

## 4. Data Entities

<details>
<summary>📋 Guidance</summary>

Describe each significant data entity. Focus on entities that are shared across systems,
subject to governance, or represent master/reference data. For each entity, capture its
definition, authoritative source, and key attributes.

</details>

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

<details>
<summary>📋 Guidance</summary>

Describe how data moves between systems, domains, and external parties. Capture source,
destination, frequency, volume (where significant), and transformation or enrichment that
occurs in transit. Highlight cross-boundary flows that have governance or compliance implications.
Include a data flow diagram reference.

**State column is mandatory.** Use `Current` for flows that exist today, `Planned (Target)` for
flows that are part of the target architecture but not yet implemented, and `Deprecated` for
flows being decommissioned. This prevents contradictions between the data flows table and the
Gap Analysis — a flow listed as Current must not also appear as a gap to be built.

</details>

*Reference diagram:* `../diagrams/{{data_flow_diagram}}`

| Flow ID | Description | Source | Destination | Frequency | State | Classification |
|---|---|---|---|---|---|---|
| DF-001 | {{description}} | {{source}} | {{destination}} | Real-time / Batch / On-demand | Current / Planned (Target) / Deprecated | {{classification}} |
| DF-002 | {{description}} | {{source}} | {{destination}} | Real-time / Batch / On-demand | Current / Planned (Target) / Deprecated | {{classification}} |

---

## 6. Data Governance

<details>
<summary>📋 Guidance</summary>

Describe the data governance arrangements relevant to this architecture. Include: data ownership
model (who is accountable for each subject area), data quality standards and how they are
enforced, master data management approach, data lineage requirements, and any regulatory
obligations (retention, right-to-erasure, cross-border transfer restrictions).

</details>

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

<details>
<summary>📋 Guidance</summary>

Summarise the key gaps between the current (baseline) data architecture and the target.
Reference the full Gap Analysis artifact for detail. Focus here on the gaps most significant
to data: missing authoritative sources, duplicated master data, ungoverned flows, quality deficits.

</details>

*See Gap Analysis artifact for full detail:* `gap-analysis.md`

| Gap ID | Description | Priority | Impact |
|---|---|---|---|
| GAP-001 | {{description}} | High / Med / Low | {{impact}} |

---

## 8. Requirements Addressed

<details>
<summary>📋 Guidance</summary>

Trace this artifact back to requirements from the Requirements Register. Demonstrate that the
data architecture decisions are driven by stated requirements, not just technical preference.

</details>

| Req ID | Requirement | How Addressed |
|---|---|---|
| {{req_id}} | {{requirement}} | {{how}} |

---

## 9. Diagrams

<details>
<summary>📋 Guidance</summary>

Standard diagrams for the Data Architecture. Individual diagram references also appear inline in §2 (Conceptual Data Model), §3 (Logical Data Model), and §5 (Data Flows). This section provides a consolidated status view. Diagrams are stored in `diagrams/` relative to the engagement root. Use `/ea-diagram` to create or edit. See `skills/ea-artifact-templates/references/diagram-catalogue.md` for Mermaid starters.

</details>

| Diagram | File | Status |
|---|---|---|
| Conceptual Data Model | `../../diagrams/data-architecture-conceptual-data-model.mmd` | ❌ Missing |
| Data Flow Diagram | `../../diagrams/data-architecture-data-flow.mmd` | ❌ Missing |

*Use `/ea-diagram` to create. Run `/ea-generate png` to render for export.*

---

---

## Appendix A3 — Decision Log

<details>
<summary>📋 Guidance</summary>

Record all decisions made during the development of this artifact.
Use /ea-decisions to aggregate this table across all artifacts into a Decision Register.

</details>

| Item | Value | State | Captured By | Owner | Authority | Domain | Cost | Impact | Risk | Subject | Date |
|---|---|---|---|---|---|---|---|---|---|---|---|
| *(no decisions recorded)* | — | — | — | — | — | — | — | — | — | — | — |

---

## Appendix A4 — Stakeholder Concerns & Objections

<details>
<summary>📋 Guidance</summary>

Record all stakeholder concerns, objections, and tough questions raised about this artifact.
Sources include grill-me sessions, Architecture Review Board feedback, executive challenge
sessions, and sponsor meetings. For each concern, record whether it is addressed in existing
documentation (Addressed / Partially Addressed) or requires further action (Requires Attention).
Use `/ea-concerns` to aggregate unresolved items across all artifacts. Concerns that represent
a material risk should also be raised as RIS-NNN entries via `/ea-risks`.

</details>

| ID | Concern | Raised By | Category | Status | Response | Action / Owner |
|---|---|---|---|---|---|---|
| *(no concerns recorded)* | — | — | — | — | — | — |


## Appendix A5 — Related Architecture Decisions

<details>
<summary>📋 Guidance</summary>

List ADRs that informed, were informed by, or are otherwise relevant to this artifact.
Reference the ADR-NNN ID so readers can navigate to the full decision record.
Use `/ea-adrs` to manage the ADR Register and surface ADR summaries.

When a significant decision is made during an interview for this artifact, the
`ea-interviewer` will suggest creating an ADR if the decision meets the threshold
criteria (technology/vendor selection, high cost/risk, hard to reverse, etc.).

</details>

| ADR ID | Title | Status | Summary |
|---|---|---|---|
| *(no related ADRs recorded)* | — | — | — |

---

*This document was created using the EA Assistant plugin.*
*Use `/ea-decisions` to generate a cross-artifact Decision Register from all A3 tables.*
*Use `/ea-concerns` to generate a cross-artifact Concerns Register from all A4 tables.*
