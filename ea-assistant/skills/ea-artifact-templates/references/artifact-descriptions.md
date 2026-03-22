# EA Artifact Descriptions — Reference

This reference describes each TOGAF-aligned architecture artefact supported by the EA Assistant. For each artefact it provides: purpose, intended audience, contents, when to create it, who reviews it, and which ADM phase it primarily belongs to.

---

## How to Use This Reference

Artefacts are listed by ADM phase. Where an artefact spans multiple phases (e.g., the Architecture Requirements Specification is updated in Phases B, C, and D), it is documented in the phase where it is first created and cross-referenced for subsequent phases.

---

## Preliminary Phase Artefacts

### Architecture Principles Catalogue

**Purpose:** Documents the set of normative statements that govern all future architecture decisions for the enterprise. Principles act as decision filters when selecting between design options.

**Audience:** Architecture governance board, enterprise architects, solution architects, business leadership.

**Contents:**
- Principle ID and Name
- Statement (the principle itself, in one declarative sentence)
- Rationale (why this principle is important)
- Implications (what this means for architects, developers, and the business)
- Owner (who is accountable for upholding this principle)
- Status (Proposed / Approved / Retired)

**When to Create:** At the start of the architecture programme, during the Preliminary Phase. Updated when new strategic direction, regulations, or technology landscape changes warrant revision.

**Who Reviews:** Chief Architect, CTO/CIO, Architecture Review Board, Business Leadership.

**Phase:** Preliminary (created); updated throughout the ADM lifecycle.

---

### Architecture Governance Framework

**Purpose:** Defines how architecture decisions are made, communicated, and enforced. Sets out the structure of the Architecture Review Board (ARB), decision-making processes, escalation paths, and compliance expectations.

**Audience:** All architecture stakeholders; particularly project managers and delivery teams who need to understand governance touchpoints.

**Contents:**
- Governance structure and the ARB's terms of reference
- Architecture decision-making process (who decides what)
- Compliance checking process and schedule
- Waiver and exception process
- Roles and responsibilities (architect, ARB chair, project EA liaison)
- Reference to Architecture Principles and Standards

**When to Create:** During the Preliminary Phase before any project-specific architecture work begins.

**Who Reviews:** Executive leadership, CTO/CIO, Enterprise Architecture team.

**Phase:** Preliminary.

---

## Phase A — Architecture Vision Artefacts

### Architecture Vision

**Purpose:** Provides a high-level, stakeholder-oriented description of the target architecture and the value it will deliver. It is the primary communication document for executive and business stakeholders.

**Audience:** Executive sponsors, programme sponsors, senior business and IT stakeholders.

**Contents:**
- Executive summary of the problem being solved
- **Direction Summary** — cross-domain table drawn from `engagement.json direction`, listing all goals, objectives, and strategies across all selected domains with their priority and (for strategies) which goals/objectives they support; items with no `statement` are excluded. Present in three grouped sections: Goals / Objectives / Strategies. Include a brief definition of each term at the top of the section to orient readers who may be unfamiliar with the distinction.
- **Metrics Summary** — cross-domain table drawn from `engagement.json metrics`, listing all metrics grouped by type (Outcome / Performance / Activity), showing name, measure, baseline → target, deadline, frequency, source, linked direction ID, and current status. Metrics with no `name` or `measure` are excluded.
- Business goals and strategic drivers
- Scope of the architecture engagement
- High-level description of the target state (narrative, not technical)
- Key stakeholder concerns and how the architecture addresses them
- Preliminary risk and constraint identification
- Solution Concept Diagram (high-level visual)
- Proposed approach and timeline summary

**When to Create:** Phase A. Produced before detailed architecture work begins; used to obtain sponsorship approval to proceed.

**Who Reviews:** Programme sponsor, key business stakeholders, Architecture Review Board.

**Phase:** A.

---

### Statement of Architecture Work

**Purpose:** A formal agreement between the architecture team and the commissioning organisation that defines the scope, schedule, deliverables, resources, and acceptance criteria for the architecture engagement.

**Audience:** Programme sponsor, architecture team, project management, governance body.

**Contents:**
- Organisation and project sponsors
- Architecture engagement scope (business domains, systems, geographies in/out of scope)
- Constraints and assumptions
- Architecture deliverables list with due dates
- Resource requirements
- Review and acceptance process
- Risks

**When to Create:** Phase A, concurrent with the Architecture Vision. Signed off by the sponsor before Phase B begins.

**Who Reviews:** Programme sponsor, architecture team lead, project manager.

**Phase:** A.

---

### Stakeholder Map and Matrix

**Purpose:** Identifies all stakeholders relevant to the architecture engagement, their concerns, interest, and influence, and defines the engagement strategy for each.

**Audience:** Architecture team (internal reference); summary versions shared with programme management.

**Contents:**
- Stakeholder name and role
- Organisation / business unit
- Interest in the architecture (what they care about)
- Concerns (specific worries or questions)
- Influence level (High / Medium / Low)
- Engagement approach (inform, consult, collaborate, empower)
- Communication plan notes

**When to Create:** Phase A. Updated throughout the engagement as new stakeholders are identified.

**Who Reviews:** Architecture team, programme manager.

**Phase:** A (updated throughout).

---

## Phase B — Business Architecture Artefacts

### Business Capability Map

**Purpose:** Provides a hierarchical view of what the enterprise can do (capabilities), independent of how those capabilities are currently implemented. Used to identify capability gaps, investment priorities, and technology alignment.

**Audience:** Business owners, strategy teams, enterprise architects.

**Contents:**
- **Business Direction** — drawn from `engagement.json direction.Business`; presented in three sections:
  - *Goals* (where the business wants to be) — each with ID, statement, priority
  - *Objectives* (measurable targets) — each with ID, statement, measure, target value, deadline, priority
  - *Strategies* (approaches chosen) — each with ID, statement, the goal/objective IDs it supports, priority
  - Capabilities in the map are then annotated to show which goals and objectives they support, and which strategies they enable
- **Business Metrics** — drawn from `engagement.json metrics.Business`; a table of all Business metrics with type, measure, baseline → target, deadline, frequency, source, and current status. Group by type: Outcome (tracks goals) / Performance (tracks objectives) / Activity (tracks strategies)
- Level 1 capability areas (e.g., "Customer Management", "Finance", "Supply Chain")
- Level 2 and Level 3 capability decomposition
- Heat mapping: optional colour coding to show maturity, investment priority, or gap status; goal-driven priority takes precedence
- Mapping of capabilities to supporting applications (optional cross-reference)

**When to Create:** Phase B. Often derived from or cross-validated against industry reference models (BIAN, eTOM, APQC PCF).

**Who Reviews:** Business owners, enterprise architect, programme sponsor.

**Phase:** B.

---

### Business Process Catalogue

**Purpose:** An inventory of the business processes in scope, providing enough detail to understand what the business does and to identify where process change is required.

**Audience:** Business analysts, process owners, enterprise architects.

**Contents:**
- Process ID and name
- Process description
- Triggering event
- Inputs and outputs
- Roles / actors involved
- Systems used
- KPIs / measures
- Pain points or known issues (baseline processes)

**When to Create:** Phase B.

**Who Reviews:** Process owners, business analysts, solution architects.

**Phase:** B.

---

### Organisation Map

**Purpose:** Shows the organisational structure of the enterprise as relevant to the architecture scope, including business units, their relationships, and key roles.

**Audience:** Business architects, HR, programme sponsors.

**Contents:**
- Business units / departments in scope
- Reporting relationships
- Key roles within each unit (architecture-relevant roles)
- Geographic distribution of units
- External partners and their organisational relationship

**When to Create:** Phase B.

**Who Reviews:** HR, business leadership, architecture team.

**Phase:** B.

---

## Phase C — Information Systems Architecture Artefacts

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

## Phase D — Technology Architecture Artefacts

### Technology Standards Catalogue

**Purpose:** Documents the approved technology standards, products, and versions that all architecture and implementation work must conform to.

**Audience:** Solution architects, developers, infrastructure engineers, procurement.

**Contents:**
- **Technology Direction** — drawn from `engagement.json direction.Technology`; presented in three sections:
  - *Goals* — desired technology state (e.g., "cloud-native platform", "zero-trust security posture")
  - *Objectives* — measurable technology targets (e.g., "achieve 99.9% availability for Tier-1 systems by Q3 2026")
  - *Strategies* — chosen technology approaches (e.g., cloud-first, containerisation, open-source preferred)
- Technology domain (e.g., Database, Middleware, Identity, Compute)
- Standard name and product/technology
- Approved versions
- Rationale for selection (including which Technology direction items the standard supports)
- **Technology Metrics** — drawn from `engagement.json metrics.Technology`; table of Technology metrics grouped by type with measure, baseline → target, deadline, frequency, source, and current status
- Exceptions process
- Review/expiry date

**When to Create:** Phase D (may originate in Preliminary if standards pre-exist).

**Who Reviews:** CTO, architecture review board, security team.

**Phase:** D (Preliminary for pre-existing standards).

---

### Environments and Locations Diagram

**Purpose:** Shows the physical and logical deployment topology of the architecture: data centres, cloud regions, network zones, and how they interconnect.

**Audience:** Infrastructure architects, security architects, operations teams.

**Contents:**
- Data centres / cloud regions / edge locations
- Network zones and security tiers (DMZ, internal, management)
- High-level server / cluster placement
- Communication paths and protocols between locations
- External network connections (internet, partner links, regulatory networks)

**When to Create:** Phase D.

**Who Reviews:** Infrastructure architect, network architect, security architect.

**Phase:** D.

---

## Phase E / F — Roadmap Artefacts

### Architecture Roadmap

**Purpose:** A sequenced, prioritised plan that shows how the architecture will evolve from its current baseline through one or more transition states to the target architecture. Connects architecture decisions to delivery projects.

**Audience:** Programme sponsors, project managers, business stakeholders, delivery teams.

**Contents:**
- Timeline (typically quarterly or by milestone)
- Work packages / initiatives, sequenced and prioritised
- Dependencies between work packages
- Transition architectures at key milestones
- Benefits expected at each stage
- Owner for each work package

**When to Create:** Phase E (draft), Phase F (finalised).

**Who Reviews:** Programme sponsor, project management office, architecture review board, business stakeholders.

**Phase:** E (draft), F (finalised).

---

## Phase G — Governance Artefacts

### Architecture Compliance Assessment

**Purpose:** A formal review of a project's deliverables or a solution design against the approved architecture. Documents the degree of conformance and any approved variances.

**Audience:** Architecture review board, project managers, delivery leads.

**Contents:**
- Project name and scope
- Architecture principles assessment (conformant / partial / non-conformant for each principle)
- Architecture standards assessment (conformant / exception approved / non-conformant)
- Approved variances with justification
- Outstanding risks
- Assessment outcome (Fully Conformant / Conditionally Conformant / Non-Conformant)
- Reviewer and date

**When to Create:** Phase G, at defined project milestones (design review, pre-build, pre-deploy).

**Who Reviews:** Architecture Review Board.

**Phase:** G.

---

### Architecture Requirements Specification

**Purpose:** The definitive, consolidated specification of all architecture requirements for the engagement: functional, non-functional, constraints, principles, and assumptions.

**Audience:** Delivery teams, solution architects, QA leads, project managers.

**Contents:**
- Functional requirements register
- Non-functional requirements register
- Constraints register
- Assumptions register
- Traceability to business goals and architectural decisions

**When to Create:** Initiated in Phase A, populated and refined in Phases B, C, and D. Baseline is signed off before Phase G.

**Who Reviews:** Business stakeholders (functional requirements), technical leads (NFRs), programme sponsor (constraints and assumptions).

**Phase:** A–D (populated), G (baselined for compliance checking).
