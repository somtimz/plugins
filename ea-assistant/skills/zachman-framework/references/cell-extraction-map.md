# Zachman Cell Extraction Map

Defines which source artifacts and sections feed each cell when auto-populating the Zachman Diagram.

## Cell → Source Artifact Mapping

| Cell | Source Artifacts | Sections / Fields |
|---|---|---|
| R1,C1 | Architecture Vision, Engagement Charter | §1 Organisation Background, §3 Scope — in-scope subject areas |
| R1,C2 | Architecture Vision, Engagement Charter | §3 Scope in-scope processes, §2 Business Drivers process scope |
| R1,C3 | Architecture Vision, Engagement Charter | §3 Scope locations, §1 Organisation Background geography |
| R1,C4 | Stakeholder Map, Engagement Charter | All stakeholder rows; §5 Organisations Affected |
| R1,C5 | Engagement Charter, Architecture Vision | §7 Programme Structure phase table; scope constraints on timing |
| R1,C6 | Architecture Vision, Engagement Charter | §2 DRV-NNN, §3 G-NNN, §4 OBJ-NNN, §7 STR-NNN; §6 Motivation Framework |
| R2,C1 | Data Architecture, Business Architecture | §2 Conceptual Data Model, §4 Data Entity Catalogue |
| R2,C2 | Business Architecture, Business Model Canvas | §3 Capability Model, §4 Business Process Catalogue, Value Propositions, Key Activities |
| R2,C3 | Business Architecture | §5 Business Logistics / Location model |
| R2,C4 | Business Architecture, Stakeholder Map | §6 Organisation Model, Role Catalogue |
| R2,C5 | Business Architecture, Architecture Roadmap | §4 Business Event Cycles, milestone sequence |
| R2,C6 | Architecture Vision, Requirements Register | §5 ISS-NNN, §6 PRB-NNN, §7 STR-NNN; Motivation column |
| R3,C1 | Data Architecture | §3 Logical Data Model, §4 Data Entity Catalogue |
| R3,C2 | Application Architecture | §3 Application Portfolio, §4 Application Function Catalogue |
| R3,C3 | Application Architecture | §6 Application Communication Diagram, §5 Integration Architecture |
| R3,C4 | Application Architecture, Business Architecture | §7 Role–Application Matrix, §8 Access Control Model |
| R3,C5 | Application Architecture | §8 Processing Architecture, any state machine or event-driven diagrams |
| R3,C6 | Requirements Register, Data Architecture | Constraint-type REQ-NNN entries; §5 Data Governance rules |
| R4,C1 | Data Architecture | §6 Physical Data Model, Data Dictionary |
| R4,C2 | Application Architecture, Technology Architecture | §9 Component Design, §4 Platform Design |
| R4,C3 | Technology Architecture | §3 Infrastructure Model, §4 Network Topology, §5 Platform Catalogue |
| R4,C4 | Application Architecture, Technology Architecture | §10 UI Architecture, §6 Security Architecture |
| R4,C5 | Technology Architecture, Migration Plan | §7 Integration Architecture, §3 Wave Plan |
| R4,C6 | Application Architecture, Technology Architecture | Rule engine design, policy enforcement |
| R5,Cx | All | Reference delivery repository / CMDB — record reference only; do not extract content |

## Coverage Classification

| Symbol | Meaning |
|---|---|
| ✅ Populated | At least one substantive content item extracted |
| ⚠️ Partial | Content extracted but sparse (< 3 items, or all placeholder text) |
| ❌ Empty | No content found in any source artifact |
| 🚫 Out of scope | Cell deliberately excluded (Row 6, or scoped-out domain) |

## Artifact → Cell Relationship

When working on an EA artifact, it primarily populates these Zachman cells:

| Artifact | Primary Cells |
|---|---|
| Architecture Vision (Phase A) | R1,C6 and R2,C6 — goals, drivers, strategies |
| Stakeholder Map (Phase A) | R1,C4 — contextual people |
| Business Architecture (Phase B) | R2,C2, R2,C4, R2,C6 — process, organisation, strategy |
| Data Architecture (Phase C) | R2,C1, R3,C1, R4,C1 — semantic, logical, physical data |
| Application Architecture (Phase C) | R3,C2, R3,C3, R3,C4 — functions, distribution, roles |
| Technology Architecture (Phase D) | R4,C3, R4,C2, R4,C4 — infrastructure, design, presentation |
| Requirements Register | R2,C6, R3,C6 — motivation and business rules |
| Architecture Roadmap (Phase E) | R2,C5 — business event cycle / timing |
| Migration Plan (Phase F) | R4,C5 — control structure / timing |
| Gap Analysis | All rows — identifies missing cells |
