# EA Artifact Descriptions — Reference

This reference describes each TOGAF-aligned architecture artefact supported by the EA Assistant. For each artefact it provides: purpose, intended audience, contents, when to create it, who reviews it, and which ADM phase it primarily belongs to.

---

## How to Use This Reference

Artefacts are listed by ADM phase. Where an artefact spans multiple phases (e.g., the Architecture Requirements Specification is updated in Phases B, C, and D), it is documented in the phase where it is first created and cross-referenced for subsequent phases.

---

## Preliminary Phase Artefacts

### Engagement Charter

**Purpose:** The foundational Preliminary Phase artifact. Establishes the authoritative record of why the engagement exists, what it covers, who it affects, how it is structured, and what it is expected to deliver. It is the mandate document — without it, scope, benefits, and governance are undefined. Subsequent artifacts build on the Charter's foundation.

**Audience:** Executive sponsors, programme directors, architecture governance board, key business stakeholders.

**Contents:**
- Organisation background (profile, history, current state)
- Engagement purpose and formal mandate (with authorisation reference)
- Scope and boundaries (in-scope, out-of-scope, assumptions, constraints)
- Relationship to other engagements and programmes (dependency map)
- Organisations affected (internal divisions, external partners, regulators)
- Motivation framework: Vision, Mission, Business Drivers (DRV-NNN), Goals (G-NNN), Objectives (OBJ-NNN), Strategies (STR-NNN), Issues (ISS-NNN), Problems (PRB-NNN)
- Programme structure (phases: planning, preparation, procurement, pilot, implementation waves, post-implementation)
- Expected outcomes (outputs, outcomes, impacts)
- Benefits (financial and non-financial, with owners and realisation phases)
- Costs (by category, one-time and ongoing, budget reference)
- Initial risk profile (high-level risks with ratings, mitigations, and owners)
- Key stakeholders (seed for the Phase A Stakeholder Map)
- Approval and sign-off

**When to Create:** At the very start of the Preliminary Phase, before any domain architecture work begins. The Charter must be approved before Phase A commences. Updated when scope, objectives, programme structure, or sponsor changes.

**Who Reviews:** Programme Sponsor, Architecture Review Board Chair, Programme Director. Must be formally approved by the sponsor.

**Phase:** Preliminary (first artifact created; baseline for all subsequent work).

**Template:** `engagement-charter.md` — create with `/ea-artifact create engagement-charter`.

---

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

**Template:** `governance-framework.md` — create with `/ea-artifact create governance-framework`.

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
- Strategic Alignment table — every G-NNN, OBJ-NNN, STR-NNN from Phase A mapped to covering Work Packages
- Timeline (typically quarterly or by milestone)
- Work packages / initiatives, sequenced and prioritised — each WP links to the Goals/Objectives it advances and the Strategies it executes
- Dependencies between work packages
- Transition architectures at key milestones
- Benefits expected at each stage
- Owner for each work package

**When to Create:** Phase E (draft), Phase F (finalised).

**Who Reviews:** Programme sponsor, project management office, architecture review board, business stakeholders.

**Phase:** E (draft), F (finalised).

---

### Risk Register

**Purpose:** A cross-cutting artifact that aggregates and tracks all architecture risks across the engagement — from initial identification in the Architecture Vision through to delivery in the Migration Plan. Provides a single authoritative view of risk status, ownership, and mitigation across all phases.

**Audience:** Programme sponsor, enterprise architect, architecture review board, risk manager, delivery teams.

**Contents:**
- Risk summary (counts by rating and status)
- Risks grouped by rating: Critical, High, Medium, Low
- Per risk: RIS-NNN ID, description, likelihood, impact, derived rating, source artifact, ADM phase identified, affected objectives (G-NNN / OBJ-NNN), mitigation, contingency, owner, status, last reviewed date
- Risk heatmap summary (likelihood × impact matrix populated with RIS-NNN IDs)
- Source artifact cross-reference (which artifacts contributed risks)
- Closed/Accepted risks retained for audit

**Risk Rating Matrix:**
- Critical: High likelihood + High impact
- High: High + Medium OR Medium + High
- Medium: Medium + Medium OR High + Low OR Low + High
- Low: Medium + Low OR Low + Medium OR Low + Low

**Risk Statuses:** Open / Monitoring / Accepted / Closed

**When to Create:** After Phase A (initial risks from Architecture Vision and Statement of Architecture Work). Refreshed at each phase gate and whenever a new risk source artifact is updated. Use `/ea-risks generate` to auto-aggregate from all artifacts.

**Who Reviews:** Programme sponsor, architecture review board, risk manager.

**Phase:** Cross-cutting (first generated in Phase A; updated throughout the engagement).

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

### Implementation Governance Plan

**Purpose:** Translates the Architecture Governance Framework into a concrete, engagement-specific schedule of reviews, checkpoints, and ownership assignments tied to this programme's work packages. Where the Governance Framework defines permanent enterprise governance structures, the Implementation Governance Plan defines how governance will be executed for this specific delivery.

**Audience:** Programme managers, delivery leads, project EA liaisons, governance authority.

**Contents:**
- Governance scope and objectives
- Named governance contacts for each role (no anonymous roles)
- Review schedule tied to delivery milestones per work package
- Compliance checkpoint process (preparation, review, gate decision)
- Waiver and exception process
- Change request process and volume thresholds
- Escalation paths
- Reporting metrics and governance calendar

**When to Create:** At the start of Phase G, before the first architecture review gate. Update when the delivery schedule changes significantly or new work packages enter scope.

**Who Reviews:** Governance Authority, Lead Architect, Programme Manager.

**Phase:** G.

**Template:** `implementation-governance-plan.md` — create with `/ea-artifact create implementation-governance-plan`.

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

---

## Phase H — Architecture Change Management Artefacts

### Architecture Change Request

**Purpose:** A formal request to deviate from, or update, the agreed target architecture. Ensures that proposed changes are assessed for architectural impact before being approved, preventing uncontrolled architectural drift.

**Audience:** Architecture Review Board, governance authority, delivery leads, Lead Architect.

**Contents:**
- Change description and type
- Justification and consequence of not changing
- Impact assessment across all architecture domains
- Risk assessment
- Disposition (approved / rejected / deferred / approved with conditions)
- List of artifacts requiring update if approved

**When to Create:** Phase H — raised whenever a business event, technology change, or implementation learning requires a deviation from or update to the agreed architecture. May also be raised during Phase G when a compliance issue cannot be resolved by remediation alone.

**Who Reviews:** Lead Architect (initial assessment), Governance Authority or ARB (disposition decision).

**Phase:** H (also raised in G for significant compliance deviations).

**Template:** `change-request.md` — create with `/ea-artifact create change-request`.

---

### Change Register

**Purpose:** Aggregates all Architecture Change Request artifacts for the engagement into a single cross-engagement view. Provides a consolidated picture of proposed, approved, rejected, and deferred changes to the architecture, including change impact on existing artifacts.

**Audience:** Governance Authority, Lead Architect, Programme Manager.

**Contents:**
- Summary counts by status and type
- Open (under review) change requests
- Approved and conditionally approved changes
- Rejected and deferred changes
- Change impact summary (which artifacts are most affected)
- Source cross-reference (one row per ACR artifact)

**When to Create:** On demand via `/ea-changes`. Regenerated whenever ACR artifacts are updated — do not edit directly.

**Who Reviews:** Governance Authority, Lead Architect.

**Phase:** H (cross-cutting — aggregates ACRs from throughout the engagement).

**Template:** `change-register.md` — generated by `/ea-changes`.

---

## Cross-Cutting Architecture Decision Artefacts

### Architecture Decision Record (ADR)

**Purpose:** A standalone document capturing a significant architecture decision — one that has lasting consequences, involves meaningful trade-offs, or requires full options analysis and documented rationale. ADRs exist so that future architects understand why things are the way they are and what constraints they are working within.

**Audience:** Architecture team, Lead Architect, Architecture Review Board, future solution architects and developers working in the same domain.

**Contents:**
- Status lifecycle history (Candidate → In Progress → Completed → Superseded / Deprecated)
- Context — the situation that forces the decision; linked drivers and goals
- Decision drivers — evaluation criteria ordered by must-have / should / nice-to-have
- Options considered — at least two options with pros/cons and driver assessments
- Decision — unambiguous statement of the chosen option and governance reference
- Rationale — why the chosen option was selected; accepted trade-offs
- Consequences — positive, negative, risks introduced (RIS-NNN links), new decisions required
- Related Architecture Decisions — ADR-to-ADR relationships
- Affected Artifacts — which artifacts are materially impacted

**When to Create:** When a significant decision is made at any phase — particularly for technology or vendor selection, architecture pattern choices, make-vs-buy decisions, data governance approaches, security architecture decisions, or any decision that is hard to reverse. Use `/ea-adrs new` to create a new ADR. The `ea-interviewer` will suggest an ADR when a decision recorded in A3 meets threshold criteria (high cost, high risk, vendor/technology selection, or contested by stakeholders).

**Who Reviews:** Lead Architect, Architecture Review Board, stakeholders with authority over the affected domain.

**Phase:** Any — ADRs are created whenever significant decisions are made throughout the ADM.

**Template:** `architecture-decision-record.md` — create with `/ea-adrs new`.

---

### ADR Register

**Purpose:** Cross-cutting aggregate artifact listing all Architecture Decision Records for the engagement. Provides a single navigable view of all ADRs by phase, status, and lifecycle state. Enables ADR portfolio management — tracking which decisions are open (Candidate / In Progress), which are completed, and which have been superseded.

**Audience:** Lead Architect, Architecture Review Board, programme governance.

**Contents:**
- Summary table by lifecycle status (count by Candidate / In Progress / Completed / Superseded / Deprecated)
- Phase-by-phase ADR table (all phases, Preliminary through H and cross-phase)
- Open ADRs table — Candidate and In Progress requiring action
- Completed ADRs table — decided and documented
- Superseded ADRs — with supersession chain links
- ADR — artifact impact map (which artifacts each ADR affects)
- Decision chain / supersession tree

**When to Create:** On demand via `/ea-adrs generate`. Regenerated whenever ADR files are created or updated — do not edit the register directly.

**Who Reviews:** Lead Architect, Architecture Review Board.

**Phase:** Cross-cutting — aggregates ADRs from all phases.

**Template:** `adr-register.md` — generated by `/ea-adrs generate`.

