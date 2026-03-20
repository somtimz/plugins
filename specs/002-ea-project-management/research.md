# Research: EA Project Management

**Feature**: 002-ea-project-management
**Date**: 2026-03-20

## R1: Engagement Status Lifecycle

**Decision**: Four valid engagement statuses: Active, On Hold, Planning, Completed.

**Rationale**: These four states cover the full engagement lifecycle. "Active" is the working state, "Planning" is pre-kickoff, "On Hold" is paused, and "Completed" marks a finished engagement. This aligns with common project management patterns and provides clear portfolio filtering.

**State transitions** (all transitions are valid — no restrictions):
- Planning → Active (engagement kicks off)
- Active → On Hold (engagement paused)
- Active → Completed (engagement finished)
- On Hold → Active (engagement resumed)
- On Hold → Completed (engagement closed while paused)
- Any → Planning (reset to pre-kickoff)

**Alternatives considered**:
- Three states (no Completed): Rejected in clarification — architects need a way to mark finished engagements.
- Five states (add Archived): Rejected — archive is a physical action (directory move), not a status value. An archived engagement retains its last status.

## R2: Archive vs Delete Semantics

**Decision**: Archive moves engagement to `EA-projects/.archive/{slug}/`. Delete permanently removes the directory.

**Rationale**: Archive is a non-destructive operation that preserves the engagement for future reference while removing it from the active view. Delete is destructive and requires slug confirmation to prevent accidental data loss. This two-tier approach follows standard portfolio management patterns.

**Archive behavior**:
- Moves `EA-projects/{slug}/` → `EA-projects/.archive/{slug}/`
- Creates `.archive/` directory if it doesn't exist
- Engagement retains its status (e.g., "Completed") in `engagement.json`
- Not visible in default `/ea-status` or `/ea-open` views
- Visible in `/ea-status` when "show archived" option is selected
- Can be restored (moved back to `EA-projects/`)

**Delete behavior**:
- Permanently removes the engagement directory
- Requires typing the slug to confirm (safety measure)
- Available from `/ea-open` next actions for both active and archived engagements
- Warning displayed before confirmation prompt

**Alternatives considered**:
- Soft delete via status flag: Rejected — moving the directory is cleaner and matches the physical directory-per-engagement model.
- Delete only (no archive): Rejected in clarification — users want a non-destructive option for completed engagements.

## R3: Edit Flow Design within /ea-open

**Decision**: All editing flows are accessed through `/ea-open` next actions menu. No separate `/ea-edit` command.

**Rationale**: The user has already selected and loaded a specific engagement when they see the next actions menu. Adding edit options here is natural — the context is established. A separate command would be redundant.

**Edit action categories in next actions menu**:
1. **Edit metadata** — prompts for field to edit, then new value, then confirms
2. **Edit phase status** — shows phase list, select phase, select new status, confirms
3. **Edit artifact status** — shows artifact list, select artifact, select new status/review status, confirms
4. **Archive engagement** — confirms, then moves to `.archive/`
5. **Delete engagement** — warns, requires slug confirmation, then removes

**Alternatives considered**:
- Separate `/ea-edit` command: Rejected in clarification — consolidating in `/ea-open` avoids command proliferation.
- Edit in both `/ea-open` and `/ea-status`: Rejected — `/ea-status` is a read-only dashboard; edit requires an engagement to be "open" in context.

## R4: Legacy Engagement Backward Compatibility

**Decision**: All commands apply sensible defaults for missing v0.2.0 fields and upgrade schema in-place when editing.

**Rationale**: Engagements created before v0.2.0 lack `engagementType`, `architectureDomains`, and `targetEndDate`. Rather than requiring migration, commands gracefully handle missing fields.

**Default values for missing fields**:
- `engagementType`: Display as "—" in dashboards; treat as `null` internally
- `architectureDomains`: Default to all four domains `["Business", "Data", "Application", "Technology"]`
- `targetEndDate`: Display as "—" in dashboards; treat as `null` internally

**In-place upgrade**: When a user edits any field on a legacy engagement, the system adds all missing v0.2.0 fields with defaults before saving, effectively upgrading the schema.

## R5: Dashboard Phase Progress Calculation

**Decision**: Phase progress excludes "Not Applicable" phases from both the total and the completed count.

**Rationale**: Including N/A phases in progress calculation would inflate completion percentages and misrepresent actual progress. An Assessment-only engagement with 3 applicable phases all complete should show 100%, not 27% (3/11).

**Progress formula**: `completed_phases / (total_phases - not_applicable_phases)`

**Display indicators**:
- ✅ Complete
- 🔄 In Progress
- ⏸ On Hold
- ⬜ Not Started
- ➖ Not Applicable (distinct from incomplete)
