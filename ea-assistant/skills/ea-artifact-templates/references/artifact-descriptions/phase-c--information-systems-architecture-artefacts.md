# Phase C — Information Systems Architecture Artefacts


### Application Portfolio Catalogue

**Purpose:** A complete inventory of the application systems in scope, providing the information needed for rationalisation, gap analysis, and migration planning.

**Audience:** IT leadership, solution architects, enterprise architects, operations.

**Contents:**
- **Application Direction** — drawn from `engagement.json direction.Application`; presented in three sections:
  - *Goals* — desired application landscape state (e.g., consolidated CRM, modern API platform)
  - *Objectives* — measurable application targets (e.g., "decommission 3 legacy systems by Q2 2027")
  - *Strategies* — chosen modernisation approaches (e.g., lift-and-shift, re-platform, replace with SaaS)
  - Each application's lifecycle status (Invest / Tolerate / Migrate / Eliminate) is annotated with the direction item(s) that drove the classification
- **Application Metrics** — drawn from `engagement.json metrics.Application`; table of Application metrics grouped by type with measure, baseline → target, deadline, frequency, source, and current status
- Application ID, name, and description
- Business capabilities supported
- Technology platform and version
- Deployment model (on-premises, SaaS, PaaS, hybrid)
- Lifecycle status (Invest / Tolerate / Migrate / Eliminate)
- Owner (business and technical)
- Integration points (key inbound and outbound interfaces)
- Key data entities managed
- Known issues / technical debt

**When to Create:** Phase C (Application Architecture).

**Who Reviews:** IT leadership, application owners, enterprise architect, security architect.

**Phase:** C.

---

### Logical Data Model

**Purpose:** Documents the enterprise's key data entities, their attributes, and relationships at the logical (technology-independent) level. Provides a common data vocabulary.

**Audience:** Data architects, application architects, integration teams, business data owners.

**Contents:**
- **Data Direction** — drawn from `engagement.json direction.Data`; presented in three sections:
  - *Goals* — where the data landscape needs to be (e.g., single source of truth, improved data quality)
  - *Objectives* — measurable data targets (e.g., "reduce duplicate customer records by 90% by June 2026")
  - *Strategies* — data management approaches chosen (e.g., master data management, data mesh, data lake)
  - Entity and model design decisions are annotated to show which direction items they address
- **Data Metrics** — drawn from `engagement.json metrics.Data`; table of Data metrics grouped by type with measure, baseline → target, deadline, frequency, source, and current status
- Entity names and descriptions
- Key attributes per entity
- Primary keys and foreign key relationships
- Entity relationships (one-to-one, one-to-many, many-to-many)
- Data ownership (which business domain owns each entity)
- Related glossary terms

**When to Create:** Phase C (Data Architecture).

**Who Reviews:** Data architect, chief data officer, application architects.

**Phase:** C.

---

### Data Flow Diagram

**Purpose:** Shows how data moves between systems, processes, and actors. Used to identify data residency, integration complexity, and privacy/compliance concerns.

**Audience:** Solution architects, integration architects, security/privacy specialists.

**Contents:**
- Systems and actors as nodes
- Data flows as directed edges (labelled with data entity and protocol/mechanism)
- Transformation steps (where data is transformed in transit)
- Data residency indicators (where data is stored)
- Classification of data in flight (public / internal / confidential)

**When to Create:** Phase C.

**Who Reviews:** Solution architect, data architect, security/privacy officer.

**Phase:** C.

---
