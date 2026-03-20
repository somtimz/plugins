# Data Model: EA Project Management

**Feature**: 002-ea-project-management
**Date**: 2026-03-20

## Entities

### Engagement (engagement.json)

No schema changes to the `engagement.json` structure — the schema was already extended in feature 001. This feature reads, displays, and modifies the existing fields.

**Existing fields used by this feature**:

| Field | Type | Editable | Validation |
|-------|------|----------|------------|
| `name` | string | Yes (display only, slug unchanged) | Non-empty |
| `slug` | string | No | Read-only |
| `description` | string | Yes | Free text |
| `sponsor` | string | Yes | Free text |
| `organisation` | string | Yes | Free text |
| `scope` | string | Yes | Free text |
| `startDate` | string (ISO 8601) | Yes | Valid date format |
| `targetEndDate` | string/null | Yes | Valid date format or null |
| `status` | string | Yes | One of: Active, On Hold, Planning, Completed |
| `engagementType` | string/null | No | Set at creation only |
| `architectureDomains` | string[] | No | Set at creation only |
| `currentPhase` | string | System-managed | Valid phase key |
| `requirementsRepoPath` | string | No | Set at creation only |
| `lastModified` | string (ISO 8601) | System-managed | Auto-updated on any change |
| `phases` | object | Yes (status only) | See Phase entity |
| `artifacts` | array | Yes (status fields only) | See Artifact entity |

**Note**: `engagementType` and `architectureDomains` are NOT editable after creation because changing them would require recalculating phase applicability and potentially invalidating existing artifacts. The user should create a new engagement if the type/domain scope changes fundamentally.

### Phase (sub-entity of engagement.json → phases)

| Field | Type | Editable | Validation |
|-------|------|----------|------------|
| `status` | string | Yes | One of: Not Started, In Progress, Complete, On Hold. Override of "Not Applicable" requires confirmation. |
| `startedAt` | string/null | System-managed | Set to now on first transition to "In Progress" |
| `completedAt` | string/null | System-managed | Set to now on transition to "Complete" |

**State transitions**:
- Not Started → In Progress (sets `startedAt`)
- In Progress → Complete (sets `completedAt`)
- In Progress → On Hold
- On Hold → In Progress
- Complete → In Progress (clears `completedAt`, preserves `startedAt`)
- Not Applicable → any (requires confirmation, see FR-014)
- Any → Not Started (resets `startedAt` and `completedAt` to null)

### Artifact (sub-entity of engagement.json → artifacts[])

| Field | Type | Editable | Validation |
|-------|------|----------|------------|
| `id` | string | No | Read-only |
| `name` | string | No | Read-only |
| `phase` | string | No | Read-only |
| `file` | string | No | Read-only |
| `reviewFile` | string | No | Read-only |
| `status` | string | Yes | One of: Draft, In Review, Approved, Needs Revision |
| `reviewStatus` | string | Yes | One of: Not Reviewed, In Review, Approved, Needs Revision |
| `createdAt` | string | No | Read-only |
| `lastModified` | string | System-managed | Auto-updated on status change |

## Archive Directory Structure

```
EA-projects/
├── engagement-a/           # Active engagement
│   └── engagement.json
├── engagement-b/           # Active engagement
│   └── engagement.json
└── .archive/               # Hidden archive directory
    ├── old-engagement-c/   # Archived engagement (retains full structure)
    │   └── engagement.json
    └── old-engagement-d/
        └── engagement.json
```

The `.archive/` directory is created on first archive operation. Its contents are only scanned when the user requests to view archived engagements.

## Backward Compatibility Defaults

For legacy engagements (pre-v0.2.0) missing fields:

| Missing Field | Display Default | Internal Default |
|---------------|----------------|------------------|
| `engagementType` | "—" | `null` |
| `architectureDomains` | All four domains | `["Business", "Data", "Application", "Technology"]` |
| `targetEndDate` | "—" | `null` |
