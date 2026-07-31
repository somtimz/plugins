---
name: ea-valuestreams
description: Manage value streams — capture end-to-end stakeholder-to-outcome flows, trace to capabilities, processes, and goals
argument-hint: "[list|add|update|trace|generate] [--status Active|Draft|Under Review|Deprecated|Retired] [--stakeholder name]"
allowed-tools: [Read, Write, Bash]
---

You are executing the `/ea-valuestreams` command. Load the `ea-value-streams-management` skill for detailed logic and the `ea-artifact-templates` skill for concept definitions.

## Overview

This command manages `VS-NNN` entries. Read `skills/ea-artifact-templates/references/concept-families/business-layer-concepts.md` (**Value Stream**) for the canonical definition before prompting or validating. The command aggregates all `VS-NNN` entries into a single Value Streams Register, supports creating or updating individual streams, traces streams to linked capabilities/processes/goals, and regenerates the register artifact.

**Modes:**
- `list` (default) — read the Value Streams Register, render a summary table
- `add` — interactively capture a new value stream and write it to the register
- `update` — update a single field on an existing stream (`/ea-valuestreams update VS-NNN <field> <value>`)
- `trace` — show which capabilities, processes, and goals reference this stream
- `generate` — regenerate `artifacts/cross-cutting/operations/value-streams-register.md` from `engagement.json → valueStreams[]`

**Filters:**
- `--status` — filter by status
- `--stakeholder` — case-insensitive partial match on Stakeholder

---

## Step 1 — Resolve Active Engagement

1. Check the conversation context for an active engagement slug.
2. If none found, scan `EA-projects/*/engagement.json` and ask the user to select one.
3. Load `engagement.json` — extract: name, slug, currentPhase, `valueStreams[]`.

---

## Mode: `list` (default)

1. Read `EA-projects/{slug}/artifacts/cross-cutting/operations/value-streams-register.md` (human-readable register).
2. Render a summary table:

```
Value Streams Register — {engagement name}
══════════════════════════════════════════════════════════
Total: {N}  |  Active: {N}  |  Draft: {N}  |  Under Review: {N}  |  Deprecated: {N}  |  Retired: {N}

By Stakeholder:  {N} distinct stakeholder(s)
Stages (avg):    {N}
Orphans:         {N} stream(s) with no linked capability, process, or goal
Untraced:        {N} stream(s) with broken link references
Detail Files:    {N} VS-NNN(s) with detail files  |  {N} open issues across all detail files
```

3. If any streams have `Status: Active` but no linked capability or process, flag: "⚠️ {N} active stream(s) with no capability or process linkage — run `/ea-valuestreams trace` to bind them."
4. If any stream has stages without triggers, activities, or outcomes, flag: "⚠️ {N} stage(s) missing trigger/activities/outcome — run `/ea-valuestreams update VS-NNN stages` to complete."

---

## Mode: `add`

Invoked as: `/ea-valuestreams add`

1. Locate the existing register in `EA-projects/{slug}/artifacts/cross-cutting/operations/value-streams-register.md`. If none exists, create a minimal register from the template with this stream as the first entry.
2. Assign the next available `VS-NNN` ID (increment from the highest existing ID in `engagement.json → valueStreams[]`).
3. Prompt for each field in sequence (all required unless noted):

```
Creating new value stream — VS-{NNN}

1. Name (outcome-oriented noun phrase, e.g. "Procure to Pay"):
2. Description (one-sentence value proposition):
3. Stakeholder (who ultimately receives value, e.g. "Customer"):
4. Status (Active / Draft / Under Review / Deprecated / Retired) [default: Draft]:
5. ADM Phase (Prelim / A / B / C-Data / C-App / D / E / F / G / H / Requirements):
6. Linked Capabilities (CAP-NNN IDs, comma-separated, or press Enter) [optional]:
7. Linked Business Processes (PROC-NNN IDs, comma-separated, or press Enter) [optional]:
8. Trace to Goals (G-NNN / OBJ-NNN IDs, comma-separated, or press Enter) [optional]:
```

4. Prompt for stages until the user enters an empty stage name:

```
Stage {N} name (or press Enter to finish):
  Trigger:
  Activities:
  Outcome:
```

5. If `Status = Active` and no linked capability or process is provided, suggest: "Consider linking this stream to the CAP-NNN / PROC-NNN that enable it."
6. Show confirmation preview:

```
New value stream — VS-NNN: {name}
Stakeholder: {stakeholder}
Description: {description}
Stages: {N}
Status: {status}  |  Phase: {admPhase}
Linked Capabilities: {linkedCapabilities or "—"}
Linked Processes: {linkedProcesses or "—"}
Trace to Goals: {linkedGoals or "—"}

Add to register? (y/n)
```

7. On confirm:
   - Append the stream to `engagement.json → valueStreams[]`.
   - Insert the stream into the register file (or regenerate if easier).
   - Set `status: Draft` if not explicitly set otherwise, `lastModified: today`.
8. Confirm: `"VS-NNN added to Value Streams Register. Use '/ea-valuestreams trace' to verify linkages."`

---

## Mode: `update`

Invoked as: `/ea-valuestreams update VS-NNN <field> <value>`

1. Locate the register and find the `VS-NNN` entry.
2. Valid fields for update:

| Field | Valid values |
|---|---|
| `name` | any string |
| `description` | any string |
| `stakeholder` | any string |
| `status` | Active / Draft / Under Review / Deprecated |
| `admPhase` | Prelim / A / B / C-Data / C-App / D / E / F / G / H / Requirements |
| `zachmanCell` | any string |
| `linkedCapabilities` | comma-separated CAP-NNN list |
| `linkedProcesses` | comma-separated PROC-NNN list |
| `linkedGoals` | comma-separated G-NNN / OBJ-NNN list |

3. Validation rules:
   - Setting `status` to `Deprecated` → suggest documenting the replacement stream
   - Removing all `linkedCapabilities`, `linkedProcesses`, and `linkedGoals` → warn: "This stream will have no linkages. Continue? (y/n)"
   - Link values must match existing IDs in the engagement; flag unknown IDs as broken references
4. Show proposed change: `"VS-NNN: {field} — '{old}' → '{new}'"`
5. Ask: `"Apply? (y/n)"`
6. On confirm: update the register and `engagement.json`, set `lastModified: today`.
7. Confirm: `"Updated VS-NNN: {field} set to '{new_value}'."`

---

## Mode: `trace`

Invoked as: `/ea-valuestreams trace [VS-NNN] [--capabilities] [--processes] [--goals]`

**Without VS-NNN:**
1. For every `VS-NNN` in `engagement.json → valueStreams[]`, scan the register and related artifacts for acknowledgments:
   - Capability Model where the capability lists this stream
   - Business Processes Register where `Linked Value Streams` contains VS-NNN
   - Goals / Objectives registers where the stream's `linkedGoals` IDs exist
   - Detail files: `artifacts/details/VS-NNN.md`
2. Output a traceability matrix:

```
| VS-NNN | Name | Stakeholder | Linked Capabilities | Linked Processes | Trace to Goals | Detail File | Orphan? |
|---|---|---|---|---|---|---|---|
```

3. Flag orphan streams (no linked capability, process, or goal) in red.

**With `--capabilities`:**
1. For each stream, list all linked CAP-NNN capabilities.
2. Flag capabilities that enable a stream but lack formal linkage.

**With `--processes`:**
1. For each stream, list all linked PROC-NNN processes.
2. Flag processes that participate in a stream but lack formal linkage.

**With `--goals`:**
1. For each stream, expand the `linkedGoals` IDs into their statements and show the upstream/downstream chain.

---

## Mode: `generate`

Invoked as: `/ea-valuestreams generate`

1. Read `engagement.json → valueStreams[]`.
2. If the register file exists at `artifacts/cross-cutting/operations/value-streams-register.md`, archive the current version to `artifacts/cross-cutting/operations/snapshots/value-streams-register-{YYYY-MM-DD-HHMM}.md`.
3. Render a new register from `templates/cross-cutting/operations/value-streams-register.md`, substituting placeholders from `engagement.json`.
4. Write the new file to `artifacts/cross-cutting/operations/value-streams-register.md`.
5. Ensure an `artifacts[]` entry exists in `engagement.json` for `value-streams-register.md` (artifactId: `value-streams-register`, phase: `cross-cutting`, status: `Draft` or existing).
6. Confirm: `"Regenerated Value Streams Register: {N} stream(s), {N} orphan(s), snapshot archived."`
