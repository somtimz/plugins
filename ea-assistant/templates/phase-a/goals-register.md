---
artifact: Goals Register
artifactId: goals-register
engagement: {{engagement_name}}
phase: A
status: Draft
reviewStatus: Not Reviewed
version: 0.1
templateVersion: 0.9.86
lastModified: {{YYYY-MM-DD}}
taxonomy:
  admPhases: [A]
  zachmanCell: "Scope/Why"
  domain: Cross-cutting
  category: Register
  audience: Executive
  layer: Motivation
  sensitivity: Internal
  tags: [goals, register, motivation, phase-a]
relatedArtifacts: ["architecture-vision"]
diagrams: []
links: []
---
<details>
<summary>🔒 TOGAF/ADM Compliance Status (author only — collapses on export)</summary>

## Compliance Checklist

| Requirement | Status | Notes |
|---|---|---|
| Every goal traces to at least one business driver | ⚠️ Pending | |
| Every goal is operationalised by at least one objective | ⚠️ Pending | |

*This section is for author guidance only. Run `/ea-grill` to validate compliance.*

</details>

<details>
<summary>📋 Guidance</summary>

Goals are broad, qualitative outcomes the strategy is intended to achieve — they answer 'where do we want to be?' Each goal traces upward to the drivers that made it necessary and downward to the objectives that operationalise it (DRV → G → OBJ).

This register is the management interface for goals; `engagement.json → direction` is the single source of truth. Use `/ea-goals` to add, update, trace, and regenerate it. The Architecture Vision summarises and links to this register rather than embedding the full table. Concept definitions live in `ea-concepts.md` — do not restate them here.

</details>

# Goals Register

**Engagement:** {{engagement_name}}
**Organisation:** {{organisation}}
**Generated:** {{YYYY-MM-DD}}
**Version:** {{version}}

---

## Summary

| Total | High | Medium | Low | Active | Achieved | Superseded | Orphans (no driver) | Not operationalised |
|---|---|---|---|---|---|---|---|---|
| {{total}} | {{high}} | {{medium}} | {{low}} | {{active}} | {{achieved}} | {{superseded}} | {{orphans}} | {{not_operationalised}} |

---

## Goals by Domain

<details>
<summary>📋 Guidance</summary>

Goals are broad, qualitative outcomes the strategy is intended to achieve. Group by architecture domain (Business, Technology, Data, Application, Cross-cutting). Each goal should trace to one or more business drivers; a goal with no driver and no objective is an orphan. **Two Layers check:** a goal about EA governance/standards belongs in the Governance Framework, not here.

</details>

### Business

#### G-001: {{goal_statement}}

| Field | Value |
|---|---|
| **ID** | [[G-001]] |
| **Goal** | {{statement}} |
| **Domain** | Business / Technology / Data / Application / Cross-cutting |
| **Type** | Strategic / Operational / Capability / Compliance |
| **Priority** | High / Medium / Low |
| **Status** | Active / Achieved / Superseded |
| **Stakeholder** | Senior Management / Business Unit Manager / Staff / Ultimate Client |
| **Business Driver(s)** | DRV-NNN |
| **Rationale** | {{rationale}} |
| **Details** | [[G-001\|→]] |

### Technology

#### G-00N: {{goal_statement}}

| Field | Value |
|---|---|
| **ID** | G-00N |
| **Goal** | {{statement}} |
| **Domain** | Business / Technology / Data / Application / Cross-cutting |
| **Type** | Strategic / Operational / Capability / Compliance |
| **Priority** | High / Medium / Low |
| **Status** | Active / Achieved / Superseded |
| **Stakeholder** | Senior Management / Business Unit Manager / Staff / Ultimate Client |
| **Business Driver(s)** | DRV-NNN |
| **Rationale** | {{rationale}} |
| **Details** | G-00N |

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

*This register was generated using the EA Assistant plugin. Run `/ea-goals generate` to refresh from `engagement.json → direction`.*

