---
name: ea-finance
description: Manage Cost Entries (FIN-NNN) — architecture-grade capex/opex/TCO/payback estimates. List, add, update, trace to work packages, ADRs and goals, and generate a Cost Model Register with a roadmap budget roll-up.
argument-hint: "[list|add|update|trace|generate] [FIN-NNN] [--subject WorkPackage|ADR|Option|Capability|Engagement] [--status Estimate|Budgeted|Committed|Actual] [--confidence High|Medium|Low]"
allowed-tools: [Read, Write, Bash]
---

You are executing the `/ea-finance` command. All mode mechanics (engagement resolution, ID assignment, list/add/update/trace/generate flows, common edge cases) follow `skills/ea-engagement-lifecycle/references/register-protocol.md` — read it, then apply the Register Spec below. For the **Cost Entry** concept and its distinctions from Metric / Business Case / Work Package field, read `skills/ea-artifact-templates/references/concept-families/implementation-concepts.md` (**Cost Entry**); do not restate the definition here.

A Cost Entry makes one subject legible in financial terms (capex, opex, TCO, payback). These are **architecture-grade estimates with explicit confidence**, not finance-grade budgets — see the concept note before adding. Cost Entries feed the Business Case (Phase A), the Architecture Roadmap budget roll-up (Phase E), and the Migration Plan costing (Phase F). The register is the management interface; the Architecture Roadmap is the primary display view.

## Register Spec

| Element | Value |
|---|---|
| Prefix / concept | `FIN-NNN` — Cost Entry |
| Storage | `engagement.json → finance[]` |
| Register file | `artifacts/cross-cutting/operations/cost-model-register.md` (artifactId `cost-model-register`; relatedArtifacts `["architecture-roadmap", "business-case"]`) |
| Display view | **none** — do not run the protocol's add/update Display View Sync (the roadmap relationship is a many-FIN→budget roll-up, not a one-row-per-item mirror). The Architecture Roadmap is refreshed at `generate` time only — see Roadmap Sync below |
| Groupings | `list` and `generate` group by Subject; summary header shows total Capex, total Opex (annual), total 3-Year TCO (per the engagement currency), plus counts by Status and Confidence, "Orphans (no linked WP/ADR/Goal)", and "Unquantified value (no annualBenefit and no benefitNarrative)" |
| Orphan rule | No `linkedWorkPackages` AND no `linkedADRs` AND no `linkedGoals` → `⚠️ Orphan` |

### Fields

| Field | Prompt | Valid values | Req |
|---|---|---|---|
| `label` | What is being costed? (e.g. "Core platform migration") | any string | ✓ |
| `subject` | What kind of thing is this costing? | WorkPackage / ADR / Option / Capability / Engagement | ✓ |
| `currency` | Currency (press Enter for engagement default) | ISO code; default from `financeCurrency` local-config (fallback `EUR`) | ✓ |
| `capex` | One-time build/transition cost (number, currency units; 0 if none) | number ≥ 0 | ✓ |
| `opexAnnual` | Recurring annual run cost once live (0 if none) | number ≥ 0 | ✓ |
| `horizonYears` | TCO horizon in years (press Enter for 3) | integer ≥ 1, default 3 | ✓ |
| `annualBenefit` | Quantified annual value — revenue, saving, or avoided cost (0 if value is qualitative only) | number ≥ 0 | opt |
| `benefitNarrative` | Qualitative value statement (required if annualBenefit is 0) | any string | opt |
| `confidence` | Estimate confidence | High / Medium / Low | ✓ |
| `confidenceBasis` | Why that confidence? (vendor quote / analogous project / rough order of magnitude) | any string | ✓ |
| `status` | Funding status | Estimate / Budgeted / Committed / Actual (default Estimate) | ✓ |
| `linkedWorkPackages` | Work packages this funds (list available WP-NNN from the roadmap) | comma-separated WP-NNN | opt |
| `linkedADRs` | Decisions this costs (list available ADR-NNN) | comma-separated ADR-NNN | opt |
| `linkedGoals` | Goals this serves (list available G-NNN) | comma-separated G-NNN | opt |
| `source` | Where the numbers came from | any string | opt |

**Derived fields (never prompted — always recomputed on `add` and `update`):**
- `tco` = `capex + opexAnnual × horizonYears`
- `paybackMonths` = `capex ÷ ((annualBenefit − opexAnnual) ÷ 12)`, rounded to a whole month, **only when `annualBenefit > opexAnnual`**; otherwise `null` (no payback — annual value does not exceed annual run cost). Display: `null` → `—`; a value `> horizonYears × 12` → `{n} months (beyond {horizonYears}-yr horizon)`; otherwise `{n} months`.

### Link fields

| Field | Target | Orphan semantics |
|---|---|---|
| `linkedWorkPackages` | Architecture Roadmap WP-NNN | unknown WP → broken-link flag |
| `linkedADRs` | ADR Register `ADR-NNN` | unknown ADR → broken-link flag |
| `linkedGoals` | `direction.goals[]` | unknown G → broken-link flag |
| (derived) benefit metrics | `metrics[]` where `type = benefit` and `linkedTo` contains this FIN-NNN | none → "no realisation tracking; use `/ea-finance` then add a benefit metric" |

### Trace chain

| Direction | Hop | Source |
|---|---|---|
| Upstream | Goals served | `direction.goals[]` referenced in `linkedGoals` |
| Lateral | Decisions costed | ADR Register entries referenced in `linkedADRs` |
| Downstream | Work Packages funded (show Wave, Status) | Architecture Roadmap WP rows referenced in `linkedWorkPackages` |
| Downstream | Benefit metrics (show Baseline, Target, Status) | `metrics[]` where `type = benefit` and `linkedTo` contains this FIN-NNN |

### Status transitions

| Transition | Extra prompt |
|---|---|
| `status: Committed` or `status: Actual` | "Committed/Actual figures are treated as authoritative, not estimates. Confirm the source of record (e.g. approved budget line, invoice): " — store in `source` |

## Register-Specific Checks

**Recompute derived fields (add and update, before the confirmation preview):** Always recompute `tco` and `paybackMonths` from the current `capex`, `opexAnnual`, `horizonYears`, and `annualBenefit`. Show both in the preview: `3-Year TCO: {currency} {tco}  ·  Payback: {payback display per the rule above}`. Never accept a hand-entered `tco` or `paybackMonths`.

**Value-quantification check (post-prompt, add; also flag in `list` with `⚠️ value?`):** If both `annualBenefit` is 0 and `benefitNarrative` is empty, warn:
```
⚠️  This Cost Entry has cost but no stated value (no annual benefit, no narrative).
A cost with no value cannot be prioritised or defended in a Business Case.
Add a value statement now? (y / n — proceed without value)
```

**Confidence-vs-status check (post-prompt, add and update):** If `status` is `Committed` or `Actual` but `confidence` is `Low`, warn: "⚠️ A Committed/Actual entry with Low confidence is contradictory — committed figures should be firm. Set confidence to High/Medium or revert status to Estimate? (y/n)".

**Currency consistency (add):** If the entry's `currency` differs from the engagement default and from other entries, note: "ℹ️ Mixed currencies in the register — totals in `list`/`generate` are shown per-currency, not summed across currencies."

## Roadmap Sync (`generate` only)

After writing the Cost Model Register, if `artifacts/phase-e/architecture-roadmap.md` exists, refresh its display view from the linked Cost Entries (do not edit the roadmap in any other direction):

1. **Per-WP cost fields** — for each WP-NNN referenced by one or more Cost Entries, set the WP field-table rows `Capex (one-time)`, `Opex (annual)`, `3-Year TCO`, `Cost Confidence`, and `Linked Cost Entry` from the sum of its linked entries (lowest confidence wins for the rating). Leave WPs with no linked entry unchanged.
2. **Roadmap Budget Summary** — recompute the wave rows and Total from the WP figures, grouping by each WP's `Phase / Wave`. Populate `Unestimated work packages` with any WP that has no linked Cost Entry.
3. Update the roadmap's `lastModified` frontmatter only. Do not touch `status`, `reviewStatus`, or `version`.
4. If the wave Total Capex for any single funding year exceeds the engagement's stated funding envelope (if recorded in local config), note it under `Funding window alignment`.

If no roadmap exists, skip silently and note in the confirmation: "ℹ️ No Architecture Roadmap yet — budget roll-up not synced."

## Messages

- **Empty state:** "No Cost Entries found. Capture them during Phase E/F roadmap costing or a `e:` economic-framing pause, then add with `/ea-finance add`. Each entry models the full cost picture of one work package, option, or capability."
- **Add success:** "FIN-NNN added — 3-Year TCO {currency} {tco}, payback {paybackMonths}mo|—. Link it to a work package with `/ea-finance update FIN-NNN linkedWorkPackages WP-NNN`, then `/ea-finance generate` to roll up the roadmap budget."
- **Orphan nudge:** "⚠️ Not linked to any WP, ADR, or goal — this cost has no traceable purpose. Run `/ea-finance update FIN-NNN linkedWorkPackages WP-NNN` (or linkedGoals / linkedADRs)."
