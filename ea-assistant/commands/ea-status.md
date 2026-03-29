---
name: ea-status
description: Show a dashboard of all EA engagements and their progress
allowed-tools: [Read, Bash]
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
