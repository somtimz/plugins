# Phase E / F — Roadmap and Transition Artefacts


### Consolidated Gap Analysis

**Purpose:** Aggregates and reconciles the domain-level gap analyses produced in Phases B, C-Data, C-App, and D into a single cross-domain view. Identifies interdependencies between domain gaps, surfaces conflicts, and provides the primary input to the Architecture Roadmap and Transition Architectures. The domain-level gap analyses remain authoritative for their domain; this document consolidates and reconciles them.

**Audience:** Architecture team, programme sponsor, delivery leads.

**Contents:**
- Executive summary (total gaps, high-priority count)
- Domain gap summary table (with links to source domain analyses)
- Consolidated gap register (all domain gaps in a single prioritised list with cross-domain IDs)
- Cross-domain dependency table (gaps that are prerequisites or enablers for other gaps)
- Reconciliation notes (conflicts between domain analyses and their resolutions)
- Roadmap input summary (candidate work packages mapped to the gaps they close)

**When to Create:** Phase E, after all applicable domain gap analyses are complete. The consolidated gap analysis is the trigger for roadmap construction.

**Who Reviews:** Lead Architect, programme sponsor, Architecture Review Board.

**Phase:** E.

**Template:** `consolidated-gap-analysis.md` — create with `/ea-artifact create consolidated-gap-analysis`.

---

### Transition Architectures

**Purpose:** Defines the intermediate architecture states between the Baseline and Target Architecture. Each Transition Architecture represents a coherent, independently deliverable state of the enterprise that provides business value on its own — not merely a partial target. Used to de-risk migration by establishing stable stepping stones and to sequence work packages in the Architecture Roadmap.

**Audience:** Architecture team, programme manager, delivery leads, Architecture Review Board.

**Contents:**
- Overview of the migration path (number of transition states and rationale)
- Transition state summary table (state, name, target date, key capability delivered, supporting work packages)
- Per-transition-state detail: changes from previous state (by domain), business value delivered, dependencies, risks
- Traceability table mapping each work package to its contributing transition state

**When to Create:** Phase E (initial definition), Phase F (refined and finalised with the Migration Plan). Updated in Phase H if change requests affect the migration sequence.

**Who Reviews:** Lead Architect, programme sponsor, Architecture Review Board.

**Phase:** E (initial), F (finalised).

**Template:** `transition-architectures.md` — create with `/ea-artifact create transition-architectures`.

---

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

### Motivation Registers (Drivers / Goals / Objectives / Strategy / Issues / Problems)

**Purpose:** Six dedicated Phase-A registers — Drivers (DRV-NNN), Goals (G-NNN), Objectives (OBJ-NNN), Strategy (STR-NNN), Issues (ISS-NNN), Problems (PRB-NNN) — that hold the full motivation chain. They are the management interface for `engagement.json → direction` (the single source of truth). The **Architecture Vision is the strategic index** that summarises and links to these registers rather than embedding their tables; it should be reviewed together with them at the Phase A gate. Each register is a first-class, **scored** artifact (guidance per section + a `## Summary` count table), unlike other command-generated registers.

**Audience:** Programme sponsor, enterprise architect, business owners, architecture review board.

**Contents:** Per register — a `## Summary` count table (totals, status/priority counts, orphan/quality flags) and items grouped per that concept's grouping (drivers by type; goals/issues/problems by domain; objectives by linked goal; strategies by type), each item as an ID-keyed field block matching the `/ea-{concept}` Register Spec fields.

**Templates:** `templates/phase-a/{drivers,goals,objectives,strategy,issues,problems}-register.md`.

**When to Create:** Populated from interview/brainstorm capture via the register commands. Regenerate with `/ea-{concept} generate` (writes to `artifacts/cross-cutting/{concept}-register.md`); `add`/`update` change `engagement.json` and nudge a regenerate. Do not hand-edit the generated register — it is overwritten from the source of truth.

**Phase:** Authored in Phase A (motivation); maintained throughout the engagement.

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
