# Tasks: Change Request Workflow

**Input**: Design documents from `/specs/003-cr-workflow/`
**Prerequisites**: plan.md (required), spec.md (required), research.md, data-model.md, contracts/

**Tests**: Not explicitly requested — test tasks omitted. Validation is manual (Claude Code session testing per constitution).

**Organization**: Tasks are grouped by user story to enable independent implementation and testing of each story.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (e.g., US1, US2, US3)
- Include exact file paths in descriptions

---

## Phase 1: Setup

**Purpose**: Plugin scaffolding and manifest

- [ ] T001 Create plugin manifest at `plugins/ITIL-assistant/.claude-plugin/plugin.json` with name, version 0.1.0, description, author, keywords
- [ ] T002 [P] Create `plugins/ITIL-assistant/.gitignore` with OS artifact exclusions
- [ ] T003 [P] Create `plugins/ITIL-assistant/LICENSE` (MIT)
- [ ] T004 [P] Create empty hooks file at `plugins/ITIL-assistant/hooks/hooks.json`

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Storage helpers and shared constants that both skills depend on

**CRITICAL**: No user story work can begin until the storage contract is finalized.

- [ ] T005 Define the CR factory function (`makeCR()`) and status/priority/risk constants in `plugins/ITIL-assistant/skills/itil-change-request/references/cr-app.jsx` — these are shared via copy in both JSX files per the storage contract in `specs/003-cr-workflow/contracts/storage-contract.md`
- [ ] T006 Implement `getCRs()` and `putCR()` storage helpers in `plugins/ITIL-assistant/skills/itil-change-request/references/cr-app.jsx` per the storage contract, including `cabHistory` append-only array and `updatedAt` refresh on every write
- [ ] T007 Implement `deleteCR()` storage helper in `plugins/ITIL-assistant/skills/itil-change-request/references/cr-app.jsx` — removes Draft CR from `cr_index` and `cr_{id}` keys
- [ ] T008 [P] Implement matching `getCRs()` and `putCR()` in `plugins/ITIL-assistant/skills/cab-review/references/cab-review-app.jsx` per the same storage contract (read-compatible with cr-app.jsx)

**Checkpoint**: Storage contract implemented — both JSX files can read/write CRs with shared schema

---

## Phase 3: User Story 1 — Create and Submit a Change Request (Priority: P1) MVP

**Goal**: User can create a CR with all ITIL v4 fields, save as draft, edit, and submit to CAB. Emergency CRs auto-approve.

**Independent Test**: Create a CR → fill all fields → Save Draft → reopen → verify persistence → Submit to CAB → verify status is "Pending CAB Approval". Create an Emergency CR → Submit → verify auto-approved with `retrospectiveReview: true`.

### Implementation for User Story 1

- [ ] T009 [US1] Build the CR form component in `plugins/ITIL-assistant/skills/itil-change-request/references/cr-app.jsx` with all ITIL v4 fields: title, changeType (Standard/Normal/Emergency), priority, requestedBy, changeOwner, dateSubmitted, affectedSystems, businessJustification, changeDescription, change window (start, duration, maintenanceWindow), risk assessment (riskLevel, riskImpact, riskUsers, riskDeps)
- [ ] T010 [US1] Build the step editor component (reusable for implSteps, rollbackSteps, validationItems) with add/remove/reorder in `plugins/ITIL-assistant/skills/itil-change-request/references/cr-app.jsx`
- [ ] T011 [US1] Build the approver picker component with checkbox grid for 8 predefined approvers in `plugins/ITIL-assistant/skills/itil-change-request/references/cr-app.jsx`
- [ ] T012 [US1] Implement Save Draft and Submit to CAB actions — validate required fields (title, changeOwner, changeDescription) before enabling Submit; handle Emergency bypass (auto-approve with `retrospectiveReview: true`) in `plugins/ITIL-assistant/skills/itil-change-request/references/cr-app.jsx`
- [ ] T013 [US1] Build the dashboard view with status-based filter pills (All, Draft, Pending CAB, Approved, Rejected) and CR list cards in `plugins/ITIL-assistant/skills/itil-change-request/references/cr-app.jsx`
- [ ] T014 [US1] Implement delete Draft CR functionality — add delete button on Draft CR cards, confirm and remove from storage in `plugins/ITIL-assistant/skills/itil-change-request/references/cr-app.jsx`
- [ ] T015 [US1] Implement Revert to Draft for Pending and Rejected CRs — add revert button, transition status back to Draft preserving `cabHistory` in `plugins/ITIL-assistant/skills/itil-change-request/references/cr-app.jsx`
- [ ] T016 [US1] Wire up the root `App` component with view routing (dashboard ↔ form ↔ checklist), toast notifications, and font loading in `plugins/ITIL-assistant/skills/itil-change-request/references/cr-app.jsx`
- [ ] T017 [US1] Enforce read-only mode in the CR form for Approved and Rejected CRs — hide Save Draft and Submit buttons, disable all form inputs, display a status banner indicating no edits permitted in `plugins/ITIL-assistant/skills/itil-change-request/references/cr-app.jsx`
- [ ] T018 [US1] Create the `itil-change-request` SKILL.md at `plugins/ITIL-assistant/skills/itil-change-request/SKILL.md` with valid frontmatter (name, description with trigger phrases, version) and workflow instructions to read and present `references/cr-app.jsx`
- [ ] T019 [US1] Create the `/itil-cr` command at `plugins/ITIL-assistant/commands/itil-cr.md` with valid frontmatter (name, description) and body invoking the `itil-change-request` skill

**Checkpoint**: User Story 1 fully functional — can create, save, edit, delete, and submit CRs

---

## Phase 4: User Story 2 — CAB Review and Approval (Priority: P2)

**Goal**: CAB administrator can review pending CRs, see full details, and approve or reject with notes. Decisions append to `cabHistory`.

**Independent Test**: Submit a CR via US1 → open CAB review → verify CR appears → Approve with notes → verify status is "Approved by CAB" and `cabHistory` has entry. Repeat with Reject.

### Implementation for User Story 2

- [ ] T020 [US2] Build the pending CR list view in `plugins/ITIL-assistant/skills/cab-review/references/cab-review-app.jsx` — filter CRs by "Pending CAB Approval" status, show priority/risk badges, sorted by updatedAt
- [ ] T021 [US2] Build the CR detail panel in `plugins/ITIL-assistant/skills/cab-review/references/cab-review-app.jsx` — display overview, change window, risk assessment, implementation steps, rollback plan, validation items, requested approvers
- [ ] T022 [US2] Implement Approve and Reject actions in `plugins/ITIL-assistant/skills/cab-review/references/cab-review-app.jsx` — transition status, set `cabNotes`, append to `cabHistory` array with action/notes/timestamp, remove from pending list
- [ ] T023 [US2] Wire up root `CABReview` component with list ↔ detail navigation, pending count badge, toast notifications in `plugins/ITIL-assistant/skills/cab-review/references/cab-review-app.jsx`
- [ ] T024 [US2] Create the `cab-review` SKILL.md at `plugins/ITIL-assistant/skills/cab-review/SKILL.md` with valid frontmatter (name, description with trigger phrases, version) and workflow instructions to read and present `references/cab-review-app.jsx`
- [ ] T025 [US2] Create the `/cab-review` command at `plugins/ITIL-assistant/commands/cab-review.md` with valid frontmatter (name, description) and body invoking the `cab-review` skill

**Checkpoint**: User Stories 1 AND 2 both work — full submission → review → approval/rejection cycle

---

## Phase 5: User Story 3 — Implementation Checklist Tracking (Priority: P3)

**Goal**: Implementer can track progress on implementation steps, rollback plan, and validation items with persistent checkbox state.

**Independent Test**: Create a CR with multiple steps → open checklist view → check off items → verify percentage updates → close and reopen → verify state persists.

### Implementation for User Story 3

- [ ] T026 [US3] Build the ChecklistView component in `plugins/ITIL-assistant/skills/itil-change-request/references/cr-app.jsx` — group steps by category (Implementation, Rollback, Validation), show progress bars per category and overall percentage
- [ ] T027 [US3] Implement checkbox toggle with immediate storage persistence in `plugins/ITIL-assistant/skills/itil-change-request/references/cr-app.jsx` — toggle `checked` state on click, save CR via `putCR()`, update progress display
- [ ] T028 [US3] Wire checklist view into the App component routing — add "Checklist" button on dashboard CR cards, navigation between dashboard ↔ form ↔ checklist in `plugins/ITIL-assistant/skills/itil-change-request/references/cr-app.jsx`

**Checkpoint**: All three core user stories independently functional

---

## Phase 6: User Story 4 — Word Document Export (Priority: P4)

**Goal**: Export a CR as a formatted .docx with all sections and approver signature table.

**Independent Test**: Create a CR with all fields → request Word export → verify .docx contains cover block, all 7 sections, approver table, and correct footer.

### Implementation for User Story 4

- [ ] T029 [US4] Create the docx template reference at `plugins/ITIL-assistant/skills/itil-change-request/references/docx-template.md` — document structure (cover block, 7 sections), styling rules (fonts, colors, table widths), and complete Node.js script pattern using `docx` npm package
- [ ] T030 [US4] Add Word export instructions to `plugins/ITIL-assistant/skills/itil-change-request/SKILL.md` — steps to read docx-template.md, generate .docx from CR data, save to output directory (Approved/ subdirectory for approved CRs), validate, and present
- [ ] T031 [US4] Add Word export instructions to `plugins/ITIL-assistant/skills/cab-review/SKILL.md` — instructions for exporting approved CRs after CAB decision, referencing the docx-template.md from the itil-change-request skill

**Checkpoint**: All four user stories functional — full lifecycle with document export

---

## Phase 7: User Story 5 — Slash Commands (Priority: P5)

**Goal**: `/itil-cr` and `/cab-review` commands provide explicit entry points to the skills.

**Independent Test**: Type `/itil-cr` → verify CR app launches. Type `/cab-review` → verify CAB review app launches.

### Implementation for User Story 5

- [ ] T032 [P] [US5] Verify `/itil-cr` command at `plugins/ITIL-assistant/commands/itil-cr.md` has correct frontmatter and invokes `itil-change-request` skill (created in T018)
- [ ] T033 [P] [US5] Verify `/cab-review` command at `plugins/ITIL-assistant/commands/cab-review.md` has correct frontmatter and invokes `cab-review` skill (created in T025)

**Checkpoint**: All user stories complete — plugin fully functional

---

## Phase 8: Polish & Cross-Cutting Concerns

**Purpose**: Documentation, marketplace entry, and final validation

- [ ] T034 [P] Create `plugins/ITIL-assistant/README.md` with overview, features, skills table, commands table, status flow diagram, and installation instructions
- [ ] T035 [P] Add ITIL-assistant entry to `.claude-plugin/marketplace.json` with name, description, version, author, source path, and category
- [ ] T036 Bump version in `plugins/ITIL-assistant/.claude-plugin/plugin.json` and both SKILL.md files to 0.1.0 (verify consistency)
- [ ] T037 Run end-to-end validation per `specs/003-cr-workflow/quickstart.md` — create CR, submit, CAB review, approve, checklist, verify all storage state

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: No dependencies — can start immediately
- **Foundational (Phase 2)**: Depends on Setup completion — BLOCKS all user stories
- **User Story 1 (Phase 3)**: Depends on Foundational phase — provides MVP
- **User Story 2 (Phase 4)**: Depends on Foundational phase — can start in parallel with US1 if desired, but benefits from US1 for end-to-end testing
- **User Story 3 (Phase 5)**: Depends on US1 (checklist is part of cr-app.jsx)
- **User Story 4 (Phase 6)**: Depends on US1 and US2 (needs CRs and approval flow)
- **User Story 5 (Phase 7)**: Depends on US1 and US2 (commands wrap existing skills)
- **Polish (Phase 8)**: Depends on all user stories

### Within Each User Story

- Storage helpers before UI components
- UI components before view routing
- SKILL.md after JSX artifact is complete
- Commands after SKILL.md is complete

### Parallel Opportunities

- T002, T003, T004 can run in parallel (Phase 1)
- T006, T008 can run in parallel (matching storage helpers)
- T032, T033 can run in parallel (independent command verification)
- T034, T035 can run in parallel (documentation)

---

## Implementation Strategy

### MVP First (User Story 1 Only)

1. Complete Phase 1: Setup
2. Complete Phase 2: Foundational (storage contract)
3. Complete Phase 3: User Story 1 (CR creation and submission)
4. **STOP and VALIDATE**: Create a CR, save, edit, submit — verify all persistence
5. Deploy/demo if ready

### Incremental Delivery

1. Setup + Foundational → Storage contract ready
2. Add User Story 1 → CR creation MVP
3. Add User Story 2 → Full submission-review-approval cycle
4. Add User Story 3 → Checklist tracking
5. Add User Story 4 → Word export
6. Add User Story 5 → Slash commands
7. Polish → README, marketplace, final validation

---

## Notes

- [P] tasks = different files, no dependencies
- [Story] label maps task to specific user story for traceability
- All JSX artifacts are self-contained — no shared imports between cr-app.jsx and cab-review-app.jsx
- Storage helpers are duplicated (not shared) between the two JSX files per the storage contract
- The existing JSX files from `temp/` provide a working reference — tasks involve updating them with clarification-driven changes (cabHistory, emergency bypass, deletion, revert)
