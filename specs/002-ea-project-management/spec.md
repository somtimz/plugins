# Feature Specification: EA Project Management

**Feature Branch**: `002-ea-project-management`
**Created**: 2026-03-19
**Status**: Draft
**Input**: User description: "modify ea-open and ea-status so that i can list all existing ea projects, check their status and modify the plan (dates, phases, artifacts, etc) as desired"

## Clarifications

### Session 2026-03-20

- Q: Where does the edit flow live — new command, part of `/ea-open`, or both? → A: Part of `/ea-open` — edit actions offered as "next actions" after opening an engagement.
- Q: Should "Completed" be a valid engagement status? → A: Yes — add "Completed" as fourth valid status (Active, On Hold, Planning, Completed).
- Q: Should users be able to delete or archive engagements? → A: Include both delete and archive capabilities.

## User Scenarios & Testing

### User Story 1 - Enhanced Engagement Dashboard (Priority: P1)

As an enterprise architect, I want to see a comprehensive dashboard of all my EA engagements showing engagement type, architecture domains, phase progress, artifact counts, and key dates so that I can quickly assess the state of my portfolio.

**Why this priority**: The dashboard is the entry point for all project management activities. Without a clear, information-rich overview, the user cannot make informed decisions about which engagement to work on or what needs attention.

**Independent Test**: Run `/ea-status` with 2+ engagements in `EA-projects/`. Verify the dashboard displays engagement type, architecture domains, all ADM phases with correct status indicators (including "Not Applicable" phases), artifact counts by status, start/target end dates, and a portfolio summary row.

**Acceptance Scenarios**:

1. **Given** two or more engagements exist in `EA-projects/`, **When** I run `/ea-status`, **Then** I see a dashboard showing each engagement's name, type, domains, current phase, phase progress bar (with N/A phases distinguished), artifact summary, dates, and status.
2. **Given** one engagement is Assessment-only with only Business and Data domains, **When** I view the dashboard, **Then** phases C-App, D, E, F, G, H show as "N/A" (not as incomplete), and the progress calculation excludes them.
3. **Given** no engagements exist, **When** I run `/ea-status`, **Then** I see a message stating no engagements found with an offer to create one via `/ea-new`.
4. **Given** an engagement was created before v0.2.0 (missing `engagementType`, `architectureDomains`, `targetEndDate`), **When** I view the dashboard, **Then** it displays gracefully using defaults (type: "—", domains: all four, target end date: "—").

---

### User Story 2 - Enhanced Open with Engagement Details (Priority: P1)

As an enterprise architect, I want `/ea-open` to show richer engagement details when opening a project — including engagement type, domains, dates, and full phase breakdown — so that I immediately have full context when switching engagements.

**Why this priority**: Opening an engagement is a frequent action. Showing complete context upfront reduces the need for follow-up commands and makes the workflow more efficient.

**Independent Test**: Run `/ea-open`, select an engagement, and verify the opened summary includes engagement type, architecture domains, start/target dates, full phase-by-phase status list, and artifact details.

**Acceptance Scenarios**:

1. **Given** multiple engagements exist, **When** I run `/ea-open`, **Then** the picklist table shows engagement type and domain count alongside name, phase, status, and last modified.
2. **Given** I select an engagement, **When** it opens, **Then** the summary displays: name, slug, folder path, engagement type, architecture domains, start date, target end date, current phase with description, full phase breakdown (each phase with status), artifact list grouped by status, and next action suggestions.
3. **Given** I provide a slug as argument (`/ea-open acme-retail-2026`), **When** it matches an existing engagement, **Then** it opens directly without showing the picklist.

---

### User Story 3 - Modify Engagement Metadata (Priority: P2)

As an enterprise architect, I want to modify engagement metadata fields (status, target end date, description, sponsor, scope) after creation so that I can keep the engagement information current as the project evolves.

**Why this priority**: Engagement details change over time — sponsors change, dates shift, scopes evolve. The ability to update metadata without recreating the engagement is essential for ongoing project management.

**Independent Test**: Open an engagement, request to edit the target end date and status, confirm the changes are saved to `engagement.json`, and verify the dashboard reflects the updated values.

**Acceptance Scenarios**:

1. **Given** an engagement is open, **When** I request to edit metadata (e.g., "edit target end date"), **Then** the system prompts me for the new value, shows a confirmation of the change, and writes it to `engagement.json` with updated `lastModified`.
2. **Given** I want to change the engagement status from "Active" to "On Hold", **When** I confirm the change, **Then** `engagement.json` status field is updated and the dashboard reflects "On Hold".
3. **Given** I want to change the engagement name, **When** I provide a new name, **Then** the system warns that the slug and directory will NOT change (to avoid breaking references) but updates the display name in `engagement.json`.
4. **Given** I try to set an invalid value (e.g., status = "Cancelled" which is not a valid status), **When** I confirm, **Then** the system rejects the value and re-prompts with valid options (Active, On Hold, Planning, Completed).

---

### User Story 4 - Modify Phase Status (Priority: P2)

As an enterprise architect, I want to manually change the status of any ADM phase (e.g., mark a phase as Complete, put it On Hold, or reset it to Not Started) so that I can reflect the actual progress of the engagement.

**Why this priority**: Phase status tracking is core to ADM lifecycle management. Architects need to manually adjust phases when work is done outside the tool or when plans change.

**Independent Test**: Open an engagement, change Phase B from "Not Started" to "In Progress", verify `engagement.json` updates the phase status and sets `startedAt`. Then mark it "Complete" and verify `completedAt` is set.

**Acceptance Scenarios**:

1. **Given** an engagement is open, **When** I request to change a phase status (e.g., "mark Phase B as In Progress"), **Then** the system updates the phase status in `engagement.json`, sets `startedAt` to now (if transitioning to In Progress for the first time), and confirms the change.
2. **Given** a phase is "In Progress", **When** I mark it as "Complete", **Then** `completedAt` is set to now and the phase shows as complete on the dashboard.
3. **Given** a phase is "Not Applicable", **When** I try to change its status, **Then** the system warns that this phase was excluded based on engagement type/domain selection and asks for confirmation before overriding.
4. **Given** I mark a phase as "Complete", **When** the change is saved, **Then** the system suggests advancing `currentPhase` to the next applicable phase.

---

### User Story 5 - Modify Artifact Metadata (Priority: P3)

As an enterprise architect, I want to view and update artifact metadata (status, review status) from the engagement context so that I can track artifact progress without opening individual files.

**Why this priority**: Artifact tracking is important but less frequent than phase management. It complements the phase workflow by providing granular progress visibility.

**Independent Test**: Open an engagement with scaffolded artifacts, list all artifacts with their statuses, change one artifact's status from "Draft" to "In Review", and verify the change persists in `engagement.json`.

**Acceptance Scenarios**:

1. **Given** an engagement is open with artifacts, **When** I request to list artifacts, **Then** I see a table showing artifact ID, name, phase, file path, status, and review status.
2. **Given** I select an artifact to update, **When** I change its status from "Draft" to "In Review", **Then** `engagement.json` is updated with the new status and `lastModified` timestamp.
3. **Given** I want to update review status, **When** I change it from "Not Reviewed" to "Approved", **Then** both `reviewStatus` and `lastModified` are updated in `engagement.json`.

---

### User Story 6 - Quick Status from Open (Priority: P3)

As an enterprise architect, I want `/ea-open` to offer a "view status" action after opening so that I can check detailed status without running a separate command.

**Why this priority**: Convenience feature that reduces command switching. Lower priority because `/ea-status` already provides this information.

**Independent Test**: Open an engagement via `/ea-open`, select "view status" from the offered actions, and verify the same dashboard-style view appears for just that engagement.

**Acceptance Scenarios**:

1. **Given** an engagement is opened via `/ea-open`, **When** I select "view status" from the next actions menu, **Then** I see a detailed single-engagement status view matching the format from `/ea-status`.

---

### User Story 7 - Archive and Delete Engagements (Priority: P3)

As an enterprise architect, I want to archive completed engagements to declutter my active project list, and delete engagements that were created in error, so that my portfolio stays clean and manageable.

**Why this priority**: Archive and delete are maintenance operations used less frequently than viewing and editing. They are important for long-term portfolio hygiene but not critical for day-to-day workflow.

**Independent Test**: Create a test engagement, archive it via `/ea-open` actions, verify it moves to `EA-projects/.archive/` and no longer appears in `/ea-status`. Then delete an archived engagement and verify the directory is removed entirely.

**Acceptance Scenarios**:

1. **Given** an engagement is open, **When** I select "archive" from the next actions menu, **Then** the system moves the engagement directory from `EA-projects/{slug}/` to `EA-projects/.archive/{slug}/`, and the engagement no longer appears in `/ea-status` or `/ea-open` picklist.
2. **Given** I want to delete an engagement, **When** I select "delete" from the next actions menu, **Then** the system requires typing the engagement slug to confirm, warns that this is irreversible, and upon confirmation removes the engagement directory entirely.
3. **Given** an archived engagement exists in `EA-projects/.archive/`, **When** I run `/ea-status`, **Then** archived engagements are shown in a separate "Archived" section below active engagements (or hidden by default with an option to show them).
4. **Given** I want to restore an archived engagement, **When** I access the archived section and select "restore", **Then** the engagement directory is moved back from `.archive/` to `EA-projects/` and appears in the active list again.

---

### Edge Cases

- What happens when `engagement.json` is malformed or missing required fields? Display a warning, show available fields, and suggest re-creating the engagement.
- What happens when an artifact file referenced in `engagement.json` no longer exists on disk? Show the artifact entry with a "File Missing" warning in the status column.
- What happens when the user tries to modify a field that doesn't exist in a pre-v0.2.0 engagement? Add the field with the provided value (upgrade the schema in-place) and confirm to the user.
- What happens when two engagements have the same display name but different slugs? Display both with their slugs to disambiguate.
- What happens when `EA-projects/` contains directories without `engagement.json`? Skip those directories silently in the scan.
- What happens when archiving and the `.archive/` directory doesn't exist? Create it automatically.
- What happens when restoring an archived engagement and a new engagement with the same slug already exists? Warn the user and block the restore until the conflict is resolved.

## Requirements

### Functional Requirements

- **FR-001**: `/ea-status` MUST display engagement type, architecture domains, and target end date for each engagement.
- **FR-002**: `/ea-status` MUST show ADM phase progress with distinct indicators for Complete, In Progress, On Hold, Not Started, and Not Applicable.
- **FR-003**: `/ea-status` MUST show artifact counts grouped by status (Draft, In Review, Approved, Needs Revision).
- **FR-004**: `/ea-status` MUST display a portfolio summary showing total engagements and counts by status.
- **FR-005**: `/ea-status` MUST handle legacy engagements (pre-v0.2.0) gracefully by applying default values for missing fields.
- **FR-006**: `/ea-open` picklist MUST include engagement type and domain count columns.
- **FR-007**: `/ea-open` summary after opening MUST display full engagement metadata including type, domains, dates, and phase-by-phase breakdown.
- **FR-008**: `/ea-open` MUST offer next actions including: continue current phase, view artifacts, start an interview, view status, edit metadata, edit phase status, and edit artifact status. All editing flows are accessed exclusively through `/ea-open` (no separate edit command).
- **FR-009**: The system MUST allow editing of engagement metadata fields: name (display only), description, sponsor, organisation, scope, status, target end date, and start date.
- **FR-010**: The system MUST validate edited values against allowed engagement status options: Active, On Hold, Planning, Completed.
- **FR-011**: The system MUST allow changing any ADM phase status to: Not Started, In Progress, Complete, On Hold.
- **FR-012**: When a phase transitions to "In Progress" for the first time, the system MUST set `startedAt` to the current timestamp.
- **FR-013**: When a phase transitions to "Complete", the system MUST set `completedAt` to the current timestamp.
- **FR-014**: Overriding a "Not Applicable" phase MUST require explicit user confirmation.
- **FR-015**: The system MUST update `lastModified` in `engagement.json` whenever any field is changed.
- **FR-016**: The system MUST allow viewing and updating artifact status and review status from the engagement context.
- **FR-017**: The system MUST NOT allow renaming the engagement slug or moving the engagement directory (display name only).
- **FR-023**: The system MUST NOT allow editing `engagementType` or `architectureDomains` after creation — changing these would invalidate phase applicability and scaffolded artifacts. Inform the user to create a new engagement if type or domain scope changes.
- **FR-018**: The system MUST allow archiving an engagement by moving its directory to `EA-projects/.archive/{slug}/`.
- **FR-019**: Archived engagements MUST NOT appear in the default `/ea-status` dashboard or `/ea-open` picklist.
- **FR-020**: The system MUST allow restoring an archived engagement back to `EA-projects/{slug}/`.
- **FR-021**: The system MUST allow deleting an engagement permanently, requiring the user to type the engagement slug as confirmation.
- **FR-022**: `/ea-status` MUST offer an option to show archived engagements in a separate section.

### Key Entities

- **Engagement**: The core entity stored in `engagement.json` — contains all metadata, phase statuses, and artifact references. Key attributes: name, slug, engagementType, architectureDomains, status, currentPhase, phases (map of phase → status/dates), artifacts (array), startDate, targetEndDate, lastModified.
- **Phase**: A sub-entity within engagement tracking ADM phase progress. Attributes: status (Not Started/In Progress/Complete/On Hold/Not Applicable), startedAt, completedAt.
- **Artifact**: A sub-entity within engagement tracking deliverable progress. Attributes: id, name, phase, file, reviewFile, status (Draft/In Review/Approved/Needs Revision), reviewStatus, createdAt, lastModified.

## Success Criteria

### Measurable Outcomes

- **SC-001**: An architect can assess the state of all engagements in under 10 seconds by running a single command (`/ea-status`).
- **SC-002**: Opening an engagement provides complete context (type, domains, phases, artifacts, dates) without requiring any follow-up commands.
- **SC-003**: Any engagement metadata field can be updated in 3 or fewer interaction steps (request → value → confirm).
- **SC-004**: Phase status changes are immediately reflected in `engagement.json` and visible in subsequent dashboard/open views.
- **SC-005**: All commands handle legacy engagements (pre-v0.2.0) without errors, applying sensible defaults for missing fields.
- **SC-006**: 100% of editable fields have validation that prevents invalid values from being written to `engagement.json`.
