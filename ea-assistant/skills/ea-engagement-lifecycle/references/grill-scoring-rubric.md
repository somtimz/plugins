# Grill Scoring Rubric

Defines the two scores the grill engine assigns to every authored artifact **and to each of its sections**: **Completeness** and **Quality**, each `0–100` with a band. Grounded exactly in three sources — the EA concept definitions (`skills/ea-artifact-templates/references/ea-concepts.md`), the artifact's own `<details>📋 Guidance</details>` blocks (Purpose / Quality indicators / Common mistakes), and the compliance tiers (`skills/ea-artifact-templates/references/compliance-check.md`). Consumed by `ea-grill-skills` and the `/ea-score` command; rendered into the artifact's **Scorecard block**.

## Scale and bands (both scores)

| Score | Band |
|---|---|
| 90–100 | Comprehensive |
| 75–89 | Substantial |
| 50–74 | Partial |
| 25–49 | Skeletal |
| 0–24 | Stub |

## Completeness — "Is everything that should be here, here and populated?"

Per section, score `0–100` on whether the content the section's guidance (or, where no guidance block exists, TOGAF best practice for the artifact type) calls for is **present and populated** — not placeholder, TBD, or empty.

Signals: all guidance-required elements present and non-placeholder (no `{{...}}` tokens, no "TBD"/"TODO", no empty tables or bullet stubs); required IDs assigned and traceability fields populated; for compliance-bearing sections, the relevant T1–T3 rule satisfied.

Map the existing section verdict (Complete / Partial / Empty / Inconsistent) to a band:

| Section state | Completeness |
|---|---|
| Complete & fully populated | 85–100 |
| Mostly populated, minor gaps | 60–84 |
| Partial / skeletal | 30–59 |
| Empty / placeholder-only | 0–29 |
| Opted out (`⊘`) or `N/A` | excluded from the roll-up |

## Quality — "Is what's here good?"

Per section with content, score `0–100` across four sub-dimensions, then take the weighted mean:

1. **Definition-correctness (30%)** — content matches the EA definitions in `ea-concepts.md`: a Goal is qualitative (not a measure), an Objective is SMART, a Strategy names an approach (not a plan or an outcome), a Constraint is not a Principle, a Risk carries a *real* mitigation (funded, owned, scheduled, measurable), a **Capability** is an outcome-based noun with a stated value/outcome and strategic anchor (not a process or org structure; an anchorless or valueless capability is "inflation"). A clear misclassification caps this sub-dimension at 40.
2. **Guidance adherence (30%)** — meets the section's **Quality indicators** and avoids its **Common mistakes** from the guidance block.
3. **Evidence & rigour (20%)** — claims are evidenced; decisions carry rationale; numbers state a basis; assumptions are explicit.
4. **Readability (20%)** — clarity, structure, concision, controlled jargon, scannability. Content a stakeholder cannot follow in a single read loses readability points regardless of correctness.

**Empty sections score Quality `—` (not 0)** and are excluded from the Quality roll-up — the quality of absent content is undefined, and completeness already penalises the absence.

## Roll-up (artifact overall)

- **Overall Completeness** = weighted mean of section completeness, weighting required / compliance-bearing sections **2×** optional ones. Appendices A3/A4/A5 count as optional.
- **Overall Quality** = mean of section Quality over sections that have content (empty excluded).
- Report each as `{score}/100 ({band})`.

## Readability pass (Quality input)

Assess per section: average sentence length and clarity; acronyms/jargon defined on first use; paragraph and table structure (no wall-of-text); consistent terminology (same concept → same word). Record the worst-offending section in the Scorecard Notes column so the author knows where to tighten prose.

## Scorecard block (written into the artifact)

`/ea-score` and `/ea-grill` write/refresh an **author-only** Scorecard block, placed immediately after the `🔒 TOGAF/ADM Compliance Status` block (or, if absent, after the H1 title). It is a `<details>` block, so it **collapses in the editor and is stripped on export** by `/ea-generate` and `/ea-publish` — scores never reach a stakeholder deliverable.

```
<details>
<summary>📊 Scorecard (author only — last scored {YYYY-MM-DD} · collapses on export)</summary>

| Section | Completeness | Quality | Notes |
|---|---|---|---|
| 1. Executive Summary | 85 (Substantial) | 70 (Partial) | readability: dense — split long sentences |
| 2. Business Drivers | 90 (Comprehensive) | 82 (Substantial) | — |
| … | … | … | … |
| **Overall** | **78 (Substantial)** | **66 (Partial)** | — |

*Scored against `grill-scoring-rubric.md`. Refresh with `/ea-score {artifact-id}`.*
</details>
```

When refreshing, **replace** the existing Scorecard block in place (match on the `📊 Scorecard` summary) — never append a second one. If the artifact is `Approved`, scoring is read-only by default: write the block only on explicit confirmation, and leave `reviewStatus` unchanged (a score is an assessment, not a content edit).

---

## Artifact-Specific Section Weights

Completeness weights by artifact type. Required / compliance-bearing sections are weighted **2×** in the overall Completeness roll-up; optional sections are weighted **1×**.

### Operating Model (`operating-model.md`)

| Section | Weight | Required? | Rationale |
|---|---|---|---|
| 1. Operating Model Context | 2× | Yes | Must anchor the OM to the Business Architecture and Architecture Vision |
| 2. Organisation Design | 2× | Yes | Core OM content — how operating units are arranged |
| 3. Roles, Decision Rights & Accountability | 2× | Yes | Core OM content — who decides and who is accountable |
| 4. Governance, Controls & SLAs | 2× | Yes | Core OM content — how conformance is managed |
| 5. Business Processes Execution Model | 2× | Yes | Must link to the authoritative PROC-NNN register |
| 6. Workforce, Locations & Channels | 1× | No | Contextual; omit only if genuinely not applicable |
| 7. Sourcing & Partnership Model | 1× | No | Required when make/buy/partner choices exist |
| 8. Information & Technology Enablement | 1× | No | Required when Phase C/D enablement is in scope |
| 9. Performance Management | 1× | No | Required when metrics are part of the OM |
| 10. Gap Analysis | 1× | No | Required when OM gaps are identified |
| 11. Requirements Addressed | 1× | No | Required when OM generates requirements |
| Appendix A3 — Decision Log | 2× | Yes | T3-A3 compliance |
| Appendix A4 — Stakeholder Concerns | 2× | Yes | T3-A4 compliance |
| Appendix A5 — Related ADRs | 1× | No | T3-ADR compliance |

### Business Model Canvas (`business-model-canvas.md`)

| Section | Weight | Required? | Rationale |
|---|---|---|---|
| 1. Customer Segments | 2× | Yes | Core BMC content — who the business serves |
| 2. Value Propositions | 2× | Yes | Core BMC content — what value is created for each segment |
| 3. Channels | 1× | No | Required when delivery channels matter to the architecture |
| 4. Customer Relationships | 1× | No | Required when relationship model affects operations |
| 5. Revenue Streams | 2× | Yes | Financial grounding — how value is captured |
| 6. Key Resources | 1× | No | Required when resource choices shape architecture |
| 7. Key Activities | 1× | No | Required when activity choices shape architecture |
| 8. Key Partnerships | 1× | No | Required when make/buy/partner choices exist |
| 9. Cost Structure | 2× | Yes | Financial grounding — what it costs to operate the model |
| 10. Business Model Summary | 1× | No | Narrative coherence across the nine blocks |
| 11. Linkage to Business Architecture | 2× | Yes | Prevents the BMC from drifting away from the blueprint |
| 12. Requirements Addressed | 1× | No | Required when the BMC generates requirements |
| Appendix A3 — Decision Log | 2× | Yes | T3-A3 compliance |
| Appendix A4 — Stakeholder Concerns | 2× | Yes | T3-A4 compliance |
| Appendix A5 — Related ADRs | 1× | No | T3-ADR compliance |

### Business Architecture (`business-architecture.md`)

| Section | Weight | Required? | Rationale |
|---|---|---|---|
| 1. Business Context | 1× | No | Context setting |
| 2. Business Capabilities | 2× | Yes | Core BA content — the stable capability blueprint |
| 3. Value Streams | 2× | Yes | Core BA content — how capabilities deliver value |
| 4. Use Case Catalog | 1× | No | Required when use cases are part of the scope |
| 5. Business Services | 1× | No | Required when service catalogue is part of the scope |
| 6. Business Information / Data Objects | 1× | No | Required when information model is part of the scope |
| 7. Gap Analysis | 1× | No | Required when capability/value-stream gaps exist |
| 8. Requirements Addressed | 1× | No | Required when BA generates requirements |
| 9. Traceability Summary | 2× | Yes | Ensures the blueprint traces back to direction |
| 10. Diagrams | 1× | No | Required when visual models are produced |
| Appendix A3 — Decision Log | 2× | Yes | T3-A3 compliance |
| Appendix A4 — Stakeholder Concerns | 2× | Yes | T3-A4 compliance |
| Appendix A5 — Related ADRs | 1× | No | T3-ADR compliance |
