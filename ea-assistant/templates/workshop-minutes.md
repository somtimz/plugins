---
artifactId: workshop-minutes
artifact: Workshop Minutes
artifactId: ws-{{NNN}}
workshopId: WS-{{NNN}}
title: {{workshop_title}}
engagement: {{engagement_name}}
date: {{YYYY-MM-DD}}
facilitator: {{facilitator_name}}
location: {{location}}
status: In Progress
phase: {{phase_or_cross-cutting}}
relatedArtifact: {{artifact_or_phase_or_topic}}
templateVersion: 0.9.55
reviewStatus: Not Reviewed
lastModified: {{YYYY-MM-DDTHH:MM:SSZ}}
taxonomy:
  domain: Cross-cutting
  category: Governance
  audience: Architecture
  layer: Governance
  sensitivity: Confidential
  tags: [workshop, facilitation, decisions, cross-cutting]
relatedArtifacts: []
diagrams: []
links: []
---

<details>
<summary>📋 Guidance</summary>

**Purpose:** Workshop Minutes capture the outcomes of a facilitated architecture workshop — the decisions made, actions raised, and outputs produced. Decisions captured here flow into the Decision Register via `/ea-decisions generate` and may inform A3 Decision Log entries in related artifacts.

**What to include:** Attendees (with roles), agenda items, session outcomes per agenda item, formal decisions (in A3-format table), actions with owners and due dates, open items deferred to follow-up, and the next steps. Actions that reveal architecture risks should be flagged for the Risk Register.

**Quality indicators:**
- Decisions are captured in A3 format — not buried in narrative — so they can be extracted to the Decision Register
- Actions have named owners and target dates; unowned actions do not get done
- Open items are clearly distinguished from decisions — if a topic was discussed but not decided, note it as open

**Common mistakes:**
- Workshop outputs that are not connected to subsequent artifacts — every workshop decision should trace to an artifact update, an A3 entry, or an ADR
- Action owners not confirmed with the person during the session — assigned without confirmation means not accepted

**TOGAF reference:** TOGAF 10 §38 — Architecture Governance. Workshops are a core governance and analysis technique throughout the ADM; their outputs must be captured formally to be actionable.

</details>

## Attendees

| Name | Role | Organisation | Present (Y/N) |
|---|---|---|---|
| {{attendee_name}} | {{role}} | {{organisation}} | Y |

**Quorum required:** {{quorum_required — or "Not specified"}}
**Quorum met:** {{Yes / No / Not applicable}}

---

## Agenda

| # | Item | Owner | Time-box | Status |
|---|---|---|---|---|
| 1 | {{agenda_item_1}} | {{owner}} | {{N}} min | Pending |

---

## Session Outcomes

<details>
<summary>📋 Guidance</summary>

One subsection per agenda item. Capture the key discussion points, decisions, and outputs. Use the `a: {text}` shorthand in the facilitated session to log decisions to the Decisions table below. Keep discussion narrative brief — focus on the outputs and what was decided, not the full conversation.

</details>

### Item 1 — {{agenda_item_1}}

**Summary:** {{discussion_summary}}

**Key points raised:**
- ⚠️ Not answered

**Outputs produced:** {{artifact links or "None"}}

---

## Decisions

<!-- GUIDANCE:
  Use the same A3 governance table format as artifact Decision Logs.
  These rows are included in /ea-decisions generate output.
  For each decision with Authority = Strategic, add an A3.N rationale block below this table.
-->

| Item | Value | State | Captured By | Owner | Authority | Domain | Cost | Impact | Risk | Subject | Date |
|---|---|---|---|---|---|---|---|---|---|---|---|
| *(no decisions recorded)* | — | — | — | — | — | — | — | — | — | — | — |

---

## Actions Register

| # | Action | Owner | Due Date | Status |
|---|---|---|---|---|
| *(no actions recorded)* | — | — | — | — |

---

## Deferred Items

<!-- GUIDANCE:
  Items raised but not resolved in this session. Each item should have a clear owner and next step.
-->

| # | Item | Reason Deferred | Owner | Target Resolution |
|---|---|---|---|---|
| *(none)* | — | — | — | — |

---

## Open Questions

| # | Question | Raised By | Owner | Due Date |
|---|---|---|---|---|
| *(none)* | — | — | — | — |

---

## Next Meeting

**Proposed date:** {{YYYY-MM-DD or "TBD"}}

**Proposed agenda items:**
- {{next_agenda_item}}

---

## Appendix A4 — Stakeholder Concerns & Objections

| ID | Concern | Raised By | Category | Status | Response | Action / Owner |
|---|---|---|---|---|---|---|
| *(no concerns recorded)* | — | — | — | — | — | — |

---

## Artifact Working Notes

> Working-layer: persists across reviews. Not included in published meeting outputs.

### Comments

*Ad-hoc notes from participants or reviewers.*

| Date | Author | Note |
|---|---|---|
| — | — | — |

### Outstanding Tasks

*Action items not yet captured in the Actions Register, or meta-tasks about this document.*

- [ ] *(Add tasks)*
