# Feature Specification: Change Request Workflow

**Feature Branch**: `003-cr-workflow`
**Created**: 2026-03-20
**Status**: Draft
**Input**: User description: "build commands, agents and skills to handle submission, review and approval of change requests"

## User Scenarios & Testing *(mandatory)*

### User Story 1 - Create and Submit a Change Request (Priority: P1)

An IT change implementer needs to submit a formal change request for an infrastructure or application change. They open the change request tool, fill in all required ITIL v4 fields (title, description, change type, priority, risk assessment, implementation steps, rollback plan, validation criteria, change window, and approvers), save it as a draft, review it, and submit it for CAB approval.

**Why this priority**: This is the foundational workflow — without the ability to create and submit CRs, no other part of the change management process can function. This alone delivers MVP value.

**Independent Test**: Can be fully tested by creating a CR, filling in all fields, saving as draft, reopening it, and submitting to CAB. Verify the CR persists between sessions and transitions from Draft to Pending CAB Approval.

**Acceptance Scenarios**:

1. **Given** no existing change requests, **When** the user says "I need to submit a change request", **Then** the `itil-change-request` skill activates and presents the interactive CR management app as a React JSX artifact.
2. **Given** the CR app is open, **When** the user fills in Title, Change Owner, and Change Description and clicks "Save Draft", **Then** the CR is persisted to `window.storage` with status "Draft" and appears on the dashboard.
3. **Given** a Draft CR with all required fields completed, **When** the user clicks "Submit to CAB", **Then** the CR status transitions to "Pending CAB Approval" and the `updatedAt` timestamp is refreshed.
4. **Given** a Draft CR missing required fields (Title, Change Owner, or Change Description), **When** the user attempts to submit to CAB, **Then** the submit button is disabled and a validation message indicates which fields are missing.
5. **Given** a CR in "Pending CAB Approval" status, **When** the user opens the CR, **Then** they can revert it back to Draft for further editing.

---

### User Story 2 - CAB Review and Approval (Priority: P2)

A CAB administrator needs to review pending change requests and approve or reject them. They open the CAB review tool, see a list of all CRs awaiting approval, open each one to review full details (risk, implementation plan, rollback plan, approvers), and render an approve or reject decision with optional notes.

**Why this priority**: Approval is the second half of the change management lifecycle. Without it, CRs can be submitted but never acted upon. This completes the end-to-end workflow.

**Independent Test**: Can be tested by first creating and submitting a CR via User Story 1, then opening the CAB review tool, reviewing the CR, and approving or rejecting it. Verify the CR status updates correctly and the decision persists.

**Acceptance Scenarios**:

1. **Given** one or more CRs with status "Pending CAB Approval", **When** the user says "review change requests" or "cab review", **Then** the `cab-review` skill activates and presents the CAB review app listing all pending CRs.
2. **Given** the CAB review app is open with pending CRs, **When** the administrator clicks on a CR, **Then** they see full details: overview, change window, risk assessment, implementation steps, rollback plan, validation items, and requested approvers.
3. **Given** a CR is open for review, **When** the administrator clicks "Approve" (with or without notes), **Then** the CR status transitions to "Approved by CAB", the decision and notes are saved, and the CR is removed from the pending list.
4. **Given** a CR is open for review, **When** the administrator clicks "Reject" (with or without notes), **Then** the CR status transitions to "Rejected", the decision and notes are saved, and the CR is removed from the pending list.
5. **Given** no CRs are pending approval, **When** the administrator opens the CAB review tool, **Then** they see an empty state message indicating no CRs require action.

---

### User Story 3 - Implementation Checklist Tracking (Priority: P3)

After a change request is approved (or during preparation), the implementer needs to track progress against the implementation steps, rollback plan, and validation criteria. They open the checklist view for a specific CR and check off completed items, with progress persisting between sessions.

**Why this priority**: Checklists add operational value after the submission/approval flow is in place. They are independently useful but depend on CRs existing.

**Independent Test**: Can be tested by creating a CR with multiple implementation steps and validation items, opening the checklist view, checking off items, closing and reopening — verifying progress persists and percentage calculations are correct.

**Acceptance Scenarios**:

1. **Given** a CR with implementation steps, rollback steps, and validation items, **When** the user clicks "Checklist" on the dashboard, **Then** the checklist view displays all steps grouped by category with checkboxes and a progress bar.
2. **Given** the checklist view is open, **When** the user checks off an implementation step, **Then** the step is marked complete, the progress percentage updates, and the change is persisted to storage immediately.
3. **Given** some steps are checked off, **When** the user closes and reopens the checklist, **Then** all checked state is preserved.
4. **Given** all steps in all categories are checked, **Then** the overall progress shows 100% complete.

---

### User Story 4 - Word Document Export (Priority: P4)

An implementer or CAB administrator needs to export a change request as a formatted Word document for formal submission, audit trail, or offline review. The exported document follows a standardized ITIL template with cover page, all CR sections, and an approver signature table.

**Why this priority**: Document export is a value-add for formal governance processes but is not required for the core digital workflow. It builds on top of the existing CR data.

**Independent Test**: Can be tested by creating a CR with all fields populated, requesting a Word export, and verifying the generated .docx contains all sections, correct formatting, and approver table.

**Acceptance Scenarios**:

1. **Given** a CR with all fields populated, **When** the user asks to "export this change request as a Word doc", **Then** the system generates a .docx file following the template in `references/docx-template.md`.
2. **Given** an approved CR, **When** exported, **Then** the document is saved to the `Approved/` subdirectory.
3. **Given** a CR with multiple approvers selected, **Then** the Word document includes an approver table with one row per approver plus a CAB Chair row, with blank Decision and Signature columns.

---

### User Story 5 - Slash Commands for Quick Access (Priority: P5)

Users need quick slash command access to the CR and CAB review tools without relying on skill auto-detection. The `/itil-cr` command opens the CR management tool and `/cab-review` opens the CAB review tool.

**Why this priority**: Commands are convenience wrappers around existing skills. They add discoverability but not new functionality.

**Independent Test**: Can be tested by typing `/itil-cr` and verifying the CR management app launches, and `/cab-review` and verifying the CAB review app launches.

**Acceptance Scenarios**:

1. **Given** the plugin is installed, **When** the user types `/itil-cr`, **Then** the `itil-change-request` skill activates and the CR management app is presented.
2. **Given** the plugin is installed, **When** the user types `/cab-review`, **Then** the `cab-review` skill activates and the CAB review app is presented.

---

### Edge Cases

- What happens when `window.storage` is empty on first use? The app MUST initialize gracefully with an empty CR list and allow the user to create the first CR.
- What happens when a CR is submitted to CAB but the approver list is empty? The system MUST still allow submission — approver selection is recommended but not blocking.
- What happens when two skills attempt to update the same CR simultaneously? Storage writes MUST use the latest `updatedAt` timestamp; last-write-wins is acceptable for single-user scenarios.
- What happens when the user tries to edit a CR that is already "Approved by CAB"? The app SHOULD allow viewing but MUST NOT allow status changes.
- What happens when a CR is Rejected? The requester MUST be able to revert it to Draft for editing and resubmission. The original rejection notes (cabNotes) MUST be preserved so the requester can address the feedback.
- What happens when the user tries to delete a CR? Only Draft CRs may be deleted. CRs in any other status (Pending, Approved, Rejected) MUST NOT be deletable — they are permanent audit records. Deleting a Draft CR removes it from both `cr_index` and `cr_{id}` storage keys.
- What happens when the change request JSX artifact fails to render? The skill MUST present the artifact — if the file is missing or corrupt, the user sees an error rather than silent failure.

## Clarifications

### Session 2026-03-20

- Q: Should Emergency change requests follow the same CAB approval workflow as Normal/Standard changes? → A: Emergency changes skip CAB — Draft → Approved by CAB (auto-approved), with retrospective review flag.
- Q: What happens when a CAB administrator rejects a CR — can the requester resubmit? → A: Revert to Draft — a Rejected CR can be moved back to Draft, edited, and resubmitted to CAB.
- Q: Should the system preserve a history of all CAB decisions across review cycles? → A: Append-only history — add a `cabHistory` array that accumulates each decision with timestamp and notes.
- Q: Can users delete change requests? → A: Allow deletion of Draft CRs only; submitted/approved/rejected CRs cannot be deleted.

## Requirements *(mandatory)*

### Functional Requirements

- **FR-001**: Plugin MUST provide an `itil-change-request` skill that activates when the user mentions change requests, RFCs, CAB submissions, or change management.
- **FR-002**: Plugin MUST provide a `cab-review` skill that activates when the user mentions CAB review, approvals, pending change requests, or acting as a CAB administrator.
- **FR-003**: The `itil-change-request` skill MUST present an interactive React JSX artifact (from `references/cr-app.jsx`) that supports creating, editing, and submitting CRs.
- **FR-004**: The `cab-review` skill MUST present an interactive React JSX artifact (from `references/cab-review-app.jsx`) that supports reviewing, approving, and rejecting pending CRs.
- **FR-005**: CRs MUST follow the ITIL v4 status flow: Draft → Pending CAB Approval → Approved by CAB / Rejected. No status may be skipped. **Exception**: Emergency change requests skip CAB approval — submitting an Emergency CR transitions it directly from Draft to "Approved by CAB" (auto-approved) and sets a retrospective review flag. The CAB reviews emergency changes post-implementation.
- **FR-006**: All CR data MUST persist between sessions using `window.storage` with the shared schema: `cr_index` (array of RFC IDs) and `cr_{id}` (individual CR JSON).
- **FR-007**: Each CR MUST include all ITIL v4 fields: title, change type (Standard/Normal/Emergency), priority, requestor, change owner, affected systems, business justification, change description, implementation steps, rollback steps, validation items, change window, risk level, risk details, approver IDs, status, and CAB notes.
- **FR-008**: The CR management app MUST provide a dashboard with status-based filtering (All, Draft, Pending CAB, Approved, Rejected).
- **FR-009**: The CR management app MUST allow deletion of Draft CRs only. CRs in Pending, Approved, or Rejected status MUST NOT be deletable.
- **FR-010**: The CR management app MUST provide a checklist view for tracking implementation steps, rollback steps, and validation items with persistent check state.
- **FR-011**: The CR management app MUST validate that Title, Change Owner, and Change Description are populated before allowing CAB submission.
- **FR-012**: The CR management app MUST display Approved and Rejected CRs in read-only mode — no edits or status changes permitted after a CAB decision.
- **FR-013**: The CAB review app MUST display the pending CR count in the header and update it in real time as decisions are made.
- **FR-014**: Plugin MUST provide `/itil-cr` and `/cab-review` slash commands that invoke the corresponding skills.
- **FR-015**: Word document export MUST follow the template structure defined in `references/docx-template.md` and save to the appropriate output directory.

### Key Entities

- **Change Request (CR)**: The central entity representing a formal request for change. Identified by an RFC ID (e.g., `RFC-2026-0042`). Contains all ITIL-required fields, status, timestamps, CAB decision notes, and an append-only `cabHistory` array that accumulates each CAB decision (approve/reject) with timestamp and notes across review cycles. Persists as JSON in `window.storage`.
- **Approver**: A predefined CAB member who may be assigned to review a CR. Has an ID, name, and role. The predefined list includes 8 approvers spanning IT Director, Application Owner, Security Lead, Infrastructure Manager, Change Manager, DBA, Network Lead, and CISO.
- **Checklist Step**: An implementation step, rollback step, or validation item within a CR. Has an ID, text description, and checked state. Steps are embedded within the CR entity, not stored separately.

## Assumptions

- This plugin operates in a single-user context (one person using Claude Code at a time). Multi-user conflict resolution is not in scope.
- The predefined approver list is hardcoded in the JSX artifacts. Customizable approver lists are a future enhancement.
- `window.storage` is available in the Claude artifact runtime environment. The plugin does not need a fallback storage mechanism.
- Word document export requires the `docx` npm package to be available in the execution environment.

## Success Criteria *(mandatory)*

### Measurable Outcomes

- **SC-001**: Users can create a complete change request (all fields populated) and submit it for CAB approval in under 5 minutes using the interactive form.
- **SC-002**: A CAB administrator can review a pending CR and render an approve/reject decision in under 2 minutes.
- **SC-003**: Skills auto-activate correctly for at least 90% of natural-language triggers (e.g., "change request", "RFC", "CAB review", "approve changes", "submit a change").
- **SC-004**: All CR data persists correctly across sessions — a CR created in one session is fully retrievable in the next with no data loss.
- **SC-005**: The checklist view accurately reflects progress — checking items updates the percentage, and state persists on reload.
- **SC-006**: Exported Word documents contain all CR sections, are correctly formatted per the template, and are readable in Microsoft Word and LibreOffice.
