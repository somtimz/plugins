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
  "direction": {
    "vision": "",
    "mission": "",
    "drivers": [
      { "id": "DRV-001", "statement": "", "type": "External | Internal", "priority": "High | Medium | Low", "evidence": "", "linkedGoals": ["G-001"] }
    ],
    "goals": [
      { "id": "G-001", "statement": "", "priority": "High | Medium | Low", "drivers": ["DRV-001"], "rationale": "" }
    ],
    "objectives": [
      { "id": "OBJ-001", "statement": "", "measure": "", "target": "", "deadline": "", "priority": "High | Medium | Low", "linkedGoal": "G-001" }
    ],
    "strategies": [
      { "id": "STR-001", "statement": "", "supports": ["G-001"], "priority": "High | Medium | Low" }
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
      "type": "outcome | performance | activity",
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

## Field Version History

**v0.2.0 fields** — absent in legacy engagements; treat as `null` / defaults if missing:
- `engagementType` — classification of the engagement; defaults to `null`
- `architectureDomains` — selected domains; defaults to all four if absent
- `targetEndDate` — optional target completion date; defaults to `null`

**v0.4.0 fields** — `direction` (flat structure, current):
- Flat object at engagement level (not domain-scoped): `{ vision, mission, drivers[], goals[], objectives[], strategies[], issues[], problems[], opportunities[], gaps[] }`
- **Driver** `{ id: DRV-NNN, statement, type, priority, evidence?, linkedGoals[] }` — WHY the engagement is needed
- **Goal** `{ id: G-NNN, statement, priority, drivers[], rationale? }` — WHERE you want to be (qualitative)
- **Objective** `{ id: OBJ-NNN, statement, measure, target, deadline, priority, linkedGoal }` — HOW FAR and BY WHEN (measurable)
- **Strategy** `{ id: STR-NNN, statement, supports: [id,...], priority }` — HOW you'll get there
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

**v0.9.5 fields**:
- `pluginVersion` — ea-assistant version that last opened this engagement (set by `/ea-open`); absent in legacy → treat as `"0.0.0"`
- `lastMigratedVersion` — version at which `/ea-migrate` last ran successfully; absent until first migration → treat as `"0.0.0"`
- `templateVersion` on artifacts — plugin version when the artifact was created or last migrated; absent in pre-v0.9.5 → treat as `"0.0.0"`

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
  "reviewStatus": "Not Reviewed"
}
```

Artifact status: `Draft` | `In Review` | `Approved` | `Needs Revision`
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

## Decision Register Entry Schema

Multiple decision registers may exist (one per generation date):

```json
{
  "id": "decision-register-{YYYY-MM-DD}",
  "name": "Decision Register ({YYYY-MM-DD})",
  "phase": "All",
  "file": "artifacts/decision-register-{YYYY-MM-DD}.md",
  "reviewFile": "artifacts/decision-register-{YYYY-MM-DD}.review.md",
  "status": "Draft",
  "createdAt": "{ISO 8601}",
  "lastModified": "{ISO 8601}",
  "reviewStatus": "Not Reviewed"
}
```

`/ea-decisions status` uses the most recently generated decision register for its summary.
