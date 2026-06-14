---
artifact: Objectives Register
artifactId: objectives-register
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
  audience: Business
  layer: Motivation
  sensitivity: Internal
  tags: [objectives, register, motivation, phase-a]
relatedArtifacts: ["architecture-vision"]
diagrams: []
links: []
---
<details>
<summary>🔒 TOGAF/ADM Compliance Status (author only — collapses on export)</summary>

## Compliance Checklist

| Requirement | Status | Notes |
|---|---|---|
| Every objective links to exactly one goal | ⚠️ Pending | |
| Every objective has a measure, target, and deadline | ⚠️ Pending | |

*This section is for author guidance only. Run `/ea-grill` to validate compliance.*

</details>

<details>
<summary>📋 Guidance</summary>

Objectives operationalise goals: each is a specific, measurable, time-bound result with a unit of measure, a target value, and a deadline. Problems block objectives; Metrics (MET-NNN) track them (DRV → G → OBJ).

This register is the management interface for objectives; `engagement.json → direction` is the single source of truth. Use `/ea-objectives` to add, update, trace, and regenerate it. The Architecture Vision summarises and links to this register rather than embedding the full table. Concept definitions live in `ea-concepts.md` — do not restate them here.

</details>

# Objectives Register

**Engagement:** {{engagement_name}}
**Organisation:** {{organisation}}
**Generated:** {{YYYY-MM-DD}}
**Version:** {{version}}

---

## Summary

| Total | High | Medium | Low | Orphans (no goal) | Not measurable |
|---|---|---|---|---|---|
| {{total}} | {{high}} | {{medium}} | {{low}} | {{orphans}} | {{not_measurable}} |

---

## Objectives by Goal

<details>
<summary>📋 Guidance</summary>

Objectives are specific, measurable, time-bound results that operationalise the goals — they answer 'how far, and by when?' Group by linked goal (orphans last). Each objective must have a measure, a target, and a deadline; missing any of the three makes it not measurable.

</details>

### Goal G-NNN

#### OBJ-001: {{objective_statement}}

| Field | Value |
|---|---|
| **ID** | [[OBJ-001]] |
| **Objective** | {{statement}} |
| **Measure** | {{measure}} |
| **Target** | {{target}} |
| **Deadline** | {{deadline}} |
| **Priority** | High / Medium / Low |
| **Linked Goal** | G-NNN |
| **Details** | [[OBJ-001\|→]] |

### Orphans (no linked goal)

#### OBJ-00N: {{objective_statement}}

| Field | Value |
|---|---|
| **ID** | OBJ-00N |
| **Objective** | {{statement}} |
| **Measure** | {{measure}} |
| **Target** | {{target}} |
| **Deadline** | {{deadline}} |
| **Priority** | High / Medium / Low |
| **Linked Goal** | — |
| **Details** | OBJ-00N |

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

*This register was generated using the EA Assistant plugin. Run `/ea-objectives generate` to refresh from `engagement.json → direction`.*

