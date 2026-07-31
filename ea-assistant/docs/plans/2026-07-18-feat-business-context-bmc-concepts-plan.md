# Plan: Business Context + Business Model Canvas as First-Class Concepts

**Objective:** Update `ea-concepts.md` and the plugin so the four business-layer concepts — **Business Context**, **Business Model Canvas**, **Business Architecture**, and **Business Operating Model** — are distinct, consistently defined, and traceable end-to-end.

**Confirmed scope (from user):**
1. Full rewrite of `ea-concepts.md` (option a — full file delivered).
2. Full plugin alignment across README, commands, skills, agents, and personas.
3. Add `CTX-NNN` (Business Context) and `BMC-NNN` (Business Model Canvas) ID prefixes.

---

## Phase A — Concept Foundation

### A1. Rewrite `skills/ea-artifact-templates/references/ea-concepts.md`

Deliver a full, production-ready replacement that preserves all existing concept definitions, ID schemes, Two Layers of Intent, practitioner notes, and TOGAF/ArchiMate mappings, and adds:

- **Business Context (CTX-NNN)** concept section:
  - What it IS: an analysis discipline capturing external and internal conditions shaping the organisation.
  - Source techniques: PESTEL, SWOT, competitor/market analysis, regulatory scanning, stakeholder power mapping.
  - Evidenced outputs: feeds `direction.drivers[]` (DRV), `direction.issues[]` (ISS), `direction.opportunities[]` (OPP), `policies[]` (POL), `constraints[]` (CST).
  - What it is NOT: not a Driver itself, not the Vision/Mission, not the Business Model Canvas.
  - TOGAF placement: Preliminary / Phase A; inputs to Architecture Vision and Engagement Charter.

- **Business Model Canvas (BMC-NNN)** concept section:
  - What it IS: a structured description of how the organisation creates, delivers, and captures (or justifies/sustains) value.
  - Sits between Strategy and Business Architecture.
  - Maps the nine blocks to existing registers:
    - Customer Segments → Stakeholder Map
    - Value Propositions → Business Services (SVC-NNN) / Value Streams (VS-NNN)
    - Channels → Operating Model §6 + service `deliveryChannel`
    - Customer Relationships → Operating Model §3 / Stakeholder Map
    - Revenue Streams → Cost Model Register (FIN-NNN)
    - Key Resources / Key Activities → Capability Model (CAP-NNN)
    - Key Partnerships → Vendor Landscape (VDR-NNN) / Sourcing model
    - Cost Structure → Cost Model Register (FIN-NNN)
  - What it is NOT: not a Capability Map, not an Operating Model, not a strategy.
  - TOGAF placement: Phase A/B boundary; BMC artifact in `templates/phase-b/business-model-canvas.md`.

- **Updated Motivation Framework diagram**
  - Insert **Business Context** above Business Drivers.
  - Insert **Business Model Canvas** alongside Strategies, feeding into Business Architecture and Operating Model.
  - Show feedback loops: Metrics → Issues/Problems; Operating Model performance → Business Context.

- **Updated Quick Reference Table**
  - Add rows for Business Context and Business Model Canvas.
  - Update Operating Model / Capability Model / Business Driver rows to reference the new concepts.

- **Concept-home table expansion**
  - Map mission, vision, goals, strategies, processes, capabilities, value streams, business rules, requirements, organisation design, roles, decision rights, and services across the four concepts.

### A2. ID Scheme Updates

- Add to `ea-assistant/CLAUDE.md` ID Scheme table:
  - `CTX-NNN` — Business Context finding/analysis entry
  - `BMC-NNN` — Business Model Canvas element/assumption entry
- Add decision journal entry: `decisions/2026-07-18-business-context-bmc-ids.md` explaining why new prefixes are justified despite the no-new-prefixes rule (BMC/CTX are cross-cutting business-layer concepts that need traceable IDs but are not domain-prefixed like BG-/DG-).

### A3. Documentation Updates

- `README.md` — add a feature bullet describing the four-concept business-layer model.
- `commands/ea-help.md` — update concepts shortcut list and add a tip referencing the four-concept flow.
- `commands/ea-help.md` command table — add `/ea-businesscontext` if a register command is created (see Phase B decision).
- `CLAUDE.md` — update version, command count, and key entry points if new commands are added.
- `docs/PRD.md` — add a new v0.9.89 section summarising the four-concept alignment.

---

## Phase B — Plugin Alignment

### B1. Commands

- `commands/ea-artifact.md` — ensure naming maps include "Business Context" and "Business Model Canvas" (Context routes to `business-architecture` §1 or a standalone context artifact; BMC routes to `business-model-canvas`).
- `commands/ea-grill.md` — add grill skill mapping:
  - Business Context → `grill-me-boardroom-strategy` or context/validity review
  - Business Model Canvas → `grill-me-boardroom-strategy`
- `commands/ea-interview.md` — update phase B intro to mention the four concepts; ensure Business Context questions route to BA §1 or context register; BMC questions route to BMC artifact.
- `commands/ea-brainstorm.md` — update Phase B prompt suggestions to include Business Context and BMC inputs.
- `commands/ea-consistency.md` — update ID pattern recognition to include `CTX-NNN` and `BMC-NNN`.
- *(Conditional)* `commands/ea-businesscontext.md` — new register command if Business Context is promoted to a managed register. If added, follows `/ea-drivers` register protocol: `list/add/update/trace/generate` for `CTX-NNN`.
- `commands/ea-migrate.md` — add migration probe for legacy Business Context placement and missing BMC/CTX links.

### B2. Skills

- `skills/ea-artifact-templates/references/compliance-check.md` — add any new T3/T4 rules for Business Context traceability (e.g., every Driver/Issue/Opportunity must cite a CTX-NNN source or be flagged as assumption) and BMC completeness.
- `skills/ea-engagement-lifecycle/references/grill-scoring-rubric.md` — add scoring weights for Business Context and BMC if they become scored artifacts.
- `skills/ea-artifact-templates/references/phase-interview-questions.md` — separate or enhance Business Context questions; ensure BMC interview bank is correctly placed.
- `skills/ea-engagement-lifecycle/references/engagement-schema.md` — add `businessContext[]` and `businessModelCanvas[]` arrays.
- `skills/ea-engagement-lifecycle/references/migration-gap-catalogue.md` — add 3m probe for Business Context / BMC alignment.
- `skills/ea-engagement-lifecycle/references/adm-phase-guide.md` — update Phase A/B descriptions to include Business Context and BMC.
- `skills/ea-engagement-lifecycle/references/persona-registry.md` — ensure personas reference all four concepts in report bundles/workflows.
- `skills/ea-artifact-templates/references/cross-topic-detection.md` — add cross-topic probes for Business Context findings vs Drivers/Issues, and BMC blocks vs Capability/OM boundaries.

### B3. Agents

- `agents/ea-interviewer.md` — load new Business Context and BMC concept definitions; route ambiguous answers using the four-concept home table.
- `agents/ea-document-analyst.md` — map uploaded business-model and context documents to CTX/BMC/BA/OM correctly.
- `agents/ea-grill-skills.md` / `skills/ea-grill-skills/SKILL.md` — include the four-concept distinction in challenge logic.

### B4. Templates

- `templates/phase-b/business-model-canvas.md` — review and update guidance to reference the new BMC concept definition and ID usage.
- `templates/phase-b/business-architecture.md` §1 Business Context — update guidance to link CTX-NNN findings.
- `templates/phase-b/operating-model.md` — update §1 to reference BMC as an input.
- *(Conditional)* `templates/cross-cutting/context/business-context-register.md` — if `/ea-businesscontext` register command is added.

### B5. Version Bump

- Bump to `v0.9.89` in:
  - `.claude-plugin/plugin.json`
  - `../.claude-plugin/marketplace.json`
  - `docs/PRD.md`
  - `commands/ea-help.md`
  - `README.md`
  - `CLAUDE.md`
  - all `skills/*/SKILL.md`

---

## Decision Point: Register Commands

The user confirmed new ID prefixes. Two implementation options:

| Option | Business Context | Business Model Canvas |
|---|---|---|
| **Minimal** | CTX-NNN used for detail files and inline references; no dedicated register command | BMC remains a single artifact; BMC-NNN used for detail files/assumptions |
| **Full register** | Add `/ea-businesscontext` command + `businessContext[]` array + register template | Add `/ea-bmcanvas` command + `businessModelCanvas[]` array + register template (more invasive; BMC is normally a single canvas) |

**Recommendation:** Minimal for BMC (it is a 9-block canvas artifact, not a list of entries); consider a `/ea-businesscontext` register command for CTX because context findings are discrete, evidenced, and reusable across phases.

---

## Verification

1. Frontmatter validation: `~/.bun/bin/bun .github/scripts/validate-frontmatter.ts ea-assistant/`
2. JSON validation: `plugin.json` and `marketplace.json`
3. Concept consistency scan: grep for inline definitions of Business Context / BMC / BA / OM; ensure they point to `ea-concepts.md`
4. ID scheme scan: confirm `CTX-NNN` and `BMC-NNN` are recognised by `/ea-consistency`
5. `/ea-help` command count check after any new commands

---

## Risks

- The full file rewrite of `ea-concepts.md` is large; must preserve existing content verbatim except for targeted insertions.
- Adding new ID prefixes breaks the recent "no new prefixes" rule; requires a decision journal entry.
- Business Model Canvas as BMC-NNN entries may confuse users if it is normally authored as one artifact.
