# TOGAF ADM Artefacts to Zachman Framework Mapping

This reference maps the major artefacts produced by the TOGAF ADM to their primary cell(s) in the Zachman Framework. Understanding this mapping helps architects communicate what a given artefact represents from multiple perspectives, identify gaps in coverage, and ensure that stakeholder concerns at every Zachman row are addressed.

---

## How to Read This Mapping

Each TOGAF artefact is mapped to one or more Zachman cells using the notation **Row,Column** — for example, **R2,C1** means Row 2 (Business Owner / Conceptual) and Column 1 (What / Data).

- **Primary cell:** The cell that best describes the artefact's dominant perspective and interrogative.
- **Secondary cells:** Additional cells the artefact partially addresses or informs.

The Zachman rows used are:
- R1 — Contextual (Planner / Executive)
- R2 — Conceptual (Business Owner)
- R3 — Logical (Designer / Architect)
- R4 — Physical (Builder)
- R5 — Detailed (Implementer)

The Zachman columns are:
- C1 — What (Data)
- C2 — How (Function/Process)
- C3 — Where (Network/Location)
- C4 — Who (People/Organisation)
- C5 — When (Time/Events)
- C6 — Why (Motivation)

---

## Mapping Table — By TOGAF ADM Phase

### Preliminary Phase Artefacts

| TOGAF Artefact | Primary Zachman Cell | Secondary Cells | Notes |
|---|---|---|---|
| Architecture Principles Catalogue | R1,C6 | R2,C6 | Principles are strategic motivations constraining all architecture work |
| Architecture Governance Framework | R1,C4 | R2,C4 | Defines who is responsible for architecture decisions |
| Tailored ADM | R1,C2 | — | Defines how architecture work will be performed — a process scope |
| Architecture Repository (structure) | R1,C1 | R3,C1 | The repository structure is contextual; its content spans all cells |

---

### Phase A — Architecture Vision Artefacts

| TOGAF Artefact | Primary Zachman Cell | Secondary Cells | Notes |
|---|---|---|---|
| Architecture Vision | R2,C6 | R1,C6, R2,C2 | Expresses the desired future state in terms of business motivation and high-level capability |
| Statement of Architecture Work | R1,C2 | R1,C4, R1,C5 | Defines the scope, schedule (when), and team (who) for architecture work |
| Stakeholder Map / Matrix | R1,C4 | R2,C4 | Who is affected by the architecture — a contextual people view |
| Value Chain Diagram | R2,C2 | R1,C2 | Shows how the business creates value — a conceptual process view |
| Solution Concept Diagram | R2,C2 | R3,C2, R3,C3 | A high-level conceptual sketch of the solution — spans conceptual and logical |

---

### Phase B — Business Architecture Artefacts

| TOGAF Artefact | Primary Zachman Cell | Secondary Cells | Notes |
|---|---|---|---|
| Business Capability Map | R2,C2 | R1,C2 | What the business can do — conceptual process/function view |
| Business Interaction Matrix | R2,C4 | R2,C2 | Which business units interact — conceptual people and process view |
| Actor / Role Catalogue | R2,C4 | R3,C4 | Business roles (conceptual) feeding into system role design (logical) |
| Business Process Catalogue | R2,C2 | R3,C2 | Business process descriptions at conceptual and logical levels |
| Organisation Map | R2,C4 | R1,C4 | Organisation structure — conceptual people view |
| Business Gap Analysis | R2,C2 | R2,C6 | Gap analysis is about what is missing from process and motivation perspectives |

---

### Phase C — Information Systems Architecture Artefacts

| TOGAF Artefact | Primary Zachman Cell | Secondary Cells | Notes |
|---|---|---|---|
| Data Entity / Data Component Catalogue | R3,C1 | R2,C1 | Logical data entities; the business semantic model informs R2,C1 |
| Logical Data Model | R3,C1 | — | Classic Zachman R3,C1 artefact |
| Application Portfolio Catalogue | R3,C2 | R4,C2 | Application inventory spans logical (what it does) and physical (what it is built on) |
| Application / Data Matrix | R3,C1 | R3,C2 | Cross-cutting — relates data entities to application functions |
| Application Communication Diagram | R3,C3 | R3,C2 | How applications connect (where/network) and what they exchange |
| Data Flow Diagram | R3,C1 | R3,C2, R3,C3 | How data moves — spans data, function, and network columns |
| Data Gap Analysis | R3,C1 | — | Gaps in the logical data model |
| Application Gap Analysis | R3,C2 | R3,C3 | Gaps in application coverage and distribution |

---

### Phase D — Technology Architecture Artefacts

| TOGAF Artefact | Primary Zachman Cell | Secondary Cells | Notes |
|---|---|---|---|
| Technology Standards Catalogue | R3,C3 | R4,C3 | Standards are logical constraints; specific implementations are physical |
| Technology Portfolio Catalogue | R4,C3 | R3,C3 | Physical technology inventory — servers, platforms, network components |
| Environments and Locations Diagram | R4,C3 | R3,C3 | Physical deployment topology |
| Platform Decomposition Diagram | R4,C2 | R4,C3 | How technology functions are decomposed — physical function and network |
| Technology Gap Analysis | R4,C3 | R3,C3 | Gaps in technology coverage |

---

### Phase E — Opportunities and Solutions Artefacts

| TOGAF Artefact | Primary Zachman Cell | Secondary Cells | Notes |
|---|---|---|---|
| Architecture Roadmap (draft) | R2,C5 | R1,C5, R3,C5 | Roadmaps are primarily about when — the business owner's time perspective |
| Transition Architecture | R3,C2 | R3,C1, R3,C3 | An intermediate logical architecture state — spans all logical cells |
| Business Transformation Readiness Assessment | R2,C6 | R2,C4 | Motivation and people perspectives — capacity and willingness to change |
| Implementation Factor Assessment | R1,C6 | R2,C6 | Risks and constraints — contextual motivation |

---

### Phase F — Migration Planning Artefacts

| TOGAF Artefact | Primary Zachman Cell | Secondary Cells | Notes |
|---|---|---|---|
| Implementation and Migration Plan | R2,C5 | R1,C5, R4,C5 | Detailed when — spans business and physical timing perspectives |
| Prioritised Project List | R1,C5 | R1,C6 | When decisions are driven by priority (motivation) and timing |
| Benefits Realisation Plan | R2,C6 | R1,C6 | Goals and motivation — will the architecture achieve the intended value? |

---

### Phase G — Implementation Governance Artefacts

| TOGAF Artefact | Primary Zachman Cell | Secondary Cells | Notes |
|---|---|---|---|
| Architecture Contract | R3,C4 | R2,C4 | Who is accountable and to what standard — logical people/governance |
| Compliance Assessment | R4,C2 | R4,C1, R4,C3 | Does the physical implementation conform to the logical design? Spans multiple physical cells |
| Architecture Compliance Certificate | R4,C4 | R3,C4 | Governance artefact — who signed off what |
| Updated Architecture Repository | All cells | — | As-built: the repository contains artefacts spanning all cells |

---

### Phase H — Architecture Change Management Artefacts

| TOGAF Artefact | Primary Zachman Cell | Secondary Cells | Notes |
|---|---|---|---|
| Architecture Updates | Varies | — | Cell depends on which domain is being updated |
| Change Request Log | R2,C5 | R2,C6 | When changes occur, driven by motivation |

---

## Coverage Analysis — Zachman Cells Not Well Covered by TOGAF Artefacts

The table below identifies Zachman cells that TOGAF ADM does not naturally produce artefacts for. These are not gaps in TOGAF per se — they represent concerns that organisations must address with supplementary frameworks or methods.

| Zachman Cell | Typical Gap | Suggested Supplement |
|---|---|---|
| R3,C4 — Logical / Who (Human Interface Architecture) | TOGAF rarely produces formal human interface architecture | UX architecture, accessibility standards, role-based access design |
| R3,C5 — Logical / When (System State / Event Model) | Event-driven architecture and state machines are rarely captured | Event storming, state machine diagrams, event catalogue |
| R3,C6 — Logical / Why (Business Rule Model) | Business rules are frequently undocumented | Business Rule Management System (BRMS), decision modelling (DMN) |
| R5,Cx — Detailed (All columns) | TOGAF stops at physical; as-built detail is out of scope | Configuration management database (CMDB), infrastructure-as-code |

---

## Using This Mapping in Practice

### Completeness Check
At the end of each ADM phase, use the mapping to check which Zachman cells have been addressed. Cells with no artefacts may represent acceptable scoping decisions or genuine gaps requiring attention.

### Stakeholder Communication
Use the Zachman row to identify which stakeholders should review a given artefact:
- R1 artefacts: Executive sponsors, programme governance
- R2 artefacts: Business owners, process owners, capability leads
- R3 artefacts: Solution architects, technical leads
- R4 artefacts: Developers, infrastructure engineers
- R5 artefacts: Operations, security, deployment teams

### Traceability
The mapping provides a traceability chain from business motivation (R1,C6) through to implementation detail (R5). When an implementation decision is challenged, trace back through the cells to the original strategic driver.

### Identifying Missing Artefacts
If a stakeholder raises a concern and no artefact addresses it, identify the Zachman cell for that concern and use the cell description to determine what artefact should be produced.
