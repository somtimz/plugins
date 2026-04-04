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
  "lastModified": "YYYY-MM-DDTHH:MM:SSZ",
  "pluginVersion": "0.9.5",
  "lastMigratedVersion": "0.9.5",
  "direction": {
    "Business": {
      "goals": [
        { "id": "G-001", "statement": "", "priority": "High | Medium | Low" }
      ],
      "objectives": [
        { "id": "OBJ-001", "statement": "", "measure": "", "target": "", "deadline": "", "priority": "High | Medium | Low" }
      ],
      "strategies": [
        { "id": "STR-001", "statement": "", "supports": ["G-001"], "priority": "High | Medium | Low" }
      ]
    },
    "Data": { "goals": [], "objectives": [], "strategies": [] },
    "Application": { "goals": [], "objectives": [], "strategies": [] },
    "Technology": { "goals": [], "objectives": [], "strategies": [] }
  },
  "metrics": {
    "Business": [
      {
        "id": "MET-001",
        "name": "",
        "type": "outcome | performance | activity",
        "description": "",
        "measure": "",
        "baseline": "",
        "target": "",
        "deadline": "",
        "frequency": "Daily | Weekly | Monthly | Quarterly",
        "source": "",
        "supports": ["G-001"],
        "status": "Not Established | On Track | At Risk | Behind | Achieved"
      }
    ],
    "Data": [],
    "Application": [],
    "Technology": []
  },
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

**v0.4.0 fields** — `direction`:
- Domain-scoped object; keys match selected `architectureDomains`
- Each domain: `{ goals: [], objectives: [], strategies: [] }`
- **Goal** `{ id: G-NNN, statement, priority }` — WHERE you want to be (qualitative)
- **Objective** `{ id: OBJ-NNN, statement, measure, target, deadline, priority }` — HOW FAR and BY WHEN (measurable)
- **Strategy** `{ id: STR-NNN, statement, supports: [id,...], priority }` — HOW you'll get there
- IDs are unique across all domains; do not restart numbering per domain
- Items with empty `statement` are placeholders — MUST NOT be referenced in artifacts
- See `skills/ea-artifact-templates/references/ea-concepts.md` for canonical definitions

**v0.5.0 fields** — `metrics`:
- Domain-scoped metrics array, tracking progress of direction items via `supports`

| Metric type | Tracks | Example |
|---|---|---|
| `outcome` | Whether a **goal** is being approached | Customer satisfaction trending toward target |
| `performance` | Whether an **objective** is on track | Onboarding time: baseline 5d → target 1d |
| `activity` | Whether a **strategy** is being executed | % of new workloads containerised |

- Metric status: `Not Established` | `On Track` | `At Risk` | `Behind` | `Achieved`
- IDs: `MET-NNN` (sequential across all domains)
- Metrics with empty `name` or `measure` are placeholders — MUST NOT be displayed in artifacts
- Every objective should have at least one metric; a metric without a linked direction item is an orphan

**v0.9.5 fields**:
- `pluginVersion` — ea-assistant version that last opened this engagement (set by `/ea-open`); absent in legacy → treat as `"0.0.0"`
- `lastMigratedVersion` — version at which `/ea-migrate` last ran successfully; absent until first migration → treat as `"0.0.0"`
- `templateVersion` on artifacts — plugin version when the artifact was created or last migrated; absent in pre-v0.9.5 → treat as `"0.0.0"`

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
