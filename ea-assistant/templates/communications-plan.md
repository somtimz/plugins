---
artifactId: communications-plan
artifact: Communications Plan
artifactId: communications-plan
engagement: {{engagement_name}}
phase: A
status: Draft
reviewStatus: Not Reviewed
version: 0.1
templateVersion: 0.9.55
lastModified: {{YYYY-MM-DD}}
taxonomy:
  domain: Cross-cutting
  category: Planning
  audience: All
  layer: Governance
  sensitivity: Internal
  tags: [communications, stakeholders, phase-a]
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

*This section is for author guidance only. Run `/ea-grill` to validate compliance.*

</details>

<details>
<summary>📋 Guidance</summary>

**Purpose:** The Communications Plan defines how and when architecture information will be communicated to each stakeholder group throughout the ADM cycle. It is the operational companion to the Stakeholder Map — where the Stakeholder Map identifies who cares about what, the Communications Plan defines the cadence, format, and channel for engaging each audience.

**What to include:** Communication objectives, stakeholder-to-audience mapping (who receives what), communication events (reviews, briefings, workshops, status reports) with frequency and format, the content tailoring strategy (executive summary vs technical detail vs operational impact), responsible owners for each communication, and the feedback mechanism.

**Quality indicators:**
- Communication events are tied to ADM phase gates — briefings are scheduled around Phase A sign-off, Phase B completion, etc., not just calendar weeks
- Content is tailored by audience — executives receive outcome summaries, delivery teams receive constraints and decisions, operational teams receive impact assessments
- The plan is updated when significant stakeholder changes occur — a new sponsor or programme director requires re-engagement strategy

**Common mistakes:**
- Communications plan that lists communication channels but not the content — a "monthly email" with no stated purpose is not a plan
- One-size-fits-all communications — all stakeholders receiving the same architecture update regardless of their interests or level of technical literacy
- Plan created in Phase A and never revisited — stakeholder communication needs change significantly as the engagement moves from analysis to delivery

**TOGAF reference:** TOGAF 10 Part III, Phase A (§25.3) — Stakeholder Management and Communications. The Communications Plan operationalises the stakeholder engagement strategy identified in Phase A.

</details>

# Communications Plan

**Engagement:** {{engagement_name}}
**Organisation:** {{organisation}}
**Date:** {{YYYY-MM-DD}}
**Owner:** {{communications_owner}}

---

## Executive Summary

<details>
<summary>📋 Guidance</summary>

Summary of the communications approach: who needs to know what, and when.
Diagram: Stakeholder communications timeline
Run `/ea-summary refresh` to regenerate this section from current artifact content.

</details>

{{executive_summary}}

---

## 1. Purpose and Scope

<details>
<summary>📋 Guidance</summary>

State the purpose of this communications plan and which audiences and phases it covers.

</details>

{{communications_purpose}}

---

## 2. Communication Objectives

<details>
<summary>📋 Guidance</summary>

List the specific goals of stakeholder communication for this engagement.
Examples: build awareness, obtain approval, manage change, provide assurance.

</details>

| Objective | Target Audience | Success Measure |
|---|---|---|
| {{objective}} | {{audience}} | {{measure}} |

---

## 3. Stakeholder Communication Matrix

<details>
<summary>📋 Guidance</summary>

For each stakeholder group, define what they need to know, how often, via what channel,
and who is responsible for that communication. Derive stakeholder groups from the Stakeholder Map.

</details>

| Stakeholder Group | Information Need | Frequency | Channel | Owner | ADM Phases |
|---|---|---|---|---|---|
| {{group}} | {{need}} | {{frequency}} | {{channel}} | {{owner}} | {{phases}} |

---

## 4. Communication Schedule

<details>
<summary>📋 Guidance</summary>

Map key communications events to ADM phase milestones. Include phase kick-offs,
phase gate reviews, Architecture Vision approval, and any formal governance checkpoints.

</details>

| Event | Audience | Format | Date / Milestone | Owner |
|---|---|---|---|---|
| Architecture Vision Briefing | Executive sponsors | Presentation | Phase A completion | {{owner}} |
| Phase Gate Review | Architecture Review Board | Formal review | End of each phase | {{owner}} |
| {{event}} | {{audience}} | {{format}} | {{date}} | {{owner}} |

---

## 5. Communication Channels

<details>
<summary>📋 Guidance</summary>

Describe the channels used for each type of communication.
Examples: email, formal report, presentation, workshop, steering committee, intranet.

</details>

| Channel | Purpose | Audience | Format |
|---|---|---|---|
| {{channel}} | {{purpose}} | {{audience}} | {{format}} |

---

## 6. Escalation and Feedback

<details>
<summary>📋 Guidance</summary>

Define how stakeholder feedback will be captured and how communications failures or
escalations will be handled.

</details>

{{escalation_process}}

---

## Appendix A3 — Decision Log

<details>
<summary>📋 Guidance</summary>

Record all decisions made during the development of this artifact.

</details>

| Item | Value | State | Captured By | Owner | Authority | Domain | Cost | Impact | Risk | Subject | Date |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| *(no decisions recorded)* | — | — | — | — | — | — | — | — | — | — | — |

---

## Appendix A4 — Stakeholder Concerns & Objections

| ID | Concern | Raised By | Category | Status | Response | Action / Owner |
|---|---|---|---|---|---|---|
| *(no concerns recorded)* | — | — | — | — | — | — |

---

## Appendix A5 — Related Architecture Decisions

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
