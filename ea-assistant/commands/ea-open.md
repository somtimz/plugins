---
name: ea-open
description: Open or switch between EA engagements
argument-hint: "[engagement-name-or-slug]"
allowed-tools: [Read, Write, Bash]
---

Display a picklist of all EA engagements, open the selected one with full details, and offer management actions.

## Instructions

1. **Scan for engagements.** Find all `EA-projects/*/engagement.json` files. The glob pattern `EA-projects/*/` excludes dotdirs like `.archive/`, so archived engagements are not included. If no engagements exist, inform the user and offer to run `/ea-new`.

2. **Build a picklist table** from all found engagements:

   ```
   #  | Name                          | Type            | Domains | Phase   | Status    | Last Modified
   ---|-------------------------------|-----------------|---------|---------|-----------|---------------
   1  | Acme Retail Transformation    | Greenfield      | 4       | Phase B | Active    | 2026-03-10
   2  | Finance Modernisation 2026    | Assessment-only | 2       | Phase A | On Hold   | 2026-02-28
   3  | Group IT Strategy             | Migration       | 4       | Phase A | Active    | 2026-03-12
   ```

   **Backward compatibility**: If `engagementType` is missing or null, display "—" in the Type column. If `architectureDomains` is missing, display "4" (default all four). If two engagements have the same display name, include slugs to disambiguate.

3. **Handle inline argument.** If an argument was provided, try to match it against engagement names or slugs directly. If a match is found, open it without showing the picklist. If no match, show the picklist.

4. **Ask the user to select** an engagement by number.

5. **Load and display the selected engagement.** Read `engagement.json` and display the full summary:

   ```markdown
   ✅ Opened: {name}
   📁 Folder: EA-projects/{slug}/

   ## Engagement Details

   | Field | Value |
   |-------|-------|
   | Name | {name} |
   | Slug | {slug} |
   | Type | {engagementType or "—"} |
   | Domains | {comma-separated domains} |
   | Sponsor | {sponsor} |
   | Organisation | {organisation} |
   | Scope | {scope} |
   | Start Date | {startDate} |
   | Target End Date | {targetEndDate or "—"} |
   | Status | {status} |

   ## ADM Phase Progress

   | Phase | Name | Status |
   |-------|------|--------|
   | Prelim | Preliminary | {status indicator} |
   | Requirements | Architecture Requirements | {status indicator} |
   | A | Architecture Vision | {status indicator} |
   | B | Business Architecture | {status indicator} |
   | C-Data | Data Architecture | {status indicator} |
   | C-App | Application Architecture | {status indicator} |
   | D | Technology Architecture | {status indicator} |
   | E | Opportunities & Solutions | {status indicator} |
   | F | Migration Planning | {status indicator} |
   | G | Implementation Governance | {status indicator} |
   | H | Architecture Change Management | {status indicator} |

   ## Artifacts ({total} total)

   | Artifact | Phase | Status | Review |
   |----------|-------|--------|--------|
   | {name} | {phase} | {status} | {reviewStatus} |
   ```

   Use phase status indicators: ✅ Complete, 🔄 In Progress, ⏸ On Hold, ⬜ Not Started, ➖ Not Applicable.

   For each artifact, check if the artifact file exists on disk. If the file referenced in `engagement.json` is missing, show "File Missing" in the Status column as a warning.

   If no artifacts exist, display "No artifacts yet."

6. **Store the active engagement** slug in the conversation context for subsequent commands.

7. **Update version tracking fields** in `engagement.json`:
   - Set `pluginVersion` to the current plugin version (read from `.claude-plugin/plugin.json`).
   - If `pluginVersion` was absent (legacy engagement), add it now.
   - Do NOT modify `lastMigratedVersion` — that is only updated by `/ea-migrate`.
   - Update `lastModified` to now.

8. **Alignment check** — after refreshing CLAUDE.md, run a lightweight gap scan (no files modified):

   a. Compare `engagement.json → lastMigratedVersion` (or `"0.0.0"` if absent) against the current plugin version.
   b. Count the following quickly detectable gaps:
      - `taxonomy:` block absent on any artifact file in `artifacts/` (check frontmatter only — do not read full file)
      - `templateVersion:` field absent on any artifact
      - Appendix A4 section absent from any artifact that should have it
      - Expected Preliminary artifacts missing: Engagement Charter
   c. If **no gaps found** → display nothing (silent pass).
   d. If **gaps found** → append a single notice to the engagement summary (do not interrupt the next actions menu):

      ```
      ⚠️ Alignment notice — {N} gap(s) detected since ea-assistant v{lastMigratedVersion or "initial"}.
         Run /ea-migrate to review and align this engagement with v{current_version} standards.
         (Use /ea-migrate --report to preview changes without applying them.)
      ```

   **This step makes no changes to any file.** It is a read-only scan.

7b. **Refresh `EA-projects/{slug}/CLAUDE.md`** using the full template defined in `/ea-new`. Populate all sections from current `engagement.json` state:
   - **Engagement Identity** — name, slug, type, organisation, sponsor, scope, phase, status, domains, dates
   - **Strategic Intent** — Vision, Mission, Business Drivers (DRV-NNN), Goals (G-NNN), Objectives (OBJ-NNN), Strategies (STR-NNN), Issues (ISS-NNN) from `engagement.json → direction`; write "Not captured yet." for any empty field — never omit a section
   - **Artifact Status** — list all artifacts with phase, status, and reviewStatus
   - **Phase Progress** — list phases that are In Progress, Complete, or On Hold (skip Not Started / Not Applicable)
   - **Open Decisions** — scan each artifact file's Appendix A3 Decision Log for rows with state Provisional or Awaiting; list with artifact name, description, state, and owner
   - **Quick Commands** — always include, with currentPhase substituted

   If the file does not exist (legacy engagement created before this feature), create it now.

7c. **Ensure ResearchAndReferences folder exists** — check for `EA-projects/{slug}/ResearchAndReferences/`. If missing (legacy engagement), create it and seed `ResearchAndReferences/research-index.md` using the same template as `/ea-new` (with current slug and name, today's date, empty item table). This is silent — do not notify the user.

7. **Offer next actions:**

   ```
   ## Next Actions

    1. Continue current phase ({currentPhase} — {phase name})
    2. View artifacts (/ea-artifact)
    3. Start an interview (/ea-interview)
    4. Research & References ({N items} — /ea-research)
    5. View detailed status
    6. Edit engagement metadata
    7. Edit phase status
    8. Edit artifact status
    9. Archive engagement
   10. Delete engagement
   11. Review & align this engagement (/ea-engage-review)
   ```

   For option 4, show the count of items in `ResearchAndReferences/research-index.md` (count rows in the Items table). If the index is empty or missing, show "0 items".

### Action: Research & References (option 4)

Invoke `/ea-research` for the active engagement.

---

### Action: Review & Align Engagement (option 11)

Invoke `/ea-engage-review` for the active engagement. This runs the full-scope consistency, alignment, governance, and quality review and produces the Engagement Review Report.

---

### Action: View Detailed Status (option 5)

Display a single-engagement status view using the same format as `/ea-status`: engagement type, domains, current phase, artifact counts by status, ADM progress line with indicators, dates, and last modified.

### Action: Edit Engagement Metadata (option 6)

1. Display the list of editable fields:

   ```
   Which field would you like to edit?

   1. Name (display only — slug unchanged)
   2. Description
   3. Sponsor
   4. Organisation
   5. Scope
   6. Status (Active / On Hold / Planning / Completed)
   7. Start Date
   8. Target End Date
   ```

   **Note**: `engagementType` and `architectureDomains` are NOT editable after creation. Changing these would invalidate phase applicability and scaffolded artifacts. If the user asks to edit these, inform them to create a new engagement instead.

2. After the user selects a field, show the current value and prompt for a new value.

3. **Validate** the new value:
   - **Name**: Must not be empty. Warn that slug and directory will NOT change.
   - **Status**: Must be one of: Active, On Hold, Planning, Completed.
   - **Start Date / Target End Date**: Must be valid ISO 8601 date (YYYY-MM-DD) or empty/null for target end date.
   - **Other text fields**: Accept any non-empty value.

4. If invalid, reject and re-prompt with valid options.

5. Write the updated value to `engagement.json`. Update `lastModified` to now.

6. **Legacy engagement upgrade**: If the engagement is missing v0.2.0 fields (`engagementType`, `architectureDomains`, `targetEndDate`), add them with defaults (null, all four domains, null) before saving.

7. Confirm: "Updated: {field} → '{new value}'. engagement.json saved."

### Action: Edit Phase Status (option 7)

1. Display all 11 phases with their current status in a numbered table:

   ```
   Select a phase to update:

   | # | Phase | Current Status |
   |---|-------|---------------|
   | 1 | Prelim | Complete |
   | 2 | Requirements | Complete |
   | 3 | A | In Progress |
   | ... | ... | ... |
   ```

2. After the user selects a phase, show current status and offer valid new statuses: Not Started, In Progress, Complete, On Hold.

3. **"Not Applicable" override**: If the selected phase has status "Not Applicable", warn: "This phase was set to Not Applicable based on engagement type ({engagementType}) and domain selection. Changing it may create inconsistencies. Are you sure?" Require explicit confirmation before proceeding.

4. **Apply state transition rules** (from SKILL.md Phase Status State Transitions):
   - Transitioning to **In Progress** for the first time: set `startedAt` to now.
   - Transitioning to **In Progress** from On Hold: preserve existing `startedAt`.
   - Transitioning to **Complete**: set `completedAt` to now.
   - Transitioning from **Complete** to In Progress: clear `completedAt`, preserve `startedAt`.
   - Transitioning to **Not Started**: reset both `startedAt` and `completedAt` to null.

5. Update `lastModified` in `engagement.json`.

6. Confirm: "Updated: Phase {phase} → '{new status}'."

7. **Suggest advancement**: If the phase was marked Complete, suggest advancing `currentPhase` to the next applicable (non-N/A) phase in sequence. If the user accepts, update `currentPhase` in `engagement.json`.

### Action: Edit Artifact Status (option 8)

1. Display all artifacts in a numbered table:

   ```
   Select an artifact to update:

   | # | Artifact | Phase | Status | Review |
   |---|----------|-------|--------|--------|
   | 1 | Architecture Principles | Prelim | Approved | Approved |
   | 2 | Stakeholder Map | Prelim | Draft | Not Reviewed |
   | ... | ... | ... | ... | ... |
   ```

   For each artifact, check if the file exists on disk. If missing, show "File Missing" warning.

2. After the user selects an artifact, ask what to update:
   - **Status**: Draft / In Review / Approved / Needs Revision
   - **Review Status**: Not Reviewed / In Review / Approved / Needs Revision

3. Validate the selected value against allowed options.

4. Update the artifact entry in the `artifacts` array in `engagement.json`. Set the artifact's `lastModified` to now. Update the engagement-level `lastModified` to now.

5. Confirm: "Updated: {artifact name} {field} → '{new value}'."

### Action: Archive Engagement (option 9)

1. Display confirmation:

   ```
   ⚠️ Archive "{name}"?

   This will move the engagement to EA-projects/.archive/{slug}/
   It will no longer appear in /ea-status or /ea-open.
   You can restore it later.

   Confirm? (yes/no)
   ```

2. If confirmed:
   - Create `EA-projects/.archive/` if it doesn't exist.
   - Move `EA-projects/{slug}/` to `EA-projects/.archive/{slug}/`.
   - Confirm: "Archived: {name}. Moved to EA-projects/.archive/{slug}/."
   - Clear the active engagement from conversation context.

3. If declined, return to next actions menu.

### Action: Delete Engagement (option 10)

1. Display warning:

   ```
   ⚠️ DELETE "{name}"?

   This will PERMANENTLY remove:
     EA-projects/{slug}/
     Including all artifacts, interviews, diagrams, and engagement data.

   This action cannot be undone.

   Type the engagement slug to confirm: {slug}
   ```

2. If the user types the correct slug:
   - Remove the engagement directory entirely.
   - Confirm: "Deleted: {name}. Directory removed."
   - Clear the active engagement from conversation context.

3. If the slug doesn't match, cancel the deletion and return to next actions menu.
