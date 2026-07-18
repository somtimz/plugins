# engagement.json Schema Reference

## Full Schema

```json
{
  "name": "Acme Retail Transformation",
  "slug": "acme-retail-2026",
  "description": "",
  "sponsor": "",
  "organisation": "",
  "scope": "",
  "startDate": "YYYY-MM-DD",
  "targetEndDate": "YYYY-MM-DD or null",
  "status": "Active",
  "engagementType": "Greenfield | Brownfield | Assessment-only | Migration",
  "architectureDomains": ["Business", "Data", "Application", "Technology"],
  "currentPhase": "Prelim",
  "requirementsRepoPath": "",
  "constraintsRepoPath": "",
  "lastModified": "YYYY-MM-DDTHH:MM:SSZ",
  "pluginVersion": "0.9.5",
  "lastMigratedVersion": "0.9.5",
  "repoPath": null,
  "direction": {
    "vision": "",
    "mission": "",
    "drivers": [
      { "id": "DRV-001", "statement": "", "type": "External | Internal", "priority": "High | Medium | Low", "evidence": "", "linkedGoals": ["G-001"] }
    ],
    "goals": [
      { "id": "G-001", "statement": "", "priority": "High | Medium | Low", "stakeholder": "Senior Management | Business Unit Manager | Staff | Ultimate Client | null", "drivers": ["DRV-001"], "rationale": "" }
    ],
    "objectives": [
      { "id": "OBJ-001", "statement": "", "measure": "", "target": "", "deadline": "", "priority": "High | Medium | Low", "linkedGoal": "G-001" }
    ],
    "strategies": [
      { "id": "STR-001", "statement": "", "type": "Build | Buy | Partner | Consolidate | Modernise | Defend | Other", "supports": ["G-001"], "horizon": "Near | Mid | Long", "priority": "High | Medium | Low", "status": "Active | Completed | Superseded", "rationale": "" }
    ],
    "issues": [
      { "id": "ISS-001", "statement": "", "area": "", "threatensGoals": ["G-001"], "evidence": "", "raisedBy": "" }
    ],
    "problems": [
      { "id": "PRB-001", "statement": "", "symptom": "", "blocksObjectives": ["OBJ-001"], "evidence": "", "raisedBy": "" }
    ],
    "opportunities": [
      { "id": "OPP-001", "statement": "", "drivers": ["DRV-001"], "type": "Exploit | Enhance | Emerge", "priority": "High | Medium | Low", "linkedGoals": ["G-001"], "rationale": "" }
    ],
    "gaps": [
      { "id": "GAP-001", "statement": "", "domain": "Business | Data | Application | Technology | Capability | Process", "severity": "Critical | High | Medium | Low", "baseline": "", "target": "", "phase": "Prelim | A | B | C-Data | C-App | D | E | F | G | H | Requirements", "linkedWorkPackages": ["WP-001"], "linkedArtifact": "", "status": "Open | Mitigated | Closed | Accepted" }
    ]
  },
  "metrics": [
    {
      "id": "MET-001",
      "name": "",
      "type": "outcome | performance | activity | benefit",
      "description": "",
      "measure": "",
      "baseline": "",
      "baselineSource": "",
      "target": "",
      "deadline": "",
      "frequency": "Daily | Weekly | Monthly | Quarterly",
      "linkedTo": ["OBJ-001"],
      "status": "Not Established | On Track | At Risk | Behind | Achieved"
    }
  ],
  "finance": [
    {
      "id": "FIN-001",
      "label": "",
      "subject": "WorkPackage | ADR | Option | Capability | Engagement",
      "currency": "EUR",
      "capex": 0,
      "opexAnnual": 0,
      "horizonYears": 3,
      "tco": 0,
      "annualBenefit": 0,
      "benefitNarrative": "",
      "paybackMonths": null,
      "confidence": "High | Medium | Low",
      "confidenceBasis": "",
      "status": "Estimate | Budgeted | Committed | Actual",
      "linkedWorkPackages": ["WP-001"],
      "linkedADRs": [],
      "linkedGoals": [],
      "source": ""
    }
  ],
  "policies": [
    {
      "id": "POL-001",
      "title": "",
      "type": "Security | Procurement | Data Governance | Technology | Compliance | HR | Operational",
      "issuingAuthority": "",
      "effectiveDate": "YYYY-MM-DD",
      "reviewCycle": "YYYY-MM-DD",
      "scope": "Enterprise | Divisional | Geographic",
      "status": "Draft | Enacted | Under Review | Superseded | Retired",
      "supersededBy": "",
      "linkedConstraints": [],
      "linkedPrinciples": [],
      "sourceFile": "policies-register.md"
    }
  ],
  "rules": [
    {
      "id": "BR-001",
      "subject": "",
      "condition": "",
      "directive": "Must | Must Not | Should | Should Not",
      "outcome": "",
      "authority": "",
      "source": "Regulatory | Internal | Contractual | Market Practice | Policy-derived",
      "enforcement": "Manual review | Automated check | Workflow approval | Audit sample | System validation",
      "scope": "Enterprise | Program",
      "status": "Active | Draft | Under Review | Superseded | Retired",
      "supersededBy": "",
      "admPhase": "Prelim | A | B | C-Data | C-App | D | E | F | G | H | Requirements",
      "zachmanCell": "",
      "linkedServices": [],
      "linkedPolicies": [],
      "linkedConstraints": [],
      "linkedMotivation": [],
      "linkedProcesses": [],
      "linkedUseCases": [],
      "sourceFile": "business-rules-register.md"
    }
  ],
  "services": [
    {
      "id": "SVC-001",
      "name": "",
      "level": "Business | Application | Technology",
      "purpose": "",
      "consumer": "",
      "outcome": "",
      "interface": "",
      "owner": "",
      "sla": "",
      "deliveryChannel": "Digital | Branch | Phone | Partner | Field | Shared Service | Other",
      "operatingModelNote": "",
      "linkedRules": [],
      "linkedCapabilities": [],
      "linkedValueStreams": [],
      "linkedProcesses": [],
      "linkedABB": [],
      "linkedSBB": [],
      "linkedInterfaces": [],
      "sourceFile": "business-services-register.md"
    }
  ],
  "valueStreams": [
    {
      "id": "VS-001",
      "name": "",
      "description": "",
      "trigger": "",
      "endOutcome": "",
      "linkedCapabilities": [],
      "linkedGoals": [],
      "linkedProcesses": [],
      "status": "Draft | Active | Under Review | Deprecated | Retired",
      "sourceFile": "value-streams-register.md"
    }
  ],
  "businessProcesses": [
    {
      "id": "PROC-001",
      "name": "",
      "purpose": "",
      "valueStream": "VS-001 | null",
      "trigger": "",
      "inputs": "",
      "outputs": "",
      "actors": "",
      "linkedCapabilities": [],
      "linkedUseCases": [],
      "linkedRules": [],
      "linkedServices": [],
      "status": "Draft | Active | Under Review | Deprecated | Retired",
      "sourceFile": "business-processes-register.md"
    }
  ],
  "useCases": [
    {
      "id": "UC-001",
      "name": "",
      "primaryActor": "",
      "goal": "",
      "trigger": "",
      "preconditions": "",
      "mainScenario": "",
      "linkedCapabilities": [],
      "linkedProcesses": [],
      "linkedRequirements": [],
      "status": "Draft | Active | Under Review | Deprecated | Retired",
      "sourceFile": "use-cases-register.md"
    }
  ],
  "phases": {
    "Prelim":        { "status": "Not Started", "startedAt": null, "completedAt": null },
    "Requirements":  { "status": "Not Started", "startedAt": null, "completedAt": null },
    "A":             { "status": "Not Started", "startedAt": null, "completedAt": null },
    "B":             { "status": "Not Started", "startedAt": null, "completedAt": null },
    "C-Data":        { "status": "Not Started", "startedAt": null, "completedAt": null },
    "C-App":         { "status": "Not Started", "startedAt": null, "completedAt": null },
    "D":             { "status": "Not Started", "startedAt": null, "completedAt": null },
    "E":             { "status": "Not Started", "startedAt": null, "completedAt": null },
    "F":             { "status": "Not Started", "startedAt": null, "completedAt": null },
    "G":             { "status": "Not Started", "startedAt": null, "completedAt": null },
    "H":             { "status": "Not Started", "startedAt": null, "completedAt": null }
  },
  "artifacts": [],
  "optOuts": []
}
```

**Phase status enum:** `Not Started | In Progress | Complete | On Hold | Not Applicable`. `Not Applicable` is set by ADM tailoring at `/ea-new` (recommended phase set derived from `architectureLevel`) and carries an `optOutReason` field on the phase entry. Not-Applicable phases keep their `phases{}` entry but are excluded from picklists and `/ea-status` progress counts (already implemented there); their `artifacts/{phase-folder}/` is not created at seeding. `/ea-phase` offers re-inclusion (restores `Not Started`, clears `optOutReason`, creates the folder). Phase-level tailoring uses this status — not the `optOuts[]` array, which remains for question- and artifact-level opt-outs.

## Schema Versioning & Source of Truth

**`schemaVersion`** (integer, current: **1**) tracks the structure of `engagement.json` itself, independent of the plugin version (`pluginVersion` tracks which plugin release last touched the engagement; `lastMigratedVersion` tracks the last `/ea-migrate` alignment). Increment the schema version only when the JSON structure changes incompatibly (renamed/moved keys, changed types) — additive fields do not bump it. Engagements without the field are pre-versioning; `/ea-migrate` adds it.

**`migrations[]`** is the audit trail: `/ea-migrate` appends one entry per run — `{ date, fromPluginVersion, toPluginVersion, fromSchemaVersion, toSchemaVersion, gapsFound, gapsFixed, gapsSkipped }`. Never edit or prune entries manually.

**Source of truth:** `engagement.json` is the single source of truth for the strategic direction (`direction.{vision, mission, drivers, goals, objectives, strategies, issues, problems, opportunities, gaps}`), the top-level governance/measurement registers (`metrics[]`, `policies[]`, `finance[]` — siblings of `direction`, not nested in it), phase state, and the artifact registry. Generated register markdown files (`*-register.md`) are **rendered views** — regenerate them after any change; never edit them to change state (the exceptions are registers whose content lives only in markdown: Risk, Requirements, Constraints, Policies registers, which are file-mastered with `engagement.json` holding metadata). Snapshot files under `snapshots/` are point-in-time archives per the register snapshot convention.

**Operating Model artifact storage:** The Operating Model is an **authored Phase B artifact** (`artifacts/phase-b/operating-model.md`) tracked in `engagement.json → artifacts[]`. It has no dedicated top-level array: structured business processes live in `businessProcesses[]`, service delivery notes in `services[]`, and org design / decision rights / controls / sourcing / workforce content in the artifact body. This keeps the OM artifact free-form while reusing the existing registers for mastered items.

## Field Version History

**v0.2.0 fields** — absent in legacy engagements; treat as `null` / defaults if missing:
- `engagementType` — classification of the engagement; defaults to `null`
- `architectureDomains` — selected domains; defaults to all four if absent
- `targetEndDate` — optional target completion date; defaults to `null`

**v0.4.0 fields** — `direction` (flat structure, current):
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

**v0.5.0 fields** — `metrics` (flat array, current):
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

**v0.9.66 fields** — `finance` (flat array) and `benefit` metric type:

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

**v0.9.85 fields** — `rules` and `services` (flat arrays):

- `rules[]` — flat array at engagement level (sibling to `metrics[]`, `policies[]`, `finance[]`). Each entry is a **Business Rule** (`BR-NNN`) capturing a declarative governance statement. Managed via `/ea-rules`. See `skills/ea-artifact-templates/references/ea-concepts.md` for the canonical Business Rule definition.

| Field | Meaning |
|---|---|
| `id` | `BR-NNN` canonical ID |
| `subject` | What the rule governs |
| `condition` | When the rule applies |
| `directive` | `Must` / `Must Not` / `Should` / `Should Not` |
| `outcome` | Business result or action |
| `authority` | Owner or enacting body |
| `source` | `Regulatory` / `Internal` / `Contractual` / `Market Practice` / `Policy-derived` |
| `enforcement` | How compliance is verified |
| `scope` | `Enterprise` / `Program` |
| `status` | `Active` / `Draft` / `Under Review` / `Superseded` / `Retired` |
| `supersededBy` | `BR-NNN` that replaces this rule |
| `admPhase` | Where identified |
| `zachmanCell` | Classification |
| `linkedServices` | `SVC-NNN` operationalising the rule |
| `linkedPolicies` | `POL-NNN` authorising the rule |
| `linkedConstraints` | `CST-NNN` enforcing the rule |
| `linkedMotivation` | `DRV-NNN` / `G-NNN` / `OBJ-NNN` / `STR-NNN` traced |
| `linkedProcesses` | `PROC-NNN` governed by this rule (v0.9.86) |
| `linkedUseCases` | `UC-NNN` consuming this rule (v0.9.86) |
| `sourceFile` | Register file the rule renders into |

- `services[]` — flat array at engagement level. Each entry is a **Service** (`SVC-NNN`) at Business, Application, or Technology level. Managed via `/ea-services`. See `skills/ea-artifact-templates/references/ea-concepts.md` for the canonical Service definition.

| Field | Meaning |
|---|---|
| `id` | `SVC-NNN` canonical ID |
| `name` | Service name |
| `level` | `Business` / `Application` / `Technology` |
| `purpose` | Why the service exists |
| `consumer` | Who uses it |
| `outcome` | Value delivered |
| `interface` | Access channel (often `IFC-NNN`) |
| `owner` | Accountable role |
| `sla` | Service-level reference |
| `linkedRules` | `BR-NNN` enacted by Business services |
| `linkedCapabilities` | `CAP-NNN` realising the service |
| `linkedValueStreams` | `VS-NNN` this service supports (v0.9.86) |
| `linkedProcesses` | `PROC-NNN` this service operationalises (v0.9.86) |
| `linkedABB` | Logical components |
| `linkedSBB` | Concrete products |
| `linkedInterfaces` | `IFC-NNN` access points |
| `sourceFile` | Register file the service renders into |

- `valueStreams[]` — flat array at engagement level. Each entry is a **Value Stream** (`VS-NNN`). Managed via `/ea-valuestreams`.

| Field | Meaning |
|---|---|
| `id` | `VS-NNN` canonical ID |
| `name` | Value stream name |
| `description` | Short description |
| `trigger` | What initiates the stream |
| `endOutcome` | What the stakeholder receives |
| `linkedCapabilities` | `CAP-NNN` exercised by this stream |
| `linkedGoals` | `G-NNN` / `STR-NNN` this stream serves |
| `linkedProcesses` | `PROC-NNN` that compose this stream |
| `status` | `Draft` / `Active` / `Under Review` / `Deprecated` / `Retired` |
| `sourceFile` | `value-streams-register.md` |

- `businessProcesses[]` — flat array at engagement level. Each entry is a **Business Process** (`PROC-NNN`). Managed via `/ea-processes`.

| Field | Meaning |
|---|---|
| `id` | `PROC-NNN` canonical ID |
| `name` | Process name |
| `purpose` | Why the process exists |
| `valueStream` | Parent `VS-NNN` |
| `trigger` | What starts it |
| `inputs` | Key inputs |
| `outputs` | Key outputs |
| `actors` | Roles / actors |
| `linkedCapabilities` | `CAP-NNN` exercised |
| `linkedUseCases` | `UC-NNN` that consume this process |
| `linkedRules` | `BR-NNN` applied |
| `linkedServices` | `SVC-NNN` that operationalise it |
| `status` | `Draft` / `Active` / `Under Review` / `Deprecated` / `Retired` |
| `sourceFile` | `business-processes-register.md` |

- `useCases[]` — flat array at engagement level. Each entry is a **Use Case** (`UC-NNN`). Managed via `/ea-usecases`.

| Field | Meaning |
|---|---|
| `id` | `UC-NNN` canonical ID |
| `name` | Use case name |
| `primaryActor` | Actor role |
| `goal` | Actor goal |
| `trigger` | What starts it |
| `preconditions` | Preconditions |
| `mainScenario` | One-sentence main success path |
| `linkedCapabilities` | `CAP-NNN` used |
| `linkedProcesses` | `PROC-NNN` consumed |
| `linkedRequirements` | `REQ-NNN` generated |
| `status` | `Draft` / `Active` / `Under Review` / `Deprecated` / `Retired` |
| `sourceFile` | `use-cases-register.md` |

- Entries with empty `subject` (rules), empty `name` (services), or empty `name` (value streams/processes/use cases) are placeholders — MUST NOT be displayed in artifacts.
- IDs are unique across the engagement; do not restart numbering per type.

**v0.9.86 fields** — Business Architecture layer + enrichment fields:

- `valueStreams[]`, `businessProcesses[]`, `useCases[]` — three new top-level arrays for first-class Business Architecture objects. Managed via `/ea-valuestreams`, `/ea-processes`, `/ea-usecases`. Process ID prefix is `PROC-NNN` to avoid collision with `BP-NNN` (Business Principle) and `PRB-NNN` (Problem).
- `direction.goals[].stakeholder` — optional stakeholder classification (`Senior Management` / `Business Unit Manager` / `Staff` / `Ultimate Client`). Used by `/ea-goals` grouping and the Goals Register. See `skills/ea-engagement-lifecycle/references/stakeholder-goal-classification.md`.
- `rules[].linkedProcesses` / `rules[].linkedUseCases` — optional `PROC-NNN` / `UC-NNN` links for Business Rules, enabling process-level rule traceability.
- `services[].linkedValueStreams` / `services[].linkedProcesses` — optional `VS-NNN` / `PROC-NNN` links for Business Services, enabling value-stream and process service traceability.
- `requirements-index.json` fields — `sourceType` (`Driver` / `Goal` / `Objective` / `Use Case` / `Business Scenario` / `Process` / `null`), `acceptanceCriteria[]`, and `upstreamLinks[]` (VS-NNN / PROC-NNN / UC-NNN / etc.) for richer requirement provenance. See `skills/ea-requirements-management/SKILL.md`.

**v0.9.5 fields**:
- `pluginVersion` — ea-assistant version that last opened this engagement (set by `/ea-open`); absent in legacy → treat as `"0.0.0"`
- `lastMigratedVersion` — version at which `/ea-migrate` last ran successfully; absent until first migration → treat as `"0.0.0"`
- `templateVersion` on artifacts — plugin version when the artifact was created or last migrated; absent in pre-v0.9.5 → treat as `"0.0.0"`

**v0.9.54 fields**:
- `repoPath` — relative path to the shared `Architecture-Repository/` directory. Always `"../../Architecture-Repository"` when set (from `EA-Projects/<slug>/`). `null` if no Architecture Repository is linked. Set via `/ea-repo link` or auto-set by `/ea-new` when an EA-Workspace is detected. Absent in legacy engagements → treat as `null`.

**v0.9.31 fields** — absent in legacy engagements; treat as `null` / defaults if missing:
- `architectureLevel` — Architecture landscape level classification; allowed values: `Strategic`, `Segment`, `Capability`, `Solution`; defaults to `null` in legacy engagements. When `null` or absent, treat as `Segment` for artifact depth and governance forum purposes — this is non-blocking and the plugin continues to operate normally. Prompt the user to set it at the next `/ea-config metadata` interaction.

## Artifact Entry Schema

```json
{
  "id": "architecture-vision",
  "name": "Architecture Vision",
  "phase": "A",
  "file": "artifacts/phase-a/architecture-vision.md",
  "reviewFile": "artifacts/phase-a/architecture-vision.review.md",
  "status": "Draft",
  "createdAt": "YYYY-MM-DDTHH:MM:SSZ",
  "lastModified": "YYYY-MM-DDTHH:MM:SSZ",
  "reviewStatus": "Not Reviewed",
  "scores": { "completeness": 78, "quality": 66, "scoredAt": "YYYY-MM-DD" }
}
```

Artifact status: `Draft` | `In Review` | `Approved` | `Needs Revision`

**`scores`** (v0.9.72; optional, absent until first scored): the latest overall artifact scores from `/ea-score` or `/ea-grill` — `completeness` and `quality` are `0–100` integers, `scoredAt` is the date last scored. The per-section breakdown lives in the artifact's `📊 Scorecard` block (the source of truth); this is the roll-up cache for `/ea-score --status` and `/ea-status`. Command-generated artifacts (registers/matrices/derived) are not scored and have no `scores` field.
Review status: `Not Reviewed` | `In Review` | `Approved` | `Needs Revision`

## optOuts[] Entry Schema

```json
{
  "type": "question | artifact",
  "artifactId": "architecture-vision",
  "questionRef": "executive_summary",
  "reason": "Not yet available — revisit in Phase A review",
  "timestamp": "ISO 8601"
}
```

- `questionRef` — placeholder key (question opt-outs only)
- Opt-outs accumulate across sessions; never auto-removed
- Removal permitted only via `/ea-config optouts`

## Cross-cutting Artifact Paths

Cross-cutting artifacts are organized into three sub-folders under `artifacts/cross-cutting/`:

| Sub-folder | Artifacts stored |
|---|---|
| `artifacts/cross-cutting/governance/` | ADR Register, Decision Register, Architecture Principles (cross-cutting), Constraints Register, Policies Register |
| `artifacts/cross-cutting/operations/` | Risk Register, Change Register, Stakeholder Concerns, Cost Model Register |
| `artifacts/cross-cutting/context/` | Zachman Diagram, Role Catalogue |

The `cross-cutting-index.md` file at `artifacts/cross-cutting/cross-cutting-index.md` is a navigation hub linking to all cross-cutting artifacts. It is created on first use and updated whenever a new cross-cutting artifact is registered.

## Decision Register Entry Schema

A single decision register entry exists at the stable path (superseded versions are archived to `snapshots/` per the register snapshot convention):

```json
{
  "id": "decision-register",
  "name": "Decision Register",
  "phase": "All",
  "file": "artifacts/cross-cutting/governance/decision-register.md",
  "reviewFile": "artifacts/cross-cutting/governance/decision-register.review.md",
  "status": "Draft",
  "createdAt": "{ISO 8601}",
  "lastModified": "{ISO 8601}",
  "reviewStatus": "Not Reviewed"
}
```

`/ea-decisions status` uses the current `decision-register.md` for its summary.
