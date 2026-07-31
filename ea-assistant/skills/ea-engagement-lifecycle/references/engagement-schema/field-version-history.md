# engagement.json Field Version History

Per-version record of `engagement.json` fields introduced in ea-assistant. Routine callers of `engagement-schema.md` do not need this; it is split out so the main reference stays at ~100 lines.

---

## v0.2.0 fields

Absent in legacy engagements; treat as `null` / defaults if missing:
- `engagementType` — classification of the engagement; defaults to `null`
- `architectureDomains` — selected domains; defaults to all four if absent
- `targetEndDate` — optional target completion date; defaults to `null`

## v0.4.0 fields

`direction` (flat structure, current):
- Flat object at engagement level (not domain-scoped): `{ vision, mission, drivers[], goals[], objectives[], strategies[], issues[], problems[], opportunities[], gaps[] }`
- **Driver** `{ id: DRV-NNN, statement, type, priority, evidence?, linkedGoals[] }` — WHY the engagement is needed
- **Goal** `{ id: G-NNN, statement, priority, stakeholder?, drivers[], rationale? }` — WHERE you want to be (qualitative). `stakeholder` is v0.9.86 (Senior Management / Business Unit Manager / Staff / Ultimate Client).
- **Objective** `{ id: OBJ-NNN, statement, measure, target, deadline, priority, linkedGoal }` — HOW FAR and BY WHEN (measurable)
- **Strategy** `{ id: STR-NNN, statement, type, supports: [id,...], horizon, priority, status, rationale? }` — HOW you'll get there. `type` ∈ Build/Buy/Partner/Consolidate/Modernise/Defend/Other; `horizon` ∈ Near/Mid/Long; `status` ∈ Active/Completed/Superseded. Managed via `/ea-strategies`. `type`/`horizon`/`status`/`rationale` are v0.9.67 fields — absent in legacy engagements; default `type: Other`, `horizon: Mid`, `status: Active`, `rationale: ""`. Executing work packages are **derived** from the Architecture Roadmap WP `Executes Strategies` field (not stored on the strategy), mirroring how goals/objectives derive their WPs.
- **Issue** `{ id: ISS-NNN, statement, area, threatensGoals[], evidence?, raisedBy? }` — strategic threats to goals
- **Problem** `{ id: PRB-NNN, statement, symptom, blocksObjectives[], evidence?, raisedBy? }` — tactical blockers of objectives
- **Opportunity** `{ id: OPP-NNN, statement, drivers[], type, priority, linkedGoals[], rationale? }` — actionable possibilities
- **Gap** `{ id: GAP-NNN (or GAP-M-NNN for migration gaps in Phase F/G), statement, domain, severity, baseline, target, phase, linkedWorkPackages[], linkedArtifact?, status }` — difference between as-is and to-be state in a given domain
- Gap status: `Open | Mitigated | Closed | Accepted`
- IDs are unique across the entire engagement; do not restart numbering per type
- Fields marked `?` are optional — absent in legacy engagements; default to `""` or `[]` if missing
- Items with empty `statement` are placeholders — MUST NOT be referenced in artifacts
- See `skills/ea-artifact-templates/references/ea-concepts.md` for canonical definitions

## v0.5.0 fields

`metrics` (flat array, current):
- Flat array at engagement level (not domain-scoped); tracking progress against direction items

| Metric type | Tracks | Example |
|---|---|---|
| `outcome` | Whether a **goal** is being approached | Customer satisfaction trending toward target |
| `performance` | Whether an **objective** is on track | Onboarding time: baseline 5d → target 1d |
| `activity` | Whether a **strategy** is being executed | % of new workloads containerised |

- Metric status: `Not Established` | `On Track` | `At Risk` | `Behind` | `Achieved`
- IDs: `MET-NNN` (sequential)
- `baselineSource` — optional; where the baseline measurement comes from
- `linkedTo` — array of G-NNN or OBJ-NNN IDs this metric tracks
- Metrics with empty `name` or `measure` are placeholders — MUST NOT be displayed in artifacts
- Every objective should have at least one metric; a metric without a `linkedTo` entry is an orphan

## v0.9.66 fields

`finance` (flat array) and `benefit` metric type:

- `finance[]` — flat array at engagement level (sibling to `metrics[]`), absent in legacy engagements → treat as `[]`. Each entry is a **Cost Entry** (`FIN-NNN`) capturing the full architecture-grade cost picture of one subject (a work package, an ADR option, a capability, or the whole engagement). Managed via `/ea-finance`.

| Field | Meaning |
|---|---|
| `label` | Short name of what is being costed |
| `subject` | `WorkPackage` / `ADR` / `Option` / `Capability` / `Engagement` |
| `currency` | ISO code; defaults to the engagement's `financeCurrency` local-config value (fallback `EUR`) |
| `capex` | One-time build/transition cost (numeric, currency units) |
| `opexAnnual` | Recurring annual run cost once live |
| `horizonYears` | TCO horizon (default 3) |
| `tco` | **Derived** = `capex + opexAnnual × horizonYears` — never hand-entered |
| `annualBenefit` | Quantified annual value (0 if value is qualitative only) |
| `benefitNarrative` | Qualitative value statement when not fully quantified |
| `paybackMonths` | **Derived** = `capex / ((annualBenefit − opexAnnual) / 12)` when `annualBenefit > opexAnnual`, else `null` (no payback within horizon) |
| `confidence` | `High` / `Medium` / `Low` |
| `confidenceBasis` | Why that confidence (vendor quote, analogous project, rough order of magnitude) |
| `status` | `Estimate` / `Budgeted` / `Committed` / `Actual` |
| `linkedWorkPackages` / `linkedADRs` / `linkedGoals` | Cross-references; an entry with no links is an orphan |
| `source` | Where the numbers came from |

- Entries with an empty `label` are placeholders — MUST NOT be displayed in artifacts.
- `tco` and `paybackMonths` are always recomputed on `add`/`update`; never trust hand-edited values.
- A `benefit`-type metric (below) tracks realisation of a Cost Entry's projected `annualBenefit`.

- `metrics[].type` gains a fourth value `benefit` — tracks realisation of projected financial value (revenue, cost saving, or avoided cost) against a Cost Entry. `linkedTo` for a `benefit` metric may reference a `FIN-NNN` Cost Entry (in addition to `G-NNN`/`OBJ-NNN`). Used in Phase G to answer the implementation-governance question *"did we deliver the expected benefit?"*. Absent in legacy engagements — the three original types remain valid.

## v0.9.85 fields

`rules`, `services`, `valueStreams`, `businessProcesses`, `useCases` (flat arrays):
- `rules[]` — **Business Rules** (`BR-NNN`). Managed via `/ea-rules`. See `skills/ea-artifact-templates/references/ea-concepts.md` for the canonical definition.
- `services[]` — **Services** (`SVC-NNN`). Managed via `/ea-services`. See `skills/ea-artifact-templates/references/ea-concepts.md` for the canonical definition.
- `valueStreams[]` — **Value Streams** (`VS-NNN`). Managed via `/ea-valuestreams`.
- `businessProcesses[]` — **Business Processes** (`PROC-NNN`). Managed via `/ea-processes`.
- `useCases[]` — **Use Cases** (`UC-NNN`). Managed via `/ea-usecases`.

For field-level details, see the canonical JSON schema: [`engagement-schema.json`](engagement-schema.json).

## v0.9.86 fields

Business Architecture layer + enrichment fields:
- `valueStreams[]`, `businessProcesses[]`, `useCases[]` — three new top-level arrays for first-class Business Architecture objects. Managed via `/ea-valuestreams`, `/ea-processes`, `/ea-usecases`. Process ID prefix is `PROC-NNN` to avoid collision with `BP-NNN` (Business Principle) and `PRB-NNN` (Problem).
- `direction.goals[].stakeholder` — optional stakeholder classification (`Senior Management` / `Business Unit Manager` / `Staff` / `Ultimate Client`). Used by `/ea-goals` grouping and the Goals Register. See `skills/ea-engagement-lifecycle/references/stakeholder-goal-classification.md`.
- `rules[].linkedProcesses` / `rules[].linkedUseCases` — optional `PROC-NNN` / `UC-NNN` links for Business Rules, enabling process-level rule traceability.
- `services[].linkedValueStreams` / `services[].linkedProcesses` — optional `VS-NNN` / `PROC-NNN` links for Business Services, enabling value-stream and process service traceability.
- `requirements-index.json` fields — `sourceType` (`Driver` / `Goal` / `Objective` / `Use Case` / `Business Scenario` / `Process` / `null`), `acceptanceCriteria[]`, and `upstreamLinks[]` (VS-NNN / PROC-NNN / UC-NNN / etc.) for richer requirement provenance. See `skills/ea-requirements-management/SKILL.md`.

## v0.9.5 fields

- `pluginVersion` — ea-assistant version that last opened this engagement (set by `/ea-open`); absent in legacy → treat as `"0.0.0"`
- `lastMigratedVersion` — version at which `/ea-migrate` last ran successfully; absent until first migration → treat as `"0.0.0"`
- `templateVersion` on artifacts — plugin version when the artifact was created or last migrated; absent in pre-v0.9.5 → treat as `"0.0.0"`

## v0.9.54 fields

- `repoPath` — relative path to the shared `Architecture-Repository/` directory. Always `"../../Architecture-Repository"` when set (from `EA-Projects/<slug>/`). `null` if no Architecture Repository is linked. Set via `/ea-repo link` or auto-set by `/ea-new` when an EA-Workspace is detected. Absent in legacy engagements → treat as `null`.

## v0.9.31 fields

Absent in legacy engagements; treat as `null` / defaults if missing:
- `architectureLevel` — Architecture landscape level classification; allowed values: `Strategic`, `Segment`, `Capability`, `Solution`; defaults to `null` in legacy engagements. When `null` or absent, treat as `Segment` for artifact depth and governance forum purposes — this is non-blocking and the plugin continues to operate normally. Prompt the user to set it at the next `/ea-config metadata` interaction.
