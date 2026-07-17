---
name: ea-meta
description: View the full engagement.json record and edit engagement metadata in one place
argument-hint: "[view|edit|raw] [field|key]"
allowed-tools: [Read, Write, Bash, Glob]
---

You are executing the `/ea-meta` command.

## Overview

`/ea-meta` is the single place to **see** the complete `engagement.json` and to
**manage** its plain metadata. It does not re-implement register editing — direction
items, metrics, finance, artifacts, phases, and opt-outs are owned by their dedicated
commands, and this command routes you to them.

**Modes:**

| Args | Mode | What it does |
|---|---|---|
| (none) / `view` | View | Full grouped, read-only overview of `engagement.json`, then a footer menu |
| `edit [field]` | Edit | Edit a plain metadata field (interactive picker, or `set <field> to <value>`) |
| `raw [key]` | Raw | Pretty-print `engagement.json` (or a single top-level `key`) in a JSON block |

All View and Raw output is read-only. Edit is the **authoritative editor** for plain
metadata fields.

---

## Step 1 — Resolve Active Engagement

> Resolve the active engagement per `skills/ea-engagement-lifecycle/references/engagement-resolution.md`.

Read the resolved `EA-projects/{slug}/engagement.json`. If it cannot be read, display
the error and stop.

---

## Step 2 — Mode Dispatch

Parse the argument and route:

- no argument or `view` → **View Mode**
- `edit` (optionally followed by a field name or `set <field> to <value>`) → **Edit Mode**
- `raw` (optionally followed by a top-level key) → **Raw Mode**
- anything else → display `Unknown mode "{arg}". Valid: view, edit, raw.` and stop.

---

## View Mode

Render the following groups from `engagement.json`. Show `(not set)` for missing or
empty scalar fields. Each group that is owned by another command ends with a
`→ managed by …` pointer.

**1. Identity**
```
Identity — {slug}

  name          {name}
  slug          {slug}            (read-only — fixed at creation)
  description   {description}
  sponsor       {sponsor}
  organisation  {organisation}
  scope         {scope}
```

**2. Classification**
```
Classification

  engagementType       {engagementType or "(not set)"}
  architectureLevel    {architectureLevel or "Segment (default)"}
  architectureDomains  {comma-joined domains}    (read-only after creation)
  status               {status}
```

**3. Timeline**
```
Timeline

  startDate      {startDate}
  targetEndDate  {targetEndDate or "(not set)"}
  currentPhase   {currentPhase}        → managed by /ea-phase
  lastModified   {lastModified}
```

**4. Execution — Phases**

Render all 11 phases in order (Prelim, Requirements, A, B, C-Data, C-App, D, E, F, G, H)
with status indicators. Legend: ✅ Complete | 🔄 In Progress | ⏸ On Hold | ⬜ Not Started | ➖ Not Applicable
```
Phases   ⬜ ⬜ ✅ 🔄 ⬜ ⬜ ⬜ ⬜ ⬜ ⬜ ⬜
         → managed by /ea-phase
```

**5. Direction**

Show whether `vision` and `mission` are set, then a count for each `direction` array
with its managing command:
```
Direction

  vision        {set / (not set)}
  mission       {set / (not set)}

  drivers        {N}   → /ea-drivers
  goals          {N}   → /ea-goals
  objectives     {N}   → /ea-objectives
  strategies     {N}   → /ea-strategies
  issues         {N}   → /ea-issues
  problems       {N}   → /ea-problems
  opportunities  {N}   → /ea-objectives (opportunities)
  gaps           {N}   → /ea-gaps
  policies       {N}   → /ea-policies
  rules             {N}   → /ea-rules
  services          {N}   → /ea-services
  valueStreams      {N}   → /ea-valuestreams
  businessProcesses {N}   → /ea-processes
  useCases          {N}   → /ea-usecases
```

**6. Metrics & Finance**
```
Metrics & Finance

  metrics   {N}   (captured via interview)
  finance   {N}   → /ea-finance
```

**7. Artifacts**

Count `artifacts[]` by `status` (Draft / In Review / Approved / Needs Revision):
```
Artifacts ({total})

  Draft {n} · In Review {n} · Approved {n} · Needs Revision {n}
  → /ea-artifact · status edits via /ea-open
```

**8. Linking & Repository**
```
Linking & Repository

  repoPath               {repoPath or "(not set)"}              (editable)
  requirementsRepoPath   {requirementsRepoPath or "(not set)"}  (editable)
  constraintsRepoPath    {constraintsRepoPath or "(not set)"}   (editable)
  adoptedRAs             {comma-joined IDs or "(none)"}         → /ea-refarch
  localRA.nextId         {n or "(not set)"}                     (read-only)
```

**9. System & Migration** (read-only)
```
System & Migration

  pluginVersion        {pluginVersion or "(not set)"}
  lastMigratedVersion  {lastMigratedVersion or "(not set)"}     → /ea-migrate
  schemaVersion        {schemaVersion}
  last migration       {migrations[-1].date} {from}→{to}  (or "(none)")
  optOuts              {N}                                       → /ea-config optouts
```

**Footer menu** — after the overview, unless invoked with an explicit mode, offer:
```
Type `edit` to change a metadata field, `raw` to view the JSON,
or press Enter to exit.

Register data (goals, finance, phases, artifacts, opt-outs) is managed by the
commands shown beside each group above.
```
- `edit` → Edit Mode
- `raw` → Raw Mode
- Enter → exit

---

## Edit Mode

The authoritative editor for plain metadata. **Editable fields** (with validation):

| Field | Validation |
|---|---|
| `name` | Non-empty. Warn: slug and directory do **not** change. |
| `description` | Any text |
| `sponsor` | Any text |
| `organisation` | Any text |
| `scope` | Any text |
| `vision` | Any text (written to `direction.vision`) |
| `mission` | Any text (written to `direction.mission`) |
| `status` | `Active` \| `On Hold` \| `Planning` \| `Completed` \| `Archived` |
| `architectureLevel` | `Strategic` \| `Segment` \| `Capability` \| `Solution` |
| `engagementType` | `Greenfield` \| `Brownfield` \| `Assessment-only` \| `Migration` — **see warning below** |
| `startDate` | `YYYY-MM-DD` |
| `targetEndDate` | `YYYY-MM-DD`, or empty to clear (sets `null`) |
| `repoPath` | Filesystem path, or empty to clear |
| `requirementsRepoPath` | Filesystem path, or empty to clear |
| `constraintsRepoPath` | Filesystem path, or empty to clear |

**engagementType warning** — before applying a change to `engagementType`, warn:
```
⚠️ Changing engagementType does not re-scaffold phases or artifacts. Phase
   applicability and any opt-outs derived from the original type are NOT
   recalculated. Change only to correct a mistake. Proceed? (y/n)
```
Apply only on `y`.

**Read-only fields** — if the user asks to edit any of these, refuse and route them:

| Field | Route |
|---|---|
| `slug` | Fixed at creation — create a new engagement to change it. |
| `architectureDomains` | Not editable — would invalidate phase applicability. Create a new engagement. |
| `currentPhase`, `phases` | `/ea-phase` |
| `artifacts` | `/ea-artifact` (or status edits via `/ea-open`) |
| `drivers`, `goals`, `objectives`, `strategies`, `issues`, `problems`, `opportunities` | `/ea-{register}` |
| `gaps` | `/ea-gaps` |
| `policies` | `/ea-policies` |
| `rules` | `/ea-rules` |
| `services` | `/ea-services` |
| `valueStreams` | `/ea-valuestreams` |
| `businessProcesses` | `/ea-processes` |
| `useCases` | `/ea-usecases` |
| `metrics` | captured via `/ea-interview` |
| `finance` | `/ea-finance` |
| `optOuts` | `/ea-config optouts` |
| `adoptedRAs`, `localRA` | `/ea-refarch` |
| `pluginVersion`, `lastMigratedVersion`, `schemaVersion`, `migrations` | system-managed (`/ea-open`, `/ea-migrate`) |

**Flow:**

1. If invoked as `edit set <field> to <value>`, go straight to step 4 with that field/value.
   If invoked as `edit <field>`, preselect that field and go to step 3. Otherwise show
   the editable-field list and ask which to edit (step 2).

2. Display the editable fields with current values; ask the user to pick one (or accept
   `set <field> to <value>` directly).

3. Show the current value and prompt for the new value.

4. **Validate** per the table. If the field is read-only, refuse with its route and
   return to step 2. If invalid, show the allowed values and re-prompt.

5. For `engagementType`, show the warning and require `y`.

6. **Write** (follow `skills/ea-engagement-lifecycle/references/write-protocol.md`):
   - Re-read `engagement.json` fresh (do not use the in-memory copy).
   - **Legacy upgrade:** if any of `engagementType`, `architectureDomains`,
     `targetEndDate` are absent, add them with defaults (`null`, all four domains,
     `null`) before saving.
   - Update the field (`vision`/`mission` under `direction`; everything else top-level).
     An empty value for `targetEndDate`/`repoPath`/`requirementsRepoPath`/`constraintsRepoPath`
     clears the field (`null` / empty string per existing convention).
   - Set `lastModified` to the current ISO 8601 timestamp (with time component).
   - Write the file.

7. Confirm: `✓ {field} updated → "{new value}". engagement.json saved.`
   Then redisplay the editable fields and re-prompt, or return on empty input.

---

## Raw Mode

1. Re-read `engagement.json`.
2. If a top-level `key` argument was given:
   - If the key exists, print only that key's value in a fenced ```json block.
   - If not, list the available top-level keys and stop.
3. If no key was given, warn that the file may be large, then print the whole file in a
   fenced ```json block.

```
Showing engagement.json{ → {key}}.
(This is the raw source of truth. Edit metadata with `/ea-meta edit`; edit
registers with their owning commands.)
```
