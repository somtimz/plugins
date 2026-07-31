---
name: ea-processes
description: Manage business processes — capture structured activity flows, trace to value streams, capabilities, use cases, rules, and services
argument-hint: "[list|add|update|trace|generate] [--status Active|Draft|Under Review|Deprecated|Retired] [--owner name]"
allowed-tools: [Read, Write, Bash]
---

You are executing the `/ea-processes` command. Load the `ea-business-processes-management` skill for detailed logic and the `ea-artifact-templates` skill for concept definitions.

## Overview

This command manages `PROC-NNN` entries. Read `skills/ea-artifact-templates/references/concept-families/business-layer-concepts.md` (**Business Process**) for the canonical definition before prompting or validating. The command aggregates all `PROC-NNN` entries into a single Business Processes Register, supports creating or updating individual processes, traces processes to linked items, and regenerates the register artifact.

**Modes:**
- `list` (default) — read the Business Processes Register, render a summary table
- `add` — interactively capture a new business process and write it to the register
- `update` — update a single field on an existing process (`/ea-processes update PROC-NNN <field> <value>`)
- `trace` — show which value streams, capabilities, use cases, rules, and services reference this process
- `generate` — regenerate `artifacts/cross-cutting/operations/business-processes-register.md` from `engagement.json → businessProcesses[]`

**Filters:**
- `--status` — filter by status
- `--owner` — case-insensitive partial match on Owner

---

## Step 1 — Resolve Active Engagement

1. Check the conversation context for an active engagement slug.
2. If none found, scan `EA-projects/*/engagement.json` and ask the user to select one.
3. Load `engagement.json` — extract: name, slug, currentPhase, `businessProcesses[]`.

---

## Mode: `list` (default)

1. Read `EA-projects/{slug}/artifacts/cross-cutting/operations/business-processes-register.md` (human-readable register).
2. Render a summary table:

```
Business Processes Register — {engagement name}
══════════════════════════════════════════════════════════
Total: {N}  |  Active: {N}  |  Draft: {N}  |  Under Review: {N}  |  Deprecated: {N}  |  Retired: {N}

By Owner:        {N} distinct owner(s)
Steps (avg):     {N}
Orphans:         {N} process(es) with no linked value stream, capability, use case, rule, or service
Untraced:        {N} process(es) with broken link references
Detail Files:    {N} PROC-NNN(s) with detail files  |  {N} open issues across all detail files
```

3. If any processes have `Status: Active` but no linked value stream, capability, use case, rule, or service, flag: "⚠️ {N} active process(es) with no linkage — run `/ea-processes trace` to bind them."
4. If any active process has no `Owner`, flag: "⚠️ {N} active process(es) without an owner — run `/ea-processes update PROC-NNN owner`."

---

## Mode: `add`

Invoked as: `/ea-processes add`

1. Locate the existing register in `EA-projects/{slug}/artifacts/cross-cutting/operations/business-processes-register.md`. If none exists, create a minimal register from the template with this process as the first entry.
2. Assign the next available `PROC-NNN` ID (increment from the highest existing ID in `engagement.json → businessProcesses[]`).
3. Prompt for each field in sequence (all required unless noted):

```
Creating new business process — PROC-{NNN}

1. Name (verb-noun phrase, e.g. "Approve Supplier Invoice"):
2. Purpose (why the process exists):
3. Owner (accountable role or team):
4. Trigger (event that starts the process):
5. Inputs (comma-separated key inputs):
6. Outputs (comma-separated key outputs):
7. Status (Active / Draft / Under Review / Deprecated / Retired) [default: Draft]:
8. ADM Phase (Prelim / A / B / C-Data / C-App / D / E / F / G / H / Requirements):
9. Linked Value Streams (VS-NNN IDs, comma-separated, or press Enter) [optional]:
10. Linked Capabilities (CAP-NNN IDs, comma-separated, or press Enter) [optional]:
11. Linked Use Cases (UC-NNN IDs, comma-separated, or press Enter) [optional]:
12. Linked Business Rules (BR-NNN IDs, comma-separated, or press Enter) [optional]:
13. Linked Business Services (SVC-NNN IDs, comma-separated, or press Enter) [optional]:
```

4. Prompt for steps until the user enters an empty activity:

```
Step {N} activity (or press Enter to finish):
  Responsible role:
  System / Tool:
  Business Rule (BR-NNN, or press Enter):
```

5. If the user provides detailed step content (actors, systems, decision points), offer: "Create a detail file `artifacts/details/PROC-NNN.md` with the full process narrative? (y/n)".
6. If `Status = Active` and no linked value stream, capability, use case, rule, or service is provided, suggest: "Consider linking this process to VS-NNN / CAP-NNN / UC-NNN / BR-NNN / SVC-NNN."
7. Show confirmation preview:

```
New business process — PROC-NNN: {name}
Owner: {owner}  |  Trigger: {trigger}
Inputs: {inputs}  |  Outputs: {outputs}
Steps: {N}
Status: {status}  |  Phase: {admPhase}
Linked Value Streams: {linkedValueStreams or "—"}
Linked Capabilities: {linkedCapabilities or "—"}
Linked Use Cases: {linkedUseCases or "—"}
Linked Rules: {linkedRules or "—"}
Linked Services: {linkedServices or "—"}

Add to register? (y/n)
```

8. On confirm:
   - Append the process to `engagement.json → businessProcesses[]`.
   - Insert the process into the register file (or regenerate if easier).
   - If accepted, create `artifacts/details/PROC-NNN.md` from the item-detail template with the step narrative.
   - Set `status: Draft` if not explicitly set otherwise, `lastModified: today`.
9. If an `operating-model.md` artifact exists, offer: "Link this process to the Operating Model §5 Business Processes Execution Model? (y/n)". If yes, append a summary row to `artifacts/phase-b/operating-model.md` §5 and update `relatedArtifacts`/`links` frontmatter if needed.
10. Confirm: `"PROC-NNN added to Business Processes Register. Use '/ea-processes trace' to verify linkages."`

---

## Mode: `update`

Invoked as: `/ea-processes update PROC-NNN <field> <value>`

1. Locate the register and find the `PROC-NNN` entry.
2. Valid fields for update:

| Field | Valid values |
|---|---|
| `name` | any string |
| `purpose` | any string |
| `owner` | any string |
| `trigger` | any string |
| `inputs` | any string |
| `outputs` | any string |
| `status` | Active / Draft / Under Review / Deprecated / Retired |
| `admPhase` | Prelim / A / B / C-Data / C-App / D / E / F / G / H / Requirements |
| `zachmanCell` | any string |
| `linkedValueStreams` | comma-separated VS-NNN list |
| `linkedCapabilities` | comma-separated CAP-NNN list |
| `linkedUseCases` | comma-separated UC-NNN list |
| `linkedRules` | comma-separated BR-NNN list |
| `linkedServices` | comma-separated SVC-NNN list |

3. Validation rules:
   - Setting `status` to `Deprecated` → suggest documenting the replacement process
   - Setting `status` to `Retired` → warn: "Retiring a process may break downstream services. Continue? (y/n)"
   - Setting `owner` to blank when `status = Active` → warn: "Active processes require an owner. Keep existing? (y/n)"
   - Removing all `linkedValueStreams`, `linkedCapabilities`, `linkedUseCases`, `linkedRules`, and `linkedServices` → warn: "This process will have no linkages. Continue? (y/n)"
   - Link values must match existing IDs in the engagement; flag unknown IDs as broken references
4. Show proposed change: `"PROC-NNN: {field} — '{old}' → '{new}'"`
5. Ask: `"Apply? (y/n)"`
6. On confirm: update the register and `engagement.json`, set `lastModified: today`.
7. Confirm: `"Updated PROC-NNN: {field} set to '{new_value}'."`

---

## Mode: `trace`

Invoked as: `/ea-processes trace [PROC-NNN] [--streams] [--capabilities] [--usecases] [--rules] [--services]`

**Without PROC-NNN:**
1. For every `PROC-NNN` in `engagement.json → businessProcesses[]`, scan the register and related artifacts for acknowledgments:
   - Value Streams Register where `Linked Business Processes` contains PROC-NNN
   - Capability Model where the capability lists this process
   - Use Cases Register where `Linked Business Processes` contains PROC-NNN
   - Business Rules Register where `Linked Business Processes` contains PROC-NNN
   - Business Services Register where `Linked Business Processes` contains PROC-NNN
   - Detail files: `artifacts/details/PROC-NNN.md`
2. Output a traceability matrix:

```
| PROC-NNN | Name | Owner | Linked VS | Linked CAP | Linked UC | Linked BR | Linked SVC | Detail File | Orphan? |
|---|---|---|---|---|---|---|---|---|---|
```

3. Flag orphan processes (no linked value stream, capability, use case, rule, or service) in red.

**With `--streams`, `--capabilities`, `--usecases`, `--rules`, `--services`:**
1. For each process, list all linked items of the requested type.
2. Flag items that reference the process but lack formal linkage.

---

## Mode: `generate`

Invoked as: `/ea-processes generate`

1. Read `engagement.json → businessProcesses[]`.
2. If the register file exists at `artifacts/cross-cutting/operations/business-processes-register.md`, archive the current version to `artifacts/cross-cutting/operations/snapshots/business-processes-register-{YYYY-MM-DD-HHMM}.md`.
3. Render a new register from `templates/cross-cutting/operations/business-processes-register.md`, substituting placeholders from `engagement.json`.
4. Write the new file to `artifacts/cross-cutting/operations/business-processes-register.md`.
5. Ensure an `artifacts[]` entry exists in `engagement.json` for `business-processes-register.md` (artifactId: `business-processes-register`, phase: `cross-cutting`, status: `Draft` or existing).
6. Confirm: `"Regenerated Business Processes Register: {N} process(es), {N} orphan(s), snapshot archived."`
