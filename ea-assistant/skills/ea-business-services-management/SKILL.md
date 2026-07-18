---
name: ea-business-services-management
description: This skill should be used when the user asks to "manage business services", "add a service", "view services", "trace a service to rules or capabilities", "update the business services register", or "assess service coverage". Handles the full service lifecycle from capture through the Consumer–Outcome–Interface triad and linkage to business rules, capabilities, ABB/SBB, and interfaces.
version: 0.9.87
---

# EA Business Services Management

This skill manages `SVC-NNN` entries. Load `skills/ea-artifact-templates/references/ea-concepts.md` for the canonical **Service** and **Business Rule** definitions before prompting for or validating any service.

## Business Services Storage

Local services are stored in `EA-projects/{slug}/artifacts/cross-cutting/operations/business-services-register.md`:

```
artifacts/cross-cutting/operations/
├── business-services-register.md   # human-readable services register (stable filename; superseded versions in snapshots/)
```

The `services` array in `engagement.json` stores metadata and links for fast lookup.

## Business Services Register Format

`business-services-register.md` uses a structured template:

```markdown
# Business Services Register

**Engagement:** {{engagement_name}}
**Last Synced:** {{last_sync_date}}
**Version:** {{version}}

---

## SVC-001: {{service_name}}   ← Business-level example

| Field | Value |
|---|---|
| **ID** | SVC-001 |
| **Name** | {{service_name}} |
| **Level** | Business |
| **Purpose** | {{purpose}} |
| **Consumer** | {{consumer}} |
| **Outcome** | {{outcome}} |
| **Interface** | {{interface / IFC-NNN}} |
| **Owner** | {{owner}} |
| **SLA / NFR** | {{REQ-NNN or SLA statement}} |
| **Linked Business Rules** | {{BR-NNN IDs}} |
| **Linked Capabilities** | {{CAP-NNN IDs}} |
| **Linked Value Streams** | {{VS-NNN IDs}} |
| **Linked Business Processes** | {{PROC-NNN IDs}} |
| **Linked ABB** | {{ABB-NNN IDs}} |
| **Linked SBB** | {{SBB-NNN IDs}} |
| **Linked Interfaces** | {{IFC-NNN IDs}} |

---

## SVC-00N: {{service_name}}   ← Application/Technology-level example

| Field | Value |
|---|---|
| **ID** | SVC-00N |
| **Name** | {{service_name}} |
| **Level** | Application / Technology |
| **Purpose** | {{purpose}} |
| **Consumer** | {{consumer}} |
| **Outcome** | {{outcome}} |
| **Interface** | {{interface / IFC-NNN}} |
| **Owner** | {{owner}} |
| **SLA / NFR** | {{REQ-NNN or SLA statement}} |
| **Linked Capabilities** | {{CAP-NNN IDs}} |
| **Linked Value Streams** | {{VS-NNN IDs}} |
| **Linked Business Processes** | {{PROC-NNN IDs}} |
| **Linked ABB** | {{ABB-NNN IDs}} |
| **Linked SBB** | {{SBB-NNN IDs}} |
| **Linked Interfaces** | {{IFC-NNN IDs}} |
```

## Engagement.json Schema

Services are tracked in `engagement.json` under the **top-level `services[]` array** (sibling to `metrics[]`, `policies[]`, `finance[]`, `rules[]` — not inside `direction`):

```json
{
  "services": [
    {
      "id": "SVC-001",
      "name": "",
      "level": "Business | Application | Technology",
      "purpose": "",
      "consumer": "",
      "outcome": "",
      "interface": "",
      "owner": "",
      "sla": "",
      "linkedRules": [],
      "linkedCapabilities": [],
      "linkedValueStreams": [],
      "linkedProcesses": [],
      "linkedABB": [],
      "linkedSBB": [],
      "linkedInterfaces": [],
      "sourceFile": "business-services-register.md"
    }
  ]
}
```

## Service Passport (Business-level services)

Capture every Business-level service with the **Consumer–Outcome–Interface** triad:

| Passport element | Question it answers |
|---|---|
| **Consumer** | Who uses the service? |
| **Outcome** | What business value do they receive? |
| **Interface** | Through what channel is it consumed? |
| **Owner** | Who is accountable? |
| **SLA / NFR** | What levels of service are guaranteed? |
| **Linked Business Rules** | Which operational rules does the service enact? |

## Traceability

Services trace to:
- **Business Rules** they operationalise (`linkedRules`) — only meaningful at Business level; Application/Technology services may leave this empty
- **Capabilities** that realise the service (`linkedCapabilities`)
- **Value Streams** the service contributes to (`linkedValueStreams`)
- **Business Processes** the service supports (`linkedProcesses`)
- **Architecture Building Blocks (ABB)** that expose the service (`linkedABB`)
- **Solution Building Blocks (SBB)** that implement it (`linkedSBB`)
- **Interfaces (IFC-NNN)** through which the service is consumed (`linkedInterfaces`)

## Service Lifecycle

```
Draft → Active → Under Review → Deprecated → Retired
```

- **Draft:** Service captured but not yet active. Links may be incomplete.
- **Active:** Service is offered and supported.
- **Under Review:** Service definition is being reassessed.
- **Deprecated:** Service is still offered but scheduled for replacement; update `supersededBy` if applicable.
- **Retired:** Service is no longer offered.

## Capture Guidance

When prompting for a new service:
1. **Name** — noun phrase for the offered behaviour.
2. **Level** — Business / Application / Technology.
3. **Purpose / Outcome** — the value delivered.
4. **Consumer** — who uses it.
5. **Interface** — access channel (human or digital; prefer IFC-NNN for digital).
6. **Owner** — accountable role.
7. **SLA / NFR** — service level or requirement reference.
8. **Trace links** — offer existing BR-NNN (Business level), CAP-NNN, ABB-NNN, SBB-NNN, IFC-NNN from `engagement.json`.

## Validation Checks

- `level` must be one of: `Business`, `Application`, `Technology`.
- A service with empty `name` is a placeholder — must not be rendered.
- A Business-level service without `consumer`, `outcome`, or `interface` is incomplete.
- Linked IDs must exist in the engagement; flag broken references in `trace` and `list`.
- A service with no linked capability, value stream, process, ABB, SBB, or interface is an **orphan** — flag in `list` and suggest `/ea-services update SVC-NNN linkedCapabilities`, `linkedValueStreams`, `linkedProcesses`, or `linkedInterfaces`.
- For Business-level services, suggest linking to BR-NNN rules where applicable; do not require it.
