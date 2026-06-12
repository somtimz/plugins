# Reference Architecture Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Add RA-NNN Reference Architecture support to the ea-assistant plugin — create, manage, and adopt reusable architectural patterns with ABB/SBB references, key decisions, constraints, and grill checklist integration.

**Architecture:** New `RA-NNN` ID prefix; rich markdown entries (mirroring VDR/THR pattern) in `Architecture-Repository/reference-library/entries/` (cross-engagement) and `artifacts/cross-cutting/reference-architectures/` (per-engagement). New `/ea-refarch` command handles all CRUD and adopt/unadopt. Grill and ABB/SBB interview flows hook into `engagement.json → adoptedRAs[]`.

**Tech Stack:** Markdown instruction files, YAML frontmatter, JSON config seeds. Validated with `~/.bun/bin/bun .github/scripts/validate-frontmatter.ts ea-assistant/`.

**Spec:** `docs/superpowers/specs/2026-06-11-reference-architecture-design.md`

---

### Task 1: Add RA-NNN to the ID scheme

**Files:**
- Modify: `CLAUDE.md` (line 166 — ID Scheme table)
- Modify: `templates/seeds/engagement-rules.md` (line 117 — ID list)
- Modify: `skills/ea-engagement-lifecycle/references/engagement-rules-reference.md` (line 125 — ID scheme note)

- [ ] **Step 1: Add RA-NNN row to CLAUDE.md ID Scheme table**

In `CLAUDE.md`, after the `IFC-NNN` row in the ID Scheme table, add:

```markdown
| RA-NNN | Reference Architecture (Architecture Repository) | RA-001 |
```

- [ ] **Step 2: Add RA-NNN to engagement-rules.md ID list**

In `templates/seeds/engagement-rules.md` line 117, change:

```
- Use the unified ID scheme: DRV-NNN, G-NNN, OBJ-NNN, STR-NNN, MET-NNN, ISS-NNN, PRB-NNN, RIS-NNN, ADR-NNN, REQ-NNN, WP-NNN, GAP-NNN, CON-NNN, CST-NNN, ABB-NNN, SBB-NNN, STY-NNN, SVC-NNN, IFC-NNN.
```

to:

```
- Use the unified ID scheme: DRV-NNN, G-NNN, OBJ-NNN, STR-NNN, MET-NNN, ISS-NNN, PRB-NNN, RIS-NNN, ADR-NNN, REQ-NNN, WP-NNN, GAP-NNN, CON-NNN, CST-NNN, ABB-NNN, SBB-NNN, STY-NNN, SVC-NNN, IFC-NNN, RA-NNN.
```

- [ ] **Step 3: Add RA-NNN to engagement-rules-reference.md**

In `skills/ea-engagement-lifecycle/references/engagement-rules-reference.md` line 125, change:

```
- Use the unified ID scheme (DRV-NNN, G-NNN, OBJ-NNN, etc.) — never invent domain-prefixed variants.
```

to:

```
- Use the unified ID scheme (DRV-NNN, G-NNN, OBJ-NNN, RA-NNN, etc.) — never invent domain-prefixed variants.
```

- [ ] **Step 4: Validate frontmatter**

```bash
~/.bun/bin/bun .github/scripts/validate-frontmatter.ts ea-assistant/
```

Expected: no errors.

- [ ] **Step 5: Commit**

```bash
git add ea-assistant/CLAUDE.md ea-assistant/templates/seeds/engagement-rules.md ea-assistant/skills/ea-engagement-lifecycle/references/engagement-rules-reference.md
git commit -m "feat(ea-assistant): add RA-NNN to unified ID scheme"
```

---

### Task 2: Create RA-NNN schema reference file

**Files:**
- Create: `skills/ea-architecture-repository/references/reference-architecture-schema.md`

- [ ] **Step 1: Create the schema reference file**

Write `skills/ea-architecture-repository/references/reference-architecture-schema.md` with this content:

```markdown
# Reference Architecture Schema

## RA-NNN Entry Frontmatter

| Field | Type | Values | Notes |
|---|---|---|---|
| `id` | string | `RA-NNN` (3-digit zero-padded) | Allocated from `repo.json → referenceArchitecture.nextId` (repo-level) or `engagement.json → localRA.nextId` (local) |
| `name` | string | any | Short descriptive name of the pattern |
| `domain` | enum | `Business \| Data \| Application \| Technology \| Cross-cutting` | Primary architecture domain |
| `status` | enum | `Draft \| Approved \| Deprecated` | Lifecycle state |
| `version` | string | semver `MAJOR.MINOR.PATCH` | Start at `1.0.0` |
| `source` | enum | `internal \| industry` | `industry` = derived from a named standard or body (e.g. BIAN, AWS WAF, Azure CAF) |
| `industryBody` | string | any | If `source: industry`, name the issuing body (e.g. "BIAN", "AWS") |
| `linkedSTDs` | array | `STD-NNN` strings | Standards this RA is derived from or aligns to |
| `linkedADRs` | array | `ADR-NNN` strings | ADRs ratified against this RA (populated during engagement adoption) |
| `createdDate` | ISO date | `YYYY-MM-DD` | |
| `lastModified` | ISO date | `YYYY-MM-DD` | Updated on every edit |

## Markdown Sections

| Section | Required | Content |
|---|---|---|
| `## Overview` | yes | 1–3 paragraphs: what the pattern is and when to use it |
| `## Architecture Layers` | yes | Table: Layer \| ABB-NNN \| ABB Name \| Role in Pattern |
| `## Key Decisions` | yes | Table: Decision \| Rationale Summary \| Candidate ADR Title |
| `## Constraints` | yes | Table: Description \| Candidate CST Title \| Flexibility (Mandatory \| Recommended) |
| `## Implied Principles` | yes | Bullet list of BP/DP/AP/TP IDs (if linked to a repo) or free-text principle statements |
| `## Adoption Notes` | yes | What is mandatory vs. flexible; known adaptations for common contexts |
| `## Grill Checklist` | yes | Numbered list of testable statements used by `/ea-grill` when this RA is adopted |

### Grill Checklist format

Each item is a single testable statement in present tense, e.g.:

```
1. All inter-service communication uses the event bus — no direct synchronous DB calls across service boundaries.
2. Each service owns exactly one bounded context — no shared schema between services.
3. Events are named in past tense (OrderPlaced, PaymentReceived) — no imperative commands (ProcessOrder).
```

The grill check passes if the engagement's artifacts are consistent with the statement; it fails (and is reported as a finding) if they contradict it or cannot be verified.

## Scope Labels

`(local)` — displayed in list output when the RA lives in `artifacts/cross-cutting/reference-architectures/` rather than the Architecture Repository. Local RAs are scoped to one engagement and are not shared. If a local and repo RA share the same ID, `/ea-refarch show` resolves the repo entry first; use `/ea-refarch show RA-NNN --local` to force local resolution.

## Storage Paths

| Scope | Path |
|---|---|
| Repo-level | `Architecture-Repository/reference-library/entries/RA-NNN.md` |
| Per-engagement | `artifacts/cross-cutting/reference-architectures/RA-NNN.md` |
| Repo index | `Architecture-Repository/reference-library/reference-architecture-index.md` |
| Engagement index | `artifacts/cross-cutting/reference-architectures/reference-architecture-index.md` |
```

- [ ] **Step 2: Validate frontmatter**

```bash
~/.bun/bin/bun .github/scripts/validate-frontmatter.ts ea-assistant/
```

Expected: no errors (this is a references file, not a skill/command/agent with required frontmatter).

- [ ] **Step 3: Commit**

```bash
git add ea-assistant/skills/ea-architecture-repository/references/reference-architecture-schema.md
git commit -m "feat(ea-assistant): add RA-NNN schema reference"
```

---

### Task 3: Create RA entry template and index stub

**Files:**
- Create: `templates/seeds/ra-entry-template.md`
- Create: `templates/seeds/ra-index.md`

- [ ] **Step 1: Create ra-entry-template.md**

Write `templates/seeds/ra-entry-template.md`:

```markdown
---
id: RA-{{id}}
name: {{name}}
domain: {{domain}}
status: Draft
version: 1.0.0
source: {{source}}
industryBody: ""
linkedSTDs: []
linkedADRs: []
createdDate: {{date}}
lastModified: {{date}}
---

## Overview

<!-- Describe what this architectural pattern is and when to use it. 1–3 paragraphs. -->

## Architecture Layers

| Layer | ABB-NNN | ABB Name | Role in Pattern |
|---|---|---|---|
| | | | |

## Key Decisions

| Decision | Rationale Summary | Candidate ADR Title |
|---|---|---|
| | | |

## Constraints

| Description | Candidate CST Title | Flexibility |
|---|---|---|
| | | Mandatory |

## Implied Principles

- <!-- e.g. AP-001: Loose Coupling -->

## Adoption Notes

<!-- What is mandatory vs. flexible when adopting this RA. Note known adaptations. -->

## Grill Checklist

1. <!-- Testable statement in present tense -->
```

- [ ] **Step 2: Create ra-index.md**

Write `templates/seeds/ra-index.md`:

```markdown
# Reference Architecture Index

| ID | Name | Domain | Status | Version | Source | Last Modified |
|---|---|---|---|---|---|---|
```

- [ ] **Step 3: Commit**

```bash
git add ea-assistant/templates/seeds/ra-entry-template.md ea-assistant/templates/seeds/ra-index.md
git commit -m "feat(ea-assistant): add RA entry template and index stub"
```

---

### Task 4: Update Architecture Repository SKILL.md and repo-schema.md

**Files:**
- Modify: `skills/ea-architecture-repository/SKILL.md`
- Modify: `skills/ea-architecture-repository/references/repo-schema.md`

- [ ] **Step 1: Add Reference Architecture register section to SKILL.md**

In `skills/ea-architecture-repository/SKILL.md`, after the `### Technology Horizon Register (THR-NNN)` section and before `### Enterprise Governance`, add:

```markdown
### Reference Architecture Register (RA-NNN)
Stores reusable architectural patterns shared across engagements:
- Named patterns with ABB/SBB layer catalogues, key decisions, constraints, and implied principles
- Each RA entry: id, name, domain, status (Draft | Approved | Deprecated), source (internal | industry), linkedSTDs, linkedADRs
- `## Grill Checklist` section drives `/ea-grill` RA compliance checks when an engagement adopts the RA
- Stored in: `Architecture-Repository/reference-library/entries/RA-NNN.md`
- Per-engagement local RAs (not shared): `artifacts/cross-cutting/reference-architectures/RA-NNN.md`
- See `references/reference-architecture-schema.md`
```

- [ ] **Step 2: Update workspace structure in SKILL.md**

In `skills/ea-architecture-repository/SKILL.md`, in the `## Workspace Structure` code block, replace:

```
│   └── reference-library/
│       └── abb-catalogue.md
```

with:

```
│   └── reference-library/
│       ├── reference-architecture-index.md
│       ├── entries/                 # RA-NNN.md files
│       └── abb-catalogue.md
```

- [ ] **Step 3: Update Commands table in SKILL.md**

In `skills/ea-architecture-repository/SKILL.md`, in the `## Commands` table, after the `/ea-standards` row add:

```
| `/ea-refarch [new|list|show|edit|adopt|unadopt|status]` | Manage Reference Architecture Register (RA-NNN) |
```

- [ ] **Step 4: Add referenceArchitecture to repo.json in repo-schema.md**

In `skills/ea-architecture-repository/references/repo-schema.md`, in the `## repo.json fields` table, after the `technologyHorizon` row add:

```
| `referenceArchitecture` | object | `{ enabled: bool, indexFile: "reference-library/reference-architecture-index.md", entriesPath: "reference-library/entries/", nextId: 1 }` |
```

Also in the `### nextId counters` section, change:

```
`sib.nextId`, `vendorLandscape.nextId`, and `technologyHorizon.nextId` are integer counters seeded to `1` on init.
```

to:

```
`sib.nextId`, `vendorLandscape.nextId`, `technologyHorizon.nextId`, and `referenceArchitecture.nextId` are integer counters seeded to `1` on init.
```

And update the sentence that follows to include `RA-NNN`:

```
Each time a new entry is created (STD-NNN, VDR-NNN, THR-NNN, RA-NNN), the relevant counter is read, used as the ID, then incremented in `repo.json`.
```

- [ ] **Step 5: Update Directory Structure in repo-schema.md**

In `skills/ea-architecture-repository/references/repo-schema.md`, in the directory structure code block, replace:

```
│   └── reference-library/
│       └── abb-catalogue.md
```

with:

```
│   └── reference-library/
│       ├── reference-architecture-index.md
│       ├── entries/
│       └── abb-catalogue.md
```

- [ ] **Step 6: Validate frontmatter**

```bash
~/.bun/bin/bun .github/scripts/validate-frontmatter.ts ea-assistant/
```

Expected: no errors.

- [ ] **Step 7: Commit**

```bash
git add ea-assistant/skills/ea-architecture-repository/SKILL.md ea-assistant/skills/ea-architecture-repository/references/repo-schema.md
git commit -m "feat(ea-assistant): add RA register to Architecture Repository skill and schema"
```

---

### Task 5: Update /ea-repo command (init + status modes)

**Files:**
- Modify: `commands/ea-repo.md`

- [ ] **Step 1: Update init mode — add reference-library/entries/ directory creation**

In `commands/ea-repo.md`, in the `## Mode: init` section, in the directory creation list (step 3), after:

```
   - `<path>/Architecture-Repository/technology-horizon/entries/`
```

add:

```
   - `<path>/Architecture-Repository/reference-library/entries/`
```

- [ ] **Step 2: Update init mode — add RA index stub write**

In `commands/ea-repo.md`, in step 6 (Write stub files), after the `Architecture-Repository/technology-horizon/horizon-index.md` line add:

```
   - `Architecture-Repository/reference-library/reference-architecture-index.md` — seed from `templates/seeds/ra-index.md`
```

- [ ] **Step 3: Update init mode — add referenceArchitecture block to repo.json seeding**

In `commands/ea-repo.md`, step 5 (Write repo.json), append this instruction after the technologyHorizon block note:

After the `technologyHorizon` block in `repo.json`, seed:

```json
"referenceArchitecture": {
  "enabled": true,
  "indexFile": "reference-library/reference-architecture-index.md",
  "entriesPath": "reference-library/entries/",
  "nextId": 1
}
```

- [ ] **Step 4: Update status mode — add RA count**

In `commands/ea-repo.md`, in the `## Mode: status` section, step 3 (Count entries), after:

```
   - STD entries: count files in `Architecture-Repository/sib/standards/`
```

add:

```
   - RA entries: count files in `Architecture-Repository/reference-library/entries/`
```

In the display block, after the `Standards (SIB)` line add:

```
     Reference Architectures: <n> patterns (RA-NNN)
```

- [ ] **Step 5: Update the next-steps message in init success report**

In `commands/ea-repo.md`, in the init success report block, after `/ea-standards` in the "Now available" list, add:

```
     /ea-refarch    — manage Reference Architecture Register (RA-NNN)
```

- [ ] **Step 6: Validate frontmatter**

```bash
~/.bun/bin/bun .github/scripts/validate-frontmatter.ts ea-assistant/
```

Expected: no errors.

- [ ] **Step 7: Commit**

```bash
git add ea-assistant/commands/ea-repo.md
git commit -m "feat(ea-assistant): update /ea-repo init and status for RA register"
```

---

### Task 6: Update engagement.json seed and /ea-new command

**Files:**
- Modify: `templates/seeds/engagement-json.md`
- Modify: `commands/ea-new.md`

- [ ] **Step 1: Add adoptedRAs and localRA fields to engagement-json.md**

In `templates/seeds/engagement-json.md`, after the `"repoPath": null,` line add:

```json
  "adoptedRAs": [],
  "localRA": { "nextId": 1 },
```

- [ ] **Step 2: Add reference-architectures folder creation to ea-new.md**

In `commands/ea-new.md`, in step 4 (Create the directory structure), in the `cross-cutting/` section of the folder tree, change:

```
   │   └── cross-cutting/
```

to:

```
   │   └── cross-cutting/
   │       └── reference-architectures/
```

- [ ] **Step 3: Document adoptedRAs and localRA seeding in ea-new.md**

In `commands/ea-new.md`, in step 5 (Write engagement.json), at the end of the paragraph describing what gets seeded, add:

```
Set `adoptedRAs` to `[]` and `localRA` to `{ "nextId": 1 }`.
```

- [ ] **Step 4: Validate frontmatter**

```bash
~/.bun/bin/bun .github/scripts/validate-frontmatter.ts ea-assistant/
```

Expected: no errors.

- [ ] **Step 5: Commit**

```bash
git add ea-assistant/templates/seeds/engagement-json.md ea-assistant/commands/ea-new.md
git commit -m "feat(ea-assistant): seed adoptedRAs and localRA in new engagements"
```

---

### Task 7: Create /ea-refarch command

**Files:**
- Create: `commands/ea-refarch.md`

- [ ] **Step 1: Create the command file**

Write `commands/ea-refarch.md` with this content:

````markdown
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
4. Else: resolve `repoRoot` from `repoPath` or active session repo. Set `raRoot = {repoRoot}/reference-library/entries/`; set `raIndex = {repoRoot}/reference-library/reference-architecture-index.md`; use `repo.json → referenceArchitecture.nextId` for ID allocation.

---

## Mode: `new [--local]`

Create a new Reference Architecture entry.

### Steps

1. Ask: **Name** — short descriptive name for this architectural pattern (e.g. "Event-Driven Microservices")
2. Ask: **Domain** — `Business | Data | Application | Technology | Cross-cutting`
3. Ask: **Source** — `internal` (org-defined) or `industry` (derived from an external standard or body)
   - If `industry`: ask "Which body or standard? (e.g. BIAN, AWS Well-Architected, Azure CAF)"
4. Allocate ID:
   - `--local`: read `engagement.json → localRA.nextId`; format as `RA-{nextId:03d}`; increment and write back `localRA.nextId`; update `lastModified`
   - repo: read `{repoRoot}/repo.json → referenceArchitecture.nextId`; format as `RA-{nextId:03d}`; increment and write back; update `repo.json → lastModified`
5. Write `{raRoot}/RA-NNN.md` from `templates/seeds/ra-entry-template.md`, substituting:
   - `{{id}}` → allocated ID (e.g. `001`)
   - `{{name}}` → user-supplied name
   - `{{domain}}` → user-supplied domain
   - `{{source}}` → `internal` or `industry`
   - `{{date}}` → today's date (YYYY-MM-DD)
   - Set `industryBody` to the named body if source is `industry`, else `""`
6. Append a row to `{raIndex}`:
   ```
   | RA-NNN | {name} | {domain} | Draft | 1.0.0 | {source} | {today} |
   ```
7. Create `{raRoot}/` directory if it does not exist (local mode only).
8. Report:
   ```
   ✓ RA-NNN created: {name}
   File: {path}/RA-NNN.md
   
   Next: fill in the sections (Architecture Layers, Key Decisions, Constraints, Grill Checklist)
   then run /ea-refarch adopt RA-NNN to use it in this engagement.
   ```

---

## Mode: `list [--local]`

Show a table of all Reference Architectures.

### Steps

1. Without `--local`: read rows from `{repoRoot}/reference-library/reference-architecture-index.md`.
2. With `--local`: read rows from `artifacts/cross-cutting/reference-architectures/reference-architecture-index.md`.
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
6. Update the row in `{raIndex}` (name, status, version, lastModified columns).
7. Report: `✓ RA-NNN updated.`

---

## Mode: `adopt RA-NNN`

Record that this engagement adopts the named Reference Architecture. Surface its ABBs and key decisions as suggestions.

### Steps

1. Resolve `RA-NNN.md` (repo first, then local). If not found: error.
2. If `RA-NNN` is already in `engagement.json → adoptedRAs[]`: "RA-NNN is already adopted in this engagement." Stop.
3. Display RA name and overview. Confirm: "Adopt RA-NNN ({name}) for this engagement? (Y/n)"
4. Add `RA-NNN` to `engagement.json → adoptedRAs[]`. Update `lastModified`.
5. Read `## Architecture Layers` table. For each row, present: "ABB-NNN ({name}) — {role in pattern}. Add to your engagement's ABB register? (Y/n/skip-all)"
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
````

- [ ] **Step 2: Validate frontmatter**

```bash
~/.bun/bin/bun .github/scripts/validate-frontmatter.ts ea-assistant/
```

Expected: no errors.

- [ ] **Step 3: Commit**

```bash
git add ea-assistant/commands/ea-refarch.md
git commit -m "feat(ea-assistant): add /ea-refarch command"
```

---

### Task 8: Add RA surface hints to /ea-abbs and /ea-sbbs

**Files:**
- Modify: `commands/ea-abbs.md`
- Modify: `commands/ea-sbbs.md`

- [ ] **Step 1: Add RA layer reference to ea-abbs new mode**

In `commands/ea-abbs.md`, find the `## Mode: new` section. After the step that asks for the ABB's domain (or at the start of the `new` interview), add a new step:

```markdown
**RA reference (if adopted RAs exist):**
Before starting the interview, check `engagement.json → adoptedRAs[]`. If non-empty:
- Load each adopted RA's `## Architecture Layers` table.
- If any RA has a row whose `Layer` matches the domain the user is creating an ABB in, display:
  ```
  Reference Architecture hint — {RA-NNN}: {RA name}
  The following ABBs are defined in this RA for the {domain} layer:
  | ABB-NNN | ABB Name | Role in Pattern |
  ...
  ```
  Then ask: "Are you implementing one of these, or defining a new ABB?"
  - If implementing an existing one: pre-fill the Name and Description from the RA row; let user confirm or override.
  - If new: continue with the standard interview.
```

- [ ] **Step 2: Add RA layer reference to ea-sbbs new mode**

In `commands/ea-sbbs.md`, find the `## Mode: new` section. After the step that asks for the SBB's domain or linked ABB, add:

```markdown
**RA reference (if adopted RAs exist):**
Before starting the interview, check `engagement.json → adoptedRAs[]`. If non-empty:
- Load each adopted RA's `## Architecture Layers` table.
- If the ABB the user is implementing (or the domain they specified) matches a row in the RA, display:
  ```
  Reference Architecture hint — {RA-NNN}: {RA name}
  The parent ABB ({ABB-NNN}: {ABB Name}) is defined in this RA.
  Adoption Notes from the RA: {RA → ## Adoption Notes, first paragraph}
  ```
  This is informational — the user proceeds with the normal SBB interview.
```

- [ ] **Step 3: Validate frontmatter**

```bash
~/.bun/bin/bun .github/scripts/validate-frontmatter.ts ea-assistant/
```

Expected: no errors.

- [ ] **Step 4: Commit**

```bash
git add ea-assistant/commands/ea-abbs.md ea-assistant/commands/ea-sbbs.md
git commit -m "feat(ea-assistant): surface adopted RA layer hints in /ea-abbs and /ea-sbbs new mode"
```

---

### Task 9: Add RA grill check block to grill-skills

**Files:**
- Modify: `skills/ea-grill-skills/SKILL.md`

- [ ] **Step 1: Add RA grill check block to artifact mode**

In `skills/ea-grill-skills/SKILL.md`, in `## Mode: artifact`, after the `**Gap Analysis artifact — unpromoted gap check:**` block (around line 327) and before the closing `---` of the artifact mode, add:

```markdown
**Adopted Reference Architecture compliance:**
If `engagement.json → adoptedRAs[]` is non-empty:
- For each RA-NNN in `adoptedRAs[]`:
  1. Resolve `RA-NNN.md` (repo first, then `artifacts/cross-cutting/reference-architectures/`). If not found: warn "⚠ Adopted RA-NNN not found — cannot run its grill checklist."
  2. Read `## Grill Checklist` — extract each numbered item as a testable statement.
  3. For each checklist item: scan the artifact under review (and the engagement's ABB/SBB register if available) for evidence that the statement is satisfied or contradicted.
     - **Satisfied:** evidence found consistent with the statement → pass silently (or list in the final scorecard as ✅).
     - **Contradicted:** evidence found that directly contradicts the statement → flag: "⚠ RA-NNN Grill Check failed: {statement} — found: {contradicting evidence}"
     - **Cannot verify:** insufficient information in the artifact to confirm or deny → flag: "❓ RA-NNN Grill Check unverifiable: {statement} — no evidence found in this artifact"
  4. Summarise at the end of the artifact review:
     ```
     Adopted RA checks (RA-NNN: {name}):
       Passed:      {n}
       Failed:      {n} ⚠
       Unverifiable: {n} ❓
     ```
```

- [ ] **Step 2: Validate frontmatter**

```bash
~/.bun/bin/bun .github/scripts/validate-frontmatter.ts ea-assistant/
```

Expected: no errors.

- [ ] **Step 3: Commit**

```bash
git add ea-assistant/skills/ea-grill-skills/SKILL.md
git commit -m "feat(ea-assistant): add adopted RA grill checklist to artifact review mode"
```

---

### Task 10: Update ea-help, version bump, and docs

**Files:**
- Modify: `commands/ea-help.md`
- Modify: `CLAUDE.md`
- Modify: `.claude-plugin/plugin.json`
- Modify: `../.claude-plugin/marketplace.json`
- Modify: `docs/PRD.md`
- Modify: `README.md`

- [ ] **Step 1: Add /ea-refarch to ea-help.md**

In `commands/ea-help.md`, in the Architecture Repository section of the commands table, after the `/ea-standards` row add:

```markdown
| `/ea-refarch [new\|list\|show\|edit\|adopt\|unadopt\|status]` | Reference Architecture Register — manage RA-NNN patterns with ABB/SBB layer catalogues, key decisions, and grill checklist integration |
```

- [ ] **Step 2: Update CLAUDE.md — version, command count, key entry points**

In `CLAUDE.md`:
- Change `**Current version:** 0.9.60` → `**Current version:** 0.9.61`
- Change `53 commands available` → `54 commands available`
- Add `/ea-refarch` to the Key entry points line

- [ ] **Step 3: Bump plugin.json to 0.9.61**

In `.claude-plugin/plugin.json`, change `"version": "0.9.60"` to `"version": "0.9.61"`.

- [ ] **Step 4: Bump marketplace.json to 0.9.61**

In `../.claude-plugin/marketplace.json`, find the `ea-assistant` entry and change its `"version"` to `"0.9.61"`. Verify the `"description"` matches `plugin.json` exactly.

- [ ] **Step 5: Add feature section to docs/PRD.md**

In `docs/PRD.md`, add a new feature entry for `v0.9.61`:

```markdown
## v0.9.61 — Reference Architecture Register

### Summary
Added RA-NNN Reference Architecture support to the Architecture Repository. Architects can define reusable architectural patterns (with ABB/SBB layer catalogues, key decisions, constraints, and grill checklists) at the org level or per-engagement, then adopt them into engagements to surface building blocks, seed decisions, and drive grill compliance checks.

### New
- `/ea-refarch` command (7 modes: new, list, show, edit, adopt, unadopt, status)
- `RA-NNN` ID prefix added to unified ID scheme
- `referenceArchitecture` register block in `repo.json`
- `adoptedRAs[]` and `localRA.nextId` fields in `engagement.json`
- RA grill checklist integration in `/ea-grill` artifact mode
- RA layer hints surfaced in `/ea-abbs new` and `/ea-sbbs new`

### Modified
- `/ea-repo init` and `status` updated for RA register
- `/ea-new` seeds new engagement fields
```

- [ ] **Step 6: Add /ea-refarch to README.md**

In `README.md`, in the commands table, add `/ea-refarch` to the Architecture Repository section. In the feature bullets, add:

```markdown
- **Reference Architecture Register** — define reusable RA-NNN patterns with ABB/SBB layer catalogues, key decisions, and grill checklist integration; adopt patterns into engagements
```

- [ ] **Step 7: Validate frontmatter**

```bash
~/.bun/bin/bun .github/scripts/validate-frontmatter.ts ea-assistant/
```

Expected: no errors.

- [ ] **Step 8: Verify plugin.json and marketplace.json versions match**

```bash
grep '"version"' /mnt/d/dev/claude-sandbox/plugins/ea-assistant/.claude-plugin/plugin.json
grep -A3 '"ea-assistant"' /mnt/d/dev/claude-sandbox/plugins/.claude-plugin/marketplace.json | grep '"version"'
```

Expected: both show `0.9.61`.

- [ ] **Step 9: Commit**

```bash
git add ea-assistant/commands/ea-help.md ea-assistant/CLAUDE.md ea-assistant/.claude-plugin/plugin.json .claude-plugin/marketplace.json ea-assistant/docs/PRD.md ea-assistant/README.md
git commit -m "feat(ea-assistant): v0.9.61 — Reference Architecture Register"
```

---

## Self-Review

**Spec coverage check:**

| Spec section | Covered by task |
|---|---|
| RA-NNN ID prefix | Task 1 |
| Repo-level storage (`reference-library/entries/`) | Tasks 3, 4, 5 |
| Per-engagement storage (`cross-cutting/reference-architectures/`) | Tasks 3, 6 |
| RA-NNN entry schema (frontmatter + sections) | Tasks 2, 3 |
| `repo.json → referenceArchitecture` block | Tasks 4, 5 |
| `engagement.json → adoptedRAs[]` and `localRA` | Task 6 |
| `/ea-refarch` command (7 modes) | Task 7 |
| Phase C/D interview ABB surface | Task 8 |
| Phase C/D interview ADR seed | Task 7 (adopt mode steps 5–6) |
| `/ea-grill` RA checklist integration | Task 9 |
| `/ea-abbs` and `/ea-sbbs` RA hints | Task 8 |
| `/ea-repo init` and `status` updates | Task 5 |
| ID collision handling (local vs repo) | Task 2 (schema ref) + Task 7 (show mode) |
| Version bump and docs | Task 10 |

All spec sections covered. No gaps.
