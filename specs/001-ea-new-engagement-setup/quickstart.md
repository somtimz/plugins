# Quickstart: EA New Engagement Setup

## Prerequisites

- Claude Code with plugin support installed
- `ea-assistant` plugin installed (`/plugin install ea-assistant`)

## Create Your First Engagement

### Option 1: Guided (recommended for first use)

```
/ea-new
```

Follow the prompts:

1. **Name**: "Acme Retail Transformation 2026"
2. **Description**: "Enterprise architecture for Acme's retail
   digital transformation programme"
3. **Sponsor**: "Jane Smith, CTO"
4. **Organisation**: "Acme Corp"
5. **Scope**: "All retail business units and supporting IT systems"
6. **Engagement Type**: Greenfield
7. **Architecture Domains**: Business, Data, Application, Technology
   (accept default: all four)
8. **Start Date**: (press Enter to accept today's date)
9. **Target End Date**: "2026-12-31"
10. **Status**: Active (press Enter to accept default)

Review the confirmation summary. Edit any field if needed, then confirm.

### Option 2: Quick start with name

```
/ea-new Acme Retail Transformation 2026
```

The name is pre-filled. Complete prompts 2-10 as above.

## What Gets Created

After confirmation, you'll find:

```
EA-projects/acme-retail-transformation-2026/
├── engagement.json           # All your metadata
├── requirements/             # Architecture requirements (empty)
├── artifacts/
│   ├── architecture-principles.md  # Starter template
│   └── stakeholder-map.md         # Starter template
├── diagrams/                 # Diagrams (empty)
├── uploads/                  # Source documents (empty)
└── interviews/               # Interview notes (empty)
```

## Next Steps

1. **Begin Preliminary phase**: `/ea-phase Prelim`
2. **Check status**: `/ea-status`
3. **Start an interview**: `/ea-interview start`
4. **Create more artifacts**: `/ea-artifact create`

## Verify It Worked

Run `/ea-status` — you should see your new engagement listed as Active
with the Preliminary phase ready to start.
