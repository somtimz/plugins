# Phase B — Business Architecture Artefacts


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
