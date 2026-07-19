# Phase C — Information Systems Architecture


### Objectives
- Develop the Baseline and Target Data Architecture and Application Architecture.
- This phase has two sub-phases: Data Architecture and Application Architecture (order may vary).

### Key Inputs
- Architecture Vision, Business Architecture outputs
- Baseline data and application assets
- Relevant standards and reference models (e.g., industry data models)

### Major Steps
1. Select reference models, viewpoints, and tools.
2. Develop Baseline Data Architecture.
3. Develop Target Data Architecture.
4. Develop Baseline Application Architecture.
5. Develop Target Application Architecture.
6. Perform gap analysis for data and applications.
7. Identify candidate roadmap components.

### Key Questions
- What data does the business depend on, and who owns it?
- What are the critical data quality and integrity concerns?
- What applications support which business capabilities?
- What systems are redundant, legacy, or to be decommissioned?
- How will data flow across the target application landscape?

### Artefacts Produced
| Artefact | Description |
|---|---|
| Data Entity / Data Component Catalogue | Canonical list of data entities and their owners |
| Application Portfolio Catalogue | Inventory of applications with lifecycle status |
| Data Flow Diagram | How data moves between systems and actors |
| Application / Data Matrix | Which apps handle which data entities |
| Data Gap Analysis | Data capability gaps |
| Application Gap Analysis | Application capability gaps |
| Logical Data Model | Entity-relationship model at the logical level |
| Application Communication Diagram | Integration and interface map |

### Deep Tactics
- Treat **data as a product** — define clear ownership, quality SLAs, and lifecycle governance for every critical data entity.
- Design **interoperability early** — specify API contracts, event schemas, and integration patterns before selecting tools.
- **Rationalize applications with measurable criteria** — retirement decisions need cost, risk, and duplication metrics, not just age.
- Adopt **domain-oriented architectures** — align data and application boundaries with business domains to reduce coupling.
- Enforce **clear boundaries** between data domains; ambiguous ownership creates silent integration debt.

### Hidden Mechanics
- Phase C is where **future integration cost is locked in**. Poor boundary decisions here multiply across every downstream phase.
- Data architecture is a **power structure** — who owns what data determines who has authority in the organization.

### Maturity Indicators
- **L1:** Application inventory is a spreadsheet; data models are IT-owned
- **L3:** Data domains have owners and quality SLAs; APIs are contract-first; application rationalization uses cost/risk metrics
- **L5:** Data products are self-serve with automated quality checks; domain boundaries are continuously refined based on usage patterns

---
