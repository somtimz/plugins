# Tasks: EA New Engagement Setup

**Input**: Design documents from `/specs/001-ea-new-engagement-setup/`
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

**Purpose**: Create the new reference file and prepare the foundation for all user stories.

- [x] T001 Create scaffolding map reference file at `skills/ea-engagement-lifecycle/references/scaffolding-map.md` defining engagement type + domain → artifact mapping per data-model.md and research.md R1/R2
- [x] T002 [P] Read current `commands/ea-new.md` and `skills/ea-engagement-lifecycle/SKILL.md` to understand existing content before modification

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Update the engagement lifecycle skill with new concepts (engagement types, domains, phase applicability) that all user stories depend on.

**CRITICAL**: No user story work can begin until this phase is complete.

- [x] T003 Update `skills/ea-engagement-lifecycle/SKILL.md` to add engagement type definitions (Greenfield, Brownfield, Assessment-only, Migration) with descriptions per research.md R1
- [x] T004 Update `skills/ea-engagement-lifecycle/SKILL.md` to add architecture domain selection guidance and domain-to-phase mapping (Business→B, Data→C-Data, Application→C-App, Technology→D) per data-model.md
- [x] T005 Update `skills/ea-engagement-lifecycle/SKILL.md` to add "Not Applicable" as a valid phase status value and document when it applies
- [x] T006 Update `skills/ea-engagement-lifecycle/SKILL.md` to document the enhanced `engagement.json` schema with three new fields (`engagementType`, `architectureDomains`, `targetEndDate`) per data-model.md, noting backward compatibility defaults

**Checkpoint**: Lifecycle skill now documents all new concepts. Command updates can begin.

---

## Phase 3: User Story 1 — Create Engagement with Guided Prompts (Priority: P1) MVP

**Goal**: Full guided creation flow with all 10 metadata fields, confirmation summary, edit-before-save, directory creation, engagement.json with new fields, and Preliminary phase artifact scaffolding.

**Independent Test**: Invoke `/ea-new` with no arguments, complete all 10 prompts, confirm, and verify: directory structure exists, `engagement.json` has all fields including `engagementType`/`architectureDomains`/`targetEndDate`, ADM phases reflect domain selection, and `artifacts/` contains scaffolded Architecture Principles and Stakeholder Map.

### Implementation for User Story 1

- [x] T007 [US1] Rewrite `commands/ea-new.md` Instructions section: replace step 1 to collect 10 fields (add engagement type as select prompt with four options, architecture domains as multi-select with all-four default, target end date as optional date prompt) per contracts/command-interface.md prompt sequence
- [x] T008 [US1] Update `commands/ea-new.md` Instructions section: add step for confirmation summary display — format as Markdown table showing all field names and values including computed slug, with three actions: Confirm / Edit [field name] / Cancel — per contracts/command-interface.md confirmation format
- [x] T009 [US1] Update `commands/ea-new.md` Instructions section: add edit-before-save logic — when user selects Edit, re-prompt for the named field only, update the value, redisplay summary, and loop until Confirm or Cancel
- [x] T010 [US1] Update `commands/ea-new.md` Instructions section: add cancel logic — when user selects Cancel, abandon creation with no directories or files written and display cancellation message
- [x] T011 [US1] Update `commands/ea-new.md` engagement.json template: add `engagementType`, `architectureDomains`, and `targetEndDate` fields per data-model.md schema
- [x] T012 [US1] Update `commands/ea-new.md` Instructions section: after directory creation, add step to determine phase applicability based on engagement type and domain selection per research.md R1 mapping table, setting inapplicable phases to "Not Applicable"
- [x] T013 [US1] Update `commands/ea-new.md` Instructions section: add artifact scaffolding step — after directory creation, read `scaffolding-map.md`, for each applicable artifact copy the template from `templates/` to `artifacts/`, replace template variables (`{{engagement_name}}`, `{{organisation}}`, `{{sponsor}}`, `{{YYYY-MM-DD}}`), mark content sections with `⚠️ Not answered`, and add artifact entries to the `artifacts` array in `engagement.json`
- [x] T014 [US1] Update `commands/ea-new.md` step 7 (confirmation): enhance success output to include list of scaffolded artifacts per contracts/command-interface.md success output format

**Checkpoint**: User Story 1 fully functional — guided creation with all enhancements works end-to-end.

---

## Phase 4: User Story 2 — Inline Name Argument (Priority: P2)

**Goal**: Accept engagement name as inline argument to `/ea-new`, skipping the name prompt.

**Independent Test**: Invoke `/ea-new "Acme Retail Transformation 2026"` and verify name is pre-filled, slug is correctly generated, and remaining 9 prompts are presented.

### Implementation for User Story 2

- [x] T015 [US2] Verify `commands/ea-new.md` step 1 correctly handles inline argument — the existing command already has this logic ("If an engagement name was provided as an argument, use it as the display name"); confirm it still works with the new 10-field prompt sequence and that only prompts 2-10 are shown when name is provided

**Checkpoint**: Inline name argument works with enhanced prompt flow.

---

## Phase 5: User Story 3 — Duplicate Engagement Detection (Priority: P2)

**Goal**: Detect slug collisions and offer to open existing or choose new name.

**Independent Test**: Create an engagement, then run `/ea-new` with the same name and verify conflict detection message appears with two options.

### Implementation for User Story 3

- [x] T016 [US3] Verify `commands/ea-new.md` step 3 duplicate detection still works correctly — the existing command already checks for existing directories; confirm the duplicate message format matches contracts/command-interface.md duplicate output and offers both "open existing" and "choose different name" options

**Checkpoint**: Duplicate detection works with enhanced flow.

---

## Phase 6: User Story 4 — Confirmation and Edit Before Save (Priority: P2)

**Goal**: Display formatted summary with edit capability before committing.

**Independent Test**: Complete all prompts, verify summary table is displayed, edit one field (e.g., change engagement type from Greenfield to Brownfield), confirm summary updates, then confirm creation and verify `engagement.json` reflects the edited value.

### Implementation for User Story 4

- [x] T017 [US4] Verify confirmation and edit logic from T008/T009 handles all field types correctly — specifically test that editing engagement type updates the phase applicability, and editing architecture domains updates both the domains list and phase applicability in the summary

**Checkpoint**: Edit-before-save works for all field types including those with side effects.

---

## Phase 7: User Story 5 — TOGAF Preliminary Phase Scaffolding (Priority: P2)

**Goal**: Auto-generate starter artifacts from templates during creation.

**Independent Test**: Create a Greenfield engagement with all domains, verify `artifacts/architecture-principles.md` and `artifacts/stakeholder-map.md` exist with correct template variables replaced and content marked `⚠️ Not answered`. Then create an Assessment-only engagement and verify the same artifacts are scaffolded (both are applicable to all types per scaffolding map).

### Implementation for User Story 5

- [x] T018 [US5] Verify scaffolding logic from T013 correctly reads `scaffolding-map.md` and applies type/domain filtering — confirm that for all four engagement types, both Architecture Principles and Stakeholder Map are generated (since both have `applicable_types: all` and `applicable_domains: all`)
- [x] T019 [US5] Verify scaffolded artifacts have template variables replaced with actual engagement metadata values and all content sections marked with `⚠️ Not answered` per constitution Principle II

**Checkpoint**: Scaffolding produces correct artifacts for all engagement type/domain combinations.

---

## Phase 8: User Story 6 — Settings Integration (Priority: P3)

**Goal**: Read requirementsRepoPath from plugin settings file during creation.

**Independent Test**: Create `.claude/ea-assistant.local.md` with `requirementsRepoPath: /shared/reqs`, run `/ea-new`, and verify `engagement.json` contains the path. Then remove the file and create another engagement to verify default empty value.

### Implementation for User Story 6

- [x] T020 [US6] Verify `commands/ea-new.md` step 6 settings integration still works — the existing command already reads `.claude/ea-assistant.local.md`; confirm this step is preserved in the enhanced command and works correctly with the new engagement.json schema

**Checkpoint**: Settings integration works with enhanced schema.

---

## Phase 9: User Story 7 — Post-Creation Navigation (Priority: P3)

**Goal**: Offer to begin Preliminary phase or return to menu after creation.

**Independent Test**: Complete `/ea-new`, verify confirmation includes engagement details, scaffolded artifact list, and two navigation options.

### Implementation for User Story 7

- [x] T021 [US7] Verify `commands/ea-new.md` step 7 post-creation navigation offers both "begin Preliminary phase" and "return to main menu" options — the existing command already has this; confirm the enhanced output from T014 includes the scaffolded artifacts list before the navigation prompt

**Checkpoint**: Post-creation navigation works with enhanced output.

---

## Phase 10: Polish & Cross-Cutting Concerns

**Purpose**: Version bump, documentation updates, and final validation.

- [x] T022 Bump version in `.claude-plugin/plugin.json` from `0.1.0` to `0.2.0` (minor: new capabilities added)
- [x] T023 [P] Update `README.md` to document new fields (engagement type, architecture domains, target end date) in the Commands section and engagement.json template
- [x] T024 [P] Review all edge cases from spec.md (cancel midway, long name truncation, auto-create EA-projects/, empty name re-prompt, deselect all domains re-prompt, missing template skip-and-warn) and verify they are addressed in the command instructions
- [x] T025 Run quickstart.md validation — walk through the quickstart guide and verify each step matches the enhanced command behavior

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: No dependencies — can start immediately
- **Foundational (Phase 2)**: Depends on T001 (scaffolding map) — BLOCKS all user stories
- **User Story 1 (Phase 3)**: Depends on Phase 2 — this is the core implementation
- **User Stories 2-5 (Phases 4-7)**: Depend on Phase 3 (US1) — these verify/extend the core implementation
- **User Stories 6-7 (Phases 8-9)**: Depend on Phase 3 (US1) — independent verification tasks
- **Polish (Phase 10)**: Depends on all user stories being complete

### User Story Dependencies

- **US1 (P1)**: Depends on Foundational (Phase 2) only. This is the main implementation.
- **US2 (P2)**: Depends on US1 — verifies inline argument works with enhanced flow
- **US3 (P2)**: Depends on US1 — verifies duplicate detection works with enhanced flow
- **US4 (P2)**: Depends on US1 — verifies edit logic handles all field types
- **US5 (P2)**: Depends on US1 — verifies scaffolding logic produces correct artifacts
- **US6 (P3)**: Depends on US1 — verifies settings integration preserved
- **US7 (P3)**: Depends on US1 — verifies navigation with enhanced output

### Parallel Opportunities

- T001 and T002 can run in parallel (different files)
- T003, T004, T005, T006 all modify the same file (`SKILL.md`) — must run sequentially
- T022, T023, T024 can run in parallel (different files)
- US2-US7 verification tasks (T015-T021) can run in parallel after US1 is complete, as they verify different aspects of the same command file

---

## Implementation Strategy

### MVP First (User Story 1 Only)

1. Complete Phase 1: Setup (T001-T002)
2. Complete Phase 2: Foundational (T003-T006)
3. Complete Phase 3: User Story 1 (T007-T014)
4. **STOP and VALIDATE**: Test `/ea-new` end-to-end with guided prompts
5. The command is fully functional at this point

### Incremental Delivery

1. Complete Setup + Foundational → New concepts documented
2. Complete US1 → Full enhanced `/ea-new` works (MVP!)
3. Verify US2-US5 → All P2 features confirmed working
4. Verify US6-US7 → All P3 features confirmed working
5. Polish → Version bump, docs, edge case review

---

## Notes

- [P] tasks = different files, no dependencies
- [Story] label maps task to specific user story for traceability
- This is a Markdown plugin — "implementation" means writing/updating command instruction files, not executable code
- US2-US7 are primarily verification tasks because the core implementation in US1 (rewriting ea-new.md) delivers most of the functionality in one pass
- Commit after each phase completion
- Stop at any checkpoint to validate independently
