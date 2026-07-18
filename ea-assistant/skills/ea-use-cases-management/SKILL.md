---
name: ea-use-cases-management
description: This skill should be used when the user asks to "manage use cases", "add a use case", "view use cases", "trace a use case to requirements or processes", "update the use cases register", or "assess use case coverage". Handles the full use-case lifecycle from capture through traceability and linkage to requirements, processes, capabilities, and value streams.
version: 0.9.88
---

# EA Use Cases Management

This skill manages `UC-NNN` entries. Load `skills/ea-artifact-templates/references/ea-concepts.md` for the canonical **Use Case**, **Business Process**, **Capability**, and **Requirement** definitions before prompting for or validating any use case.

## Use Cases Storage

Local use cases are stored in `EA-projects/{slug}/artifacts/cross-cutting/operations/use-cases-register.md`:

```
artifacts/cross-cutting/operations/
├── use-cases-register.md   # human-readable use cases register (stable filename; superseded versions in snapshots/)
```

The `useCases` array in `engagement.json` stores metadata and links for fast lookup.

## Use Cases Register Format

`use-cases-register.md` uses a structured template:

```markdown
# Use Cases Register

**Engagement:** {{engagement_name}}
**Last Synced:** {{last_sync_date}}
**Version:** {{version}}

---

## UC-001: {{use_case_name}}

| Field | Value |
|---|---|
| **ID** | UC-001 |
| **Name** | {{name}} |
| **Actor** | {{actor}} |
| **Goal** | {{goal}} |
| **Preconditions** | {{preconditions}} |
| **Postconditions** | {{postconditions}} |
| **Priority** | High / Medium / Low |
| **Status** | Active / Draft / Under Review / Deprecated / Retired |
| **ADM Phase** | {{phase}} |
| **Zachman Cell** | {{zachman_cell}} |
| **Linked Requirements** | {{REQ-NNN IDs}} |
| **Linked Business Processes** | {{PROC-NNN IDs}} |
| **Linked Capabilities** | {{CAP-NNN IDs}} |
| **Linked Value Streams** | {{VS-NNN IDs}} |

### Main Flow

| Step | Actor Action | System / Business Response |
|---|---|---|
| 1 | {{action}} | {{response}} |
| ... | ... | ... |

### Alternative / Exception Flows

| ID | Condition | Flow |
|---|---|---|
| A1 | {{condition}} | {{flow}} |
```

## Engagement.json Schema

Use Cases are tracked in `engagement.json` under the **top-level `useCases[]` array** (sibling to `rules[]`, `services[]`, `valueStreams[]`, `businessProcesses[]`, etc.):

```json
{
  "useCases": [
    {
      "id": "UC-001",
      "name": "",
      "actor": "",
      "goal": "",
      "preconditions": "",
      "postconditions": "",
      "priority": "High | Medium | Low",
      "status": "Active | Draft | Under Review | Deprecated | Retired",
      "admPhase": "Prelim | A | B | C-Data | C-App | D | E | F | G | H | Requirements",
      "zachmanCell": "",
      "mainFlow": [
        {
          "step": 1,
          "actorAction": "",
          "systemResponse": ""
        }
      ],
      "altFlows": [
        {
          "id": "A1",
          "condition": "",
          "flow": ""
        }
      ],
      "linkedRequirements": [],
      "linkedProcesses": [],
      "linkedCapabilities": [],
      "linkedValueStreams": [],
      "sourceFile": "use-cases-register.md"
    }
  ]
}
```

## Traceability

Use Cases trace to:
- **Requirements** they realise or constrain (`linkedRequirements`)
- **Business Processes** they trigger or participate in (`linkedProcesses`)
- **Capabilities** they exercise (`linkedCapabilities`)
- **Value Streams** they contribute to (`linkedValueStreams`)

## Use Case Lifecycle

```
Draft → Active → Under Review → Deprecated → Retired
```

- **Draft:** Use case captured but not yet ratified. Flows and links may be incomplete.
- **Active:** Use case is in scope and should be supported by linked processes/requirements.
- **Under Review:** Use case is being reassessed. Linked requirements/processes remain active but may need revalidation.
- **Deprecated:** Use case no longer in scope. Linked requirements/processes should be reviewed.
- **Retired:** Use case no longer used. Linked requirements/processes should be reviewed for removal or waiver.

## Capture Guidance

When prompting for a new use case:
1. **Name** — goal-oriented verb phrase (e.g. "Submit Claim", "Verify Customer Identity").
2. **Actor** — primary user or system that initiates the use case.
3. **Goal** — the measurable outcome the actor wants.
4. **Preconditions / Postconditions** — what must be true before and after.
5. **Main Flow** — numbered actor action ↔ system/business response pairs.
6. **Alternative / Exception Flows** — deviations and error paths.
7. **Trace links** — offer existing REQ-NNN, PROC-NNN, CAP-NNN, VS-NNN IDs from `engagement.json`.

## Validation Checks

- At least one main-flow step must be present.
- Every main-flow step must have non-empty `actorAction` and `systemResponse`.
- `priority` must be one of: `High`, `Medium`, `Low`.
- `status` must be one of the allowed enum values.
- Linked IDs must exist in the engagement; flag broken references in `trace` and `list`.
- A use case with no linked requirement, process, capability, or value stream is an **orphan** — flag in `list` and suggest `/ea-usecases update UC-NNN linkedRequirements` or `linkedProcesses`.

## Maturity Marker

- **L1:** Use cases scattered in requirements documents or workshop notes.
- **L3:** Use cases catalogued with actor/goal/flow and linked to requirements/processes.
- **L5:** Use cases tied to acceptance criteria, test cases, and continuous backlog traceability.
