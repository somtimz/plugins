---
artifact: Problems Register
artifactId: problems-register
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
  audience: Governance
  layer: Motivation
  sensitivity: Internal
  tags: [problems, register, motivation, phase-a]
relatedArtifacts: ["architecture-vision"]
diagrams: []
links: []
---
<details>
<summary>🔒 TOGAF/ADM Compliance Status (author only — collapses on export)</summary>

## Compliance Checklist

| Requirement | Status | Notes |
|---|---|---|
| Every problem blocks at least one objective | ⚠️ Pending | |
| Every problem has an observable symptom and evidence | ⚠️ Pending | |

*This section is for author guidance only. Run `/ea-grill` to validate compliance.*

</details>

<details>
<summary>📋 Guidance</summary>

Problems are specific, observable, fixable symptoms actively blocking objectives — certain and present, with a measurable symptom. They are linked to the objective(s) they block and are parallel to Issues. The Engagement domain covers problems with the EA engagement itself.

This register is the management interface for problems; `engagement.json → direction` is the single source of truth. Use `/ea-problems` to add, update, trace, and regenerate it. The Architecture Vision summarises and links to this register rather than embedding the full table. Concept definitions live in `ea-concepts.md` — do not restate them here.

</details>

# Problems Register

**Engagement:** {{engagement_name}}
**Organisation:** {{organisation}}
**Generated:** {{YYYY-MM-DD}}
**Version:** {{version}}

---

## Summary

| Total | Critical | High | Medium | Low | Open | In Progress | Resolved | No evidence | No objectives |
|---|---|---|---|---|---|---|---|---|---|
| {{total}} | {{critical}} | {{high}} | {{medium}} | {{low}} | {{open}} | {{in_progress}} | {{resolved}} | {{no_evidence}} | {{no_objectives}} |

---

## Problems by Domain

<details>
<summary>📋 Guidance</summary>

Problems are specific, observable, and fixable — concrete symptoms actively blocking an objective, with a clear cause-and-effect relationship. Group by domain (Engagement first, then Business, Technology, Data, Application). Each problem links to the objective(s) it blocks. Problems are parallel to Issues, not derived from them.

</details>

### Engagement

#### PRB-001: {{problem_statement}}

| Field | Value |
|---|---|
| **ID** | [[PRB-001]] |
| **Problem** | {{statement}} |
| **Observable Symptom** | {{symptom}} |
| **Area / Domain** | Engagement / Business / Technology / Data / Application |
| **Type** | Operational / Technical / Data / Engagement / Compliance |
| **Severity** | Critical / High / Medium / Low |
| **Status** | Open / In Progress / Resolved |
| **Blocks Objective(s)** | OBJ-NNN |
| **Evidence** | {{evidence}} |
| **Raised By** | {{raisedBy}} |
| **Details** | [[PRB-001\|→]] |

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

*This register was generated using the EA Assistant plugin. Run `/ea-problems generate` to refresh from `engagement.json → direction`.*

