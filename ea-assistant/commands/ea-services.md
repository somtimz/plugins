---
name: ea-services
description: Manage business, application, and technology services — capture service passports, trace to rules, capabilities, ABB/SBB, and interfaces
argument-hint: "[list|add|update|trace|coverage] [--level Business|Application|Technology] [--consumer name] [--status Active|Draft|Under Review|Deprecated|Retired]"
allowed-tools: [Read, Write, Bash]
---

You are executing the `/ea-services` command. Load the `ea-business-services-management` skill for detailed logic and the `ea-artifact-templates` skill for concept definitions.

## Overview

This command manages `SVC-NNN` entries. Read `skills/ea-artifact-templates/references/concept-families/architecture-products-concepts.md` (**Service**) for the canonical definition before prompting or validating. The command aggregates all `SVC-NNN` entries into a single Business Services Register, supports creating or updating individual services, traces services to linked rules and building blocks, and assesses service coverage across capabilities.

**Modes:**
- `list` (default) — read the Business Services Register, render a table grouped by Level
- `add` — interactively capture a new service and write it to the register
- `update` — update a single field on an existing service (`/ea-services update SVC-NNN <field> <value>`)
- `trace` — show which rules, capabilities, ABBs, SBBs, and interfaces reference this service
- `coverage` — assess capability coverage and flag capabilities with no linked service

**Filters:**
- `--level` — filter by service level
- `--consumer` — case-insensitive partial match on Consumer
- `--status` — filter by status

---

## Step 1 — Resolve Active Engagement

1. Check the conversation context for an active engagement slug.
2. If none found, scan `EA-projects/*/engagement.json` and ask the user to select one.
3. Load `engagement.json` — extract: name, slug, currentPhase, `services[]`.

---

## Mode: `list` (default)

1. Read `EA-projects/{slug}/artifacts/cross-cutting/operations/business-services-register.md` (human-readable register).
2. Render a summary table grouped by Level:

```
Business Services Register — {engagement name}
══════════════════════════════════════════════════════════
Total: {N}  |  Active: {N}  |  Draft: {N}  |  Under Review: {N}  |  Deprecated: {N}  |  Retired: {N}

By Level:      Business {N}  |  Application {N}  |  Technology {N}
By Status:     Active {N}  |  Draft {N}  |  Under Review {N}  |  Deprecated {N}  |  Retired {N}
Orphans:       {N} service(s) with no linked capability, ABB, SBB, or interface
Untraced:      {N} service(s) with broken link references
Detail Files:  {N} SVC-NNN(s) with detail files  |  {N} open issues across all service detail files
```

3. If any Business-level services have no linked rules, flag: "ℹ️ {N} Business service(s) with no linked business rules — run `/ea-services update SVC-NNN linkedRules` if they enact operational rules."
4. If any services have `Status: Active` but no linked capability or interface, flag: "⚠️ {N} active service(s) with no capability or interface linkage — run `/ea-services trace` to bind them."

---

## Mode: `add`

Invoked as: `/ea-services add`

1. Locate the existing register in `EA-projects/{slug}/artifacts/cross-cutting/operations/business-services-register.md`. If none exists, create a minimal register from the template with this service as the first entry.
2. Assign the next available `SVC-NNN` ID (increment from the highest existing ID in `engagement.json → services[]`).
3. Prompt for each field in sequence (all required unless noted):

```
Creating new service — SVC-{NNN}

1. Name (noun phrase for the offered behaviour, e.g. "Claims Settlement"):
2. Level (Business / Application / Technology):
3. Purpose / Why (the reason the service exists):
4. Consumer (who uses it, e.g. "Customer", "Claims Handler", "Payment Service"):
5. Outcome (the value received, e.g. "Claim resolved and payment initiated"):
6. Interface (access channel; prefer IFC-NNN ID, or free-text for human channels):
7. Owner (accountable role):
8. SLA / NFR (REQ-NNN ID or free-text SLA statement) [optional]:
9. Delivery Channel (Digital / Branch / Phone / Partner / Field / Shared Service / Other) [optional]:
10. Operating Model Note (delivery arrangement, sourcing, location, or control context) [optional]:
11. Linked Business Rules (BR-NNN IDs, comma-separated; Business-level only, or press Enter) [optional]:
10. Linked Capabilities (CAP-NNN IDs, comma-separated, or press Enter) [optional]:
11. Linked Value Streams (VS-NNN IDs, comma-separated, or press Enter) [optional]:
12. Linked Business Processes (PROC-NNN IDs, comma-separated, or press Enter) [optional]:
13. Linked ABB (ABB-NNN IDs, comma-separated, or press Enter) [optional]:
14. Linked SBB (SBB-NNN IDs, comma-separated, or press Enter) [optional]:
15. Linked Interfaces (IFC-NNN IDs, comma-separated, or press Enter) [optional]:
```

4. If `Level = Business` and `Consumer` or `Outcome` is blank, warn: "⚠️ Business services require Consumer and Outcome. Provide them or change Level."
5. If `Level = Business` and `linkedRules` is empty, suggest: "Consider linking this service to the BR-NNN rules it operationalises."
6. Show confirmation preview:

```
New service — SVC-NNN: {name}
Level: {level}
Consumer: {consumer}  |  Outcome: {outcome}
Interface: {interface or "—"}  |  Owner: {owner or "—"}
SLA / NFR: {sla or "—"}
Delivery Channel: {deliveryChannel or "—"}
Operating Model Note: {operatingModelNote or "—"}
Linked Rules: {linkedRules or "—"}
Linked Capabilities: {linkedCapabilities or "—"}
Linked Value Streams: {linkedValueStreams or "—"}
Linked Processes: {linkedProcesses or "—"}
Linked ABB: {linkedABB or "—"}
Linked SBB: {linkedSBB or "—"}
Linked Interfaces: {linkedInterfaces or "—"}

Add to register? (y/n)
```

7. On confirm:
   - Append the service to `engagement.json → services[]`.
   - Insert the service into the register file.
   - Set `status: Draft` if not explicitly set otherwise, `lastModified: today`.
8. Confirm: `"SVC-NNN added to Business Services Register. Use '/ea-services trace' to verify linkages."`

---

## Mode: `update`

Invoked as: `/ea-services update SVC-NNN <field> <value>`

1. Locate the register and find the `SVC-NNN` entry.
2. Valid fields for update:

| Field | Valid values |
|---|---|
| `name` | any string |
| `level` | Business / Application / Technology |
| `purpose` | any string |
| `consumer` | any string |
| `outcome` | any string |
| `interface` | any string or IFC-NNN |
| `owner` | any string |
| `sla` | any string or REQ-NNN |
| `deliveryChannel` | Digital / Branch / Phone / Partner / Field / Shared Service / Other |
| `operatingModelNote` | any string |
| `status` | Active / Draft / Under Review / Deprecated / Retired |
| `linkedRules` | comma-separated BR-NNN list |
| `linkedCapabilities` | comma-separated CAP-NNN list |
| `linkedValueStreams` | comma-separated VS-NNN list |
| `linkedProcesses` | comma-separated PROC-NNN list |
| `linkedABB` | comma-separated ABB-NNN list |
| `linkedSBB` | comma-separated SBB-NNN list |
| `linkedInterfaces` | comma-separated IFC-NNN list |

3. Validation rules:
   - Setting `status` to `Deprecated` → suggest documenting the replacement or successor service
   - Setting `status` to `Retired` → warn: "Retiring a service may break consumers. Continue? (y/n)"
   - Setting `level` to `Business` with empty `consumer` or `outcome` → warn: "Business services require Consumer and Outcome."
   - Removing all `linkedCapabilities`, `linkedValueStreams`, `linkedProcesses`, `linkedABB`, `linkedSBB`, and `linkedInterfaces` → warn: "This service will have no delivery linkage. Continue? (y/n)"
   - Link values must match existing IDs in the engagement; flag unknown IDs as broken references
4. Show proposed change: `"SVC-NNN: {field} — '{old}' → '{new}'"`
5. Ask: `"Apply? (y/n)"`
6. On confirm: update the register and `engagement.json`, set `lastModified: today`.
7. Confirm: `"Updated SVC-NNN: {field} set to '{new_value}'."`

---

## Mode: `trace`

Invoked as: `/ea-services trace [SVC-NNN] [--rules] [--capabilities] [--abb] [--sbb] [--interfaces]`

**Without SVC-NNN:**
1. For every `SVC-NNN` in `engagement.json → services[]`, scan the register and related artifacts for acknowledgments:
   - Business Rules Register where `Linked Business Services` contains SVC-NNN
   - Capability Model where the capability lists this service
   - ABB/SBB files with service references
   - Interface Catalogue where the interface exposes this service
   - Detail files: `artifacts/details/SVC-NNN.md`
2. Output a traceability matrix:

```
| SVC-NNN | Name | Level | Consumer | Linked Rules | Linked Capabilities | Linked ABB | Linked SBB | Linked Interfaces | Orphan? |
|---|---|---|---|---|---|---|---|---|---|
```

3. Flag orphan services (no linked capability, ABB, SBB, or interface) in red.

**With `--rules`:**
1. For Business-level services, list linked BR-NNN rules and whether each rule is Active.
2. Flag rules operationalised by a service but not linked back from the rule.

**With `--capabilities`:**
1. For each service, list linked CAP-NNN capabilities.
2. Flag capabilities that realise a service but lack formal linkage.

**With `--abb`, `--sbb`, `--interfaces`:**
1. For each service, list linked ABB/SBB/IFC-NNN and the artifacts that reference them.

---

## Mode: `coverage`

Invoked as: `/ea-services coverage`

1. Load `engagement.json → services[]` and the Capability Model (`engagement.json → direction` does not hold capabilities; read `Architecture-Repository/`, `artifacts/*/capability-model*.md`, or `artifacts/cross-cutting/` depending on engagement layout).
2. For each capability, check whether at least one service links to it.
3. Render a coverage matrix:

```
Capability-Service Coverage — {engagement name}
══════════════════════════════════════════════════════════

Capabilities with linked services:     {N} / {total}
Capabilities without services:       {N} / {total}  ⚠️

| CAP-NNN | Capability | Linked Services | Coverage Gap |
|---|---|---|---|
```

4. For each capability with no linked service, suggest: "Create a service that realises this capability (`/ea-services add`) or link an existing service."

---

## Edge Cases

| Scenario | Handling |
|---|---|
| No services found | Report "No services found. Capture services during Business Architecture phase interviews or /ea-brainstorm." |
| Service appears in multiple artifacts | Merge fields; prefer the most complete version; list all sources |
| Business service with no Consumer or Outcome | Flag as incomplete; cannot be set to Active without both |
| `add`: Business level with blank Consumer/Outcome | Warn and require values; or downgrade to Application/Technology |
| `update`: status Retired with linked consumers | Warn about impact on consumers; offer to update linked interfaces/rules |
| `update`: level changed to Business without Consumer/Outcome | Reject or prompt for Consumer/Outcome first |
| Duplicate SVC-NNN across artifacts | Keep both; note: "Duplicate ID — re-numbering applied: SVC-NNN (from {artifact})" |
| Broken link reference | Flag in `trace`; suggest `/ea-services update SVC-NNN <link-field>` |
