# Data Model: EA New Engagement Setup

## Entity: Engagement (engagement.json)

The enhanced `engagement.json` schema adds three new fields to the
existing schema. All new fields are optional for backward compatibility.

### Updated Schema

```json
{
  "name": "string (required, display name)",
  "slug": "string (required, URL-safe identifier, max 60 chars)",
  "description": "string (required)",
  "sponsor": "string (required)",
  "organisation": "string (required)",
  "scope": "string (required)",
  "startDate": "string (required, ISO 8601 date: YYYY-MM-DD)",
  "targetEndDate": "string | null (optional, ISO 8601 date: YYYY-MM-DD)",
  "status": "string (enum: Active | On Hold | Planning, default: Active)",
  "engagementType": "string | null (enum: Greenfield | Brownfield | Assessment-only | Migration)",
  "architectureDomains": ["string (enum: Business | Data | Application | Technology)"],
  "currentPhase": "string (default: Prelim)",
  "requirementsRepoPath": "string (default: empty)",
  "lastModified": "string (ISO 8601 datetime: YYYY-MM-DDTHH:MM:SSZ)",
  "phases": {
    "<phase-key>": {
      "status": "string (enum: Not Started | In Progress | Complete | On Hold | Not Applicable)",
      "startedAt": "string | null (ISO 8601 datetime)",
      "completedAt": "string | null (ISO 8601 datetime)"
    }
  },
  "artifacts": [
    {
      "id": "string (kebab-case artifact identifier)",
      "name": "string (display name)",
      "phase": "string (phase key)",
      "file": "string (relative path in engagement directory)",
      "reviewFile": "string (relative path to review file)",
      "status": "string (enum: Draft | In Review | Approved | Needs Revision)",
      "createdAt": "string (ISO 8601 datetime)",
      "lastModified": "string (ISO 8601 datetime)",
      "reviewStatus": "string (enum: Not Reviewed | In Review | Approved | Needs Revision)"
    }
  ]
}
```

### New Fields (added by this feature)

| Field | Type | Required | Default | Description |
|-------|------|----------|---------|-------------|
| `engagementType` | string \| null | No | null | One of: Greenfield, Brownfield, Assessment-only, Migration. Null for legacy engagements. |
| `architectureDomains` | string[] | No | ["Business", "Data", "Application", "Technology"] | Selected architecture domains. At least one required at creation. |
| `targetEndDate` | string \| null | No | null | Optional target completion date in ISO 8601 format. |

### Phase Status Change

The `status` enum for individual phases gains a new value:
**Not Applicable** — used when a phase is excluded based on engagement
type and domain selection (e.g., C-Data is Not Applicable if the Data
domain was deselected).

### State Transitions

**Engagement creation flow**:
```
No engagement → fields collected → confirmation displayed →
  user confirms → directories created → engagement.json written →
  artifacts scaffolded → artifacts array populated → done
```

**Confirmation flow** (new):
```
fields collected → summary displayed →
  user confirms → proceed to creation
  user edits → re-prompt single field → summary displayed (loop)
  user cancels → abandon (no files written)
```

## Entity: Scaffolding Map (scaffolding-map.md)

A new reference file defining the mapping from engagement type and
domain selection to scaffolded Preliminary phase artifacts.

### Structure

```yaml
preliminary_artifacts:
  - id: architecture-principles
    template: templates/architecture-principles.md
    applicable_types: [Greenfield, Brownfield, Assessment-only, Migration]
    applicable_domains: all
  - id: stakeholder-map
    template: templates/stakeholder-map.md
    applicable_types: [Greenfield, Brownfield, Assessment-only, Migration]
    applicable_domains: all
```

The scaffolding map is a reference document, not executable code. It
guides the command's behavior when generating starter artifacts.

### Artifact Scaffolding Rules

1. For each entry in `preliminary_artifacts`:
   - If the engagement type matches `applicable_types`
   - AND the domain requirement is met (`all` or specific domain selected)
   - THEN copy the template to `artifacts/{id}.md`
2. Replace template variables (`{{engagement_name}}`, `{{organisation}}`,
   `{{sponsor}}`, `{{YYYY-MM-DD}}`) with values from the engagement
   metadata.
3. Mark all content sections with `⚠️ Not answered` (content not yet
   collected from user).
4. Add the artifact to the `artifacts` array in `engagement.json` with
   status "Draft" and reviewStatus "Not Reviewed".

## Entity: Domain-to-Phase Mapping

| Domain | ADM Phase(s) |
|--------|-------------|
| Business | B |
| Data | C-Data |
| Application | C-App |
| Technology | D |

Phases always applicable regardless of domain:
Prelim, Requirements, A

Phases applicable by engagement type (see research.md R1):
E, F, G, H — applicable for all types except Assessment-only
