---
artifact: ARB Minutes
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
templateVersion: 0.9.31
lastModified: {{YYYY-MM-DDTHH:MM:SSZ}}
taxonomy:
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

<!-- GUIDANCE:
  ARB Minutes are the formal record of Architecture Review Board decisions.
  They are stored in artifacts/cross-cutting/ and always cross-cutting in scope.
  Decisions in the Decisions table link to ADR-NNN records and can be propagated 
  via /ea-arb close.
  If quorum was not met, all decisions are provisional — note this in the Quorum section.
-->

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

## Decisions

<!-- GUIDANCE:
  Record each formal decision made at this ARB meeting.
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
