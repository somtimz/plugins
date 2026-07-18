---
name: ea-usecases
description: Manage use cases — capture actor-goal interactions, trace to requirements, processes, capabilities, and value streams
argument-hint: "[list|add|update|trace|generate] [--status Active|Draft|Under Review|Deprecated|Retired] [--actor name] [--priority High|Medium|Low]"
allowed-tools: [Read, Write, Bash]
---

You are executing the `/ea-usecases` command. Load the `ea-use-cases-management` skill for detailed logic and the `ea-artifact-templates` skill for concept definitions.

## Overview

This command manages `UC-NNN` entries. Read `skills/ea-artifact-templates/references/ea-concepts.md` (**Use Case**) for the canonical definition before prompting or validating. The command aggregates all `UC-NNN` entries into a single Use Cases Register, supports creating or updating individual use cases, traces use cases to linked requirements/processes/capabilities/value streams, and regenerates the register artifact.

**Modes:**
- `list` (default) — read the Use Cases Register, render a summary table
- `add` — interactively capture a new use case and write it to the register
- `update` — update a single field on an existing use case (`/ea-usecases update UC-NNN <field> <value>`)
- `trace` — show which requirements, processes, capabilities, and value streams reference this use case
- `generate` — regenerate `artifacts/cross-cutting/operations/use-cases-register.md` from `engagement.json → useCases[]`

**Filters:**
- `--status` — filter by status
- `--actor` — case-insensitive partial match on Actor
- `--priority` — filter by priority

---

## Step 1 — Resolve Active Engagement

1. Check the conversation context for an active engagement slug.
2. If none found, scan `EA-projects/*/engagement.json` and ask the user to select one.
3. Load `engagement.json` — extract: name, slug, currentPhase, `useCases[]`.

---

## Mode: `list` (default)

1. Read `EA-projects/{slug}/artifacts/cross-cutting/operations/use-cases-register.md` (human-readable register).
2. Render a summary table:

```
Use Cases Register — {engagement name}
══════════════════════════════════════════════════════════
Total: {N}  |  Active: {N}  |  Draft: {N}  |  Under Review: {N}  |  Deprecated: {N}  |  Retired: {N}

By Priority:     High {N}  |  Medium {N}  |  Low {N}
By Actor:        {N} distinct actor(s)
Orphans:         {N} use case(s) with no linked requirement, process, capability, or value stream
Untraced:        {N} use case(s) with broken link references
Detail Files:    {N} UC-NNN(s) with detail files  |  {N} open issues across all detail files
```

3. If any use cases have `Status: Active` but no linked requirement, process, capability, or value stream, flag: "⚠️ {N} active use case(s) with no linkage — run `/ea-usecases trace` to bind them."
4. If any high-priority use case has no linked requirement, flag: "⚠️ {N} High-priority use case(s) with no REQ-NNN linkage — run `/ea-usecases update UC-NNN linkedRequirements`."

---

## Mode: `add`

Invoked as: `/ea-usecases add`

1. Locate the existing register in `EA-projects/{slug}/artifacts/cross-cutting/operations/use-cases-register.md`. If none exists, create a minimal register from the template with this use case as the first entry.
2. Assign the next available `UC-NNN` ID (increment from the highest existing ID in `engagement.json → useCases[]`).
3. Prompt for each field in sequence (all required unless noted):

```
Creating new use case — UC-{NNN}

1. Name (goal-oriented verb phrase, e.g. "Submit Claim"):
2. Actor (primary user or external system):
3. Goal (measurable outcome the actor wants):
4. Preconditions (what must be true before; comma-separated, or press Enter):
5. Postconditions (what must be true after; comma-separated, or press Enter):
6. Priority (High / Medium / Low) [default: Medium]:
7. Status (Active / Draft / Under Review / Deprecated / Retired) [default: Draft]:
8. ADM Phase (Prelim / A / B / C-Data / C-App / D / E / F / G / H / Requirements):
9. Linked Requirements (REQ-NNN IDs, comma-separated, or press Enter) [optional]:
10. Linked Business Processes (PROC-NNN IDs, comma-separated, or press Enter) [optional]:
11. Linked Capabilities (CAP-NNN IDs, comma-separated, or press Enter) [optional]:
12. Linked Value Streams (VS-NNN IDs, comma-separated, or press Enter) [optional]:
```

4. Prompt for main-flow steps until the user enters an empty actor action:

```
Step {N} actor action (or press Enter to finish):
  System / Business response:
```

5. Prompt for alternative/exception flows until the user enters an empty condition:

```
Alternative ID (A1, A2..., or press Enter to finish):
  Condition:
  Flow:
```

6. If the user provides detailed flow content, offer: "Create a detail file `artifacts/details/UC-NNN.md` with the full use-case narrative? (y/n)".
7. If `Priority = High` and no linked requirement is provided, suggest: "High-priority use cases should link to REQ-NNN requirements."
8. Show confirmation preview:

```
New use case — UC-NNN: {name}
Actor: {actor}  |  Goal: {goal}
Priority: {priority}  |  Status: {status}  |  Phase: {admPhase}
Main Flow Steps: {N}
Linked Requirements: {linkedRequirements or "—"}
Linked Processes: {linkedProcesses or "—"}
Linked Capabilities: {linkedCapabilities or "—"}
Linked Value Streams: {linkedValueStreams or "—"}

Add to register? (y/n)
```

9. On confirm:
   - Append the use case to `engagement.json → useCases[]`.
   - Insert the use case into the register file (or regenerate if easier).
   - If accepted, create `artifacts/details/UC-NNN.md` from the item-detail template with the full narrative.
   - Set `status: Draft` if not explicitly set otherwise, `lastModified: today`.
10. Confirm: `"UC-NNN added to Use Cases Register. Use '/ea-usecases trace' to verify linkages."`

---

## Mode: `update`

Invoked as: `/ea-usecases update UC-NNN <field> <value>`

1. Locate the register and find the `UC-NNN` entry.
2. Valid fields for update:

| Field | Valid values |
|---|---|
| `name` | any string |
| `actor` | any string |
| `goal` | any string |
| `preconditions` | any string |
| `postconditions` | any string |
| `priority` | High / Medium / Low |
| `status` | Active / Draft / Under Review / Deprecated |
| `admPhase` | Prelim / A / B / C-Data / C-App / D / E / F / G / H / Requirements |
| `zachmanCell` | any string |
| `linkedRequirements` | comma-separated REQ-NNN list |
| `linkedProcesses` | comma-separated PROC-NNN list |
| `linkedCapabilities` | comma-separated CAP-NNN list |
| `linkedValueStreams` | comma-separated VS-NNN list |

3. Validation rules:
   - Setting `status` to `Deprecated` → suggest documenting the replacement use case
   - Removing all `linkedRequirements`, `linkedProcesses`, `linkedCapabilities`, and `linkedValueStreams` → warn: "This use case will have no linkages. Continue? (y/n)"
   - Link values must match existing IDs in the engagement; flag unknown IDs as broken references
4. Show proposed change: `"UC-NNN: {field} — '{old}' → '{new}'"`
5. Ask: `"Apply? (y/n)"`
6. On confirm: update the register and `engagement.json`, set `lastModified: today`.
7. Confirm: `"Updated UC-NNN: {field} set to '{new_value}'."`

---

## Mode: `trace`

Invoked as: `/ea-usecases trace [UC-NNN] [--requirements] [--processes] [--capabilities] [--streams]`

**Without UC-NNN:**
1. For every `UC-NNN` in `engagement.json → useCases[]`, scan the register and related artifacts for acknowledgments:
   - Requirements Register where `Linked Use Cases` contains UC-NNN
   - Business Processes Register where `Linked Use Cases` contains UC-NNN
   - Capability Model where the capability lists this use case
   - Value Streams Register where `Linked Use Cases` contains UC-NNN
   - Detail files: `artifacts/details/UC-NNN.md`
2. Output a traceability matrix:

```
| UC-NNN | Name | Actor | Linked REQ | Linked PROC | Linked CAP | Linked VS | Detail File | Orphan? |
|---|---|---|---|---|---|---|---|---|
```

3. Flag orphan use cases (no linked requirement, process, capability, or value stream) in red.

**With `--requirements`, `--processes`, `--capabilities`, `--streams`:**
1. For each use case, list all linked items of the requested type.
2. Flag items that reference the use case but lack formal linkage.

---

## Mode: `generate`

Invoked as: `/ea-usecases generate`

1. Read `engagement.json → useCases[]`.
2. If the register file exists at `artifacts/cross-cutting/operations/use-cases-register.md`, archive the current version to `artifacts/cross-cutting/operations/snapshots/use-cases-register-{YYYY-MM-DD-HHMM}.md`.
3. Render a new register from `templates/cross-cutting/operations/use-cases-register.md`, substituting placeholders from `engagement.json`.
4. Write the new file to `artifacts/cross-cutting/operations/use-cases-register.md`.
5. Ensure an `artifacts[]` entry exists in `engagement.json` for `use-cases-register.md` (artifactId: `use-cases-register`, phase: `cross-cutting`, status: `Draft` or existing).
6. Confirm: `"Regenerated Use Cases Register: {N} use case(s), {N} orphan(s), snapshot archived."`
