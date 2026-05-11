---
name: ea-constraints-management
description: This skill should be used when the user asks to "manage architecture constraints", "add a constraint", "view constraints", "trace a constraint to an artifact", "update the constraints register", or "assess constraint impact". Handles the full constraints lifecycle from capture through traceability and sync with a shared constraints repository.
version: 0.1.0
---

# EA Constraints Management

Architecture Constraints Management captures, classifies, traces, and enforces non-negotiable restrictions on the solution space. Constraints are distinct from requirements (which define outcomes) and risks (which are uncertain).

## Constraints Storage

Local constraints are stored in `EA-projects/{slug}/constraints/`:

```
constraints/
├── constraints.md           # human-readable constraints register
└── constraints-index.json   # machine-readable index for traceability
```

The `constraintsRepoPath` in `engagement.json` points to a shared folder (currently a file system path; SharePoint integration planned).

## Constraints Register Format

`constraints.md` uses a structured template:

```markdown
# Architecture Constraints Register

**Engagement:** {{engagement_name}}
**Last Synced:** {{last_sync_date}}
**Version:** {{version}}

---

## 🔒CST-001: {{constraint_title}}   ← Enterprise example

| Field | Value |
|---|---|
| **ID** | CST-001 |
| **Type** | Technology / Regulatory / Budget / Timeline / Organisational / Interoperability |
| **Statement** | {{constraint_statement}} |
| **Source** | {{source_document_or_policy}} |
| **Owner** | {{owner_name_and_role}} |
| **Scope** | Enterprise 🔒 |
| **Priority** | High / Medium / Low |
| **Status** | Active / Waived / Proposed |
| **Waiver Justification** | {{required_if_status_is_Waived — leave blank otherwise}} |
| **ADM Phase** | {{phase_where_identified}} |
| **Zachman Cell** | {{row}} / {{column}} |
| **Linked Artifacts** | {{artifact_ids}} |
| **Impact Assessment** | {{affected_capabilities_or_work_packages}} |

---

## CST-00N: {{constraint_title}}   ← Program example

| Field | Value |
|---|---|
| **ID** | CST-00N |
| **Type** | Technology / Regulatory / Budget / Timeline / Organisational / Interoperability |
| **Statement** | {{constraint_statement}} |
| **Source** | {{source_document_or_policy}} |
| **Owner** | {{owner_name_and_role}} |
| **Scope** | Program |
| **Priority** | High / Medium / Low |
| **Status** | Active / Waived / Proposed |
| **Waiver Justification** | {{required_if_status_is_Waived — leave blank otherwise}} |
| **ADM Phase** | {{phase_where_identified}} |
| **Zachman Cell** | {{row}} / {{column}} |
| **Linked Artifacts** | {{artifact_ids}} |
| **Impact Assessment** | {{affected_capabilities_or_work_packages}} |
```

## JSON Schema

`constraints-index.json`:

```json
{
  "lastSynced": "YYYY-MM-DDTHH:MM:SSZ",
  "repoPath": "",
  "constraints": [
    {
      "id": "CST-001",
      "title": "",
      "statement": "",
      "type": "Technology | Regulatory | Budget | Timeline | Organisational | Interoperability",
      "scope": "Enterprise | Program",
      "priority": "High | Medium | Low",
      "phase": "Prelim | A | B | C | D | E | F | G | H",
      "source": "",
      "owner": "",
      "status": "Active | Waived | Proposed",
      "linkedArtifacts": [],
      "waiverJustification": "",
      "impactAssessment": "",
      "sourceFile": "constraints.md"
    }
  ]
}
```

## Enterprise Edit Protection

For `Scope: Enterprise` constraints:
- **Read-only fields:** `title`, `statement`, `type`, `priority`, `source`, `phase`, `owner`
- **Editable fields:** `status`, `linkedArtifacts`, `waiverJustification`, `impactAssessment`
- Enforce non-empty `waiverJustification` when `status` is `Waived`

## Sync Behavior

1. Read `constraintsRepoPath` from `engagement.json`.
2. Handle `.md`, `.docx`, `.xlsx`, `.csv` via `ea-document-ingestion`.
3. Default imported records to `scope: "Enterprise"`.
4. Never overwrite `status`, `linkedArtifacts`, or `waiverJustification` on re-sync.

## Traceability

Constraints trace to:
- **Artifacts** that must respect them (via `linkedArtifacts`)
- **SBBs** that are selected within their boundaries (via `Referenced Constraints` field in SBB records)
- **Requirements** that are bounded by them (cross-reference in Requirements Register)
- **Work Packages** that must validate compliance before scheduling
