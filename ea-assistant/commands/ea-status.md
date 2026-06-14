---
name: ea-status
description: Show a dashboard of all EA engagements and their progress. Flags --next and --direction provide focused views.
allowed-tools: [Read, Bash, Glob]
---

Display a comprehensive status dashboard for all EA engagements.

## Instructions

1. **Read the plugin version.** Read `.claude-plugin/plugin.json` from the ea-assistant plugin directory and extract the `version` field.

2. **Scan for engagements.** Find all `EA-projects/*/engagement.json` files. The glob pattern `EA-projects/*/` excludes dotdirs like `.archive/`, so archived engagements are not included in the default view. If no engagements exist, display:

   ```
   No EA engagements found.

   Get started by creating your first engagement: /ea-new
   ```

3. **Read each engagement.** For each `engagement.json`, extract:
   - `name`, `status`, `currentPhase`, `lastModified`
   - `engagementType` (display "—" if field is missing or null)
   - `architectureDomains` (default to all four if field is missing)
   - `startDate`, `targetEndDate` (display "—" if missing or null)
   - Count artifacts by status: Draft, In Review, Approved, Needs Revision
   - Each phase status from the `phases` object
   - `optOuts[]` — count entries by type: `question` and `artifact`
   - For each artifact in `artifacts[]`, check the artifact file frontmatter for `complianceNote: accepted-non-standard` — count these as non-standard artifacts
   - Count rows in `ResearchAndReferences/research-index.md` Items table (0 if file missing)
   - Count `ABB-\d{3}` tokens across all artifact `.md` files (0 if none found)
   - Count `SBB-\d{3}` tokens across all artifact `.md` files (0 if none found)
   - Count `STY-\d{3}` tokens across all artifact `.md` files (0 if none found)

   **Backward compatibility**: If `engagementType`, `architectureDomains`, `targetEndDate`, or `optOuts` fields are missing, apply defaults: type = null (display "—"), domains = all four, targetEndDate = null (display "—"), optOuts = [] (display nothing).

4. **Display the dashboard.** For each engagement, show:

   ```
   ═══════════════════════════════════════════════════════════════
   EA ENGAGEMENT DASHBOARD                        ea-assistant v{version}
   ═══════════════════════════════════════════════════════════════

   📁 {name}          [{STATUS}]     {engagementType or "—"}
      Domains       : {comma-separated domains}
      Current Phase : {currentPhase} — {phase name}
      Artifacts     : {total} total ({n} Draft, {n} In Review, {n} Approved, {n} Needs Revision)
      ADM Progress  : Prelim {i} | Req {i} | A {i} | B {i} | C-Data {i} | C-App {i} | D {i} | E {i} | F {i} | G {i} | H {i}
      Dates         : {startDate} → {targetEndDate or "—"}
      Last Modified : {lastModified}
      📚 Research    : {N items in ResearchAndReferences/ — omit this line entirely if 0}
      ⊘ Opt-outs    : {N artifact opt-outs, N question opt-outs — omit this line entirely if optOuts[] is empty}
      ⚠️ Non-standard: {N} artifact(s) accepted as-is — run /ea-review to remediate (omit if none)
      🧱 Blocks      : {N} ABBs, {N} SBBs, {N} Stories — omit this line entirely if all three counts are 0

   [repeat for each engagement]

   ═══════════════════════════════════════════════════════════════
   Total: {n} | Active: {n} | On Hold: {n} | Planning: {n} | Completed: {n}
   ═══════════════════════════════════════════════════════════════
   ```

   **Phase status indicators** — use these symbols for each phase in the ADM Progress line:
   - ✅ Complete
   - 🔄 In Progress
   - ⏸ On Hold
   - ⬜ Not Started
   - ➖ Not Applicable

   **Progress calculation**: Exclude "Not Applicable" phases from both the total and completed count. For example, an Assessment-only engagement with 5 applicable phases (3 complete) shows progress as 3/5, not 3/11.

   If a specific engagement is currently open (active in conversation context), highlight it with a ► marker before its name.

5. **Display portfolio summary.** After all engagements, show the total count and breakdown by engagement status (Active, On Hold, Planning, Completed).

6. **Display legend and options.**

   ```
   Legend: ✅ Complete | 🔄 In Progress | ⏸ On Hold | ⬜ Not Started | ➖ Not Applicable

   Options:
   1. Open an engagement (/ea-open)
   2. Create a new engagement (/ea-new)
   3. Show archived engagements
   {if an engagement is currently open (► marker):}
   4. Review & align active engagement (/ea-engage-review)
   ```

   Option 4 is shown only when an engagement is active in conversation context. Selecting it invokes `/ea-engage-review` for that engagement.

7. **Show archived engagements** (when user selects option 3). Scan `EA-projects/.archive/*/engagement.json` files. If `.archive/` doesn't exist or contains no engagements, display "No archived engagements found." Otherwise display:

   ```
   ───────────────────────────────────────────────────────────────
   ARCHIVED ENGAGEMENTS
   ───────────────────────────────────────────────────────────────

   📦 {name}          [{STATUS}]     {engagementType or "—"}
      Last Modified : {lastModified}

   [repeat for each archived engagement]

   Options:
   1. Restore an archived engagement
   2. Delete an archived engagement
   3. Return to active dashboard
   ```

8. **Restore an archived engagement** (when user selects restore from archived section). Display a numbered list of archived engagements. After user selects one:
   - Check if `EA-projects/{slug}/` already exists. If so, warn: "Cannot restore: an active engagement with slug '{slug}' already exists. Rename or delete the active engagement first." and stop.
   - Move the directory from `EA-projects/.archive/{slug}/` to `EA-projects/{slug}/`.
   - Confirm: "Restored: {name}. Now visible in /ea-status and /ea-open."

9. **Delete an archived engagement** (when user selects delete from archived section). Display a numbered list of archived engagements. After user selects one:
   - Display warning: "DELETE '{name}'? This will PERMANENTLY remove EA-projects/.archive/{slug}/ including all artifacts, interviews, diagrams, and engagement data. This action cannot be undone."
   - Require user to type the engagement slug to confirm.
   - If slug matches, remove the directory. Confirm: "Deleted: {name}."
   - If slug doesn't match, cancel the deletion.

---

## Flag: --next

Suggest the single most valuable next action for the active EA engagement.

**Require active engagement.** Check for `engagement.json` in context. If none, prompt: "No engagement is active. Run `/ea-open` to open one first."

**Read engagement state.** From `engagement.json` extract: `currentPhase`, `artifacts[]` (id, phase, status, reviewStatus, file), `phases[]` (phase, status).

**Apply the Next Step Algorithm** — evaluate conditions in priority order and stop at the first match:

| Priority | Condition | Recommendation |
|---|---|---|
| 1 | Any artifact in `currentPhase` has `reviewStatus: Needs Revision` | Run `/ea-grill {artifact-id}` to address review findings before proceeding |
| 2 | `currentPhase` has blocking gate violations — read `skills/ea-engagement-lifecycle/references/phase-constraints.md` for the phase's Blocking Gates and check against artifact statuses | Run `/ea-consistency` — blocking issues found in {phase} must be resolved |
| 3 | `currentPhase` has artifacts with `status: Draft` — read each draft artifact file and check for unanswered `{{placeholder}}` fields or `⚠️ Not answered` values | Run `/ea-interview {artifact-id}` to complete {N} unanswered fields |
| 4 | `currentPhase` has no artifacts registered yet | Run `/ea-interview start phase {phase}` to start the phase interview, or `/ea-artifact create` to scaffold artifacts manually |
| 5 | All artifacts in `currentPhase` have `status: Approved` or `reviewStatus: Approved` | Run `/ea-engage-review` to confirm phase health, then mark phase complete with `/ea-phase` |
| 6 | No phase has status `In Progress` | Run `/ea-phase {next-phase}` to start the next recommended phase (use the phase order: Prelim → Requirements → A → B → C-Data → C-App → D → E → F → G → H) |
| 7 | Glob `artifacts/cross-cutting/zachman-diagram-*.md` returns no results | Run `/ea-zachman generate` to create the Zachman coverage diagram |
| 8 | No issues found in any of the above | "Engagement looks healthy" |

**Output the recommendation:**

```
## What to do next

**{one sentence explaining why this is the recommended next step}**

→ `{exact command to run}`

Want to do something else? Run `/ea-status` for a full dashboard or `/ea-open` for the full next-actions menu.
```

For priority 8 (no issues):
```
## What to do next

**Engagement looks healthy — no outstanding gaps or blockers detected.**

→ `/ea-status` for a full dashboard

Want to go deeper? Run `/ea-engage-review` for a full health check or `/ea-zachman review` for Zachman coverage.
```

---

## Flag: --direction

Display the Direction Register — Goals, Objectives, Strategies, Opportunities, Issues, and Problems — read from `engagement.json → direction` (the single source of truth), with drift detection against the artifact display tables. This flag can be combined with additional filters:

| Additional argument | Effect |
|---|---|
| *(none)* | Full register — all artifacts, all item types |
| `--domain Business\|Data\|Application\|Technology` | Filter by inferred domain |
| `--quality` | Run quality scan on all parsed items after rendering the register |
| `goals` | Goals table only |
| `objectives` | Objectives table only |
| `strategies` | Strategies table only |
| `opportunities` | Opportunities table only |
| `issues` | Issues table only |
| `problems` | Problems table only |

Arguments are combinable: `/ea-status --direction goals --domain Business`

### Step 1 — Resolve Active Engagement

Check the conversation context for an active engagement slug. If none found, scan `EA-projects/*/engagement.json` (excluding `.archive/`) and ask the user to select one. Load `engagement.json` to confirm the slug and engagement name.

### Step 2 — Read Direction Data

Read `engagement.json → direction` — the single source of truth for direction items:

| Section type | Source array | Fields |
|---|---|---|
| **Goals** | `direction.goals[]` | id, statement, domain, type, priority, status, drivers, rationale |
| **Objectives** | `direction.objectives[]` | id, statement, measure, target, deadline, priority, linkedGoal |
| **Strategies** | `direction.strategies[]` | id, statement, supports, priority |
| **Opportunities** | `direction.opportunities[]` | id, statement, drivers, type, priority, linkedGoals, rationale |
| **Issues** | `direction.issues[]` | id, statement, domain/area, threatensGoals, evidence, raisedBy |
| **Problems** | `direction.problems[]` | id, statement, symptom, blocksObjectives, evidence, raisedBy |

**Domain resolution:** use the item's own `domain` field where present (goals, issues, problems). Items without one (objectives, strategies, opportunities) inherit the domain of their linked goal (`linkedGoal` / first of `supports` / first of `linkedGoals`); if no linked goal, show `—`.

### Step 2b — Drift Detection

The artifact display tables (Architecture Vision §2–§11 and sibling artifacts) are rendered projections of `engagement.json`. Check they have not drifted:

1. List all `*.md` files under `EA-projects/{slug}/artifacts/` recursively, excluding `*.review.md` and `*-register*.md` files.
2. In each file, locate **direction-bearing section tables**: a heading containing "Goals", "Objectives", "Strategies", "Opportunities", "Issues", or "Problems" whose next table has first-cell rows matching the corresponding ID pattern (`G-\d{3}`, `OBJ-\d{3}`, `STR-\d{3}`, `OPP-\d{3}`, `ISS-\d{3}`, `PRB-\d{3}`). Skip `{{...}}` placeholder rows and `G-00N`-style template examples. ID tokens appearing elsewhere (e.g. a Roadmap's "Advances Goals/Objectives" column, A3 notes) are cross-references, not display rows — out of scope here; broken references are surfaced by `/ea-trace`.
3. **Artifact-only IDs** — a row ID present in a display table but absent from the corresponding `direction` array: collect as drift, noting the artifact file.
4. Record, per item in the register, the first artifact whose display table contains its ID — this populates the `Displayed In` column (items not yet rendered in any display table show `—`).

### Step 3 — Apply Filters

Apply `--domain X` and item-type arguments. If filtering yields zero rows, omit that section. If zero rows across all sections, output: "No direction items match the applied filters."

### Step 4 — Render Inline

```
## Direction Register
Engagement: {name}  ·  Date: {YYYY-MM-DD}

### Goals
| ID | Statement | Domain | Drivers | Linked Strategies | Displayed In |
|---|---|---|---|---|---|

### Objectives
| ID | Statement | Domain | Measure | Target | Deadline | Linked Goal | Displayed In |
|---|---|---|---|---|---|---|---|

### Strategies
| ID | Statement | Domain | Supports | Displayed In |
|---|---|---|---|---|

### Opportunities
| ID | Statement | Domain | Type | Priority | Driver(s) | Linked Goals | Displayed In |
|---|---|---|---|---|---|---|---|

### Issues (ISS-NNN) — Strategic Threats
| ID | Statement | Area | Threatens Goal(s) | Evidence | Raised By | Displayed In |
|---|---|---|---|---|---|---|

### Problems (PRB-NNN) — Tactical Blockers
| ID | Statement | Symptom | Blocks Objective(s) | Evidence | Raised By | Displayed In |
|---|---|---|---|---|---|---|

---
{N} goals · {N} objectives · {N} strategies · {N} opportunities · {N} issues · {N} problems (source: engagement.json)
```

A goal's `Linked Strategies` is derived from `direction.strategies[]` where `supports` contains the goal's ID. `Displayed In` is the artifact file recorded in Step 2b, or `—` if the item is not yet rendered in any artifact. Sort rows within each section by ID number. Null/absent fields: show `—`. Do not write any file.

**Drift report** — if Step 2b found artifact-only IDs, append after the footer:

```
⚠️ Drift detected — {N} item(s) appear in artifact tables but not in engagement.json:
  {ID} — {artifact file}
    → import with `/ea-{register} add` (re-enter the item; the register assigns engagement.json mastery)
    → or remove the row from the artifact if it is obsolete
```

If no drift: omit the block entirely.

### Step 5 — Quality Scan (`--quality` only)

Load `skills/ea-engagement-lifecycle/references/grill-direction-quality.md`. Apply all rules to every parsed item. Group and report using the Summary Format from that file. After the report, offer:
```
  1. Open an item for revision   →  /ea-interview start {artifact-name}
  2. Deep-review direction items →  /ea-grill {artifact-name} --skill direction
  3. Continue
```

### Edge Cases

| Scenario | Handling |
|---|---|
| All `direction` arrays empty or missing | "No direction items in engagement.json. Capture them via `/ea-interview start phase A` or the register commands (`/ea-goals add`, `/ea-objectives add`, ...)." Still run Step 2b — artifact-only IDs found with an empty register are all drift |
| No artifacts directory or no `.md` files found | Skip Step 2b; `Displayed In` shows `—` for all items |
| Artifact tables contain only `{{...}}` placeholders | Treat as empty for drift detection |
| Same ID displayed in multiple artifacts | `Displayed In` shows the first occurrence (Architecture Vision takes priority) |
