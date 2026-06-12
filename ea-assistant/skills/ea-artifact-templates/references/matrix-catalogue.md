# TOGAF Matrix Catalogue

Single source of truth for all TOGAF 10 relationship matrices. Consumed by:
- `/ea-matrix` — `list`, `new` (axis seeding), `edit`, `check`
- `/ea-interview` phase mode — matrix offer + elicitation questions
- `/ea-brainstorm` — `[Matrix]` context hints
- `/ea-grill` — recommended-matrices advisory block + matrix grilling

A **matrix** is a grid artifact exposing relationships between architecture elements. Catalogs list things, diagrams visualize things, matrices expose relationships between things. Use a matrix when the relationship is too dense for a diagram (e.g. CRUD across a large application estate).

Matrices are recommended, not mandated — presence checks are always advisory (TOGAF tailoring applies).

**Entry fields:**
- **Key** — slug used by commands. File name is `{key}-matrix.md` in the phase folder.
- **Axes** — row entity × column entity, with ID prefixes where they exist.
- **Seed sources** — engagement files scanned to propose row/column candidates (paths relative to `EA-projects/{slug}/`).
- **Markers** — the legal cell vocabulary. Cells may combine markers (e.g. `CRU`). Empty cell = no relationship.
- **Grill checks** — testable statements run by `/ea-grill` and `/ea-matrix check`.
- **Elicitation questions** — prompts used by `/ea-interview` and `/ea-brainstorm`.

Entries marked **Managed by:** are not handled by `/ea-matrix` — follow the pointer.

---

## Phase Index

| Phase | Matrices (keys) |
|---|---|
| Preliminary | `principle-decision` |
| A | Stakeholder Map Matrix (managed elsewhere) |
| B | `business-interaction`, `actor-role`, `capability-organization`, `capability-value-stream`, `capability-application` |
| C-Data | `data-function`, `app-data` |
| C-App | `app-organization`, `role-application`, `app-function`, `app-interaction`, `capability-application` |
| D | `system-technology` |
| E / F | `wp-dependency`, Work Package / Gap (managed elsewhere) |
| Requirements / Cross-cutting | Requirements Traceability Matrix, Requirement / Work Package (both managed elsewhere) |

> `capability-application` spans Phases B and C-App (single file in `artifacts/phase-b/`); it appears in both rows above by design.

---

## Managed by `/ea-matrix` (14)

### principle-decision — Principle / Decision Matrix
- **Phase:** Preliminary / Cross-cutting · **Folder:** `artifacts/preliminary/` · **File:** `principle-decision-matrix.md`
- **Axes:** rows = architecture principles (BP/DP/AP/TP-NNN), columns = decisions (ADR-NNN and Strategic A3 entries)
- **Seed sources:** rows — `artifacts/preliminary/architecture-principles.md`; columns — `artifacts/cross-cutting/governance/adr-register.md` and `artifacts/cross-cutting/governance/decision-register.md`
- **Markers:** `S` supports · `X` constrains · `E` exception granted · `C` conflict · `?` requires review
- **Shows:** which architecture decisions support, constrain, or conflict with architecture principles
- **Why:** strengthens governance and makes decision rationale visible
- **How:** put principles on rows, decisions on columns; mark each intersection; route every `C` and `E` to the Observations section with the resolution or exception authority
- **Grill checks:**
  1. Every `C` (conflict) cell has a corresponding entry in `## Observations` naming the resolution or escalation path.
  2. Every `E` (exception) cell names the granting authority in `## Observations`.
  3. No ADR with status Completed (per the Status column in `artifacts/cross-cutting/governance/adr-register.md`) is absent from the columns — an unassessed completed decision is a governance gap.
- **Elicitation questions:**
  1. "Does {decision} support or strain any of your architecture principles?"
  2. "Have any exceptions to principles been granted for this decision — and who approved them?"

### business-interaction — Business Interaction Matrix
- **Phase:** B · **Folder:** `artifacts/phase-b/` · **File:** `business-interaction-matrix.md`
- **Axes:** rows = business functions or organization units, columns = the same set (square matrix)
- **Seed sources:** both axes — `artifacts/phase-b/business-architecture.md` function catalogue and organization sections
- **Markers:** `P` provides service to · `D` depends on · `G` governs · `C` collaborates with
- **Shows:** relationships and interactions between organizations, business units, business functions, or services
- **Why:** exposes cross-functional dependencies, handoffs, service relationships, and organizational complexity
- **How:** same entity set on both axes; read row → column (e.g. row Finance, column Procurement, cell `D` = Finance depends on Procurement); note interaction strength or pain points in Observations
- **Grill checks:**
  1. The matrix is square — row and column sets are identical.
  2. No function row is entirely empty in both its row and its column — an isolated function suggests a scoping error.
  3. Mutual `D` pairs (A depends on B and B depends on A) are listed in `## Observations` as coupling risks.
- **Elicitation questions:**
  1. "Which business functions does {function} depend on to operate?"
  2. "Who provides services to whom between {A} and {B} — or do they only collaborate?"

### actor-role — Actor / Role Matrix
- **Phase:** B · **Folder:** `artifacts/phase-b/` · **File:** `actor-role-matrix.md`
- **Axes:** rows = actors (named people, teams, or organizational actors), columns = roles (ROLE-NNN)
- **Seed sources:** rows — `artifacts/phase-a/stakeholder-map.md` and `artifacts/phase-b/business-architecture.md` actor sections; columns — `artifacts/cross-cutting/context/role-catalogue.md`
- **Markers:** `P` primary performer · `S` secondary performer · `A` approving / accountable · `C` consulted
- **Shows:** which actors perform which roles
- **Why:** separates actors from the roles they play — supports accountability, access design, process design, and operating model work
- **How:** list actors on rows, ROLE-NNN on columns; mark the relationship; exactly one `A` per role keeps accountability single-threaded
- **Grill checks:**
  1. Every ROLE-NNN column has at least one `P` — a role nobody performs is unstaffed.
  2. No role column has more than one `A` — split accountability must be flagged in `## Observations`.
  3. Every actor row references an actor present in the stakeholder map or business architecture.
- **Elicitation questions:**
  1. "Who actually performs the {role} role today — and who is accountable for it?"
  2. "Does any single actor hold so many roles that they are a key-person risk?"

### capability-organization — Capability / Organization Matrix
- **Phase:** B · **Folder:** `artifacts/phase-b/` · **File:** `capability-organization-matrix.md`
- **Axes:** rows = capabilities (CAP-NNN), columns = organization units
- **Seed sources:** rows — `artifacts/phase-b/business-architecture.md` capability model (CAP-NNN tokens); columns — same artifact, organization sections
- **Markers:** `O` accountable owner · `P` performer · `C` consumer · `G` governance responsibility
- **Shows:** which organizational units own, perform, or depend on capabilities
- **Why:** clarifies accountability and operating model alignment — useful when Phase B includes capability-based planning
- **How:** CAP-NNN on rows, org units on columns; exactly one `O` per capability; performers and consumers may be many
- **Grill checks:**
  1. Every CAP-NNN row has exactly one `O` — zero means unowned capability, two or more means contested ownership.
  2. Every capability in the engagement's capability model appears as a row (no orphan capabilities).
- **Elicitation questions:**
  1. "Which organization unit is accountable for {capability} — and who actually performs it?"
  2. "Are there capabilities where ownership is contested or unclear?"

### capability-value-stream — Capability / Value Stream Matrix
- **Phase:** B · **Folder:** `artifacts/phase-b/` · **File:** `capability-value-stream-matrix.md`
- **Axes:** rows = value stream stages (VS-NNN, stage-level), columns = capabilities (CAP-NNN)
- **Seed sources:** rows — `artifacts/phase-b/business-architecture.md` value stream sections (VS-NNN tokens); columns — same artifact, capability model
- **Markers:** `E` enabling · `D` differentiating · `W` weak · `M` missing · `T` target-state
- **Shows:** which capabilities enable each value stream stage
- **Why:** shows which capabilities are needed to deliver business outcomes
- **How:** stages on rows, capabilities on columns; mark how each capability serves each stage; `W` and `M` cells are direct gap-analysis inputs
- **Grill checks:**
  1. Every value stream stage row has at least one `E` or `D` — a stage with no enabling capability cannot deliver.
  2. Every `M` (missing) cell has a corresponding GAP-NNN entry or is listed in `## Open Questions`.
- **Elicitation questions:**
  1. "Which capabilities enable the {stage} stage of {value stream}?"
  2. "Where are capabilities weak or missing along this value stream?"

### capability-application — Capability / Application Matrix
- **Phase:** B / C · **Folder:** `artifacts/phase-b/` · **File:** `capability-application-matrix.md`
- **Axes:** rows = capabilities (CAP-NNN), columns = applications
- **Seed sources:** rows — `artifacts/phase-b/business-architecture.md` capability model; columns — `artifacts/phase-c-app/application-architecture.md` application catalogue
- **Markers:** `T` tolerate · `I` invest · `M` migrate · `R` retire (target disposition of the application for that capability); `+` strong support · `-` weak support may prefix (e.g. `+I`)
- **Shows:** which applications support which business capabilities
- **Why:** connects application portfolio management to business value and capability gaps
- **How:** capabilities on rows, applications on columns; mark disposition per intersection; capabilities supported only by `R`-marked applications are modernization targets — record in Observations
- **Grill checks:**
  1. Every CAP-NNN row has at least one non-`R` cell — a capability supported only by retiring applications has an unplanned gap.
  2. Applications marked `R` anywhere also appear in the Gap Analysis or Roadmap; otherwise flag in `## Observations`.
  3. Columns with no cells (application supports no capability) are flagged as rationalization candidates.
- **Elicitation questions:**
  1. "Which applications support {capability} today, and how well?"
  2. "For each supporting application: tolerate, invest, migrate, or retire?"

### data-function — Data Entity / Business Function Matrix
- **Phase:** C-Data · **Folder:** `artifacts/phase-c-data/` · **File:** `data-function-matrix.md`
- **Axes:** rows = data entities, columns = business functions
- **Seed sources:** rows — `artifacts/phase-c-data/data-architecture.md` entity/subject-area tables; columns — `artifacts/phase-b/business-architecture.md` function catalogue
- **Markers:** `C` create · `R` read · `U` update · `D` delete (combinable) · `O` owner · `S` steward
- **Shows:** which business functions create, use, update, delete, or govern data entities
- **Why:** clarifies data ownership, stewardship, data quality responsibility, and business dependence on data
- **How:** entities on rows, functions on columns; mark CRUD plus ownership/stewardship; exactly one `O` per entity row
- **Grill checks:**
  1. Every data entity row has exactly one `O` — unowned or multi-owned data is a governance gap.
  2. Every entity row has at least one `C` — data nobody creates is either external (note it in Observations) or a modelling error.
- **Elicitation questions:**
  1. "Which business function owns {entity}, and who stewards its quality?"
  2. "Which functions create or update {entity} — and which only read it?"

### app-data — Application / Data Matrix
- **Phase:** C-Data · **Folder:** `artifacts/phase-c-data/` · **File:** `app-data-matrix.md`
- **Axes:** rows = applications, columns = data entities
- **Seed sources:** rows — `artifacts/phase-c-app/application-architecture.md` application catalogue; columns — `artifacts/phase-c-data/data-architecture.md` entity tables
- **Markers:** `C` create · `R` read · `U` update · `D` delete (combinable) · `★` system of record · `!` sensitive data (PII/regulated)
- **Shows:** which applications create, read, update, delete, store, or exchange data
- **Why:** identifies systems of record, duplicate data stores, integration needs, privacy exposure, and modernization impacts
- **How:** applications on rows, entities on columns; mark CRUD per cell; flag exactly one `★` per entity column; mark `!` wherever a sensitive entity is touched; note integration methods in Observations
- **Grill checks:**
  1. Every data entity column has exactly one `★` — zero means no system of record, more than one means duplicate masters.
  2. Any entity with `C` from more than one application is listed in `## Observations` as a duplication risk.
  3. Every `!`-marked cell's application appears in the engagement's security or privacy considerations (or `## Open Questions` notes the follow-up).
- **Elicitation questions:**
  1. "Which applications touch {entity}, and how — create, read, update, or delete?"
  2. "Which application is the system of record for {entity}?"
  3. "Which of these entities carry sensitive or regulated data?"

### app-organization — Application / Organization Matrix
- **Phase:** C-App · **Folder:** `artifacts/phase-c-app/` · **File:** `app-organization-matrix.md`
- **Axes:** rows = applications, columns = organization units
- **Seed sources:** rows — `artifacts/phase-c-app/application-architecture.md` application catalogue; columns — `artifacts/phase-b/business-architecture.md` organization sections
- **Markers:** `O` owns · `H` heavy use · `L` light use · `S` support responsibility · `F` funding responsibility
- **Shows:** which organizational units own, use, fund, support, or depend on applications
- **Why:** supports application rationalization, ownership cleanup, chargeback/showback, and support model design
- **How:** applications on rows, org units on columns; one `O` per application; mark usage weight and support/funding; note business criticality in Observations
- **Grill checks:**
  1. Every application row has exactly one `O` — unowned applications block rationalization decisions.
  2. Every application row has at least one `F` — applications nobody funds are flagged as orphan-cost risks.
- **Elicitation questions:**
  1. "Who owns {application} — and who funds and supports it?"
  2. "Which units use {application} heavily versus occasionally?"

### role-application — Role / Application Matrix
- **Phase:** C-App · **Folder:** `artifacts/phase-c-app/` · **File:** `role-application-matrix.md`
- **Axes:** rows = roles (ROLE-NNN), columns = applications
- **Seed sources:** rows — `artifacts/cross-cutting/context/role-catalogue.md`; columns — `artifacts/phase-c-app/application-architecture.md` application catalogue
- **Markers:** `M` mandatory for the role · `O` optional · access level suffix: `r` read-only · `w` read-write · `a` admin (e.g. `Mw`)
- **Shows:** which roles use which applications
- **Why:** supports access management, role-based permissions, training, licensing analysis, and process enablement
- **How:** ROLE-NNN on rows, applications on columns; mark use type and access level; note frequency or licensing implications in Observations
- **Grill checks:**
  1. Every `a` (admin) cell is justified in `## Observations` — admin access without rationale is a least-privilege violation.
  2. Application columns with no cells are flagged — an application no role uses is a rationalization candidate or an access-model gap.
- **Elicitation questions:**
  1. "Which applications must someone in the {role} role use — and at what access level?"
  2. "Are there applications where admin access is broader than it should be?"

### app-function — Application / Function Matrix
- **Phase:** C-App · **Folder:** `artifacts/phase-c-app/` · **File:** `app-function-matrix.md`
- **Axes:** rows = applications, columns = business functions
- **Seed sources:** rows — `artifacts/phase-c-app/application-architecture.md` application catalogue; columns — `artifacts/phase-b/business-architecture.md` function catalogue
- **Markers:** `P` primary support · `S` secondary support · `D` duplicate support · `R` planned replacement · `T` target-state support
- **Shows:** which applications support which business functions
- **Why:** reveals functional coverage, overlap, duplication, under-supported business areas, and modernization targets
- **How:** applications on rows, functions on columns; mark support type; columns with multiple `P` indicate duplication; columns with none indicate under-support
- **Grill checks:**
  1. Every business function column has at least one `P` or `T` — uncovered functions are gaps.
  2. Every `D` cell pair is listed in `## Observations` with a consolidation note or a deliberate-duplication rationale.
- **Elicitation questions:**
  1. "Which application primarily supports {function} — and do any others overlap it?"
  2. "Which functions feel under-supported by the current application estate?"

### app-interaction — Application Interaction Matrix
- **Phase:** C-App · **Folder:** `artifacts/phase-c-app/` · **File:** `app-interaction-matrix.md`
- **Axes:** rows = applications, columns = applications (square matrix)
- **Seed sources:** both axes — `artifacts/phase-c-app/application-architecture.md` application catalogue; existing IFC-NNN entries in interface catalogues enrich cells
- **Markers:** `→` sends to · `←` receives from · `↔` bidirectional · `!` critical interface; cell may name the interface (e.g. `→ IFC-003`)
- **Shows:** application-to-application relationships and dependencies
- **Why:** clarifies integration complexity, critical interfaces, failure impact, and migration sequencing
- **How:** same application set on both axes; read row → column; record direction and interface; capture data exchanged, frequency, and integration style in Observations or the linked IFC-NNN entry
- **Grill checks:**
  1. The matrix is square — row and column sets are identical.
  2. Every `!` (critical) cell names an interface (IFC-NNN or description) — unnamed critical interfaces cannot be governed.
  3. Applications with the most connections are listed in `## Observations` as migration-sequencing hotspots.
- **Elicitation questions:**
  1. "Which applications does {application} exchange data with — sending, receiving, or both?"
  2. "Which of these interfaces would hurt most if it failed tomorrow?"

### system-technology — System / Technology Matrix
- **Phase:** D · **Folder:** `artifacts/phase-d/` · **File:** `system-technology-matrix.md`
- **Axes:** rows = systems/applications, columns = technology components (platforms, databases, middleware, OS, network, cloud services)
- **Seed sources:** rows — `artifacts/phase-c-app/application-architecture.md` application catalogue; columns — `artifacts/phase-d/technology-architecture.md` component/SBB tables (SBB-NNN, ABB-NNN tokens)
- **Markers:** `X` depends on; lifecycle suffix: `a` active · `s` sunset · `e` end-of-life (e.g. `Xe`); `!` high risk
- **Shows:** which systems or applications depend on which technology components
- **Why:** supports technology lifecycle management, vulnerability response, platform modernization, and infrastructure impact analysis
- **How:** systems on rows, technology components on columns; mark dependency with lifecycle status; `Xe` cells answer "what breaks if we retire this platform?"
- **Grill checks:**
  1. Every `Xe` (EoL dependency) cell has a remediation note in `## Observations` or a linked GAP/WP reference.
  2. Every technology column with three or more dependent systems is assessed in `## Observations` as a concentration/single-point-of-failure risk.
  3. Column entries correspond to components present in the Technology Architecture (no phantom technology).
- **Elicitation questions:**
  1. "Which platforms, databases, and middleware does {system} run on?"
  2. "Which of these components are sunset or end-of-life — and what depends on them?"

### wp-dependency — Work Package / Dependency Matrix
- **Phase:** E / F · **Folder:** `artifacts/phase-f/` · **File:** `wp-dependency-matrix.md`
- **Axes:** rows = work packages (WP-NNN), columns = work packages (square matrix)
- **Seed sources:** both axes — `artifacts/phase-e/architecture-roadmap.md` work package tables (WP-NNN tokens); `artifacts/phase-f/migration-plan.md` if present
- **Markers:** `P` predecessor (row must precede column) · `T` technical dependency · `B` business dependency · `F` funding dependency · `G` governance dependency
- **Shows:** dependencies between work packages, projects, or transition states
- **Why:** supports migration sequencing and delivery governance
- **How:** WP-NNN on both axes; read row → column (row WP-001, column WP-003, cell `P` = WP-001 must precede WP-003); circular `P` chains are sequencing errors. The file lives in `phase-f/` because sequencing is finalised during Migration Planning; row/column candidates come from the Phase E roadmap.
- **Grill checks:**
  1. No circular `P` chains (A precedes B, B precedes A — directly or transitively).
  2. Every WP scheduled in Wave 1 of the Roadmap has no `P` dependency on a WP in a later wave.
  3. Every WP-NNN in the Roadmap appears on both axes (no orphan work packages).
- **Elicitation questions:**
  1. "Which work packages must complete before {WP} can start?"
  2. "Are any dependencies non-technical — funding, business readiness, or governance approvals?"

---

## Managed elsewhere (4)

### Stakeholder Map Matrix
- **Phase:** A · **Managed by:** existing `stakeholder-map.md` artifact in `artifacts/phase-a/` (created via `/ea-interview` Phase A or `/ea-artifact`)
- **Shows:** stakeholders, concerns, influence, engagement needs, and relevant architecture views
- **Why:** ensures the architecture addresses the right concerns from the right people

### Requirements Traceability Matrix
- **Phase:** Requirements Management / Cross-cutting · **Managed by:** existing `traceability-matrix.md` artifact in `artifacts/requirements/` plus the `/ea-trace` link graph
- **Shows:** requirements linked to drivers, stakeholders, architecture components, decisions, work packages, and validation evidence
- **Why:** proves architecture choices satisfy business and technical requirements

### Work Package / Gap Matrix
- **Phase:** E / F · **Managed by:** `/ea-trace` View 9 — rendered read-only from the gaps register's `linkedWorkPackages` field (`/ea-gaps update GAP-NNN linkedWorkPackages WP-NNN` to edit)
- **Shows:** which work packages resolve which architecture gaps
- **Why:** makes roadmap logic explicit and avoids orphaned work packages

### Requirement / Work Package Matrix
- **Phase:** E / F / G · **Managed by:** `/ea-trace` View 10 — derived read-only from the transitive Requirement → Capability → Work Package chain (edit the underlying links via Views 4 and 5)
- **Shows:** which work packages satisfy which requirements
- **Why:** preserves traceability from architecture intent to delivery execution
