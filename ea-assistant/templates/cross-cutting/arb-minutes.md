---
artifact: ARB Minutes
artifactId: arb-minutes-{{ARB-NNN}}
phase: All
arbId: ARB-{{NNN}}
title: ARB Meeting {{NNN}} — {{YYYY-MM-DD}}
engagement: {{engagement_name}}
date: {{YYYY-MM-DD}}
chair: {{chair_name}}
secretary: {{secretary_name}}
location: {{location}}
quorumRequired: {{N}}
quorumMet: true
status: Draft
nextMeeting: null
templateVersion: 0.9.81
reviewStatus: Not Reviewed
lastModified: {{YYYY-MM-DDTHH:MM:SSZ}}
taxonomy:
  admPhases: [Preliminary, Requirements, A, B, C-Data, C-App, D, E, F, G, H]
  zachmanCell: ""
  domain: Cross-cutting
  category: Governance
  audience: Governance
  layer: Governance
  sensitivity: Confidential
  tags: [arb, governance, decisions, architecture-review, cross-cutting]
relatedArtifacts: []
diagrams: []
links: []
---

<details>
<summary>📋 Guidance</summary>

**Purpose:** ARB Minutes are the formal governance record of Architecture Review Board decisions. They provide the audit trail for all architecture decisions ratified at ARB level, and decisions captured here can be propagated to linked ADR-NNN records via `/ea-arb close`.

**What to include:** Attendees (with voting status), quorum confirmation, agenda items discussed, decisions made (with ADR links), actions raised, and the next meeting date. If quorum was not met, all decisions in the Decisions table are provisional — note this explicitly.

**Quality indicators:**
- Every decision has a named decision authority and links to its ADR-NNN where one exists
- Decisions are clearly separated from discussion points — a reader should be able to identify all binding decisions without reading the full minutes
- Actions have named owners and target dates — unowned actions are unmanaged actions

**Common mistakes:**
- Meeting minutes with no decisions — if the ARB met but made no formal decisions, note that explicitly; ambiguity about what was decided is a governance risk
- Provisional decisions (quorum not met) not flagged — provisional decisions must be ratified at the next quorate meeting before they are binding

**TOGAF reference:** TOGAF 10 §38 — Architecture Governance. ARB Minutes are the formal record of the Architecture Board's decision-making function, maintained in the Architecture Repository.

</details>

## Meeting Details

| Field | Value |
|---|---|
| ARB Reference | ARB-{{NNN}} |
| Date | {{YYYY-MM-DD}} |
| Time | {{HH:MM}} |
| Location / Platform | {{location}} |
| Chair | {{chair_name}} |
| Secretary | {{secretary_name}} |

---

## Attendees

| Name | Role | Member (Y/N) | Voting (Y/N) | Present (Y/N) |
|---|---|---|---|---|
| {{attendee_name}} | {{role}} | Y | Y | Y |

---

## Quorum

**Quorum required:** {{N}} voting members
**Voting members present:** {{N}}
**Quorum met:** {{Yes / No}}

<!-- GUIDANCE:
  If quorum is not met, all decisions in this meeting must be marked 
  "🔄 Provisional — pending quorum confirmation" rather than "✓ Verified".
  The /ea-arb close command enforces this check.
-->

---

## Agenda

| # | Item | Presenter | Time-box | Status |
|---|---|---|---|---|
| 1 | {{agenda_item}} | {{presenter}} | {{N}} min | Pending |

---

## Council Review

<!-- GUIDANCE:
  Populated by /ea-council or /ea-arb council. The ARB Council is an advisory review panel
  (planner, security, budget, architect, innovator, conservative — see
  skills/ea-engagement-lifecycle/references/arb-council-roster.md). Each member examines the
  subject through one mandate and casts a vote; the consolidated verdict informs the Decisions
  below. Leave as-is if no council review was held. Multiple reviews in one meeting stack as
  sub-blocks under a "### {subject}" heading.
-->

**Subject reviewed:** {{council_subject or "—"}}

| Member | Vote | Top Concern | Conditions |
|---|---|---|---|
| *(no council review held)* | — | — | — |

**Tally:** {{X}} Approve · {{Y}} Approve-with-conditions · {{Z}} Reject · {{W}} Abstain

**Consensus:** {{consensus}}

**Points of contention:** {{contention — e.g. Innovator vs Conservative trade-off}}

**Consolidated recommendation:** {{Endorse | Endorse with conditions | Do not endorse | Defer}}

---

## Decisions

<!-- GUIDANCE:
  Record each formal decision made at this ARB meeting.
  A council-reviewed subject yields a row whose Vote is the council tally and Outcome is the
  consolidated recommendation; conditions go to the Actions Register.
  Link to the relevant ADR-NNN when the decision relates to an Architecture Decision Record.
  Vote format: "X For / Y Against / Z Abstain"
  Governance Authority: Strategic / Tactical / Operational
  Use /ea-arb close to propagate these decisions back to the ADR register.
-->

| # | Item | Decision | Vote | ADR Reference | Governance Authority | Outcome | Owner |
|---|---|---|---|---|---|---|---|
| *(no decisions recorded)* | — | — | — | — | — | — | — |

---

## Deferred Items

| # | Item | Deferred To | Reason | Owner |
|---|---|---|---|---|
| *(none)* | — | — | — | — |

---

## Actions Register

| # | Action | Owner | Due Date | Status | Carried Forward From |
|---|---|---|---|---|---|
| *(no actions recorded)* | — | — | — | — | — |

---

## Next Meeting

**Proposed date:** {{YYYY-MM-DD or "TBD"}}

**Proposed agenda items:**
- {{next_agenda_item}}

**Standing agenda items:**
- Review outstanding actions from previous meeting
- Open ADRs requiring ARB decision
- Compliance assessment updates

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
