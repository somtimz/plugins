---
artifact: Architecture Decision Record
adrid: ADR-{{NNN}}
title: {{decision_title}}
engagement: {{engagement_name}}
phase: {{phase}}
status: Candidate
decisionDate: {{YYYY-MM-DD}}
decisionOwner: {{owner}}
reviewedBy: {{reviewed_by}}
supersededBy: null
templateVersion: 0.9.7
lastModified: {{YYYY-MM-DD}}
taxonomy:
  domain: Cross-cutting
  category: Governance
  audience: Architecture
  layer: Governance
  sensitivity: Internal
  tags: [adr, decision, rationale, options]
---

<details>
<summary>📋 Guidance</summary>

An Architecture Decision Record (ADR) is a standalone document capturing a significant
architecture decision — one that has lasting consequences, involves meaningful trade-offs,
or requires full options analysis and documented rationale.

**When to create an ADR (not an A3 Decision Log entry):**
- Technology or vendor selection (cloud platform, database engine, integration middleware)
- Architecture pattern or style choice (microservices, event-driven, CQRS, layered)
- Make-vs-buy or build-vs-configure decisions
- Data governance approach (ownership, sharing, sovereignty model)
- Security or compliance architecture approach
- Significant API or integration design choice
- Any decision that is hard to reverse or whose rationale may be questioned later

**ADR vs. A3 Decision Log:**
- The **A3 Decision Log** (within an artifact's appendix) tracks governance state —
  who decided what, at what authority level, and whether it has been verified.
- An **ADR** documents the full decision context: what situation triggered it, what
  options were considered, why one was chosen, and what the consequences are.
- They complement each other: log a high-level entry in A3; create an ADR for the
  full documentation. Link them via the ADR-NNN ID.

**ADR lifecycle:**
Candidate → In Progress → Completed → Superseded (by ADR-NNN) | Deprecated

Use `/ea-adrs` to manage ADRs, track the register, and surface ADR summaries in
other artifacts. Run `/ea-adrs status` for a quick portfolio view.

</details>

# {{adrid}}: {{decision_title}}

**Engagement:** {{engagement_name}}
**Phase:** {{phase}}
**Status:** Candidate
**Decision Owner:** {{owner}}
**Reviewed By:** {{reviewed_by}}
**Decision Date:** {{YYYY-MM-DD}}

---

## 1. Status

<details>
<summary>📋 Guidance</summary>

Update this section as the ADR progresses through its lifecycle. Record the full history
— when the ADR was proposed, when review began, when the decision was made, and if/when
it was superseded.

</details>

| Date | Status | Changed By | Note |
|---|---|---|---|
| {{YYYY-MM-DD}} | Candidate | {{author}} | ADR proposed |
| {{YYYY-MM-DD}} | In Progress | {{reviewer}} | Options analysis underway |
| {{YYYY-MM-DD}} | Completed | {{decision_owner}} | Decision made |

**Current Status:** Candidate / In Progress / Completed / Superseded / Deprecated

**Superseded By:** *(if applicable)* — {{superseding_adr_id}}: {{superseding_adr_title}}

**Deprecation Reason:** *(if applicable)* — {{deprecation_reason}}

---

## 2. Context

<details>
<summary>📋 Guidance</summary>

Describe the situation that forces a decision. What is the problem or opportunity? What
constraints or forces are at play? What would happen if no decision were made?

Be concrete — describe the actual situation in this engagement, not a generic architecture
problem. Reference specific business drivers (DRV-NNN), goals (G-NNN), or existing
artifacts that surface the need for this decision.

</details>

{{decision_context}}

**Related business drivers / goals:** {{linked_drivers_goals}}

**Triggering artifact / section:** {{triggering_artifact}}
*(e.g. "Architecture Vision §7 STR-002 — Cloud-first strategy requires a cloud platform selection")*

---

## 3. Decision Drivers

<details>
<summary>📋 Guidance</summary>

List the specific criteria that must be satisfied by the decision. These become the
evaluation framework for the options. Good decision drivers are specific and testable —
"must support 10,000 concurrent users" is better than "must be scalable".

Order by importance: must-haves first, then nice-to-haves.

</details>

| # | Driver | Priority | Notes |
|---|---|---|---|
| 1 | {{driver}} | Must / Should / Nice-to-have | {{notes}} |
| 2 | {{driver}} | Must / Should / Nice-to-have | {{notes}} |
| 3 | {{driver}} | Must / Should / Nice-to-have | {{notes}} |

---

## 4. Options Considered

<details>
<summary>📋 Guidance</summary>

Document every option that was seriously considered — including the status quo (do nothing)
if that is a genuine option. For each option, list the pros and cons against the decision
drivers. Avoid being superficial: if an option was rejected, explain exactly why.

A minimum of two options should be documented. If only one option exists, document why
alternatives were not feasible.

</details>

### Option 1: {{option_1_title}}

{{option_1_description}}

**Pros:**
- {{pro}}
- {{pro}}

**Cons:**
- {{con}}
- {{con}}

**Assessment against drivers:**

| Driver | Satisfies? | Notes |
|---|---|---|
| {{driver}} | ✅ Yes / ⚠️ Partial / ❌ No | {{notes}} |

---

### Option 2: {{option_2_title}}

{{option_2_description}}

**Pros:**
- {{pro}}
- {{pro}}

**Cons:**
- {{con}}
- {{con}}

**Assessment against drivers:**

| Driver | Satisfies? | Notes |
|---|---|---|
| {{driver}} | ✅ Yes / ⚠️ Partial / ❌ No | {{notes}} |

---

### Option 3: {{option_3_title}} *(add or remove options as needed)*

{{option_3_description}}

**Pros:**
- {{pro}}

**Cons:**
- {{con}}

**Assessment against drivers:**

| Driver | Satisfies? | Notes |
|---|---|---|
| {{driver}} | ✅ Yes / ⚠️ Partial / ❌ No | {{notes}} |

---

## 5. Decision

<details>
<summary>📋 Guidance</summary>

State the decision clearly in one or two sentences. Name the chosen option. Do not
justify here — justification belongs in the Rationale section. The decision statement
should be unambiguous: a reader should be able to act on it without reading the rest
of the ADR.

</details>

**Decision:** {{decision_statement}}

**Chosen Option:** {{chosen_option_title}}

**Decision Made By:** {{decision_owner}}
**Decision Date:** {{YYYY-MM-DD}}
**Governance Reference:** {{a3_reference_or_arb_minute}}
*(Link to the A3 Decision Log entry or ARB meeting minute that formally recorded this decision)*

---

## 6. Rationale

<details>
<summary>📋 Guidance</summary>

Explain why the chosen option was selected over the alternatives. Reference the decision
drivers — show how the chosen option satisfies the must-have criteria and why the
trade-offs on the nice-to-haves are acceptable. If the decision was close, say so and
explain the tie-breaker.

</details>

{{rationale}}

**Key trade-offs accepted:**
- {{tradeoff}}
- {{tradeoff}}

---

## 7. Consequences

<details>
<summary>📋 Guidance</summary>

Describe the implications of this decision — what becomes easier, what becomes harder,
what new decisions are now required, and what risks are introduced. Be honest about
negative consequences — a decision with no downsides was probably not a hard decision.

Consequences are what make an ADR valuable over time: they tell future architects why
things are the way they are and what constraints they are working within.

</details>

### 7.1 Positive Consequences
- {{positive_consequence}}
- {{positive_consequence}}

### 7.2 Negative Consequences / Trade-offs
- {{negative_consequence}}
- {{negative_consequence}}

### 7.3 Neutral / Risks Introduced

| Risk | Likelihood | Impact | Mitigation | Linked Risk Register |
|---|---|---|---|---|
| {{risk}} | High / Med / Low | High / Med / Low | {{mitigation}} | RIS-NNN / — |

### 7.4 New Decisions Required

*Decisions that must now be made as a result of this decision:*

| Decision Needed | Priority | Suggested ADR | Owner |
|---|---|---|---|
| {{decision_needed}} | High / Med / Low | ADR-NNN (proposed) / — | {{owner}} |

---

## 8. Related Architecture Decisions

| ADR ID | Title | Relationship | Status |
|---|---|---|---|
| ADR-NNN | {{title}} | Precedes / Follows / Contradicts / Refines / Supersedes | {{status}} |

---

## 9. Affected Artifacts

*Architecture artifacts that document or are affected by this decision:*

| Artifact | Phase | Section | Nature of Impact |
|---|---|---|---|
| {{artifact_name}} | {{phase}} | §{N} {{section}} | {{impact_description}} |

---

## Appendix A4 — Stakeholder Concerns & Objections

<details>
<summary>📋 Guidance</summary>
Record concerns and objections raised about this decision during review. Use `/ea-concerns` to generate a cross-artifact Concerns Register.
</details>

| ID | Concern | Raised By | Category | Status | Response | Action / Owner |
|---|---|---|---|---|---|---|
| *(no concerns recorded)* | — | — | — | — | — | — |

---

*Use `/ea-adrs` to manage this ADR, update its status, and generate the ADR Register. Use `/ea-concerns` to manage concerns.*
