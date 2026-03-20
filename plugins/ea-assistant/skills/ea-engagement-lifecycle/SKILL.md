---
name: EA Engagement Lifecycle
description: This skill should be used when the user asks to "start an EA engagement", "manage an EA project", "set up a new architecture engagement", "what phase are we in", "advance the ADM", "continue the engagement", "resume an EA project", or when working within any TOGAF ADM phase. Provides end-to-end lifecycle guidance for Enterprise Architecture engagements using TOGAF 10 as the backbone.
version: 0.3.0
---

# EA Engagement Lifecycle

This skill guides the management of Enterprise Architecture engagements from initiation through closeout using TOGAF 10 as the process backbone, with Zachman as the classification lens and ArchiMate as the notation language.

## Engagement Structure

Every EA engagement is stored as a folder under `EA-projects/`:

```
EA-projects/
├── {engagement-slug}/           # Active engagements
│   ├── engagement.json          # metadata and state
│   ├── requirements/            # local architecture requirements
│   ├── artifacts/               # generated artifacts + review files
│   ├── diagrams/                # .mmd, .dot, .drawio files
│   ├── uploads/                 # source documents and diagrams
│   └── interviews/              # dated, versioned interview notes
└── .archive/                    # Archived engagements (hidden dotdir)
    └── {engagement-slug}/       # Retains full structure
        └── engagement.json
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

### Engagement Status Values

Engagement-level status: `Active` | `On Hold` | `Planning` | `Completed`

- **Active**: Engagement is currently being worked on.
- **On Hold**: Engagement is paused; may resume later.
- **Planning**: Engagement is in pre-kickoff preparation.
- **Completed**: Engagement has finished all planned work. All phases are either Complete or Not Applicable.

Note: Engagement-level "Completed" is distinct from phase-level "Complete". An engagement is "Completed" when the overall project is done. Individual phases are marked "Complete" when their deliverables are finished.

### Phase Status Values

Phase-level status: `Not Started` | `In Progress` | `Complete` | `On Hold` | `Not Applicable`

`Not Applicable` is used when a phase is excluded based on engagement type and domain selection. For example, if the Data domain is deselected, C-Data is set to "Not Applicable". Assessment-only engagements set phases E-H to "Not Applicable" because they focus on current-state review without implementation planning.

### Phase Status State Transitions

All transitions below are valid. Timestamp management is automatic:

| From | To | Timestamp Effect |
|------|----|-----------------|
| Not Started | In Progress | Sets `startedAt` to now |
| In Progress | Complete | Sets `completedAt` to now |
| In Progress | On Hold | No timestamp change |
| On Hold | In Progress | No timestamp change (preserves original `startedAt`) |
| Complete | In Progress | Clears `completedAt` (preserves `startedAt`) |
| Any | Not Started | Resets both `startedAt` and `completedAt` to null |
| Not Applicable | Any | Requires explicit user confirmation before override |

When a phase transitions to "In Progress" for the first time, `startedAt` is set. If the phase was previously started (has a `startedAt`), it is preserved on re-entry from On Hold.

## Engagement Types

Each engagement is classified by type, which determines ADM phase emphasis and default applicability. See `references/engagement-patterns.md` for detailed tailoring guidance.

| Type | Description | ADM Focus |
|------|-------------|-----------|
| Greenfield | Building a new capability, business unit, or system from scratch. No baseline architecture. | Full ADM; emphasis on Phase A (Vision) and Phases B-D (target state) |
| Brownfield | Transforming existing systems, processes, or data while keeping the business running. | Full ADM; emphasis on baseline documentation in B-D and transition planning in E-F |
| Assessment-only | Current-state review of existing architecture without planning implementation changes. | Prelim, Requirements, A, and domain phases only; E-H are Not Applicable |
| Migration | Re-platforming or re-hosting workloads (e.g., cloud migration, data centre move). | Full ADM; emphasis on Phase D (Technology) and E-F (migration planning) |

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

1. Scan `EA-projects/*/engagement.json` files (excludes `.archive/` dotdir)
2. Display picklist showing: name, engagement type, domain count, currentPhase, status, lastModified
3. If argument provided, match against names or slugs directly
4. Load selected engagement context into conversation
5. Display full engagement summary: metadata table, phase-by-phase breakdown, artifact list
6. Offer next actions menu (see Editing Workflows below)
7. Store the active engagement slug in the conversation context for subsequent commands

### Editing Workflows

All editing flows are accessed through `/ea-open` next actions menu after opening an engagement. There is no separate edit command.

**Next actions menu** (offered after opening an engagement):

1. Continue current phase (`/ea-phase`)
2. View artifacts (`/ea-artifact`)
3. Start an interview (`/ea-interview`)
4. View detailed status
5. Edit engagement metadata
6. Edit phase status
7. Edit artifact status
8. Archive engagement
9. Delete engagement

**Edit engagement metadata**: Prompts for which field to edit, shows current value, accepts new value, validates, writes to `engagement.json`, updates `lastModified`. Editable fields: name (display only — slug unchanged), description, sponsor, organisation, scope, status, start date, target end date. Non-editable after creation: `engagementType`, `architectureDomains` (changing these would invalidate phase applicability).

**Edit phase status**: Shows all 11 phases with current status, user selects phase and new status. Timestamp rules applied automatically per the Phase Status State Transitions table above. When a phase is marked Complete, suggest advancing `currentPhase` to the next applicable phase.

**Edit artifact status**: Shows all artifacts with current status and review status. User selects an artifact and updates status (Draft/In Review/Approved/Needs Revision) or review status (Not Reviewed/In Review/Approved/Needs Revision).

### Archive, Restore, and Delete

**Archive**: Moves the engagement directory from `EA-projects/{slug}/` to `EA-projects/.archive/{slug}/`. Creates `.archive/` if it doesn't exist. Archived engagements retain their `engagement.json` and all data intact. They do not appear in the default `/ea-status` dashboard or `/ea-open` picklist.

**Restore**: Moves an archived engagement back from `EA-projects/.archive/{slug}/` to `EA-projects/{slug}/`. Blocked if an active engagement with the same slug already exists.

**Delete**: Permanently removes the engagement directory. Requires the user to type the engagement slug to confirm. This action is irreversible.

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
