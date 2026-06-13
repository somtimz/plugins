---
artifact: Business Transformation Readiness Assessment
artifactId: business-transformation-readiness
engagement: {{engagement_name}}
phase: A
status: Draft
reviewStatus: Not Reviewed
version: 0.1
templateVersion: 0.9.59
lastModified: {{YYYY-MM-DD}}
taxonomy:
  domain: Business
  category: Assessment
  audience: Executive
  layer: Strategy
  sensitivity: Internal
  tags: [readiness, transformation, btra, phase-a]
relatedArtifacts: ["architecture-vision", "architecture-roadmap"]
diagrams: []
links: []
---

# Business Transformation Readiness Assessment

**Engagement:** {{engagement_name}}
**Assessed:** {{YYYY-MM-DD}}
**Assessors:** {{assessor_names_and_roles}}

<details>
<summary>📋 Guidance</summary>

**Purpose:** A TOGAF Phase A technique (refined in Phase E) that rates the organisation's readiness to absorb the transformation **before** the roadmap is committed. Each factor gets a readiness rating, an urgency, and a degree of difficulty to fix. Low-readiness / high-urgency factors become risks (RIS-NNN) and often readiness work packages (WP-NNN) sequenced in Wave 1.

**Quality indicators:** every factor is rated with evidence (not opinion); low-readiness factors carry a named action and an owner; readiness findings are traced to RIS/WP/ISS IDs; the assessment is revisited at Phase E so wave sequencing respects readiness rather than assuming it.

**Common mistakes:** rating readiness without evidence; assessing only IT readiness and ignoring business absorption capacity; treating the assessment as a one-off Phase A checkbox instead of a Phase E sequencing input.

**TOGAF reference:** TOGAF 10 Part III — Business Transformation Readiness Assessment; complements the Architecture Vision and feeds the Architecture Roadmap.

</details>

---

## Executive Summary

<details>
<summary>📋 Guidance</summary>

A short verdict a sponsor can act on: overall readiness (e.g. "Conditionally ready — 3 of 12 factors Low"), the factors that most threaten delivery, and the readiness work required before Wave 1 can safely start.
Run `/ea-summary refresh` to regenerate this section from current content.

</details>

{{executive_summary}}

---

## Readiness Factor Assessment

<details>
<summary>📋 Guidance</summary>

Rate all 12 factors. **Readiness** = how ready the organisation is on that dimension today; **Urgency** = how soon it must be addressed for the transformation to proceed; **Difficulty** = how hard it is to raise. Each rating needs evidence — an incident, a quote, a missing budget line — not a gut feel. The dangerous quadrant is **Low readiness + High urgency**: those factors gate the roadmap and almost always need a readiness work package before Wave 1. Don't average the scores into a single number; the distribution is what matters.

</details>

Rating scale — **Readiness:** High / Acceptable / Low / None · **Urgency:** High / Medium / Low · **Difficulty to fix:** High / Medium / Low

| # | Factor | Readiness | Urgency | Difficulty | Evidence |
|---|---|---|---|---|---|
| 1 | Vision clarity — is the transformation vision defined and understood? | {{r1}} | {{u1}} | {{d1}} | {{e1}} |
| 2 | Desire / willingness — do stakeholders want this change? | {{r2}} | {{u2}} | {{d2}} | {{e2}} |
| 3 | Need — is the case for change recognised as urgent and real? | {{r3}} | {{u3}} | {{d3}} | {{e3}} |
| 4 | Business case — is there an approved, funded business case? | {{r4}} | {{u4}} | {{d4}} | {{e4}} |
| 5 | Funding — is funding secured for the full change horizon, not just phase 1? | {{r5}} | {{u5}} | {{d5}} | {{e5}} |
| 6 | Sponsorship & leadership — is there an active, senior, accountable sponsor? | {{r6}} | {{u6}} | {{d6}} | {{e6}} |
| 7 | Governance — can decisions be made and enforced at the required pace? | {{r7}} | {{u7}} | {{d7}} | {{e7}} |
| 8 | Accountability — are change outcomes owned by named individuals? | {{r8}} | {{u8}} | {{d8}} | {{e8}} |
| 9 | Workable approach — is the delivery approach realistic for this organisation? | {{r9}} | {{u9}} | {{d9}} | {{e9}} |
| 10 | IT capacity to execute — can IT deliver the technical change at this scale? | {{r10}} | {{u10}} | {{d10}} | {{e10}} |
| 11 | Enterprise capacity to execute — can the business absorb the change alongside operations? | {{r11}} | {{u11}} | {{d11}} | {{e11}} |
| 12 | Ability to implement and operate — can the organisation run the target state once delivered? | {{r12}} | {{u12}} | {{d12}} | {{e12}} |

---

## Factor Detail — Low / None Readiness Only

<details>
<summary>📋 Guidance</summary>

One block per factor rated Low or None — these are the factors that can sink the transformation. State what was observed, the consequence if it is not addressed, the actions to raise readiness, and the ID each finding was captured as (RIS-NNN risk, WP-NNN readiness work package, or ISS-NNN issue). Delete this section if all factors are High / Acceptable.

</details>

### Factor {{N}} — {{factor_name}}

- **Finding:** {{what_was_observed}}
- **Impact if unaddressed:** {{consequence_for_the_transformation}}
- **Readiness actions:** {{actions_to_raise_readiness}}
- **Captured as:** {{RIS-NNN / WP-NNN / ISS-NNN references}}

---

## Roadmap Implications

<details>
<summary>📋 Guidance</summary>

Completed / refined at Phase E. Translate readiness findings into concrete constraints on the roadmap: change-capacity ceilings (how many business-facing work packages can run at once), readiness work packages that must precede Wave 1, and any sequencing forced by low-readiness factors. A roadmap that ignores these implications is fiction — this is where readiness becomes a planning input, not a report.

</details>

| Implication | Affected waves / work packages |
|---|---|
| {{e.g. "Change-capacity ceiling: max 2 concurrent business-facing WPs"}} | {{WP-NNN list}} |
| {{e.g. "Readiness WP required before Wave 1: governance decision rights"}} | {{WP-NNN}} |

---

## Appendix A3 — Decision Log

| Item | Value | State | Captured By | Owner | Authority | Domain | Cost | Impact | Risk | Subject | Date |
|---|---|---|---|---|---|---|---|---|---|---|---|
| *(no decisions recorded)* | | | | | | | | | | | |

## Appendix A4 — Stakeholder Concerns & Objections

| ID | Concern | Raised By | Category | Status | Response | Action/Owner |
|---|---|---|---|---|---|---|
| *(no concerns recorded)* | | | | | | |
