---
artifact: Strategy Register
artifactId: strategy-register
engagement: {{engagement_name}}
phase: A
status: Draft
reviewStatus: Not Reviewed
version: 0.1
templateVersion: 0.9.80
lastModified: {{YYYY-MM-DD}}
taxonomy:
  admPhases: [A]
  zachmanCell: "Scope/Why"
  domain: Cross-cutting
  category: Register
  audience: Executive
  layer: Motivation
  sensitivity: Internal
  tags: [strategies, register, motivation, phase-a]
relatedArtifacts: ["architecture-vision"]
diagrams: []
links: []
---
<details>
<summary>🔒 TOGAF/ADM Compliance Status (author only — collapses on export)</summary>

## Compliance Checklist

| Requirement | Status | Notes |
|---|---|---|
| Every strategy supports at least one goal or objective | ⚠️ Pending | |
| Every strategy is executed by at least one work package | ⚠️ Pending | |

*This section is for author guidance only. Run `/ea-grill` to validate compliance.*

</details>

<details>
<summary>📋 Guidance</summary>

Strategies are the chosen approaches ('how') that execute goals and objectives — they name a path, not an outcome. Each should support at least one goal/objective and be executed by at least one work package (DRV → G → OBJ → STR → WP).

This register is the management interface for strategy; `engagement.json → direction` is the single source of truth. Use `/ea-strategies` to add, update, trace, and regenerate it. The Architecture Vision summarises and links to this register rather than embedding the full table. Concept definitions live in `ea-concepts.md` — do not restate them here.

</details>

# Strategy Register

**Engagement:** {{engagement_name}}
**Organisation:** {{organisation}}
**Generated:** {{YYYY-MM-DD}}
**Version:** {{version}}

---

## Summary

| Total | Near | Mid | Long | High | Medium | Low | Active | Completed | Superseded | Orphans | Not executed |
|---|---|---|---|---|---|---|---|---|---|---|---|
| {{total}} | {{near}} | {{mid}} | {{long}} | {{high}} | {{medium}} | {{low}} | {{active}} | {{completed}} | {{superseded}} | {{orphans}} | {{not_executed}} |

---

## Strategies by Type

<details>
<summary>📋 Guidance</summary>

Strategy is the 'how' in the motivation chain — the chosen approach for pursuing goals and objectives (DRV → G → OBJ → STR → WP). Group by Type (Build, Buy, Partner, Consolidate, Modernise, Defend, Other). Every strategy should support at least one goal/objective and be executed by at least one work package.

</details>

### {{strategy_type}}

#### STR-001: {{strategy_statement}}

| Field | Value |
|---|---|
| **ID** | [[STR-001]] |
| **Strategy** | {{statement}} |
| **Type** | Build / Buy / Partner / Consolidate / Modernise / Defend / Other |
| **Supports Goal(s)/Objective(s)** | G-NNN, OBJ-NNN |
| **Horizon** | Near / Mid / Long |
| **Priority** | High / Medium / Low |
| **Status** | Active / Completed / Superseded |
| **Rationale** | {{rationale}} |
| **Details** | [[STR-001\|→]] |

---

## Appendix A3 — Decision Log

<details>
<summary>📋 Guidance</summary>

Record decisions made in the context of this register — e.g. acceptance of an item,
re-prioritisation, or scoping calls. Use A3 rows for decisions with strategic or
cross-artifact impact.

</details>

| Item | Value | State | Captured By | Owner | Authority | Domain | Cost | Impact | Risk | Subject | Date |
|---|---|---|---|---|---|---|---|---|---|---|---|
| *(no decisions recorded)* | | | | | | | | | | | |

---

## Artifact Working Notes

> Working-layer: persists across reviews. Populated by `/ea-grill` (Critiques), `/ea-review` (Comments), and manually. Never exported to Word/PPTX — stripped by `/ea-generate`.

### Comments

*Ad-hoc notes from architects, reviewers, or stakeholders.*

| Date | Author | Note |
|---|---|---|
| — | — | — |

### Critiques

*Formal findings from `/ea-grill` or `/ea-review` that require a response before this artifact can be approved.*

| # | Section | Finding | Source | Date | Status |
|---|---|---|---|---|---|
| — | — | — | — | — | Open |

### Outstanding Tasks

*Things that must be completed before this artifact can move to Approved status.*

- [ ] *(Add tasks)*

---

*This register was generated using the EA Assistant plugin. Run `/ea-strategies generate` to refresh from `engagement.json → direction`.*

