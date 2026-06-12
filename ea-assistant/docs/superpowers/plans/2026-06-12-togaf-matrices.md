# TOGAF Matrix Artifacts Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Add first-class TOGAF 10 relationship-matrix support — an 18-matrix catalogue, a `/ea-matrix` command managing 14 of them, and integrations into `/ea-interview`, `/ea-brainstorm`, `/ea-grill`, and `/ea-trace`.

**Architecture:** A single catalogue reference (`matrix-catalogue.md`) is the source of truth for axes, seed sources, marker vocabularies, grill checks, and elicitation questions. Commands read the catalogue; none restate its logic. Matrix files are per-phase artifacts seeded from one template. Four overlapping matrices are documented with pointers instead of duplicated: two existing artifacts, and two new read-only `/ea-trace` views.

**Tech Stack:** Markdown instruction files (Claude Code plugin framework). No test framework — verification is `~/.bun/bin/bun .github/scripts/validate-frontmatter.ts ea-assistant/` plus grep checks stated per task.

**Spec:** `ea-assistant/docs/superpowers/specs/2026-06-12-togaf-matrices-design.md`

**Working directory:** all paths below are relative to `ea-assistant/` unless prefixed `../`. Validation and git commands run from the repo root `/mnt/d/dev/claude-sandbox/plugins/`.

---

### Task 1: Matrix Catalogue Reference

**Files:**
- Create: `skills/ea-artifact-templates/references/matrix-catalogue.md`

- [ ] **Step 1: Write the catalogue file**

Create `skills/ea-artifact-templates/references/matrix-catalogue.md` with exactly this content:

````markdown
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
  3. No ADR with status Completed is absent from the columns — an unassessed completed decision is a governance gap.
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
- **Phase:** C · **Folder:** `artifacts/phase-c-data/` · **File:** `data-function-matrix.md`
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
- **Phase:** C · **Folder:** `artifacts/phase-c-data/` · **File:** `app-data-matrix.md`
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
- **Phase:** C · **Folder:** `artifacts/phase-c-app/` · **File:** `app-organization-matrix.md`
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
- **Phase:** C · **Folder:** `artifacts/phase-c-app/` · **File:** `role-application-matrix.md`
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
- **Phase:** C · **Folder:** `artifacts/phase-c-app/` · **File:** `app-function-matrix.md`
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
- **Phase:** C · **Folder:** `artifacts/phase-c-app/` · **File:** `app-interaction-matrix.md`
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
- **How:** WP-NNN on both axes; read row → column (row WP-001, column WP-003, cell `P` = WP-001 must precede WP-003); circular `P` chains are sequencing errors
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
````

- [ ] **Step 2: Verify**

Run from repo root:
```bash
grep -c "^### " ea-assistant/skills/ea-artifact-templates/references/matrix-catalogue.md
```
Expected: `18`

```bash
grep -c "Elicitation questions" ea-assistant/skills/ea-artifact-templates/references/matrix-catalogue.md
```
Expected: `14`

- [ ] **Step 3: Commit**

```bash
git add ea-assistant/skills/ea-artifact-templates/references/matrix-catalogue.md
git commit -m "feat(ea-assistant): add TOGAF matrix catalogue reference (18 matrices)"
```

---

### Task 2: Matrix Template Seed

**Files:**
- Create: `templates/seeds/matrix-template.md`

- [ ] **Step 1: Write the template**

Create `templates/seeds/matrix-template.md` with exactly this content:

````markdown
# Matrix Template Seed

Used by `/ea-matrix new` and the `/ea-interview` matrix offer. Substitute all `{{placeholders}}` before writing.

---

```markdown
---
id: {{key}}-matrix
name: {{name}}
matrixKey: {{key}}
phase: {{phase}}
status: Draft
version: 0.1.0
relatedArtifacts: []
diagrams: []
links: []
lastModified: {{YYYY-MM-DD}}
---

# {{name}}

## Overview

{{overview}}

## Matrix

| {{rowEntityLabel}} \ {{columnEntityLabel}} | {{column1}} | {{column2}} |
|---|---|---|
| {{row1}} |  |  |
| {{row2}} |  |  |

## Legend

{{legend}}

## Observations

*(none yet)*

## Open Questions

*(none yet)*
```

**Substitution notes:**
- `{{key}}`, `{{name}}`, `{{phase}}` — from the catalogue entry (`skills/ea-artifact-templates/references/matrix-catalogue.md`)
- `{{overview}}` — one or two sentences: the catalogue's "Why" line adapted to this engagement
- `{{rowEntityLabel}}` / `{{columnEntityLabel}}` — the axis names from the catalogue (e.g. "Data Entity \ Application")
- Row/column placeholders — replace with the confirmed seeded axes; add as many rows/columns as confirmed
- `{{legend}}` — copy the catalogue entry's **Markers** line verbatim as a bulleted list
````

- [ ] **Step 2: Verify**

```bash
grep -c "{{" ea-assistant/templates/seeds/matrix-template.md
```
Expected: a number ≥ 14 (placeholders present), and:
```bash
grep -n "matrixKey" ea-assistant/templates/seeds/matrix-template.md
```
Expected: one match.

- [ ] **Step 3: Commit**

```bash
git add ea-assistant/templates/seeds/matrix-template.md
git commit -m "feat(ea-assistant): add matrix artifact template seed"
```

---

### Task 3: `/ea-matrix` Command

**Files:**
- Create: `commands/ea-matrix.md`

- [ ] **Step 1: Write the command file**

Create `commands/ea-matrix.md` with exactly this content:

````markdown
---
name: ea-matrix
description: Manage TOGAF relationship matrices — create, list, show, edit, and check grid artifacts (Actor/Role, Application/Data CRUD, Capability/Application, System/Technology, and 10 more) per ADM phase, with axis seeding from existing artifacts
argument-hint: "[list|new|show|edit|check] [key]"
allowed-tools: [Read, Write, Glob, Grep, Bash]
---

# /ea-matrix — TOGAF Relationship Matrices

Uses skill: `ea-artifact-templates` → `references/matrix-catalogue.md` (the catalogue) and `templates/seeds/matrix-template.md` (the template).

The catalogue is the single source of truth for axes, seed sources, marker vocabularies, grill checks, and elicitation questions. Never restate them here.

---

## Resolve context

Before executing any mode:
1. Resolve the active engagement: check context for slug; if none, scan `EA-projects/*/engagement.json` and ask the user to select. If no engagement exists, error: "No engagement is active. Run `/ea-open` or `/ea-new` first."
2. Load `engagement.json` — extract `slug`, `currentPhase`.
3. Read the catalogue: `skills/ea-artifact-templates/references/matrix-catalogue.md`.
4. If a `key` argument was given, look it up in the catalogue:
   - Unknown key → error listing the 14 valid keys.
   - Managed-elsewhere entry (Stakeholder Map, Requirements Traceability, Work Package/Gap, Requirement/Work Package) → print its **Managed by:** pointer and stop.
5. Matrix file path for a key: `EA-projects/{slug}/artifacts/{folder}/{key}-matrix.md` where `{folder}` is the catalogue entry's Folder.

Mode defaults to `list` when no arguments are given.

---

## Mode: `list`

1. For each of the 18 catalogue entries, determine status:
   - **➡️ managed elsewhere** — the 4 pointer entries; show the pointer.
   - **✅ exists** — the matrix file exists. Compute cell fill %: count non-empty body cells in the `## Matrix` table (cells after the first column, excluding the header and separator rows) divided by total body cells. Show `({pct}% filled, {status})` from frontmatter.
   - **⬜ recommended** — file does not exist.
2. Render grouped by phase (use the catalogue's Phase Index ordering). Mark the group matching `currentPhase` with `← current phase`.
3. Footer: `Create one with /ea-matrix new <key> · Validate with /ea-matrix check`

---

## Mode: `new <key>`

1. Resolve the key (see Resolve context). If the matrix file already exists, error: "{key}-matrix.md already exists — use `/ea-matrix edit {key}`."
2. **Seed axes.** Read the catalogue entry's Seed sources. For each axis, scan the listed engagement files for candidate entities (ID tokens like `CAP-\d{3}` where the axis is ID-based; otherwise table rows / list items naming the entity type). Present the candidates:
   ```
   Proposed rows ({rowEntityLabel}): {list}
   Proposed columns ({columnEntityLabel}): {list}
   Confirm, edit (add/remove), or enter axes manually:
   ```
   If a seed source file does not exist, say so and ask the user to provide that axis manually. Harvest any `[Matrix]`-relevant thoughts from `artifacts/{folder}/notes/brainstorm/brainstorm-notes.md` (category `relationships`) and offer them as additional candidates.
3. **Elicit cells (optional).** Ask: "Fill cells now, row by row? (y = guided / n = leave empty)". If yes: for each row, ask the catalogue's elicitation questions adapted to that row entity, and record markers using only the catalogue's Markers vocabulary for this key.
4. Create the phase folder if it does not exist. Write the matrix file from `templates/seeds/matrix-template.md`, substituting per the template's substitution notes. Set `lastModified` to today.
5. Register the artifact in `engagement.json → artifacts` (same shape as other artifacts: id `{key}-matrix`, phase, path, status Draft, version 0.1.0) and update the engagement's `lastModified`.
6. Report: file path, axis sizes, fill %, and a reminder: "Run `/ea-matrix check {key}` after filling cells."

---

## Mode: `show <key>`

1. Resolve the key; if the file does not exist, error: "{key}-matrix.md not found — create it with `/ea-matrix new {key}`."
2. Render the full file: frontmatter summary line (name, phase, status, version, lastModified), then `## Matrix`, `## Legend`, `## Observations`, `## Open Questions`.
3. Footer: cell fill % and `Edit with /ea-matrix edit {key} · Validate with /ea-matrix check {key}`.

---

## Mode: `edit <key>`

1. Resolve the key; if the file does not exist, error and point to `new`.
2. **Stale-axis check first.** Re-scan the catalogue entry's Seed sources. List entities present in the sources but missing from the matrix axes (e.g. "CAP-009 exists in the Capability Model but has no row"), and axis entries no longer found in any source. Offer to add/remove each.
3. Guided edit menu:
   ```
   1. Add/remove rows or columns
   2. Update cells (pick a row, walk its cells)
   3. Edit Observations
   4. Edit Open Questions
   D. Done
   ```
   Cell values must use only the catalogue's Markers vocabulary for this key — reject others, showing the legal set.
4. On Done: bump the patch version in frontmatter, set `lastModified` to today, write the file, update `engagement.json → lastModified`.

---

## Mode: `check [<key>]`

1. If a key is given, check that one matrix; otherwise check every existing matrix file for the engagement (glob `EA-projects/{slug}/artifacts/*/[a-z]*-matrix.md` and match frontmatter `matrixKey` against the catalogue).
2. For each matrix, run:
   - **Axes check:** row/column entity types match the catalogue entry's Axes.
   - **Marker check:** every non-empty cell uses only the catalogue's Markers vocabulary for this key.
   - **Orphan check:** the stale-axis comparison from `edit` step 2 (seed-source entities missing from axes, and vice versa).
   - **Catalogue grill checks:** each numbered item in the entry's Grill checks, evaluated against the matrix content (and `## Observations` where the check requires a note).
   - **Approval check:** if frontmatter `status: Approved` and `## Observations` is empty or `*(none yet)*`, flag: "Approved matrix with no observations — a filled matrix always exposes findings."
3. Report per matrix: `✅ passed / ⚠ failed / ❓ unverifiable` per check, then a one-line summary. This is the same check logic `/ea-grill` runs when grilling a matrix artifact — defined once, in the catalogue.
````

- [ ] **Step 2: Validate frontmatter**

```bash
~/.bun/bin/bun .github/scripts/validate-frontmatter.ts ea-assistant/
```
Expected: `0 errors` (file count increases by 1 to 85).

- [ ] **Step 3: Commit**

```bash
git add ea-assistant/commands/ea-matrix.md
git commit -m "feat(ea-assistant): add /ea-matrix command (list, new, show, edit, check)"
```

---

### Task 4: `/ea-interview` Matrix Offer

**Files:**
- Modify: `commands/ea-interview.md` (phase mode, step 4 bullet list — the framework-lens bullet is at line ~153)

- [ ] **Step 1: Add the matrix offer bullet**

In `commands/ea-interview.md`, find this bullet (inside `### Mode: start phase`, step 4):

```markdown
   - **Framework lens offer** (phases A, B, C-Data, C-App, D, E, F — offering only lenses whose Interview Questions cover the current phase): after the question bank's optional Security Questions section, offer framework lens questions per consumption point 2 in `skills/ea-framework-lenses/SKILL.md` — load the chosen lens reference and ask its Interview Questions for the current phase, routing answers per the lens's routing tables. Skip the offer silently when the engagement has no cloud or infrastructure scope signals.
```

Immediately AFTER it, insert this new bullet:

```markdown
   - **Matrix offer** (phases Prelim, B, C-Data, C-App, D, E, F): after the framework lens offer, read `skills/ea-artifact-templates/references/matrix-catalogue.md` and filter to entries whose Phase matches the interview phase (per the catalogue's Phase Index), excluding managed-elsewhere entries. Skip any matrix whose file already exists with at least one filled cell. If any remain, offer: "This phase has {N} recommended matrices: {names}. Capture any now? (pick / skip)". On accept, for each chosen matrix: ask the catalogue entry's Elicitation questions, seed axes from its Seed sources (same logic as `/ea-matrix new` steps 2–4), and write the matrix file from `templates/seeds/matrix-template.md`. Record answers in the interview notes as usual. Skipping is silent and free — matrices are recommended, not mandated.
```

- [ ] **Step 2: Verify**

```bash
grep -n "Matrix offer" ea-assistant/commands/ea-interview.md
```
Expected: exactly one match, on the line after the Framework lens offer bullet.

```bash
~/.bun/bin/bun .github/scripts/validate-frontmatter.ts ea-assistant/
```
Expected: `0 errors`.

- [ ] **Step 3: Commit**

```bash
git add ea-assistant/commands/ea-interview.md
git commit -m "feat(ea-assistant): add recommended-matrix offer to /ea-interview phase mode"
```

---

### Task 5: `/ea-brainstorm` Integration

**Files:**
- Modify: `commands/ea-brainstorm.md` (category rules in step 3b; context hints also in step 3b)
- Modify: `skills/ea-interview-ui/SKILL.md` (category enum, two occurrences at lines ~146 and ~156)

- [ ] **Step 1: Add the `relationships` category rule**

In `commands/ea-brainstorm.md` step 3b, find the category assignment list ending:

```markdown
   - Questions about network topology, segmentation, connectivity, or traffic patterns → `"network"`
   - All others → `"other"`
```

Replace with:

```markdown
   - Questions about network topology, segmentation, connectivity, or traffic patterns → `"network"`
   - Questions about relationships between elements — which application uses which data, who performs which role, what depends on what → `"relationships"`
   - All others → `"other"`
```

- [ ] **Step 2: Add `[Matrix]` context hints**

In the same step 3b, find the bullet beginning `- **Filter engagement direction by phase relevance.**` and insert this new bullet immediately BEFORE it:

```markdown
   - **Surface recommended matrices.** For phase-scoped sessions (phases Prelim, B, C-Data, C-App, D, E, F): read `skills/ea-artifact-templates/references/matrix-catalogue.md`, filter to entries whose Phase matches (excluding managed-elsewhere entries) and whose matrix file does not yet exist or has no filled cells. For each, add a `prefilled` entry: `{ questionRef: null, questionText: "[Matrix] {name} — {rowEntityLabel} × {columnEntityLabel}", answer: "{first elicitation question from the catalogue entry}", source: "matrix-catalogue", category: "relationships" }`. These hints prompt relationship statements that `/ea-interview` and `/ea-matrix new` later harvest as cell candidates.
```

- [ ] **Step 3: Extend the category enum in the interview-ui skill**

In `skills/ea-interview-ui/SKILL.md`, two lines (~146 and ~156) contain the category enum:

```
      category: "concerns | goals | constraints | opportunities | assumptions | other | value-streams | use-cases | processes | conceptual-model | logical-model | platforms | languages | infrastructure | network",
```

In BOTH occurrences, replace `| network",` with `| network | relationships",` so each reads:

```
      category: "concerns | goals | constraints | opportunities | assumptions | other | value-streams | use-cases | processes | conceptual-model | logical-model | platforms | languages | infrastructure | network | relationships",
```

(New category ids auto-create a card in the brainstorm app — no JSX change needed, per the same SKILL.md.)

- [ ] **Step 4: Verify**

```bash
grep -c '"relationships"' ea-assistant/commands/ea-brainstorm.md
```
Expected: `2` (category rule + prefilled entry).

```bash
grep -c "| relationships" ea-assistant/skills/ea-interview-ui/SKILL.md
```
Expected: `2`.

```bash
~/.bun/bin/bun .github/scripts/validate-frontmatter.ts ea-assistant/
```
Expected: `0 errors`.

- [ ] **Step 5: Commit**

```bash
git add ea-assistant/commands/ea-brainstorm.md ea-assistant/skills/ea-interview-ui/SKILL.md
git commit -m "feat(ea-assistant): add matrix context hints and relationships category to /ea-brainstorm"
```

---

### Task 6: `/ea-grill` Integration

**Files:**
- Modify: `skills/ea-grill-skills/SKILL.md` (artifact mode — after the Adopted Reference Architecture block at line ~335)

- [ ] **Step 1: Add the two matrix blocks**

In `skills/ea-grill-skills/SKILL.md`, find the end of the **Adopted Reference Architecture compliance** block:

```markdown
  4. Summarise at the end of the artifact review:
     ```
     Adopted RA checks (RA-NNN: {name}):
       Passed:      {n}
       Failed:      {n} ⚠
       Unverifiable: {n} ❓
     ```
```

Immediately AFTER it (before the `---` that precedes "At the end, provide:"), insert:

```markdown
**Recommended matrices (advisory):**
When reviewing a phase artifact (any artifact whose phase maps to Prelim, B, C-Data, C-App, D, E, or F):
- Read `skills/ea-artifact-templates/references/matrix-catalogue.md` and filter to entries whose Phase matches the artifact's phase (excluding managed-elsewhere entries).
- For each: if the matrix file does not exist, note "⬜ Recommended matrix not created: {name} — `/ea-matrix new {key}`"; if it exists but has no filled cells, note "⚠ Matrix {name} exists but is empty."
- Advisory only — never fails the review and never affects the verdict. Present as a short block after the scorecard. Omit the block entirely if all recommended matrices exist with content.

**Matrix artifact grilling:**
If the artifact under review is itself a matrix (frontmatter contains a `matrixKey` field):
- Look up the key in `skills/ea-artifact-templates/references/matrix-catalogue.md` and run the full check set defined by `/ea-matrix check` mode in `commands/ea-matrix.md` (axes check, marker check, orphan check, catalogue grill checks, approval check) — the check definitions live in the catalogue; do not restate them.
- Report each as ✅ / ⚠ / ❓ in the scorecard, and treat ⚠ marker or axes failures as Inconsistent sections in the verdict.
```

- [ ] **Step 2: Verify**

```bash
grep -n "Recommended matrices (advisory)" ea-assistant/skills/ea-grill-skills/SKILL.md
grep -n "Matrix artifact grilling" ea-assistant/skills/ea-grill-skills/SKILL.md
```
Expected: one match each, both located after the Adopted RA block and before the "At the end, provide:" section.

```bash
~/.bun/bin/bun .github/scripts/validate-frontmatter.ts ea-assistant/
```
Expected: `0 errors`.

- [ ] **Step 3: Commit**

```bash
git add ea-assistant/skills/ea-grill-skills/SKILL.md
git commit -m "feat(ea-assistant): add matrix advisory block and matrix grilling to grill skill"
```

---

### Task 7: `/ea-trace` Views 9 and 10

**Files:**
- Modify: `commands/ea-trace.md` (menu at line ~55, new views after View 8 at line ~372, Step 6 full gap report at line ~425)

- [ ] **Step 1: Update the menu**

Find:

```
  8. SBB → Story                   ({N} gaps)
  9. Full gap report               (all views, gaps + contradictions only)
  Q. Quit
```

Replace with:

```
  8. SBB → Story                   ({N} gaps)
  9. Gap → Work Package            ({N} gaps)
 10. Requirement → Work Package    ({N} gaps)
 11. Full gap report               (all views, gaps + contradictions only)
  Q. Quit
```

- [ ] **Step 2: Add View 9 and View 10 sections**

After the View 8 section (which ends with `**After view:** Return to the persistent menu (Step 3).` followed by `---`), insert:

```markdown
### View 9: Gap → Work Package (read-only)

**Entity sources:**
- GAP-NNN: read `engagement.json → direction.gaps[]` — each entry's `id` and `linkedWorkPackages` field
- WP-NNN: scan `EA-projects/{slug}/artifacts/phase-e*/**/*.md` for tokens matching `WP-\d{3}`

**Render matrix:** rows = GAP-NNN, columns = WP-NNN. A cell is marked `R` (resolves) when the WP appears in the gap's `linkedWorkPackages`. This view renders from the gaps register only — it does NOT read or write `traceability-index.json`, and no bootstrap mechanism applies. Edit links via `/ea-gaps update GAP-NNN linkedWorkPackages WP-NNN`.

**Gaps section:**

For each GAP-NNN with an empty `linkedWorkPackages`:
```
⚠️ GAP-001 ({severity}) has no work package resolving it
   → Link one via /ea-gaps update GAP-001 linkedWorkPackages WP-NNN
   → Or accept the gap deliberately and record the acceptance in the Gap Analysis
```

For each WP-NNN appearing in no gap's `linkedWorkPackages`:
```
⚠️ WP-002 resolves no recorded gap — orphaned work package
   → Verify the WP traces to a goal/objective instead (see T3-ROAD-WP), or link a gap
```

**After view:** Return to the persistent menu (Step 3).

---

### View 10: Requirement → Work Package (derived, read-only)

**Entity sources:**
- REQ-NNN: scan `EA-projects/{slug}/artifacts/requirements/*.md` for tokens matching `REQ-\d{3}`
- WP-NNN: scan `EA-projects/{slug}/artifacts/phase-e*/**/*.md` for tokens matching `WP-\d{3}`

**Render matrix:** rows = REQ-NNN, columns = WP-NNN. A cell is marked `~` (derived) when a transitive path exists in `traceability-index.json`: REQ —`satisfiedBy`→ CAP —`deliveredBy`→ WP. This view is a composition of Views 4 and 5 — it writes nothing and has no bootstrap mechanism. To change it, edit the underlying links via View 4 or View 5.

**Gaps section:**

For each REQ-NNN with no derived path to any WP:
```
⚠️ REQ-003 has no delivery path (no Requirement → Capability → Work Package chain)
   → Add the missing link via View 4 (Requirement → Capability) or View 5 (Capability → Work Package)
```

**After view:** Return to the persistent menu (Step 3).

---
```

- [ ] **Step 3: Update Step 6 (Full Gap Report)**

In Step 6, make these replacements:

1. `Triggered by menu option 9 or the `--gaps` argument.` → `Triggered by menu option 11 or the `--gaps` argument.`
2. `Run all eight views silently` → `Run all ten views silently`
3. In the Summary block, after the line `SBB → Story               {N} gaps, {N} contradictions`, add:
```
Gap → Work Package        {N} gaps
Requirement → Work Package {N} gaps
```
4. In the post-report offer, `1. Open a specific view  →  enter 1–8` → `1. Open a specific view  →  enter 1–10`

Also in Step 3 (gap counts), the menu note "recompute gap counts before redisplaying" needs no change — but ensure View 9/10 gap counts are computed the same way (View 9: gaps with empty `linkedWorkPackages`; View 10: REQs with no derived WP path).

- [ ] **Step 4: Verify**

```bash
grep -n "View 9: Gap → Work Package" ea-assistant/commands/ea-trace.md
grep -n "View 10: Requirement → Work Package" ea-assistant/commands/ea-trace.md
grep -n "menu option 11" ea-assistant/commands/ea-trace.md
grep -n "all ten views" ea-assistant/commands/ea-trace.md
```
Expected: one match each.

```bash
grep -n "eight types" ea-assistant/commands/ea-trace.md
```
Expected: still one match — Step 5's link-type validation is unchanged (Views 9/10 are read-only and add no link types).

```bash
~/.bun/bin/bun .github/scripts/validate-frontmatter.ts ea-assistant/
```
Expected: `0 errors`.

- [ ] **Step 5: Commit**

```bash
git add ea-assistant/commands/ea-trace.md
git commit -m "feat(ea-assistant): add Gap→WP and Req→WP read-only views to /ea-trace"
```

---

### Task 8: Docs, Help, and Version Bump (0.9.62)

**Files:**
- Modify: `commands/ea-help.md`
- Modify: `CLAUDE.md`
- Modify: `.claude-plugin/plugin.json`
- Modify: `../.claude-plugin/marketplace.json`
- Modify: `docs/PRD.md`
- Modify: `README.md`
- Modify: `skills/ea-artifact-templates/SKILL.md`, `skills/ea-grill-skills/SKILL.md`, `skills/ea-interview-ui/SKILL.md` (frontmatter `version` only)

- [ ] **Step 1: ea-help.md**

In the commands table, immediately after the `/ea-refarch` row, add:

```markdown
| `/ea-matrix [list\|new\|show\|edit\|check] [key]` | TOGAF relationship matrices — 14 grid artifacts (Actor/Role, App/Data CRUD, Capability/Application, System/Technology…) with axis seeding and catalogue-driven checks |
```

If `ea-help.md` states a total command count, increment it by one.

- [ ] **Step 2: CLAUDE.md**

1. `**Current version:** 0.9.61` → `**Current version:** 0.9.62`
2. `54 commands available` → `55 commands available`
3. In Command Reference key entry points, append ` · /ea-matrix` after `/ea-refarch`.

- [ ] **Step 3: plugin.json and marketplace.json**

- `.claude-plugin/plugin.json`: `"version": "0.9.61"` → `"version": "0.9.62"`
- `../.claude-plugin/marketplace.json` (repo root): the ea-assistant entry's `"version": "0.9.61"` → `"version": "0.9.62"` (must exactly match plugin.json; description unchanged)

Verify both parse:
```bash
python3 -c "import json; json.load(open('ea-assistant/.claude-plugin/plugin.json')); json.load(open('.claude-plugin/marketplace.json')); print('OK')"
```
Expected: `OK`

- [ ] **Step 4: Bump touched SKILL.md versions**

In the frontmatter of `skills/ea-artifact-templates/SKILL.md`, `skills/ea-grill-skills/SKILL.md`, and `skills/ea-interview-ui/SKILL.md`, set `version:` to `0.9.62`.

- [ ] **Step 5: PRD.md**

Add a `## v0.9.62 — TOGAF Relationship Matrices` section (following the format of the existing v0.9.61 section), covering: the 18-matrix catalogue (14 managed by `/ea-matrix`, 4 managed elsewhere), the `/ea-matrix` command modes, the interview/brainstorm/grill integrations, and `/ea-trace` Views 9–10. Update any version line at the top of the PRD to 0.9.62.

- [ ] **Step 6: README.md**

1. Add the same `/ea-matrix` row to the commands table (after `/ea-refarch`).
2. Add a feature bullet: `**TOGAF relationship matrices** — 18-matrix catalogue (Actor/Role, Application/Data CRUD, Capability/Application, System/Technology, Work Package/Dependency…) with /ea-matrix management, axis seeding from existing artifacts, and grill compliance checks.`
3. If the README states a command count, increment it by one.

- [ ] **Step 7: Verify**

```bash
~/.bun/bin/bun .github/scripts/validate-frontmatter.ts ea-assistant/
grep -rn "0.9.61" ea-assistant/CLAUDE.md ea-assistant/.claude-plugin/plugin.json .claude-plugin/marketplace.json
grep -c "ea-matrix" ea-assistant/commands/ea-help.md ea-assistant/README.md
```
Expected: `0 errors`; no remaining `0.9.61` matches in those three files; at least one `ea-matrix` match in each of help and README.

- [ ] **Step 8: Commit**

```bash
git add ea-assistant/commands/ea-help.md ea-assistant/CLAUDE.md ea-assistant/.claude-plugin/plugin.json .claude-plugin/marketplace.json ea-assistant/docs/PRD.md ea-assistant/README.md ea-assistant/skills/ea-artifact-templates/SKILL.md ea-assistant/skills/ea-grill-skills/SKILL.md ea-assistant/skills/ea-interview-ui/SKILL.md
git commit -m "feat(ea-assistant): v0.9.62 — TOGAF relationship matrices"
```

---

## Final Verification (after all tasks)

```bash
~/.bun/bin/bun .github/scripts/validate-frontmatter.ts ea-assistant/        # 0 errors, 85 files
grep -c "^### " ea-assistant/skills/ea-artifact-templates/references/matrix-catalogue.md   # 18
grep -n "matrix-catalogue.md" ea-assistant/commands/ea-matrix.md ea-assistant/commands/ea-interview.md ea-assistant/commands/ea-brainstorm.md ea-assistant/skills/ea-grill-skills/SKILL.md   # all four consumers reference the catalogue
```
