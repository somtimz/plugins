---
artifact: Business Case
artifactId: business-case
engagement: {{engagement_name}}
phase: A
status: Draft
reviewStatus: Not Reviewed
version: 0.1
templateVersion: 0.9.66
lastModified: {{YYYY-MM-DD}}
taxonomy:
  domain: Cross-cutting
  category: Planning
  audience: Executive
  layer: Motivation
  sensitivity: Confidential
  tags: [business-case, funding, cost-benefit, tco, phase-a]
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
| T4-ECON | ⚠️ Pending | Recommended option framed in cost/risk/value terms |
| T4-TCO | ⚠️ Pending | Options carry numeric TCO with confidence (from FIN entries) |

*This section is for author guidance only. Run `/ea-grill` to validate compliance.*

</details>

<details>
<summary>📋 Guidance</summary>

**Purpose:** The Business Case is the economic and political instrument that secures the mandate and funding for the architecture engagement. It states the problem, compares the realistic options on cost, value, and risk, and recommends one — backed by architecture-grade Cost Entries (FIN-NNN), not hand-waving. It is the artifact a sponsor reads before committing money.

**What to include:** A clear problem/opportunity tied to business drivers and goals; a small set of genuinely distinct options (including "do nothing"); a cost-benefit comparison drawn from the Cost Model Register (`/ea-finance`); a defensible recommendation with rationale; assumptions with confidence; key risks; funding and timing aligned to the roadmap waves; and how benefit realisation will be tracked.

**Quality indicators:**
- Every option carries a TCO and a value statement at a stated confidence — no option is costed in isolation from its benefit
- The recommended option's rationale addresses cost, risk, AND value — not just one (T4-ECON)
- "Do nothing" is costed honestly — the cost of inaction is the baseline every other option is measured against
- Funding asks line up with roadmap waves and annual funding cycles — a business case that ignores the funding calendar rarely gets approved
- Benefit realisation is assigned a `benefit`-type metric and an owner — claimed value that no one tracks is a promise no one keeps

**Common mistakes:**
- Single-option business cases — if there is only one option, it is a justification, not a business case
- Benefits stated qualitatively while costs are precise — asymmetry that makes the case look worse than it is, or hides weak value
- Spurious precision — a Low-confidence estimate dressed up as an exact figure; state the confidence and basis instead
- Costing the build but not the run — Opex over the horizon usually dwarfs Capex

**TOGAF reference:** TOGAF 10 Part II, Phase A — the Business Case supports the Request for Architecture Work and Architecture Vision. Drafted in Phase A with directional estimates; refined in Phase F once the Architecture Roadmap and Cost Entries are firm.

</details>

# Business Case

**Engagement:** {{engagement_name}}
**Organisation:** {{organisation}}
**Sponsor:** {{sponsor}}
**Date:** {{YYYY-MM-DD}}
**Decision sought:** {{funding_or_mandate_decision_requested}}

---

## Executive Summary

<details>
<summary>📋 Guidance</summary>

One paragraph a sponsor can act on: the problem, the recommended option, what it costs (3-year TCO), what it returns (payback / annual benefit), and the decision being asked for.
Run `/ea-summary refresh` to regenerate this section from current artifact content.

</details>

{{executive_summary}}

---

## 1. Problem / Opportunity

<details>
<summary>📋 Guidance</summary>

What business problem or opportunity drives this investment? Link to the drivers (DRV-NNN), goals (G-NNN), and objectives (OBJ-NNN) it serves, and state the cost of inaction.

</details>

| Element | Detail |
|---|---|
| **Problem / opportunity** | {{problem_statement}} |
| **Business drivers** | {{drv_ids}} |
| **Goals / objectives served** | {{g_obj_ids}} |
| **Cost of inaction** | {{what_happens_if_we_do_nothing}} |

---

## 2. Options Considered

<details>
<summary>📋 Guidance</summary>

Compare genuinely distinct options, including "do nothing". Pull cost figures from the Cost Model Register (`/ea-finance`) — each option should reference its FIN-NNN entries. TCO and payback are architecture-grade estimates with a confidence rating; do not present them as committed budgets.

</details>

| Option | Cost Entry | Capex | Opex (annual) | 3-Year TCO | Annual Benefit | Payback | Confidence | Key trade-off |
|---|---|---|---|---|---|---|---|---|
| Option 0 — Do nothing | [[FIN-00N]] | {{capex}} | {{opex_annual}} | {{tco}} | {{benefit}} | {{payback}} | {{confidence}} | {{tradeoff}} |
| Option 1 — {{name}} | [[FIN-00N]] | {{capex}} | {{opex_annual}} | {{tco}} | {{benefit}} | {{payback}} | {{confidence}} | {{tradeoff}} |
| Option 2 — {{name}} | [[FIN-00N]] | {{capex}} | {{opex_annual}} | {{tco}} | {{benefit}} | {{payback}} | {{confidence}} | {{tradeoff}} |

---

## 3. Recommended Option

<details>
<summary>📋 Guidance</summary>

State the recommendation and justify it in cost, risk, AND value terms (T4-ECON). Explain why the rejected options were rejected — the reasoning is as important as the choice.

</details>

| Element | Detail |
|---|---|
| **Recommended option** | {{option}} |
| **Rationale (cost · risk · value)** | {{rationale}} |
| **Why not the alternatives** | {{why_others_rejected}} |
| **Related decision** | {{adr_or_pad_id}} |

---

## 4. Cost-Benefit Summary

<details>
<summary>📋 Guidance</summary>

The headline economics of the recommended option, drawn from its Cost Entries. Keep this consistent with the Cost Model Register — regenerate via `/ea-finance generate` rather than editing figures by hand.

</details>

| Measure | Value | Confidence |
|---|---|---|
| Total Capex | {{currency}} {{capex}} | {{confidence}} |
| Opex (annual run-rate) | {{currency}} {{opex_annual}} | {{confidence}} |
| 3-Year TCO | {{currency}} {{tco}} | {{confidence}} |
| Annual benefit (quantified) | {{currency}} {{annual_benefit}} | {{confidence}} |
| Payback period | {{payback_months}} months | {{confidence}} |
| Qualitative value | {{benefit_narrative}} | — |

---

## 5. Assumptions & Confidence

<details>
<summary>📋 Guidance</summary>

The estimates above are only as good as their assumptions. List the material ones and what would change the case if they prove wrong.

</details>

| Assumption | Confidence | Impact if wrong |
|---|---|---|
| {{assumption}} | High / Medium / Low | {{impact}} |

---

## 6. Key Risks

<details>
<summary>📋 Guidance</summary>

Risks that materially affect the cost, value, or deliverability of the recommended option. Material risks should also be raised as RIS-NNN via `/ea-risks`.

</details>

| Risk | Likelihood | Impact | Mitigation | RIS-NNN |
|---|---|---|---|---|
| {{risk}} | High / Medium / Low | High / Medium / Low | {{mitigation}} | {{ris_id}} |

---

## 7. Funding & Timing

<details>
<summary>📋 Guidance</summary>

Align the funding ask to the Architecture Roadmap waves and the organisation's annual funding cycles. State what is needed, when, and from which budget.

</details>

| Wave / Year | Work Packages | Capex ask | Opex impact | Funding source |
|---|---|---|---|---|
| {{wave_or_year}} | {{wp_ids}} | {{capex}} | {{opex}} | {{source}} |

---

## 8. Benefits Realisation

<details>
<summary>📋 Guidance</summary>

Claimed value that no one tracks is a promise no one keeps. Assign a `benefit`-type metric (`/ea-finance` projects the value; the metric measures the actual) and an owner for each benefit. Reviewed in Phase G against the implementation-governance question *"did we deliver the expected benefit?"*.

</details>

| Benefit | Cost Entry | Benefit Metric | Owner | Realisation date |
|---|---|---|---|---|
| {{benefit}} | [[FIN-00N]] | {{met_id}} | {{owner}} | {{date}} |

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

- [ ] *(Add tasks — e.g. "Cost the 'do nothing' option before sponsor review")*

*This document was created using the EA Assistant plugin.*
