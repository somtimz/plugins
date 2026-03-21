---
name: EA Engagement Lifecycle
description: This skill should be used when the user asks to "start an EA engagement", "manage an EA project", "set up a new architecture engagement", "what phase are we in", "advance the ADM", "continue the engagement", "resume an EA project", or when working within any TOGAF ADM phase. Provides end-to-end lifecycle guidance for Enterprise Architecture engagements using TOGAF 10 as the backbone.
version: 0.4.0
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
  "direction": {
    "Business": {
      "goals": [
        { "id": "BG-001", "statement": "", "priority": "High | Medium | Low" }
      ],
      "objectives": [
        { "id": "BO-001", "statement": "", "measure": "", "target": "", "deadline": "", "priority": "High | Medium | Low" }
      ],
      "strategies": [
        { "id": "BS-001", "statement": "", "supports": ["BG-001"], "priority": "High | Medium | Low" }
      ]
    },
    "Data": { "goals": [], "objectives": [], "strategies": [] },
    "Application": { "goals": [], "objectives": [], "strategies": [] },
    "Technology": { "goals": [], "objectives": [], "strategies": [] }
  },
  "metrics": {
    "Business": [
      {
        "id": "BM-001",
        "name": "",
        "type": "outcome | performance | activity",
        "description": "",
        "measure": "",
        "baseline": "",
        "target": "",
        "deadline": "",
        "frequency": "Daily | Weekly | Monthly | Quarterly",
        "source": "",
        "supports": ["BG-001"],
        "status": "Not Established | On Track | At Risk | Behind | Achieved"
      }
    ],
    "Data": [],
    "Application": [],
    "Technology": []
  },
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

**New fields** (added in v0.4.0):
- `direction`: Domain-scoped direction object. Keys match selected `architectureDomains`. Each domain has three sub-arrays — `goals`, `objectives`, `strategies` — with the following schemas:
  - **Goal** `{ id, statement, priority }` — high-level desired outcome (WHERE). IDs: `BG-`, `DG-`, `AG-`, `TG-`
  - **Objective** `{ id, statement, measure, target, deadline, priority }` — specific measurable target (HOW FAR, BY WHEN). IDs: `BO-`, `DO-`, `AO-`, `TO-`
  - **Strategy** `{ id, statement, supports: [id,...], priority }` — course of action (HOW). IDs: `BS-`, `DS-`, `AS-`, `TS-`
  - `supports` links a strategy to the goal or objective IDs it serves.
  - Items with an empty `statement` are placeholders and MUST NOT be referenced in artifacts.
  - Only domains in `architectureDomains` are populated — unused domains are omitted.

**Direction vs. Goals vs. Objectives vs. Strategies — definitions commands MUST use:**

| Term | Answers | Characteristics | Example |
|------|---------|-----------------|---------|
| **Direction** | *Why are we doing this?* | Superset of all three below; the complete performance expectation and constraint set | "Transform our data capability to support real-time decision-making" |
| **Goal** | *Where do we want to be?* | Qualitative, long-term, not directly measurable | "Become the most trusted financial services provider in the region" |
| **Objective** | *How far, by when?* | Specific, measurable, time-bound; testable | "Reduce customer onboarding from 5 days to 1 day by Q4 2026" |
| **Strategy** | *How will we get there?* | Course of action; choice of approach; not an outcome | "Adopt API-first integration to enable real-time data access" |

When capturing direction from a user, ALWAYS classify what they say before writing it. If a user says something that could be any of the three, ask a clarifying question rather than guessing. Common confusions:
- A goal stated with a number in it is usually an objective (e.g. "achieve 99.9% availability" → objective, not goal).
- A strategy stated as an outcome is usually a goal or objective (e.g. "move to the cloud" is a strategy; "have 80% of workloads on cloud by 2027" is an objective).
- "We want to improve data quality" is a goal; "reduce duplicate customer records by 90% by June 2026" is the corresponding objective.

Existing engagements created before v0.4.0 will not have the `direction` field. All commands MUST handle a missing `direction` field gracefully by treating each domain as `{ goals: [], objectives: [], strategies: [] }`.

**New fields** (added in v0.5.0):
- `metrics`: Domain-scoped metrics array. Each metric tracks the performance of one or more direction items (goals, objectives, or strategies) via its `supports` array of direction IDs. Metric `type` determines what it tracks:

| Metric type | Tracks | Linked to | Example |
|-------------|--------|-----------|---------|
| `outcome` | Whether a **goal** is being approached | `BG-`, `DG-`, `AG-`, `TG-` | Customer satisfaction score trending toward target |
| `performance` | Whether an **objective** is on track | `BO-`, `DO-`, `AO-`, `TO-` | Onboarding time: baseline 5 days → target 1 day |
| `activity` | Whether a **strategy** is being executed | `BS-`, `DS-`, `AS-`, `TS-` | % of new workloads containerised |

Metric status values: `Not Established` | `On Track` | `At Risk` | `Behind` | `Achieved`

ID patterns: `BM-` (Business), `DM-` (Data), `AM-` (Application), `TM-` (Technology).

Metrics with an empty `name` or `measure` are placeholders and MUST NOT be displayed in artifacts.

**Metrics vs. Objectives — avoid confusion:**
- An **objective** defines the commitment: *what* will be achieved and *by when*.
- A **metric** defines the instrument: *how* progress will be measured, *how often*, and *from what source*.
- Every objective should have at least one metric. A metric without a linked direction item is an orphan — flag it for the user to link or remove.

Existing engagements before v0.5.0 will not have `metrics`. Handle gracefully as empty arrays per domain.

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
3. **Capture direction per selected domain.** For each domain in `architectureDomains`, work through goals, objectives, and strategies in order. Before capturing, briefly explain the distinction:

   > "For each architecture domain I'll capture three types of direction:
   > - **Goals** — where you want to be (qualitative, long-term)
   > - **Objectives** — specific measurable targets with a deadline
   > - **Strategies** — the approaches you'll take to get there"

   For each domain:
   - Ask: "What are the **goals** for the **{Domain}** architecture?" Capture each; assign IDs (`BG-001`, `DG-001`, etc.)
   - Ask: "What **objectives** do you have — specific, measurable targets with a deadline?" Capture statement, measure, target value, deadline; assign IDs (`BO-001`, `DO-001`, etc.)
   - Ask: "What **strategies** will you use — the approaches or courses of action?" For each, ask which goal(s) or objective(s) it supports; assign IDs (`BS-001`, `DS-001`, etc.)
   - If the user gives something that could be any of the three, classify it and confirm: "That sounds like a [goal/objective/strategy] — I'll record it as one. Does that sound right?"
   - Direction may be skipped at creation time — user can add it later via Edit engagement metadata
   - After capturing direction, ask: "Do you want to define metrics now to track these goals, objectives, and strategies?" If yes, for each direction item prompt: metric name, what will be measured (measure), baseline value, target value, frequency, and data source. Classify metric type automatically from what it supports (outcome for goals, performance for objectives, activity for strategies). Metrics may also be added later.

4. Display confirmation summary of all fields including direction and metrics (grouped by domain); allow user to edit or cancel
5. Create folder structure under `EA-projects/{slug}/`
6. Write `engagement.json` with all fields including `direction` and `metrics`, set phase applicability based on engagement type and domain selection (see `references/scaffolding-map.md`)
7. Scaffold Preliminary phase artifacts from templates (see `references/scaffolding-map.md`)
8. Set `currentPhase` to `Prelim`
9. Confirm engagement created, list scaffolded artifacts and captured direction summary, and offer to begin the Preliminary phase

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

**Edit engagement metadata**: Prompts for which field to edit, shows current value, accepts new value, validates, writes to `engagement.json`, updates `lastModified`. Editable fields: name (display only — slug unchanged), description, sponsor, organisation, scope, status, start date, target end date, direction. Non-editable after creation: `engagementType`, `architectureDomains` (changing these would invalidate phase applicability).

**Edit metrics**: Accessible via Edit engagement metadata → Metrics. Shows all metrics grouped by domain with status indicators:

```
Business Metrics
  BM-001  Customer Onboarding Time     [Performance → BO-001]  On Track   5d → 1d by Q4 2026
  BM-002  Customer Satisfaction Score  [Outcome → BG-001]      At Risk    72 → 85 by Q2 2026
  BM-003  API-first adoption rate      [Activity → BS-001]     On Track   0% → 100% by Q3 2026
```

User may: add a new metric (select the direction item(s) it supports — type is inferred automatically), edit an existing metric (any field including status), or remove a metric. When adding, always confirm the `supports` link — a metric without a linked direction item is an orphan and should not be saved. After saving, offer to update the status field for metrics where current data is available.

**Edit direction**: Accessible via Edit engagement metadata → Direction. Shows all current direction items grouped by domain and type (Goals / Objectives / Strategies). Displays:

```
Business Direction
  Goals:      BG-001  Become the most trusted provider in the region        [High]
  Objectives: BO-001  Reduce onboarding from 5 days to 1 day by Q4 2026    [High]
  Strategies: BS-001  Adopt API-first integration                           [High]  → supports BG-001
```

User may: add a new item (selecting type first), edit an existing item, or remove an item. IDs are never reused after deletion. When adding, always confirm the type with the user using the definitions:
- **Goal** = where you want to be (qualitative, no number required)
- **Objective** = how far and by when (must have a measure, a target value, and a deadline)
- **Strategy** = how you'll get there (a course of action, not an outcome)

After saving, offer to propagate updated direction to the relevant domain artifacts (Architecture Vision for cross-domain direction; Business/Data/Application/Technology Architecture artifacts for domain-specific direction).

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
   - Document export (Word/Markdown): use the `ea-publish` command
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
- **`references/phase-inputs-outputs.md`** — Detailed input/output tables per ADM phase with quality gates
- **`references/adm-tailoring.md`** — Tailoring the ADM for agile, programme, capability-based, and security contexts
