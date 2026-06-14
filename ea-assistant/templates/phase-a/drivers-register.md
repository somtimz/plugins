---
artifact: Drivers Register
artifactId: drivers-register
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
  domain: Business
  category: Register
  audience: Executive
  layer: Motivation
  sensitivity: Internal
  tags: [drivers, register, motivation, phase-a]
relatedArtifacts: ["architecture-vision"]
diagrams: []
links: []
---
<details>
<summary>🔒 TOGAF/ADM Compliance Status (author only — collapses on export)</summary>

## Compliance Checklist

| Requirement | Status | Notes |
|---|---|---|
| Every driver has at least one linked goal | ⚠️ Pending | |
| Every driver cites evidence or a source | ⚠️ Pending | |

*This section is for author guidance only. Run `/ea-grill` to validate compliance.*

</details>

<details>
<summary>📋 Guidance</summary>

Business drivers are the internal or external forces that make this engagement necessary — the conditions creating pressure to act. They sit at the top of the motivation chain (DRV → G → OBJ → STR → WP). Every driver should be answered by at least one goal.

This register is the management interface for drivers; `engagement.json → direction` is the single source of truth. Use `/ea-drivers` to add, update, trace, and regenerate it. The Architecture Vision summarises and links to this register rather than embedding the full table. Concept definitions live in `ea-concepts.md` — do not restate them here.

</details>

# Drivers Register

**Engagement:** {{engagement_name}}
**Organisation:** {{organisation}}
**Generated:** {{YYYY-MM-DD}}
**Version:** {{version}}

---

## Summary

| Total | External | Internal | High | Medium | Low | Orphans (no goal) | No evidence |
|---|---|---|---|---|---|---|---|
| {{total}} | {{external}} | {{internal}} | {{high}} | {{medium}} | {{low}} | {{orphans}} | {{no_evidence}} |

---

## External Drivers

<details>
<summary>📋 Guidance</summary>

External drivers are forces originating outside the organisation — market shifts, regulatory mandates, competitive moves. Group all External drivers here, highest priority first.

</details>

### DRV-001: {{driver_statement}}

| Field | Value |
|---|---|
| **ID** | [[DRV-001]] |
| **Driver** | {{statement}} |
| **Type** | External / Internal |
| **Priority** | High / Medium / Low |
| **Linked Goals** | G-NNN |
| **Evidence / Source** | {{evidence}} |
| **Details** | [[DRV-001\|→]] |

---

## Internal Drivers

<details>
<summary>📋 Guidance</summary>

Internal drivers are forces originating inside the organisation — cost pressure, capability gaps, leadership mandates. A driver with no linked goal is an orphan: it exerts pressure that no goal yet answers.

</details>

### DRV-00N: {{driver_statement}}

| Field | Value |
|---|---|
| **ID** | DRV-00N |
| **Driver** | {{statement}} |
| **Type** | External / Internal |
| **Priority** | High / Medium / Low |
| **Linked Goals** | G-NNN |
| **Evidence / Source** | {{evidence}} |
| **Details** | DRV-00N |

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

*This register was generated using the EA Assistant plugin. Run `/ea-drivers generate` to refresh from `engagement.json → direction`.*

