---
artifact: Architecture Roadmap
artifactId: architecture-roadmap
engagement: {{engagement_name}}
phase: E/F
status: Draft
reviewStatus: Not Reviewed
version: 0.1
templateVersion: 0.9.55
lastModified: {{YYYY-MM-DD}}
taxonomy:
  domain: Cross-cutting
  category: Planning
  audience: All
  layer: Transition
  sensitivity: Internal
  tags: [roadmap, work-packages, sequencing, phase-e]
relatedArtifacts: []
diagrams: []
links: []
---
<details>
<summary>🔒 TOGAF/ADM Compliance Status (author only — collapses on export)</summary>

## Compliance Checklist

| Requirement | Status | Notes |
|---|---|---|
| T3-A3 | ⚠️ Pending | |
| T3-A4 | ⚠️ Pending | |
| T3-ADR | ⚠️ Pending | |
| T3-RATIONALE | ⚠️ Pending | |
| T3-ROAD-SA | ⚠️ Pending | |
| T3-ROAD-WP | ⚠️ Pending | |
| Linked to Architecture Vision | ⚠️ Pending | |

*This section is for author guidance only. Run `/ea-grill` to validate compliance.*

</details>

<details>
<summary>📋 Guidance</summary>

**Purpose:** The Architecture Roadmap organises the work packages (WP-NNN) that collectively deliver the Target Architecture, sequenced by priority and grouped into delivery waves. It is the primary planning instrument for Phase E–F and the reference for Phase H change management. Every gap identified in the Gap Analysis must trace to at least one work package here.

**What to include:** Work packages (WP-NNN) with priority, effort, dependencies, strategic alignment (goals/objectives they advance), evidence status, and the transition architecture state they contribute to. The roadmap must include a Strategic Alignment section (T3-ROAD-SA) and at least one WP must reference a goal or objective (T3-ROAD-WP). Waves group WPs into logical delivery increments.

**Quality indicators:**
- Every gap in the Gap Analysis maps to a WP in this roadmap — gaps without WPs are unplanned
- WPs are sequenced by business value, not just technical dependency — quick wins in Wave 1 build delivery credibility
- Dependencies are explicit: "WP-005 cannot start until WP-003 is complete and accepted"
- Evidence status is rated for each WP — WPs with Insufficient evidence should not appear in Wave 1

**Common mistakes:**
- Work packages that deliver technical milestones but no business value — "upgrade the database" is not a roadmap item unless the upgrade enables a specific business capability
- Roadmap without delivery waves — a flat priority list does not communicate the migration sequencing or transition architecture states
- Missing strategic alignment — every WP should trace to at least one goal (G-NNN) or strategy (STR-NNN)

**TOGAF reference:** TOGAF 10 Part III, Phase E (§29) and Phase F (§30) — Architecture Roadmap. Produced in Phase E, refined in Phase F, and updated in Phase H via the ACR process.

</details>

<details>
<summary>💡 Practitioner Tip — Roadmap</summary>

- **Package work as value increments** — every work package must deliver measurable business value, not just close a technical gap. (Deep tactic #26)
- Prioritize by **impact × feasibility** — high-impact, low-effort quick wins build momentum and credibility. (Deep tactic #27)
- Design **transition architectures** deliberately — the path matters more than the ideal end state. (Deep tactic #28)
- **Expose trade-offs explicitly** — when sequencing work, state what is deferred and the risk of deferral. (Deep tactic #29)
- Align work packages to **funding cycles and capacity windows** — architecture that ignores budget reality is fantasy. (Deep tactic #30)
- Replace heavy gates with **guardrails** — pre-approved patterns and automated checks allow local autonomy while protecting enterprise integrity. (Tip #24)
- Treat transition architectures as **strategic instruments**, not temporary compromises. (Tip #45)

</details>

# Architecture Roadmap

**Engagement:** {{engagement_name}}
**Organisation:** {{organisation}}
**Date:** {{YYYY-MM-DD}}
**Horizon:** {{time_horizon}}

---

## Executive Summary

<details>
<summary>📋 Guidance</summary>

High-level overview of the transformation journey: key work packages, phases, and expected outcomes.
Diagram: Roadmap timeline or swimlane diagram showing phases and major milestones
Run `/ea-summary refresh` to regenerate this section from current artifact content.

</details>

{{executive_summary}}

---

## Strategic Alignment

<details>
<summary>📋 Guidance</summary>

Map this roadmap to the Goals, Objectives, and Strategies defined in Phase A. Every Goal and Strategy in the Architecture Vision should be traceable to at least one Work Package. Gaps in coverage should be flagged explicitly.

</details>

| ID | Goal / Objective / Strategy | Type | Addressed by Work Packages | Details |
|---|---|---|---|---|
| [[{{G-001}}]] | {{goal_description}} | Goal | {{WP-NNN}} | [[{{G-001}}\|→]] |
| [[{{OBJ-001}}]] | {{objective_description}} | Objective | {{WP-NNN}} | [[{{OBJ-001}}\|→]] |
| [[{{STR-001}}]] | {{strategy_description}} | Strategy | {{WP-NNN}} | [[{{STR-001}}\|→]] |
| [[{{OPP-001}}]] | {{opportunity_description}} | Opportunity | {{WP-NNN}} | [[{{OPP-001}}\|→]] |

**Unaddressed items:** {{list_any_goals_objectives_strategies_not_covered_or_None}}

---

## Roadmap Overview

<details>
<summary>📋 Guidance</summary>

Provide a high-level timeline view. Reference a diagram if available.

</details>

*Reference diagram:* `../diagrams/{{roadmap_diagram}}`

---

## Work Packages

<details>
<summary>📋 Guidance</summary>

Each work package is a discrete unit of change that can be planned and resourced.
Work packages close gaps identified in the Gap Analysis.

</details>

### WP-001: {{work_package_name}}

| Field | Value |
|---|---|
| **ID** | [[WP-001]] |
| **Description** | {{description}} |
| **Advances Goals / Objectives** | {{g_obj_ids}} |
| **Executes Strategies** | {{str_ids}} |
| **Closes Gaps** | {{gap_ids}} |
| **Addresses Requirements** | {{req_ids}} |
| **Phase / Wave** | Wave 1 / Wave 2 / Wave 3 |
| **Estimated Effort** | {{effort}} |
| **Dependencies** | {{dependencies}} |
| **Owner** | {{owner}} |
| **Status** | Proposed / Approved / In Progress / Complete |
| **Resources Required** | Roles: {{roles}}  ·  FTE estimate: {{fte_estimate}}  ·  Skill dependencies: {{skill_dependencies}}  ·  Vendor / partner: {{vendor_or_partner}} |
| **Capacity note** | {{capacity_constraints_or_conflicts}} |
| **Resolves PAD** | {{pad_ids}} |
| **Evidence Required Before Start** | {{evidence_requirements}} |
| **Evidence Status** | Sufficient / Partial / Insufficient |
| **Decision Reversibility** | High / Medium / Low |
| **Value Delivery** | Standalone / Cumulative / Enabling |
| **Details** | [[WP-001\|→]] |

---

## Transition Architectures

<details>
<summary>📋 Guidance</summary>

Define the intermediate states (plateaus) between baseline and target.
Each plateau should be a stable, usable architecture state.

</details>

| Plateau | Description | Target Date | Work Packages |
|---|---|---|---|
| Plateau 1 | {{description}} | {{date}} | WP-001, WP-002 |
| Plateau 2 | {{description}} | {{date}} | WP-003 |
| Target | {{target_description}} | {{date}} | All |

---

## Prioritisation

<details>
<summary>📋 Guidance</summary>

Explain the prioritisation criteria used to sequence work packages.

</details>

{{prioritisation_rationale}}

---

## PAD Resolution Tracking

<details>
<summary>📋 Guidance</summary>

Work packages in Phase E must resolve Pending Architecture Decisions (PAD-NNN) from earlier
phases. Track which PADs each work package resolves, and flag any PADs that remain open
after their target work package completes.

</details>

| PAD-NNN | Description | Target WP | Resolution Status | Expiry Date | Risk if Expired |
|---|---|---|---|---|---|
| [[PAD-001]] | {{description}} | WP-003 | Resolved / Open / Expired | {{date}} | {{risk}} |

**Open PADs with expired target dates:** {{list_or_None}}

---

## Evidence-Gated Prioritisation

<details>
<summary>📋 Guidance</summary>

Prioritise work packages not only by impact and feasibility, but by evidence sufficiency.
Work packages with insufficient evidence should be flagged as high-risk or deferred until
evidence is gathered. Evidence gating prevents scheduling work packages whose underlying
decisions are still speculative.

</details>

| WP-NNN | Impact | Feasibility | Evidence Status | Prioritisation Verdict | Action |
|---|---|---|---|---|---|
| [[WP-001]] | High | High | Sufficient | ✅ Proceed | [[WP-001\|→]] |
| [[WP-002]] | High | Medium | Insufficient | ⚠️ Defer — gather evidence | {{action}} |
| [[WP-003]] | Medium | High | Partial | ⚠️ Proceed with guardrails | {{guardrails}} |

**Work packages blocked by insufficient evidence:** {{list_or_None}}

---

## Appendix A3 — Decision Log

<details>
<summary>📋 Guidance</summary>

Record all decisions made during the development of this artifact.
Each row captures the decision item, agreed value, governance state, who captured it,
who owns or must verify it, and classification fields used by /ea-decisions.
Use /ea-decisions to aggregate this table across all artifacts into a Decision Register.

</details>

| Item | Value | State | Captured By | Owner | Authority | Domain | Cost | Impact | Risk | Subject | Date |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| *(no decisions recorded)* | — | — | — | — | — | — | — | — | — | — | — |

---

## Appendix A4 — Stakeholder Concerns & Objections

<details>
<summary>📋 Guidance</summary>

Record all stakeholder concerns, objections, and tough questions raised about this artifact.
Sources include grill-me sessions, Architecture Review Board feedback, executive challenge
sessions, and sponsor meetings. For each concern, record whether it is addressed in existing
documentation (Addressed / Partially Addressed) or requires further action (Requires Attention).
Use `/ea-concerns` to aggregate unresolved items across all artifacts. Concerns that represent
a material risk should also be raised as RIS-NNN entries via `/ea-risks`.

</details>

| ID | Concern | Raised By | Category | Status | Response | Action / Owner |
|---|---|---|---|---|---|---|
| *(no concerns recorded)* | — | — | — | — | — | — |


## Appendix A5 — Related Architecture Decisions

<details>
<summary>📋 Guidance</summary>

List ADRs that informed, were informed by, or are otherwise relevant to this artifact.
Reference the ADR-NNN ID so readers can navigate to the full decision record.
Use `/ea-adrs` to manage the ADR Register and surface ADR summaries.

When a significant decision is made during an interview for this artifact, the
`ea-interviewer` will suggest creating an ADR if the decision meets the threshold
criteria (technology/vendor selection, high cost/risk, hard to reverse, etc.).

</details>

| ADR ID | Title | Status | Summary |
|---|---|---|---|
| *(no related ADRs recorded)* | — | — | — |

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

### Exceptions

*Formal exceptions granted to a standard, principle, or compliance rule — each must have a rationale and approver.*

| # | Rule / Principle Waived | Rationale | Approver | Date |
|---|---|---|---|---|
| — | — | — | — | — |

### Outstanding Tasks

*Things that must be completed before this artifact can move to Approved status.*

- [ ] *(Add tasks — e.g. "Populate §3 Assumptions before Phase B sign-off")*

*This document was created using the EA Assistant plugin.*
*Use `/ea-concerns` to generate a cross-artifact Concerns Register from all A4 tables.*
