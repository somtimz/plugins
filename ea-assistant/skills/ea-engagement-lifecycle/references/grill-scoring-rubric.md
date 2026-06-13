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

1. **Definition-correctness (30%)** — content matches the EA definitions in `ea-concepts.md`: a Goal is qualitative (not a measure), an Objective is SMART, a Strategy names an approach (not a plan or an outcome), a Constraint is not a Principle, a Risk carries a *real* mitigation (funded, owned, scheduled, measurable). A clear misclassification caps this sub-dimension at 40.
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
