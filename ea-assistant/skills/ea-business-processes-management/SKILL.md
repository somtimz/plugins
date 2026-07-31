---
name: ea-business-processes-management
description: This skill should be used when the user asks to "manage business processes", "add a business process", "view business processes", "trace a process to value streams or use cases", "update the business processes register", or "assess process coverage". Handles the full business-process lifecycle from capture through traceability and linkage to value streams, capabilities, use cases, services, and rules.
version: 0.9.89
---

# EA Business Processes Management

This skill manages `PROC-NNN` entries. Load `skills/ea-artifact-templates/references/concept-families/business-layer-concepts.md` for the canonical **Business Process**, **Value Stream**, **Use Case**, **Capability**, and **Business Service** definitions before prompting for or validating any process.

## Business Processes Storage

Local business processes are stored in `EA-projects/{slug}/artifacts/cross-cutting/operations/business-processes-register.md`:

```
artifacts/cross-cutting/operations/
├── business-processes-register.md   # human-readable business processes register (stable filename; superseded versions in snapshots/)
```

The `businessProcesses` array in `engagement.json` stores metadata and links for fast lookup.

## Business Processes Register Format

`business-processes-register.md` uses a structured template:

```markdown
# Business Processes Register

**Engagement:** {{engagement_name}}
**Last Synced:** {{last_sync_date}}
**Version:** {{version}}

---

## PROC-001: {{process_name}}

| Field | Value |
|---|---|
| **ID** | PROC-001 |
| **Name** | {{name}} |
| **Purpose** | {{purpose}} |
| **Owner** | {{owner}} |
| **Trigger** | {{trigger}} |
| **Inputs** | {{inputs}} |
| **Outputs** | {{outputs}} |
| **Status** | Active / Draft / Under Review / Deprecated / Retired |
| **ADM Phase** | {{phase}} |
| **Zachman Cell** | {{zachman_cell}} |
| **Linked Value Streams** | {{VS-NNN IDs}} |
| **Linked Capabilities** | {{CAP-NNN IDs}} |
| **Linked Use Cases** | {{UC-NNN IDs}} |
| **Linked Business Rules** | {{BR-NNN IDs}} |
| **Linked Business Services** | {{SVC-NNN IDs}} |

### Steps

| Step | Activity | Responsible | System / Tool | Business Rule |
|---|---|---|---|---|
| 1 | {{activity}} | {{role}} | {{system}} | {{BR-NNN}} |
| ... | ... | ... | ... | ... |
```

## Engagement.json Schema

Business Processes are tracked in `engagement.json` under the **top-level `businessProcesses[]` array** (sibling to `rules[]`, `services[]`, `valueStreams[]`, etc.):

```json
{
  "businessProcesses": [
    {
      "id": "PROC-001",
      "name": "",
      "purpose": "",
      "owner": "",
      "trigger": "",
      "inputs": "",
      "outputs": "",
      "status": "Active | Draft | Under Review | Deprecated | Retired",
      "admPhase": "Prelim | A | B | C-Data | C-App | D | E | F | G | H | Requirements",
      "zachmanCell": "",
      "steps": [
        {
          "step": 1,
          "activity": "",
          "responsible": "",
          "system": "",
          "businessRule": ""
        }
      ],
      "linkedValueStreams": [],
      "linkedCapabilities": [],
      "linkedUseCases": [],
      "linkedRules": [],
      "linkedServices": [],
      "sourceFile": "business-processes-register.md"
    }
  ]
}
```

## Traceability

Business Processes trace to:
- **Value Streams** they participate in (`linkedValueStreams`)
- **Capabilities** they exercise or realise (`linkedCapabilities`)
- **Use Cases** that drive or depend on the process (`linkedUseCases`)
- **Business Rules** that govern decisions within the process (`linkedRules`)
- **Business Services** that operationalise the process (`linkedServices`)

## Business Process Lifecycle

```
Draft → Active → Under Review → Deprecated → Retired
```

- **Draft:** Process captured but not yet active. Steps and links may be incomplete.
- **Active:** Process is the target operating model and should be supported by linked capabilities/services.
- **Under Review:** Process is being reassessed. Linked items remain active but may need revalidation.
- **Deprecated:** Process replaced by a newer design. Linked services/capabilities should be reviewed for migration.
- **Retired:** Process no longer used. Linked services/rules should be reviewed for removal or waiver.

## Capture Guidance

When prompting for a new business process:
1. **Name** — verb-noun phrase describing the output (e.g. "Approve Supplier Invoice").
2. **Purpose** — why the process exists and the value it produces.
3. **Owner** — accountable role or team.
4. **Trigger** — event that starts the process.
5. **Inputs / Outputs** — key artifacts or data consumed and produced.
6. **Steps** — numbered activities with responsible role, supporting system/tool, and governing BR-NNN if any.
7. **Trace links** — offer existing VS-NNN, CAP-NNN, UC-NNN, BR-NNN, SVC-NNN IDs from `engagement.json`.

## Validation Checks

- At least one step must be present.
- Every step must have non-empty `activity` and `responsible`.
- `status` must be one of the allowed enum values.
- Linked IDs must exist in the engagement; flag broken references in `trace` and `list`.
- A process with no linked value stream, capability, use case, rule, or service is an **orphan** — flag in `list` and suggest `/ea-processes update PROC-NNN linkedValueStreams` or `linkedCapabilities`.

## Maturity Marker

- **L1:** Processes described informally in documents or presentations.
- **L3:** Processes catalogued with trigger/inputs/outputs/steps and linked to value streams, capabilities, and rules.
- **L5:** Processes measured by KPIs, owned by accountable roles, automated where appropriate, and continuously optimised.
