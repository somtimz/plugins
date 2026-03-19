---
name: EA Engagement Lifecycle
description: This skill should be used when the user asks to "start an EA engagement", "manage an EA project", "set up a new architecture engagement", "what phase are we in", "advance the ADM", "continue the engagement", "resume an EA project", or when working within any TOGAF ADM phase. Provides end-to-end lifecycle guidance for Enterprise Architecture engagements using TOGAF 10 as the backbone.
version: 0.1.0
---

# EA Engagement Lifecycle

This skill guides the management of Enterprise Architecture engagements from initiation through closeout using TOGAF 10 as the process backbone, with Zachman as the classification lens and ArchiMate as the notation language.

## Engagement Structure

Every EA engagement is stored as a folder under `EA-projects/`:

```
EA-projects/
└── {engagement-slug}/
    ├── engagement.json          # metadata and state
    ├── requirements/            # local architecture requirements
    ├── artifacts/               # generated artifacts + review files
    ├── diagrams/                # .mmd, .dot, .drawio files
    ├── uploads/                 # source documents and diagrams
    └── interviews/              # dated, versioned interview notes
```

### engagement.json schema

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
  "phases": {
    "Prelim": { "status": "Not Started", "startedAt": null, "completedAt": null },
    "Requirements": { "status": "Not Started", "startedAt": null, "completedAt": null },
    "A": { "status": "Not Started", "startedAt": null, "completedAt": null },
    "B": { "status": "Not Started", "startedAt": null, "completedAt": null },
    "C-Data": { "status": "Not Started", "startedAt": null, "completedAt": null },
    "C-App": { "status": "Not Started", "startedAt": null, "completedAt": null },
    "D": { "status": "Not Started", "startedAt": null, "completedAt": null },
    "E": { "status": "Not Started", "startedAt": null, "completedAt": null },
    "F": { "status": "Not Started", "startedAt": null, "completedAt": null },
    "G": { "status": "Not Started", "startedAt": null, "completedAt": null },
    "H": { "status": "Not Started", "startedAt": null, "completedAt": null }
  },
  "artifacts": []
}
```

**New fields** (added in v0.2.0):
- `engagementType`: Classification of the engagement. Defaults to `null` for legacy engagements without this field.
- `architectureDomains`: Array of selected domains. Defaults to all four if absent.
- `targetEndDate`: Optional target completion date. Defaults to `null` if absent.

Existing engagements created before v0.2.0 will not have these fields. All commands MUST handle missing fields gracefully by applying the defaults above.

Phase status values: `Not Started` | `In Progress` | `Complete` | `On Hold` | `Not Applicable`

`Not Applicable` is used when a phase is excluded based on engagement type and domain selection. For example, if the Data domain is deselected, C-Data is set to "Not Applicable". Assessment-only engagements set phases E–H to "Not Applicable" because they focus on current-state review without implementation planning.

## Engagement Types

Each engagement is classified by type, which determines ADM phase emphasis and default applicability. See `references/engagement-patterns.md` for detailed tailoring guidance.

| Type | Description | ADM Focus |
|------|-------------|-----------|
| Greenfield | Building a new capability, business unit, or system from scratch. No baseline architecture. | Full ADM; emphasis on Phase A (Vision) and Phases B–D (target state) |
| Brownfield | Transforming existing systems, processes, or data while keeping the business running. | Full ADM; emphasis on baseline documentation in B–D and transition planning in E–F |
| Assessment-only | Current-state review of existing architecture without planning implementation changes. | Prelim, Requirements, A, and domain phases only; E–H are Not Applicable |
| Migration | Re-platforming or re-hosting workloads (e.g., cloud migration, data centre move). | Full ADM; emphasis on Phase D (Technology) and E–F (migration planning) |

## Architecture Domains

Users select which architecture domains are in scope when creating an engagement. At least one domain MUST be selected. Default: all four.

| Domain | ADM Phase | Description |
|--------|-----------|-------------|
| Business | B | Business processes, capabilities, organisation, functions |
| Data | C-Data | Data entities, data components, data management |
| Application | C-App | Application components, interfaces, application services |
| Technology | D | Technology components, platforms, infrastructure |

Deselecting a domain sets its corresponding ADM phase to "Not Applicable" and excludes domain-specific artifacts from scaffolding.

## ADM Phase Map

| Phase | Name | Key Deliverables |
|---|---|---|
| Prelim | Preliminary | Architecture Principles, Org Model, Tailoring |
| Requirements | Architecture Requirements | Requirements Register, Traceability Matrix |
| A | Architecture Vision | Statement of Architecture Work, Architecture Vision |
| B | Business Architecture | Business Architecture document |
| C-Data | Data Architecture | Data Architecture document |
| C-App | Application Architecture | Application Architecture document |
| D | Technology Architecture | Technology Architecture document |
| E | Opportunities & Solutions | Architecture Roadmap, Implementation Plan |
| F | Migration Planning | Migration Plan, Architecture Roadmap (updated) |
| G | Implementation Governance | Architecture Contracts, Compliance Assessments |
| H | Architecture Change Management | Change Requests, Updated Architecture |

Phases can be started, edited, or resumed in any order. Navigation is non-linear.

## Lifecycle Workflow

### Starting a New Engagement

1. Collect required fields: Name, Description, Sponsor, Organisation, Scope, Engagement Type, Architecture Domains, Start Date, Target End Date (optional), Status
2. Create slug: lowercase, hyphens, no spaces, max 60 chars (e.g. `acme-retail-2026`)
3. Display confirmation summary; allow user to edit fields or cancel
4. Create folder structure under `EA-projects/{slug}/`
5. Write `engagement.json` with all fields, set phase applicability based on engagement type and domain selection (see `references/scaffolding-map.md`)
6. Scaffold Preliminary phase artifacts from templates (see `references/scaffolding-map.md`)
7. Set `currentPhase` to `Prelim`
8. Confirm engagement created, list scaffolded artifacts, and offer to begin the Preliminary phase

### Opening an Existing Engagement

1. Scan all `EA-projects/*/engagement.json` files
2. Display picklist showing: name, currentPhase, status, lastModified
3. Load selected engagement context into conversation
4. Summarise engagement state: current phase, in-progress artifacts, last activity

### Advancing or Resuming a Phase

1. Update `currentPhase` in `engagement.json`
2. Update phase `status` to `In Progress` and set `startedAt` if first entry
3. Load the relevant artifact templates for the phase
4. Reference plugin components for phase-specific guidance:
   - Phase facilitation: use the `ea-facilitator` agent
   - Artifact creation and population: use the `ea-artifact-templates` skill
   - Document export (Word/Markdown): use the `ea-merge` command
   - Interviews: use the `ea-interviewer` agent via the `ea-interview` command

### Completing a Phase

1. Verify all required artifacts for the phase exist in `artifacts/`
2. Set phase `status` to `Complete` and `completedAt` timestamp
3. Update `lastModified` in `engagement.json`
4. Offer to advance to the next recommended phase

## Artifact Tracking

Track artifacts in `engagement.json` under the `artifacts` array:

```json
{
  "artifacts": [
    {
      "id": "architecture-vision",
      "name": "Architecture Vision",
      "phase": "A",
      "file": "artifacts/architecture-vision.md",
      "reviewFile": "artifacts/architecture-vision.review.md",
      "status": "Draft",
      "createdAt": "YYYY-MM-DDTHH:MM:SSZ",
      "lastModified": "YYYY-MM-DDTHH:MM:SSZ",
      "reviewStatus": "Not Reviewed"
    }
  ]
}
```

Artifact status: `Draft` | `In Review` | `Approved` | `Needs Revision`
Review status: `Not Reviewed` | `In Review` | `Approved` | `Needs Revision`

## Content Policy

Artifacts are populated from three sources only:
1. User interview answers
2. Uploaded documents (processed by `ea-document-ingestion` skill)
3. Explicit user input

Any AI-generated or suggested content MUST be marked:
```
> 🤖 **AI Draft — Review Required**
> [suggested content here]
```

Unanswered fields: `⚠️ Not answered`
Not applicable fields: `➖ Not applicable`
Default answers accepted by user: value written + `✓ Default accepted`

## Settings

Read plugin settings from `.claude/ea-assistant.local.md`:

```yaml
requirementsRepoPath: /path/to/shared/requirements-folder
```

Store the path in `engagement.json` under `requirementsRepoPath` at engagement creation.

## Additional Resources

- **`references/adm-phase-guide.md`** — Detailed inputs, outputs, and steps for each ADM phase
- **`references/engagement-patterns.md`** — Common engagement patterns and anti-patterns
- **`references/scaffolding-map.md`** — Engagement type/domain to artifact scaffolding mapping
