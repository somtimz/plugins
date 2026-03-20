# Quickstart: EA Project Management

**Feature**: 002-ea-project-management

## Prerequisites

- At least one engagement created via `/ea-new` in `EA-projects/`

## Scenario 1: View Enhanced Dashboard

1. Run `/ea-status`
2. Verify the dashboard shows for each engagement:
   - Engagement type (Greenfield, Brownfield, etc.) and status badge
   - Architecture domains line
   - Current phase with description
   - Artifact counts grouped by status
   - ADM progress bar with ✅ 🔄 ⏸ ⬜ ➖ indicators
   - Start date → Target end date
   - Last modified date
3. Verify the portfolio summary row at the bottom shows total and counts by status
4. Verify "Not Applicable" phases show ➖ (not ⬜)

## Scenario 2: Open Engagement with Full Details

1. Run `/ea-open`
2. Verify the picklist includes Type and Domains columns
3. Select an engagement by number
4. Verify the opened summary includes:
   - Full metadata table (name, slug, type, domains, sponsor, org, scope, dates, status)
   - Phase-by-phase progress table with status indicators
   - Artifact table with status and review status
   - Next actions menu (9 options including edit, archive, delete)

## Scenario 3: Edit Engagement Metadata

1. Run `/ea-open` and select an engagement
2. Select "Edit engagement metadata" from next actions
3. Select "Status" from the field list
4. Change from "Active" to "On Hold"
5. Verify confirmation message shows the change
6. Run `/ea-status` and verify the engagement now shows [ON HOLD]
7. Read `engagement.json` and verify `status` is "On Hold" and `lastModified` is updated

## Scenario 4: Edit Phase Status

1. Run `/ea-open` and select an engagement
2. Select "Edit phase status" from next actions
3. Select a phase (e.g., Phase B)
4. Change status from "Not Started" to "In Progress"
5. Verify `startedAt` is set in `engagement.json`
6. Repeat: change Phase B to "Complete"
7. Verify `completedAt` is set and system suggests advancing `currentPhase`

## Scenario 5: Edit Artifact Status

1. Run `/ea-open` and select an engagement with artifacts
2. Select "Edit artifact status" from next actions
3. Select an artifact from the list
4. Change status from "Draft" to "In Review"
5. Verify change persists in `engagement.json`

## Scenario 6: Archive and Restore

1. Run `/ea-open` and select an engagement
2. Select "Archive engagement" from next actions
3. Confirm the archive
4. Run `/ea-status` — verify the engagement is gone from the active list
5. Select "Show archived engagements" from `/ea-status` options
6. Verify the archived engagement appears in the archived section
7. Select "Restore" for the archived engagement
8. Run `/ea-status` — verify it's back in the active list

## Scenario 7: Delete Engagement

1. Create a test engagement via `/ea-new` (e.g., "Test Delete Engagement")
2. Run `/ea-open` and select the test engagement
3. Select "Delete engagement" from next actions
4. Verify warning message and slug confirmation prompt
5. Type the slug to confirm
6. Verify the directory is removed from `EA-projects/`
7. Run `/ea-status` — verify the engagement is gone

## Scenario 8: Legacy Engagement Compatibility

1. Manually create `EA-projects/legacy-test/engagement.json` without `engagementType`, `architectureDomains`, `targetEndDate` fields
2. Run `/ea-status` — verify it displays with "—" for type and target date, all four domains shown
3. Run `/ea-open` and select the legacy engagement
4. Select "Edit engagement metadata" and change the status
5. Verify `engagement.json` now includes the missing v0.2.0 fields with defaults
