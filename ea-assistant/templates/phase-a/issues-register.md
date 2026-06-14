---
artifact: Issues Register
artifactId: issues-register
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
  tags: [issues, register, motivation, phase-a]
relatedArtifacts: ["architecture-vision"]
diagrams: []
links: []
---
<details>
<summary>🔒 TOGAF/ADM Compliance Status (author only — collapses on export)</summary>

## Compliance Checklist

| Requirement | Status | Notes |
|---|---|---|
| Every issue links to at least one threatened goal | ⚠️ Pending | |
| Every issue cites observable evidence | ⚠️ Pending | |

*This section is for author guidance only. Run `/ea-grill` to validate compliance.*

</details>

<details>
<summary>📋 Guidance</summary>

Issues are systemic concerns threatening goals — present and ongoing, broad, with multiple contributing causes. They are linked to the goal(s) they threaten and are parallel to Problems. The Engagement domain covers issues about the EA engagement itself.

This register is the management interface for issues; `engagement.json → direction` is the single source of truth. Use `/ea-issues` to add, update, trace, and regenerate it. The Architecture Vision summarises and links to this register rather than embedding the full table. Concept definitions live in `ea-concepts.md` — do not restate them here.

</details>

# Issues Register

**Engagement:** {{engagement_name}}
**Organisation:** {{organisation}}
**Generated:** {{YYYY-MM-DD}}
**Version:** {{version}}

---

## Summary

| Total | Critical | High | Medium | Low | Open | Under Mitigation | Resolved | Accepted | No evidence | No goals |
|---|---|---|---|---|---|---|---|---|---|---|
| {{total}} | {{critical}} | {{high}} | {{medium}} | {{low}} | {{open}} | {{under_mitigation}} | {{resolved}} | {{accepted}} | {{no_evidence}} | {{no_goals}} |

---

## Issues by Domain

<details>
<summary>📋 Guidance</summary>

Issues are broad, systemic concerns that threaten the organisation's ability to achieve its goals — a pattern of dysfunction or capability gap with no single fix. Group by domain (Engagement first, then Business, Technology, Data, Application). Each issue links to the goal(s) it threatens. Issues are parallel to Problems, not parents of them.

</details>

### Engagement

#### ISS-001: {{issue_statement}}

| Field | Value |
|---|---|
| **ID** | [[ISS-001]] |
| **Issue** | {{statement}} |
| **Area / Domain** | Engagement / Business / Technology / Data / Application |
| **Type** | Organisational / Process / Technology / Regulatory / Capability |
| **Severity** | Critical / High / Medium / Low |
| **Status** | Open / Under Mitigation / Resolved / Accepted |
| **Threatens Goal(s)** | G-NNN |
| **Evidence** | {{evidence}} |
| **Raised By** | {{raisedBy}} |
| **Details** | [[ISS-001\|→]] |

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

*This register was generated using the EA Assistant plugin. Run `/ea-issues generate` to refresh from `engagement.json → direction`.*

