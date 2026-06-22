---
name: ea-requirements-management
description: This skill should be used when the user asks to "manage architecture requirements", "add a requirement", "sync requirements from the repo", "view requirements", "trace a requirement to an artifact", "update the requirements register", or "start the architecture requirements phase". Handles the full requirements lifecycle from capture through traceability and sync with a shared requirements repository.
version: 0.9.83
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

## 🔒REQ-001: {{requirement_title}}   ← Enterprise example

| Field | Value |
|---|---|
| **ID** | REQ-001 |
| **Scope** | Enterprise 🔒 |
| **Statement** | {{requirement_statement}} |
| **Category** | Functional / Non-Functional / Constraint / Principle |
| **NFR Sub-Type** | Performance / Reliability / Availability / Usability / Security / Maintainability / Portability / Compatibility / Recoverability — or ➖ Not applicable |
| **Measurable Target** | {{sla_or_threshold}} — or ➖ Not applicable |
| **Priority** | High / Medium / Low |
| **Source** | {{source_document_or_stakeholder}} |
| **Status** | Draft / Approved / Deferred / Waived / Rejected |
| **Waiver Justification** | {{required_if_status_is_Waived — leave blank otherwise}} |
| **ADM Phase** | {{phase_where_relevant}} |
| **Zachman Cell** | {{row}} / {{column}} |
| **Linked Artifacts** | {{artifact_ids}} |

---

## REQ-00N: {{requirement_title}}   ← Program example

| Field | Value |
|---|---|
| **ID** | REQ-00N |
| **Scope** | Program |
| **Statement** | {{requirement_statement}} |
| **Category** | Functional / Non-Functional / Constraint / Principle |
| **NFR Sub-Type** | Performance / Reliability / Availability / Usability / Security / Maintainability / Portability / Compatibility / Recoverability — or ➖ Not applicable |
| **Measurable Target** | {{sla_or_threshold}} — or ➖ Not applicable |
| **Priority** | High / Medium / Low |
| **Source** | {{source_stakeholder_or_document}} |
| **Status** | Draft / Approved / Deferred / Rejected |
| **Derived From** | {{enterprise_req_id — leave blank if not derived from an Enterprise requirement}} |
| **ADM Phase** | {{phase_where_relevant}} |
| **Zachman Cell** | {{row}} / {{column}} |
| **Linked Artifacts** | {{artifact_ids}} |

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
      "statement": "",
      "category": "Functional | Non-Functional | Constraint | Principle | Assumption",
      "scope": "Enterprise | Program",
      "nfrSubType": "Performance | Reliability | Availability | Usability | Security | Maintainability | Portability | Compatibility | Recoverability | null",
      "measurableTarget": "",
      "status": "Draft | Approved | Deferred | Rejected | Waived",
      "priority": "High | Medium | Low",
      "phase": "A",
      "source": "",
      "linkedArtifacts": [],
      "derivedFrom": [],
      "waiverJustification": "",
      "sourceFile": "requirements.md"
    }
  ]
}
```

**Fields added vs. previous schema:** `statement`, `category`, `scope`, `source`, `derivedFrom`, `waiverJustification`. `Waived` added to status enum. `nfrSubType` and `measurableTarget` added in v0.9.35 — null/empty for non-NFR requirements.

## Enterprise Requirement Edit Protection

Requirements with `scope: "Enterprise"` have restricted editability. The following rules apply:

**Read-only fields (content is authoritative from the shared repo):**
- `title`, `statement`, `category`, `priority`, `source`, `phase`, `nfrSubType`, `measurableTarget`

**Editable fields (engagement-specific state):**
- `status`, `linkedArtifacts`, `derivedFrom`, `waiverJustification`

**Waived status rules:**
- `Waived` status may only be set when `waiverJustification` is non-empty. Enforce this before writing to the index for Enterprise-scoped requirements. If the field is blank, prompt: "A waiver justification is required for Enterprise requirements. Please enter the justification."
- For Program-scoped requirements, `waiverJustification` is strongly recommended but not enforced.
- A re-sync must never overwrite `status`, `waiverJustification`, or `linkedArtifacts` on an existing Enterprise record, even if the source has different values.

**Display:** Prefix Enterprise requirement IDs with 🔒 in all list and table views to indicate read-only content.

## Backward Compatibility

When reading a `requirements-index.json` where entries are missing the `scope` field (engagements created before this version):

1. Apply a migration heuristic per entry:
   - If the entry's `sourceFile` matches a file path under `requirementsRepoPath` → infer `scope: "Enterprise"`
   - Otherwise → infer `scope: "Program"`
2. Write the inferred `scope` values on the next write operation (lazy, one-time migration — do not trigger a separate write just for migration)
3. When unscoped records are detected, display a banner:
   > "Note: X requirements are missing scope classification. Inferred scope has been applied — run `/ea-requirements list` to review."

**Legacy scope values:** If entries use the old values `"Corporate"` or `"Project"` (pre-v0.9.35), treat them as `"Enterprise"` and `"Program"` respectively on read. Rewrite to the new values on the next write operation. Run `/ea-migrate` for a bulk rename.

### Scope Reclassification on Re-sync

If a Program-scoped record matches an incoming Enterprise record on re-sync (same ID, incoming `scope` is Enterprise):
- Flag as a scope reclassification conflict
- Prompt: "REQ-XXX was Program-scoped and is now Enterprise in the shared repo. Confirming will make its content fields read-only. Confirm reclassification?"
- Only reclassify on explicit user confirmation

## Syncing from the Requirements Repository

The requirements repository may contain mixed formats: Markdown, Word (.docx), Excel (.xlsx/.csv).

### Sync Workflow

1. Read `requirementsRepoPath` from `engagement.json`
2. Scan the directory for supported files: `.md`, `.docx`, `.xlsx`, `.csv`
3. For each file, extract requirements using the `ea-document-ingestion` skill
4. Present extracted requirements to the user for review and confirmation
5. Merge approved requirements into `requirements.md` and `requirements-index.json`. Set `scope: "Enterprise"` on all sync-imported records. Never overwrite `status`, `linkedArtifacts`, or `waiverJustification` of existing Enterprise records during re-sync.
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
1. Sync from requirements repo — all synced records are automatically tagged `scope: "Enterprise"`
2. Conduct requirements interview using `ea-interviewer` agent
3. Classify each requirement (functional, non-functional, constraint, principle)
4. Assign Zachman cell classification
5. Set initial priority and status

**Ongoing updates (any phase):**
1. Add new requirements as they emerge from phase activities
2. Update status of existing requirements
3. Re-sync from repo if updated externally
4. Trigger consistency check when requirements change

`/ea-phase` reinforces the continuous discipline: on every phase entry it surfaces open requirements whose `phase` field matches the entered phase (the requirements check-in), and on Requirements-phase completion it bridges directly into Phase A with the register carried as interview context.

## Content Policy

- Requirements must be sourced from stakeholder input, uploaded documents, or explicit user entry
- AI-suggested requirements must be marked: `🤖 AI Draft — Review Required`
- Never auto-approve requirements — all require user confirmation before status is set to `Approved`

## Additional Resources

- **`references/requirement-categories.md`** — Taxonomy of requirement types with TOGAF alignment
- **`references/sync-formats.md`** — Detailed parsing rules for Word, Excel, and CSV requirement formats

## Traceability Graph

Cross-entity links are stored in `EA-projects/{slug}/artifacts/requirements/traceability-index.json`. This file is separate from `requirements-index.json` and is created on first use by `/ea-trace`.

### traceability-index.json Schema

```json
{
  "lastUpdated": "YYYY-MM-DDTHH:MM:SSZ",
  "links": [
    {"from": "DRV-001", "to": "G-001",   "type": "motivates"},
    {"from": "G-001",   "to": "STR-001", "type": "addresses"},
    {"from": "STR-001", "to": "REQ-001", "type": "supports"},
    {"from": "REQ-001", "to": "CAP-003", "type": "satisfiedBy"},
    {"from": "CAP-003", "to": "WP-002",  "type": "deliveredBy"}
  ]
}
```

### Link Type Vocabulary (v1)

| Type | From | To | Meaning |
|---|---|---|---|
| `motivates` | DRV-NNN | G-NNN | Driver motivates a goal |
| `addresses` | G-NNN | STR-NNN | Goal is addressed by a strategy |
| `supports` | STR-NNN | REQ-NNN | Requirement supports a strategy |
| `satisfiedBy` | REQ-NNN | CAP-NNN | Requirement is satisfied by a capability |
| `deliveredBy` | CAP-NNN | WP-NNN | Capability is delivered by a work package |

Reserved for v2 (do not use in v1):

| Type | From | To |
|---|---|---|
| `ownedBy` | REQ-NNN | Stakeholder name |
| `measuredBy` | G-NNN | MET-NNN |
| `enabledBy` | VS-NNN | CAP-NNN |

### Backward Compatibility

If `traceability-index.json` does not exist, create it with `{"lastUpdated": "", "links": []}` on first write. All entities will appear as gaps until links are added.
