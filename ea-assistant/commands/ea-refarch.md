---
name: ea-refarch
description: Manage Reference Architectures (RA-NNN) in the Architecture Repository or per-engagement. Create, list, show, edit, adopt, and unadopt reusable architectural patterns with ABB/SBB references, key decisions, constraints, and grill checklist integration.
argument-hint: "[new|list|show|edit|adopt|unadopt|status] [RA-NNN] [--local]"
allowed-tools: [Read, Write, Bash]
---

# /ea-refarch — Reference Architecture Register

Uses skill: `ea-architecture-repository` → `references/reference-architecture-schema.md`

`--local` flag: operates on the engagement's `artifacts/cross-cutting/reference-architectures/` instead of the Architecture Repository. Without `--local`, requires a linked Architecture Repository (`repoPath` in `engagement.json` or active session repo via `/ea-repo open`).

---

## Resolve paths

Before executing any mode:
1. Resolve the active engagement: check context for slug; if none, scan `EA-projects/*/engagement.json` and ask.
2. Load `engagement.json` — extract `repoPath`, `adoptedRAs`, `localRA.nextId`.
3. If `--local` flag: set `raRoot = EA-projects/{slug}/artifacts/cross-cutting/reference-architectures/`; set `raIndex = {raRoot}/reference-architecture-index.md`; use `engagement.json → localRA.nextId` for ID allocation.
4. Else: resolve `repoRoot` from `repoPath` or active session repo. If neither is set, error: "No Architecture Repository linked. Run `/ea-repo link <slug>` or use `--local` to work with per-engagement RAs." Set `raRoot = {repoRoot}/reference-library/entries/`; set `raIndex = {repoRoot}/reference-library/reference-architecture-index.md`; use `repo.json → referenceArchitecture.nextId` for ID allocation.

---

## Mode: `new [--local]`

Create a new Reference Architecture entry. For the concept — what an RA is and is not, its boundary conditions, failure modes, and the consistency-vs-freedom stress test — read the **Reference Architecture (RA-NNN)** definition in `skills/ea-artifact-templates/references/ea-concepts.md`; do not restate it. The enriched `ra-entry-template.md` carries `<details>📋 Guidance</details>` per section, so a new RA is interview-able (`/ea-interview`), scorable (`/ea-score`), and grillable (`/ea-grill`) like any authored artifact.

### Steps

1. Ask: **Name** — short descriptive name for this architectural pattern (e.g. "Event-Driven Microservices")
2. Ask: **Domain** — `Business | Data | Application | Technology | Cross-cutting`
3. Ask: **Source** — `internal` (org-defined) or `industry` (derived from an external standard or body)
   - If `industry`: ask "Which body or standard? (e.g. BIAN, AWS Well-Architected, Azure CAF)"
4. Allocate ID:
   - `--local`: read `engagement.json → localRA.nextId`; format as `RA-{nextId:03d}`; increment and write back `localRA.nextId`; update `lastModified`
   - repo: read `{repoRoot}/repo.json → referenceArchitecture.nextId`; format as `RA-{nextId:03d}`; increment and write back; update `repo.json → lastModified`
5. Create `{raRoot}/` directory if it does not exist (local mode only).
6. Write `{raRoot}/RA-NNN.md` from `templates/seeds/ra-entry-template.md`, substituting:
   - `{{id}}` → allocated ID (e.g. `001`)
   - `{{name}}` → user-supplied name
   - `{{domain}}` → user-supplied domain
   - `{{source}}` → `internal` or `industry`
   - `{{date}}` → today's date (YYYY-MM-DD)
   - `{{industryBody}}` → the named body if source is `industry`, else `""`
7. Append a row to `{raIndex}`:
   ```
   | RA-NNN | {name} | {domain} | Draft | 1.0.0 | {source} | {today} |
   ```
8. Report:
   ```
   ✓ RA-NNN created: {name}
   File: {path}/RA-NNN.md
   
   Next: populate the boundary sections that give an RA governance value —
   Mandatory vs Optional Components, Integration Mechanisms, Security Trust
   Boundaries, Data Ownership & Sovereignty, Governance Checkpoints — plus
   Architecture Layers, Key Decisions, Constraints, and the Grill Checklist.
   Use `/ea-interview {raRoot}/RA-NNN.md` to fill it guidance-by-guidance, or
   `/ea-score RA-NNN` to check completeness/quality. Then `/ea-refarch adopt RA-NNN`.
   ```

---

## Mode: `list [--local]`

Show a table of all Reference Architectures.

### Steps

1. Without `--local`: read rows from `{repoRoot}/reference-library/reference-architecture-index.md`.
2. With `--local`: read rows from `EA-projects/{slug}/artifacts/cross-cutting/reference-architectures/reference-architecture-index.md`.
3. If both repo and local RAs exist (repo-linked engagement): show combined table with a **Scope** column (`Repo` or `Local`).
4. Mark adopted RAs (those in `engagement.json → adoptedRAs[]`) with `✓` in an **Adopted** column.
5. Display: `ID | Name | Domain | Status | Version | Source | Scope | Adopted`
6. If no RAs exist: "No Reference Architectures found. Run `/ea-refarch new` to create one."

---

## Mode: `show RA-NNN [--local]`

Render the full content of a Reference Architecture entry.

### Steps

1. Without `--local`: look for `RA-NNN.md` in `{repoRoot}/reference-library/entries/` first; if not found, look in `artifacts/cross-cutting/reference-architectures/`.
2. With `--local`: look only in `artifacts/cross-cutting/reference-architectures/`.
3. If not found: "RA-NNN not found in repo or local reference architectures."
4. Display the full markdown content of `RA-NNN.md`.
5. If RA is in `engagement.json → adoptedRAs[]`, prepend: `✓ This RA is adopted in the current engagement.`

---

## Mode: `edit RA-NNN [--local]`

Guided re-editing of an existing RA entry.

### Steps

1. Resolve and load `RA-NNN.md` (same search order as `show`).
2. Display current frontmatter values. Ask user which fields to change (name, domain, status, source, industryBody). Apply changes.
3. For each markdown section (`## Overview`, `## Architecture Layers`, `## Key Decisions`, `## Constraints`, `## Implied Principles`, `## Adoption Notes`, `## Grill Checklist`): display current content and ask "Update this section? (Y/n)". If yes, accept new content.
4. Update `lastModified` to today.
5. Write updated `RA-NNN.md`.
6. Update the row in `{raIndex}` (Name, Status, Version, Last Modified columns).
7. Report: `✓ RA-NNN updated.`

---

## Mode: `adopt RA-NNN`

Record that this engagement adopts the named Reference Architecture. Surface its ABBs and key decisions as suggestions.

### Steps

1. Resolve `RA-NNN.md` (repo first, then local). If not found: error.
2. If `RA-NNN` is already in `engagement.json → adoptedRAs[]`: "RA-NNN is already adopted in this engagement." Stop.
3. Display RA name and overview. Confirm: "Adopt RA-NNN ({name}) for this engagement? (Y/n)"
4. Add `RA-NNN` to `engagement.json → adoptedRAs[]`. Update `lastModified`.
5. Read `## Architecture Layers` table. For each row where the ABB-NNN cell is non-empty and not a placeholder (`ABB-NNN`), present: "ABB-NNN ({name}) — {role in pattern}. Add to your engagement's ABB register? (Y/n/skip-all)"
   - If all rows are empty or placeholder: skip this step silently.
   - If Y: instruct user to run `/ea-abbs new` for this ABB (do not auto-write — ABBs require engagement context).
   - If skip-all: stop surfacing ABBs.
6. Read `## Key Decisions` table. For each row, present: "Decision: {title} — {rationale summary}. Create a candidate ADR? (Y/n/skip-all)"
   - If Y: instruct user to run `/ea-adrs new` with this title as a starting point.
   - If skip-all: stop surfacing decisions.
7. Report:
   ```
   ✓ RA-NNN adopted: {name}
   
   Adopted RAs: {engagement.json → adoptedRAs[]}
   
   /ea-grill will now check this engagement against the RA's Grill Checklist.
   Run /ea-refarch status to see coverage.
   ```

---

## Mode: `unadopt RA-NNN`

Remove an adopted Reference Architecture from this engagement.

### Steps

1. If `RA-NNN` is not in `engagement.json → adoptedRAs[]`: "RA-NNN is not adopted in this engagement." Stop.
2. Warn: "Removing RA-NNN will also remove its Grill Checklist checks from `/ea-grill`. Continue? (Y/n)"
3. Remove `RA-NNN` from `engagement.json → adoptedRAs[]`. Update `lastModified`.
4. Report: `✓ RA-NNN unadopted. Grill Checklist checks for this RA will no longer run.`

---

## Mode: `status`

Show adopted Reference Architectures and their grill-check coverage for the active engagement.

### Steps

1. Read `engagement.json → adoptedRAs[]`. If empty: "No Reference Architectures adopted. Run `/ea-refarch adopt RA-NNN` to adopt one."
2. For each adopted RA-NNN:
   - Resolve and load `RA-NNN.md`.
   - Count items in `## Grill Checklist`.
   - Display: `RA-NNN | {name} | {domain} | {checklist item count} grill checks`
3. Show summary:
   ```
   Adopted RAs: {count}
   Total grill checks contributed: {sum}
   
   Run /ea-grill to execute all checks including RA grill checklists.
   ```
