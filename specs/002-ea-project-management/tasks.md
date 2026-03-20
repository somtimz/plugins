# Tasks: EA Project Management

**Input**: Design documents from `/specs/002-ea-project-management/`
**Prerequisites**: plan.md (required), spec.md (required), research.md, data-model.md, contracts/

**Tests**: Not requested in feature specification. No test tasks included.

**Organization**: Tasks are grouped by user story to enable independent implementation and testing of each story.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (e.g., US1, US2, US3)
- Include exact file paths in descriptions

## Path Conventions

All paths are relative to `plugins/ea-assistant/`.

---

## Phase 1: Setup

**Purpose**: Read current command files and understand existing content before modification.

- [x] T001 Read current `commands/ea-status.md` and `commands/ea-open.md` to understand existing content before modification
- [x] T002 [P] Read current `skills/ea-engagement-lifecycle/SKILL.md` to understand lifecycle documentation that needs updating

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Update the engagement lifecycle skill with new concepts (Completed status, archive/restore lifecycle, editing workflows) that all user stories depend on.

**CRITICAL**: No user story work can begin until this phase is complete.

- [x] T003 Update `skills/ea-engagement-lifecycle/SKILL.md` to add "Completed" as a fourth valid engagement status value (Active, On Hold, Planning, Completed) with description — note: engagement-level uses "Completed" while phase-level uses "Complete" (distinct concepts, document the distinction)
- [x] T004 Update `skills/ea-engagement-lifecycle/SKILL.md` to document the archive/restore lifecycle: archive moves engagement to `EA-projects/.archive/{slug}/`, restore moves it back, delete permanently removes the directory
- [x] T005 Update `skills/ea-engagement-lifecycle/SKILL.md` to document the editing workflow: all editing flows (metadata, phase status, artifact status) are accessed through `/ea-open` next actions menu after opening an engagement
- [x] T006 Update `skills/ea-engagement-lifecycle/SKILL.md` to document phase status state transitions per data-model.md: Not Started → In Progress (sets startedAt), In Progress → Complete (sets completedAt), Complete → In Progress (clears completedAt), any → Not Started (resets timestamps), Not Applicable → any (requires confirmation)

**Checkpoint**: Lifecycle skill now documents all new concepts. Command updates can begin.

---

## Phase 3: User Story 1 — Enhanced Engagement Dashboard (Priority: P1) MVP

**Goal**: Comprehensive `/ea-status` dashboard showing engagement type, domains, dates, N/A-aware phase progress, artifact counts, and portfolio summary.

**Independent Test**: Run `/ea-status` with 2+ engagements in `EA-projects/`. Verify dashboard displays type, domains, phase progress with ➖ for N/A phases, artifact counts by status, dates, and portfolio summary row.

### Implementation for User Story 1

- [x] T007 [US1] Rewrite `commands/ea-status.md` steps 1-2: ensure scan pattern `EA-projects/*/engagement.json` excludes dotdirs (`.archive/`); for each engagement, read and display engagement type (from `engagementType` field, "—" if missing), architecture domains line, and dates (startDate → targetEndDate, "—" if missing) per contracts/command-interface.md dashboard format
- [x] T008 [US1] Update `commands/ea-status.md` step 3: replace the ADM Progress line to use distinct indicators — ✅ Complete, 🔄 In Progress, ⏸ On Hold, ⬜ Not Started, ➖ Not Applicable — and show all 11 phases (Prelim, Req, A, B, C-Data, C-App, D, E, F, G, H) per contracts/command-interface.md
- [x] T009 [US1] Update `commands/ea-status.md` step 3: add artifact count line showing counts grouped by status (Draft, In Review, Approved, Needs Revision) per FR-003
- [x] T010 [US1] Update `commands/ea-status.md` step 3: add portfolio summary row at bottom showing total engagements and counts by status (Active, On Hold, Planning, Completed) per FR-004 and contracts/command-interface.md
- [x] T011 [US1] Update `commands/ea-status.md` step 1: add backward compatibility handling — when `engagementType`, `architectureDomains`, or `targetEndDate` fields are missing, apply defaults per research.md R4 (type: null/"—", domains: all four, targetEndDate: null/"—")
- [x] T012 [US1] Update `commands/ea-status.md` step 5: replace existing options with: Open an engagement (`/ea-open`), Create a new engagement (`/ea-new`), Show archived engagements — per contracts/command-interface.md

**Checkpoint**: User Story 1 fully functional — enhanced dashboard works end-to-end.

---

## Phase 4: User Story 2 — Enhanced Open with Engagement Details (Priority: P1)

**Goal**: `/ea-open` shows richer picklist with type/domains columns and full engagement details on open including phase-by-phase breakdown and expanded next actions menu.

**Independent Test**: Run `/ea-open`, verify picklist includes Type and Domains columns, select an engagement, verify opened summary shows full metadata table, phase-by-phase status, artifact table, and 9-option next actions menu.

### Implementation for User Story 2

- [x] T013 [US2] Update `commands/ea-open.md` steps 1-2: ensure scan pattern `EA-projects/*/engagement.json` excludes dotdirs (`.archive/`); add Type and Domains columns to the picklist table per contracts/command-interface.md picklist format, with backward compatibility for missing fields
- [x] T014 [US2] Rewrite `commands/ea-open.md` step 5: replace the opened engagement summary with full metadata table (name, slug, type, domains, sponsor, org, scope, dates, status), phase-by-phase progress table with status indicators, and artifact table grouped by status per contracts/command-interface.md opened summary format
- [x] T015 [US2] Update `commands/ea-open.md` step 5: replace the next actions list with 9 options: continue current phase, view artifacts, start an interview, view detailed status, edit metadata, edit phase status, edit artifact status, archive engagement, delete engagement — per FR-008 and contracts/command-interface.md

**Checkpoint**: User Story 2 fully functional — enhanced open with full details works end-to-end.

---

## Phase 5: User Story 3 — Modify Engagement Metadata (Priority: P2)

**Goal**: Edit engagement metadata fields (name, description, sponsor, organisation, scope, status, dates) through `/ea-open` next actions.

**Independent Test**: Open an engagement, select "edit metadata", change status from Active to On Hold, confirm saved to `engagement.json` with updated `lastModified`. Verify dashboard reflects change.

### Implementation for User Story 3

- [x] T016 [US3] Add new step to `commands/ea-open.md`: when user selects "Edit engagement metadata" from next actions, display numbered list of editable fields (name, description, sponsor, organisation, scope, status, start date, target end date) per contracts/command-interface.md edit metadata flow
- [x] T017 [US3] Add edit metadata logic to `commands/ea-open.md`: when user selects a field, show current value, prompt for new value, validate against allowed options (status must be Active/On Hold/Planning/Completed per FR-010, dates must be ISO 8601), and confirm the change
- [x] T018 [US3] Add edit metadata save logic to `commands/ea-open.md`: write updated value to `engagement.json`, update `lastModified` timestamp per FR-015, and if editing a legacy engagement add missing v0.2.0 fields with defaults per research.md R4
- [x] T019 [US3] Add name edit warning to `commands/ea-open.md`: when editing the name field, warn that the slug and directory will NOT change (FR-017), then update display name only

**Checkpoint**: User Story 3 fully functional — metadata editing works for all field types.

---

## Phase 6: User Story 4 — Modify Phase Status (Priority: P2)

**Goal**: Manually change ADM phase statuses with automatic timestamp management and currentPhase advancement suggestions.

**Independent Test**: Open an engagement, select "edit phase status", change Phase B from Not Started to In Progress, verify `startedAt` set. Change to Complete, verify `completedAt` set and system suggests advancing `currentPhase`.

### Implementation for User Story 4

- [x] T020 [US4] Add new step to `commands/ea-open.md`: when user selects "Edit phase status" from next actions, display all 11 phases with current status in a numbered table per contracts/command-interface.md edit phase flow
- [x] T021 [US4] Add phase edit logic to `commands/ea-open.md`: when user selects a phase, show current status, offer valid transitions (Not Started, In Progress, Complete, On Hold), apply state transition rules per data-model.md — set `startedAt` on first In Progress (FR-012), set `completedAt` on Complete (FR-013), reset timestamps on Not Started
- [x] T022 [US4] Add "Not Applicable" override logic to `commands/ea-open.md`: when user selects a phase with status "Not Applicable", warn that this phase was excluded based on engagement type/domain selection, require explicit confirmation before allowing the override per FR-014
- [x] T023 [US4] Add currentPhase advancement suggestion to `commands/ea-open.md`: when a phase is marked Complete, suggest advancing `currentPhase` to the next applicable (non-N/A) phase in sequence, and update `currentPhase` if user accepts

**Checkpoint**: User Story 4 fully functional — phase status editing with timestamps and suggestions works.

---

## Phase 7: User Story 5 — Modify Artifact Metadata (Priority: P3)

**Goal**: View artifact list and update artifact status/review status from the engagement context.

**Independent Test**: Open an engagement with scaffolded artifacts, select "edit artifact status", change an artifact from Draft to In Review, verify change persists in `engagement.json`.

### Implementation for User Story 5

- [x] T024 [US5] Add new step to `commands/ea-open.md`: when user selects "Edit artifact status" from next actions, display all artifacts in a numbered table showing id, name, phase, file path, status, and review status per contracts/command-interface.md edit artifact flow
- [x] T025 [US5] Add artifact edit logic to `commands/ea-open.md`: when user selects an artifact, offer to update status (Draft/In Review/Approved/Needs Revision) or review status (Not Reviewed/In Review/Approved/Needs Revision), validate selection, update `engagement.json` artifacts array entry, and set artifact `lastModified` and engagement `lastModified` per FR-015 and FR-016
- [x] T026 [US5] Add artifact file existence check to `commands/ea-open.md`: when displaying artifacts, check if the artifact file exists on disk; if missing, show "File Missing" warning in the status column per edge case specification

**Checkpoint**: User Story 5 fully functional — artifact metadata viewing and editing works.

---

## Phase 8: User Story 6 — Quick Status from Open (Priority: P3)

**Goal**: View detailed status for a single engagement directly from `/ea-open` next actions.

**Independent Test**: Open an engagement via `/ea-open`, select "view detailed status", verify single-engagement dashboard view appears matching `/ea-status` format.

### Implementation for User Story 6

- [x] T027 [US6] Add new step to `commands/ea-open.md`: when user selects "View detailed status" from next actions, display a single-engagement status view using the same format as `/ea-status` (type, domains, phase progress, artifact counts, dates) for just the currently opened engagement

**Checkpoint**: User Story 6 fully functional — quick status view from open works.

---

## Phase 9: User Story 7 — Archive and Delete Engagements (Priority: P3)

**Goal**: Archive completed engagements to `.archive/`, restore archived engagements, permanently delete engagements with slug confirmation.

**Independent Test**: Archive an engagement via `/ea-open`, verify it moves to `EA-projects/.archive/` and disappears from `/ea-status`. Restore it and verify it returns. Delete a test engagement and verify directory removed.

### Implementation for User Story 7

- [x] T028 [US7] Add archive logic to `commands/ea-open.md`: when user selects "Archive engagement" from next actions, display confirmation with target path (`EA-projects/.archive/{slug}/`), create `.archive/` if needed, move the engagement directory, and confirm per contracts/command-interface.md archive flow
- [x] T029 [US7] Add delete logic to `commands/ea-open.md`: when user selects "Delete engagement" from next actions, display irreversibility warning, require user to type the slug to confirm, remove the engagement directory, and confirm per contracts/command-interface.md delete flow
- [x] T030 [US7] Add archived engagement display to `commands/ea-status.md`: when user selects "Show archived engagements", scan `EA-projects/.archive/*/engagement.json`, display in a separate "Archived Engagements" section with name, status, and last modified date per contracts/command-interface.md archived section format
- [x] T031 [US7] Add restore logic to `commands/ea-status.md`: when viewing archived engagements, offer restore option — check for slug conflicts with active engagements, move directory from `.archive/` back to `EA-projects/`, and confirm per contracts/command-interface.md restore flow and edge case (block if conflict exists)

**Checkpoint**: User Story 7 fully functional — archive, restore, and delete all work.

---

## Phase 10: Polish & Cross-Cutting Concerns

**Purpose**: Version bump, documentation updates, and final validation.

- [x] T032 Bump version in `.claude-plugin/plugin.json` from `0.2.0` to `0.3.0` (minor: new capabilities added)
- [x] T032b [P] Bump version in `skills/ea-engagement-lifecycle/SKILL.md` frontmatter from `0.1.0` to `0.3.0` to sync with plugin.json
- [x] T033 [P] Update `README.md` to document enhanced `/ea-status` dashboard (type, domains, dates, N/A-aware progress), enhanced `/ea-open` details and editing capabilities, and archive/delete/restore features
- [x] T034 [P] Review all edge cases from spec.md (malformed engagement.json, missing artifact files, legacy engagement field upgrade, same-name disambiguation, directories without engagement.json, .archive auto-creation, restore slug conflict) and verify they are addressed in the command instructions
- [x] T035 Run quickstart.md validation — walk through all 8 scenarios and verify each step matches the enhanced command behavior

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: No dependencies — can start immediately
- **Foundational (Phase 2)**: Depends on T001/T002 (reading existing files) — BLOCKS all user stories
- **User Story 1 (Phase 3)**: Depends on Phase 2 — modifies `ea-status.md`
- **User Story 2 (Phase 4)**: Depends on Phase 2 — modifies `ea-open.md`
- **User Stories 3-6 (Phases 5-8)**: Depend on User Story 2 (Phase 4) — they add steps to `ea-open.md` after US2 establishes the next actions menu
- **User Story 7 (Phase 9)**: Depends on US2 (archive/delete in ea-open.md) AND US1 (archived section in ea-status.md)
- **Polish (Phase 10)**: Depends on all user stories being complete

### User Story Dependencies

- **US1 (P1)**: Modifies `ea-status.md` only — independent of US2
- **US2 (P1)**: Modifies `ea-open.md` only — independent of US1
- **US1 and US2 can run in parallel** (different files)
- **US3 (P2)**: Depends on US2 — adds edit metadata steps to `ea-open.md`
- **US4 (P2)**: Depends on US3 — adds edit phase steps to `ea-open.md` (same file, sequential)
- **US5 (P3)**: Depends on US4 — adds edit artifact steps to `ea-open.md` (same file, sequential)
- **US6 (P3)**: Depends on US2 — adds view status step to `ea-open.md`
- **US7 (P3)**: Depends on US2 (archive/delete in ea-open.md) and US1 (archived section in ea-status.md)

### Parallel Opportunities

- T001 and T002 can run in parallel (different files)
- T003, T004, T005, T006 all modify the same file (`SKILL.md`) — must run sequentially
- **US1 and US2 can run in parallel** (US1 modifies ea-status.md, US2 modifies ea-open.md)
- US3, US4, US5, US6 all modify `ea-open.md` — must run sequentially after US2
- T032, T033, T034 can run in parallel (different files)

---

## Implementation Strategy

### MVP First (User Stories 1 + 2)

1. Complete Phase 1: Setup (T001-T002)
2. Complete Phase 2: Foundational (T003-T006)
3. Complete Phase 3: User Story 1 — enhanced dashboard (T007-T012)
4. Complete Phase 4: User Story 2 — enhanced open (T013-T015)
5. **STOP and VALIDATE**: Test `/ea-status` and `/ea-open` end-to-end
6. Both commands are fully functional at this point

### Incremental Delivery

1. Complete Setup + Foundational → New concepts documented in SKILL.md
2. Complete US1 + US2 in parallel → Enhanced dashboard and open work (MVP!)
3. Complete US3 → Metadata editing works
4. Complete US4 → Phase status editing works
5. Complete US5 → Artifact metadata editing works
6. Complete US6 + US7 → Status view and archive/delete work
7. Polish → Version bump, docs, edge case review

---

## Notes

- [P] tasks = different files, no dependencies
- [Story] label maps task to specific user story for traceability
- This is a Markdown plugin — "implementation" means writing/updating command instruction files, not executable code
- US1 and US2 are the core enhancements and can be developed in parallel since they modify different files
- US3-US6 all add new steps to `ea-open.md` and must run sequentially
- US7 touches both command files (archive in ea-open, archived section in ea-status)
- Commit after each phase completion
- Stop at any checkpoint to validate independently
