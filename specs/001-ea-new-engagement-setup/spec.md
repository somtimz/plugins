# Feature Specification: EA New Engagement Setup

**Feature Branch**: `001-ea-new-engagement-setup`
**Created**: 2026-03-19
**Status**: Draft
**Input**: User description: "help me define an ea-new command that helps me setup a new EA engagement"

## Clarifications

### Session 2026-03-19

- Q: Is this spec formalizing the existing command or defining enhancements? → A: Enhance the existing `/ea-new` command with new capabilities.
- Q: What enhancement areas to focus on? → A: All three: richer metadata fields, smarter UX (confirmation/edit/undo), and TOGAF-aware scaffolding of starter artifacts.
- Q: How should engagement types be classified? → A: Four types: Greenfield, Brownfield, Assessment-only, Migration.
- Q: Should users select architecture domains in scope? → A: Yes, user selects applicable domains at creation (Business, Data, Application, Technology) with all four selected by default.

## User Scenarios & Testing *(mandatory)*

### User Story 1 - Create Engagement with Guided Prompts (Priority: P1)

An enterprise architect invokes `/ea-new` without arguments. The system
guides them through a series of prompts to collect all required engagement
metadata: name, description, sponsor, organisation, scope, start date,
status, engagement type, target end date, and architecture domains in
scope. Once collected, the system displays a confirmation summary of all
entered values. The user can edit any field before confirming. Upon
confirmation, the system creates the full engagement directory structure,
scaffolds starter artifacts for the Preliminary phase appropriate to the
selected engagement type and domains, and confirms the engagement is
ready.

**Why this priority**: This is the primary happy-path flow. Without guided
creation, no engagement can be started. It delivers the core value of the
command including all three enhancement areas.

**Independent Test**: Can be fully tested by invoking `/ea-new` with no
arguments and completing all prompts. Delivers a ready-to-use engagement
directory with valid `engagement.json`, correct subdirectories, and
scaffolded Preliminary phase artifacts.

**Acceptance Scenarios**:

1. **Given** no existing engagements, **When** the user runs `/ea-new`
   and provides all required fields, **Then** the system creates
   `EA-projects/{slug}/` with all subdirectories and a valid
   `engagement.json` containing the provided metadata including
   engagement type, target end date, and selected architecture domains.
2. **Given** the user is prompted for start date, **When** they press
   enter without typing a value, **Then** today's date is used as the
   default.
3. **Given** the user is prompted for status, **When** they press enter
   without typing a value, **Then** "Active" is used as the default.
4. **Given** the user is prompted for architecture domains, **When** they
   press enter without typing a value, **Then** all four domains
   (Business, Data, Application, Technology) are selected by default.
5. **Given** all fields are collected, **When** the confirmation summary
   is displayed, **Then** the user can review all values and choose to
   edit any field before final confirmation.
6. **Given** the user confirms creation, **When** the engagement is
   created, **Then** all ADM phases are initialised to "Not Started",
   `currentPhase` is set to "Prelim", and starter artifacts for the
   Preliminary phase are generated in `artifacts/`.
7. **Given** the user selects engagement type "Assessment-only", **When**
   the engagement is created, **Then** only ADM phases relevant to
   assessment work are marked as applicable in `engagement.json`.

---

### User Story 2 - Create Engagement with Inline Name (Priority: P2)

An enterprise architect invokes `/ea-new Acme Retail Transformation 2026`
with the engagement name provided as an argument. The system uses this as
the display name and still prompts for the remaining required fields
(description, sponsor, organisation, scope, start date, status,
engagement type, target end date, architecture domains).

**Why this priority**: Power users who already know the engagement name
want to skip the first prompt and move faster. This builds on US1 by
accepting partial inline input.

**Independent Test**: Can be tested by invoking `/ea-new "Acme Retail
Transformation 2026"` and verifying the name is pre-filled while
remaining fields are still prompted.

**Acceptance Scenarios**:

1. **Given** the user runs `/ea-new Acme Retail Transformation 2026`,
   **When** the system begins setup, **Then** "Acme Retail
   Transformation 2026" is used as the engagement name and the user is
   NOT prompted for name again.
2. **Given** the inline name contains special characters, **When** the
   slug is generated, **Then** it is lowercased, spaces replaced with
   hyphens, and special characters removed (e.g., "Acme & Partners
   (2026)" becomes `acme-partners-2026`).

---

### User Story 3 - Duplicate Engagement Detection (Priority: P2)

An enterprise architect attempts to create an engagement whose slug
matches an existing engagement directory. The system detects the conflict
and asks the user whether to open the existing engagement or choose a
different name.

**Why this priority**: Prevents accidental data loss from overwriting an
existing engagement. Shares priority with US2 as both are essential
safety and usability features.

**Independent Test**: Can be tested by creating an engagement, then
attempting to create another with the same name. Verify the conflict
is detected and no data is overwritten.

**Acceptance Scenarios**:

1. **Given** `EA-projects/acme-retail-2026/` already exists, **When**
   the user runs `/ea-new Acme Retail 2026`, **Then** the system
   informs the user that the engagement already exists and offers two
   options: open the existing engagement or provide a different name.
2. **Given** the user chooses to provide a different name, **When** they
   enter a new name, **Then** the system continues with the standard
   creation flow using the new name.

---

### User Story 4 - Confirmation and Edit Before Save (Priority: P2)

After collecting all fields, the system displays a formatted summary of
the engagement configuration. The user can accept, edit individual fields,
or cancel entirely. Only upon explicit confirmation does the system
create the directory structure and write files.

**Why this priority**: Prevents mistakes from typos or wrong selections.
Without review-before-save, users must manually fix `engagement.json`
or recreate the engagement.

**Independent Test**: Can be tested by completing all prompts, verifying
the summary is displayed, editing one field, and confirming. Verify the
final `engagement.json` reflects the edited value.

**Acceptance Scenarios**:

1. **Given** all fields have been collected, **When** the confirmation
   summary is displayed, **Then** it shows all field names and values
   in a readable format.
2. **Given** the user chooses to edit a field, **When** they select a
   field and provide a new value, **Then** the summary updates to
   reflect the change and the user is asked to confirm again.
3. **Given** the user chooses to cancel, **When** the cancellation is
   confirmed, **Then** no directories or files are created.

---

### User Story 5 - TOGAF Preliminary Phase Scaffolding (Priority: P2)

Upon engagement creation, the system automatically generates starter
artifacts for the TOGAF Preliminary phase based on the selected
engagement type and architecture domains. These artifacts are created
from the plugin's templates with fields pre-populated where possible
and remaining fields marked as unanswered.

**Why this priority**: Scaffolding eliminates the manual step of running
`/ea-artifact` for each Preliminary deliverable. It gives users an
immediate starting point aligned with their engagement scope.

**Independent Test**: Can be tested by creating an engagement and
verifying that Preliminary phase artifacts (Architecture Principles,
Stakeholder Map) exist in `artifacts/` with correct template structure
and appropriate field markers.

**Acceptance Scenarios**:

1. **Given** a Greenfield engagement with all four domains selected,
   **When** the engagement is created, **Then** the `artifacts/`
   directory contains starter versions of Architecture Principles and
   Stakeholder Map templates.
2. **Given** an Assessment-only engagement, **When** the engagement is
   created, **Then** scaffolded artifacts are tailored to assessment
   scope (e.g., no migration-related sections in roadmap templates).
3. **Given** any engagement type, **When** starter artifacts are
   generated, **Then** all AI-suggested content is marked with
   `🤖 AI Draft — Review required` and unanswered fields are marked
   with `⚠️ Not answered`, per the plugin content policy.
4. **Given** the user deselected the Data domain, **When** artifacts are
   scaffolded, **Then** no Data Architecture-specific artifacts or
   sections are included.

---

### User Story 6 - Settings Integration (Priority: P3)

When creating a new engagement, the system reads plugin settings from
`.claude/ea-assistant.local.md` and stores the shared requirements
repository path in the engagement metadata. If no settings file exists,
the field defaults to empty.

**Why this priority**: Requirements repository integration is important
for enterprise workflows but the engagement can function without it.
This is additive configuration, not core creation logic.

**Independent Test**: Can be tested by creating a
`.claude/ea-assistant.local.md` file with a `requirementsRepoPath`
value, then running `/ea-new` and verifying `engagement.json` contains
the path. Also test without the settings file to confirm the default
empty value.

**Acceptance Scenarios**:

1. **Given** `.claude/ea-assistant.local.md` exists with
   `requirementsRepoPath: /shared/requirements`, **When** a new
   engagement is created, **Then** `engagement.json` contains
   `"requirementsRepoPath": "/shared/requirements"`.
2. **Given** `.claude/ea-assistant.local.md` does not exist, **When** a
   new engagement is created, **Then** `engagement.json` contains
   `"requirementsRepoPath": ""`.

---

### User Story 7 - Post-Creation Navigation (Priority: P3)

After successfully creating an engagement, the system displays a
confirmation summary and offers the user the choice to begin the
Preliminary phase immediately or return to the main menu.

**Why this priority**: Smooth workflow continuation improves user
experience but is not required for engagement creation itself.

**Independent Test**: Can be tested by completing `/ea-new` and verifying
the confirmation message includes engagement name, slug, folder location,
scaffolded artifacts list, and the navigation prompt.

**Acceptance Scenarios**:

1. **Given** an engagement is successfully created, **When** the
   confirmation is displayed, **Then** it shows the engagement name,
   slug, folder path (`EA-projects/{slug}/`), list of scaffolded
   artifacts, and two options: begin Preliminary phase or return to
   main menu.
2. **Given** the user chooses to begin the Preliminary phase, **When**
   the system proceeds, **Then** it transitions to the `/ea-phase Prelim`
   workflow for the newly created engagement.

---

### Edge Cases

- What happens when the user cancels midway through the prompts?
  The system abandons creation; no directories or files are written.
- What happens when the engagement name is extremely long (>100 chars)?
  The slug is truncated to a maximum of 60 characters while preserving
  readability. The full name is stored in `engagement.json`.
- What happens when `EA-projects/` directory does not exist yet?
  The system creates `EA-projects/` automatically before creating the
  engagement subdirectory.
- What happens when the user provides an empty name?
  The system re-prompts, explaining that a name is required.
- What happens when the user deselects all architecture domains?
  The system requires at least one domain to be selected and re-prompts.
- What happens when a template file for scaffolding is missing?
  The system skips that artifact, logs a warning, and continues creating
  the remaining artifacts. The confirmation summary notes which artifacts
  could not be scaffolded.

## Requirements *(mandatory)*

### Functional Requirements

- **FR-001**: The command MUST collect ten metadata fields: name
  (required), description (required), sponsor (required), organisation
  (required), scope (required), start date (required, default: today),
  status (default: Active), engagement type (required, one of:
  Greenfield, Brownfield, Assessment-only, Migration), target end date
  (optional), and architecture domains in scope (required, default: all
  four — Business, Data, Application, Technology).
- **FR-002**: The command MUST generate a URL-safe slug from the
  engagement name: lowercase, spaces to hyphens, special characters
  removed, maximum 60 characters.
- **FR-003**: The command MUST create the engagement directory structure
  with five subdirectories: `requirements/`, `artifacts/`, `diagrams/`,
  `uploads/`, `interviews/`.
- **FR-004**: The command MUST write a valid `engagement.json` file
  containing all collected metadata (including engagement type, target
  end date, and selected architecture domains), all ADM phases
  initialised to "Not Started", `currentPhase` set to "Prelim", and
  an empty `artifacts` array.
- **FR-005**: The command MUST detect and prevent overwriting an existing
  engagement directory with the same slug.
- **FR-006**: The command MUST accept the engagement name as an optional
  inline argument to `/ea-new`.
- **FR-007**: The command MUST read `requirementsRepoPath` from
  `.claude/ea-assistant.local.md` if the file exists, and store it in
  `engagement.json`.
- **FR-008**: The command MUST display a confirmation summary of all
  entered values before creating any files or directories, allowing the
  user to edit individual fields or cancel.
- **FR-009**: The command MUST scaffold starter artifacts for the TOGAF
  Preliminary phase upon engagement creation, appropriate to the selected
  engagement type and architecture domains.
- **FR-010**: The command MUST mark all AI-suggested content in
  scaffolded artifacts with `🤖 AI Draft — Review required` and
  unanswered fields with `⚠️ Not answered`.
- **FR-011**: The command MUST offer to begin the Preliminary phase or
  return to the main menu after successful creation.
- **FR-012**: The command MUST set `lastModified` in `engagement.json`
  to the creation timestamp.
- **FR-013**: The command MUST require at least one architecture domain
  to be selected.
- **FR-014**: The command MUST record which ADM phases are applicable
  based on the selected architecture domains (e.g., if Data domain is
  deselected, C-Data phase is marked not applicable).

### Key Entities

- **Engagement**: The top-level project entity. Key attributes: name,
  slug, description, sponsor, organisation, scope, startDate, targetEndDate,
  status, engagementType, architectureDomains, currentPhase,
  requirementsRepoPath, lastModified, phases, artifacts.
- **Engagement Type**: Classification of the engagement. Values:
  Greenfield (new architecture), Brownfield (transform existing),
  Assessment-only (current-state review), Migration (re-platform/re-host).
- **Architecture Domain**: A domain of architecture in scope. Values:
  Business, Data, Application, Technology. At least one MUST be selected.
- **ADM Phase**: A tracked stage within an engagement. Key attributes:
  status (Not Started | In Progress | Complete | On Hold | Not Applicable),
  startedAt, completedAt. There are 11 phases: Prelim, Requirements,
  A through H. Phases may be marked Not Applicable based on domain
  selection.
- **Plugin Settings**: Configuration read from
  `.claude/ea-assistant.local.md`. Key attribute: requirementsRepoPath.

## Success Criteria *(mandatory)*

### Measurable Outcomes

- **SC-001**: Users can create a new engagement and have it ready for
  use within 2 minutes of invoking `/ea-new`.
- **SC-002**: 100% of created engagements have a valid `engagement.json`
  file with all required fields populated and all ADM phases initialised.
- **SC-003**: No existing engagement data is lost or overwritten when a
  duplicate slug is detected.
- **SC-004**: Users who provide the engagement name inline skip the name
  prompt and complete setup faster than the fully-prompted flow.
- **SC-005**: 100% of created engagement directories contain all five
  required subdirectories and at least one scaffolded Preliminary phase
  artifact.
- **SC-006**: 100% of scaffolded artifacts follow the plugin content
  policy (AI Draft markers, unanswered field markers).
- **SC-007**: Users can review and edit any field before the engagement
  is created, reducing setup errors to zero for confirmed engagements.

## Assumptions

- The working directory is the plugin's project root, and `EA-projects/`
  is created relative to it.
- Only one user interacts with the engagement at a time (no concurrent
  creation of the same engagement).
- The slug generation algorithm (lowercase, hyphens, no special chars)
  is sufficient for all expected engagement names.
- Status defaults to "Active" because most engagements are created when
  work is about to begin.
- Start date defaults to today because most engagements begin on the day
  they are initiated.
- The four engagement types (Greenfield, Brownfield, Assessment-only,
  Migration) cover the majority of real-world EA engagement patterns.
- Preliminary phase artifacts (Architecture Principles, Stakeholder Map)
  are universally applicable across all engagement types and are
  appropriate as default scaffolded artifacts.
- The mapping of engagement type and domain selection to applicable ADM
  phases and scaffolded artifacts will be defined during implementation
  planning.
