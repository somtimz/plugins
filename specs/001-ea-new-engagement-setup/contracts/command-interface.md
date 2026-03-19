# Command Interface Contract: /ea-new

## Invocation

```
/ea-new [engagement-name]
```

- `engagement-name` (optional): Display name of the engagement. If
  provided, the name prompt is skipped.

## Prompt Sequence

When invoked without arguments, prompts are presented sequentially:

| Order | Field | Required | Default | Format |
|-------|-------|----------|---------|--------|
| 1 | Name | Yes | — | Free text |
| 2 | Description | Yes | — | Free text |
| 3 | Sponsor / Owner | Yes | — | Free text |
| 4 | Organisation | Yes | — | Free text |
| 5 | Scope | Yes | — | Free text |
| 6 | Engagement Type | Yes | — | Select: Greenfield, Brownfield, Assessment-only, Migration |
| 7 | Architecture Domains | Yes | All four | Multi-select: Business, Data, Application, Technology |
| 8 | Start Date | Yes | Today | ISO 8601 date (YYYY-MM-DD) |
| 9 | Target End Date | No | None | ISO 8601 date (YYYY-MM-DD) |
| 10 | Status | Yes | Active | Select: Active, On Hold, Planning |

When invoked with an argument, prompt 1 (Name) is skipped and the
argument value is used.

## Confirmation Summary

After all prompts, a summary is displayed:

```markdown
## New Engagement Summary

| Field | Value |
|-------|-------|
| Name | Acme Retail Transformation 2026 |
| Slug | acme-retail-transformation-2026 |
| Description | ... |
| Sponsor | ... |
| Organisation | ... |
| Scope | ... |
| Engagement Type | Greenfield |
| Architecture Domains | Business, Data, Application, Technology |
| Start Date | 2026-03-19 |
| Target End Date | 2026-12-31 |
| Status | Active |

**Actions**: Confirm / Edit [field name] / Cancel
```

## Output on Success

```markdown
## Engagement Created

**Name**: Acme Retail Transformation 2026
**Slug**: acme-retail-transformation-2026
**Location**: EA-projects/acme-retail-transformation-2026/

### Scaffolded Artifacts
- artifacts/architecture-principles.md (Draft)
- artifacts/stakeholder-map.md (Draft)

**Next**: Begin Preliminary phase (`/ea-phase Prelim`) or return to menu?
```

## Output on Duplicate

```markdown
An engagement with slug "acme-retail-transformation-2026" already exists.

**Options**:
1. Open the existing engagement
2. Choose a different name
```

## Output on Cancel

```
Engagement creation cancelled. No files were created.
```

## Files Created on Success

```
EA-projects/{slug}/
├── engagement.json
├── requirements/
├── artifacts/
│   ├── architecture-principles.md
│   └── stakeholder-map.md
├── diagrams/
├── uploads/
└── interviews/
```
