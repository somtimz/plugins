---
name: EA Requirements Management
description: This skill should be used when the user asks to "manage architecture requirements", "add a requirement", "sync requirements from the repo", "view requirements", "trace a requirement to an artifact", "update the requirements register", or "start the architecture requirements phase". Handles the full requirements lifecycle from capture through traceability and sync with a shared requirements repository.
version: 0.1.0
---

# EA Requirements Management

Architecture Requirements Management is a continuous phase in the TOGAF ADM. This skill handles capturing, classifying, tracing, and syncing requirements across an EA engagement.

## Requirements Storage

Local requirements are stored in `EA-projects/{slug}/requirements/`:

```
requirements/
├── requirements.md           # human-readable requirements register
└── requirements-index.json   # machine-readable index for traceability
```

The `requirementsRepoPath` in `engagement.json` points to a shared folder (currently a file system path; SharePoint integration planned).

## Requirements Register Format

`requirements.md` uses a structured template:

```markdown
# Architecture Requirements Register
<!-- GUIDANCE: This register captures all architecture requirements for the engagement.
     Each requirement should be traceable to a driver, goal, or business need.
     Guidance text is marked with HTML comments and is NOT part of the deliverable. -->

**Engagement:** {{engagement_name}}
**Last Synced:** {{last_sync_date}}
**Version:** {{version}}

---

## REQ-001: {{requirement_title}}

| Field | Value |
|---|---|
| ID | REQ-001 |
| Statement | {{requirement_statement}} |
| Category | Functional / Non-Functional / Constraint / Principle |
| Priority | High / Medium / Low |
| Source | {{source_document_or_stakeholder}} |
| Status | Draft / Approved / Deferred / Rejected |
| ADM Phase | {{phase_where_relevant}} |
| Zachman Cell | {{row}} / {{column}} |
| Linked Artifacts | {{artifact_ids}} |

> ⚠️ Not answered  ← use this if field is incomplete
```

## requirements-index.json Schema

```json
{
  "lastSynced": "YYYY-MM-DDTHH:MM:SSZ",
  "repoPath": "/path/to/shared/requirements",
  "requirements": [
    {
      "id": "REQ-001",
      "title": "",
      "status": "Draft",
      "priority": "High",
      "phase": "A",
      "linkedArtifacts": [],
      "sourceFile": "requirements.md"
    }
  ]
}
```

## Syncing from the Requirements Repository

The requirements repository may contain mixed formats: Markdown, Word (.docx), Excel (.xlsx/.csv).

### Sync Workflow

1. Read `requirementsRepoPath` from `engagement.json`
2. Scan the directory for supported files: `.md`, `.docx`, `.xlsx`, `.csv`
3. For each file, extract requirements using the `ea-document-ingestion` skill
4. Present extracted requirements to the user for review and confirmation
5. Merge approved requirements into `requirements.md` and `requirements-index.json`
6. Update `lastSynced` timestamp
7. Flag conflicts where a repo requirement differs from a locally edited version

### Conflict Resolution

When a repo requirement conflicts with a local edit:
- Show both versions side by side
- Ask the user which to keep, or whether to merge
- Never silently overwrite local changes

## Requirements Traceability

Link requirements to artifacts to ensure every requirement is addressed:

1. Each requirement in `requirements-index.json` has a `linkedArtifacts` array
2. When creating an artifact, check for unlinked requirements relevant to that phase
3. When a requirement is marked `Approved`, verify it is linked to at least one artifact
4. Use the `ea-consistency-checker` agent to audit traceability gaps

### Traceability Matrix

Generate a traceability matrix on demand:

```
| Req ID | Requirement | Phase | Architecture Vision | Biz Arch | App Arch |
|--------|-------------|-------|---------------------|----------|----------|
| REQ-001 | ... | A | ✅ | ❌ | ❌ |
| REQ-002 | ... | B | ❌ | ✅ | ❌ |
```

## Requirements Phase Workflow

The Architecture Requirements phase runs in two modes:

**Initial capture (before Phase A):**
1. Sync from requirements repo
2. Conduct requirements interview using `ea-interviewer` agent
3. Classify each requirement (functional, non-functional, constraint, principle)
4. Assign Zachman cell classification
5. Set initial priority and status

**Ongoing updates (any phase):**
1. Add new requirements as they emerge from phase activities
2. Update status of existing requirements
3. Re-sync from repo if updated externally
4. Trigger consistency check when requirements change

## Content Policy

- Requirements must be sourced from stakeholder input, uploaded documents, or explicit user entry
- AI-suggested requirements must be marked: `🤖 AI Draft — Review Required`
- Never auto-approve requirements — all require user confirmation before status is set to `Approved`

## Additional Resources

- **`references/requirement-categories.md`** — Taxonomy of requirement types with TOGAF alignment
- **`references/sync-formats.md`** — Detailed parsing rules for Word, Excel, and CSV requirement formats
