---
name: ea-value-streams-management
description: This skill should be used when the user asks to "manage value streams", "add a value stream", "view value streams", "trace a value stream to capabilities or processes", "update the value streams register", or "assess value stream coverage". Handles the full value-stream lifecycle from capture through traceability and linkage to capabilities, processes, goals, and stakeholders.
version: 0.9.87
---

# EA Value Streams Management

This skill manages `VS-NNN` entries. Load `skills/ea-artifact-templates/references/ea-concepts.md` for the canonical **Value Stream**, **Capability**, and **Business Process** definitions before prompting for or validating any value stream.

## Value Streams Storage

Local value streams are stored in `EA-projects/{slug}/artifacts/cross-cutting/operations/value-streams-register.md`:

```
artifacts/cross-cutting/operations/
├── value-streams-register.md   # human-readable value streams register (stable filename; superseded versions in snapshots/)
```

The `valueStreams` array in `engagement.json` stores metadata and links for fast lookup.

## Value Streams Register Format

`value-streams-register.md` uses a structured template:

```markdown
# Value Streams Register

**Engagement:** {{engagement_name}}
**Last Synced:** {{last_sync_date}}
**Version:** {{version}}

---

## VS-001: {{value_stream_name}}

| Field | Value |
|---|---|
| **ID** | VS-001 |
| **Name** | {{name}} |
| **Description** | {{description}} |
| **Stakeholder** | {{stakeholder}} |
| **Status** | Active / Draft / Under Review / Deprecated / Retired |
| **ADM Phase** | {{phase}} |
| **Zachman Cell** | {{zachman_cell}} |
| **Linked Capabilities** | {{CAP-NNN IDs}} |
| **Linked Business Processes** | {{PROC-NNN IDs}} |
| **Trace to Goals** | {{G-NNN / OBJ-NNN IDs}} |

### Stages

| Stage | Trigger | Activities | Outcome |
|---|---|---|---|
| 1 — {{stage_name}} | {{trigger}} | {{activities}} | {{outcome}} |
| ... | ... | ... | ... |
```

## Engagement.json Schema

Value Streams are tracked in `engagement.json` under the **top-level `valueStreams[]` array** (sibling to `rules[]`, `services[]`, `metrics[]`, etc.):

```json
{
  "valueStreams": [
    {
      "id": "VS-001",
      "name": "",
      "description": "",
      "stakeholder": "",
      "status": "Active | Draft | Under Review | Deprecated | Retired",
      "admPhase": "Prelim | A | B | C-Data | C-App | D | E | F | G | H | Requirements",
      "zachmanCell": "",
      "stages": [
        {
          "stage": 1,
          "name": "",
          "trigger": "",
          "activities": "",
          "outcome": ""
        }
      ],
      "linkedCapabilities": [],
      "linkedProcesses": [],
      "linkedGoals": [],
      "sourceFile": "value-streams-register.md"
    }
  ]
}
```

## Traceability

Value Streams trace to:
- **Capabilities** that enable each stage (`linkedCapabilities`)
- **Business Processes** that operationalise the stream (`linkedProcesses`)
- **Goals / Objectives** the stream realises (`linkedGoals`)
- **Stakeholders** who receive the end value (`stakeholder`)

## Value Stream Lifecycle

```
Draft → Active → Under Review → Deprecated → Retired
```

- **Draft:** Stream captured but not yet ratified. Links may be incomplete.
- **Active:** Stream is the target operating model and should be supported by linked processes and capabilities.
- **Under Review:** Stream is being reassessed. Linked processes/capabilities remain active but may need revalidation.
- **Deprecated:** Stream replaced by a newer design. Linked processes/capabilities should be reviewed for migration.
- **Retired:** Stream no longer used. Linked processes/capabilities should be reviewed for removal or waiver.

## Capture Guidance

When prompting for a new value stream:
1. **Name** — outcome-oriented noun phrase (e.g. "Procure to Pay", "Order to Delivery").
2. **Stakeholder** — who ultimately receives value (prefer a role or persona, e.g. "Customer", "Supplier", "Regulator").
3. **Description** — the value proposition in one sentence.
4. **Stages** — 3–7 high-level stages. For each: trigger → activities → outcome.
5. **Trace links** — offer existing CAP-NNN, PROC-NNN, G-NNN / OBJ-NNN IDs from `engagement.json`.

## Validation Checks

- At least one stage must be present.
- Every stage must have non-empty `trigger`, `activities`, and `outcome`.
- `status` must be one of the allowed enum values.
- Linked IDs must exist in the engagement; flag broken references in `trace` and `list`.
- A value stream with no linked capability, process, or goal is an **orphan** — flag in `list` and suggest `/ea-valuestreams update VS-NNN linkedCapabilities` or `linkedGoals`.

## Maturity Marker

- **L1:** Value streams implied by org charts or system modules.
- **L3:** Value streams catalogued with stages and linked to capabilities/processes.
- **L5:** Value streams measured by stage-level KPIs, continuously improved, and traced to business outcomes.
