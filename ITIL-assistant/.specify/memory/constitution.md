<!--
SYNC IMPACT REPORT
==================
Version change: 1.0.0 → 1.0.1 (PATCH — clarified Emergency bypass exception in Principle III;
aligns constitution with user-approved clarification from speckit.clarify session 2026-03-20)

Modified principles:
  - III. ITIL v4 Compliance: added explicit Emergency change bypass exception to "no skip states" rule

Added sections:
  - None

Removed sections:
  - None

Templates reviewed:
  - .specify/templates/plan-template.md        ✅ no changes needed
  - .specify/templates/spec-template.md        ✅ no changes needed
  - .specify/templates/tasks-template.md       ✅ no changes needed
  - .specify/templates/constitution-template.md ✅ no changes needed

Follow-up TODOs:
  - None
-->

# ITIL-assistant Constitution

## Core Principles

### I. Standard Directory Layout (Convention-Over-Configuration)

The plugin MUST follow the Claude Code standard directory structure exactly. Auto-discovery
depends on convention; deviating from it silently breaks component loading.

- `.claude-plugin/plugin.json` MUST exist and be the sole manifest — no metadata outside it
- Component directories (`commands/`, `agents/`, `skills/`, `hooks/`) MUST live at
  the plugin root, NOT inside `.claude-plugin/`
- Only create directories for component types the plugin actually uses — no empty scaffolding
- All directory and file names MUST use kebab-case; no camelCase, no underscores, no spaces
- Commands → `.md` files in `commands/`; Agents → `.md` files in `agents/`;
  Skills → subdirectory per skill with a `SKILL.md` file;
  Hooks → `hooks/hooks.json`
- Each skill subdirectory MAY contain a `references/` directory for supporting files
  (JSX artifacts, templates, reference docs) that the skill reads at runtime

**Rationale**: Claude Code's auto-discovery is purely convention-based. A misnamed file or
wrongly-nested directory simply does not load — there is no error, just silent absence.

### II. Skill-First Design with Artifact Rendering

Skills are the primary unit of reusable, context-triggered behavior. This plugin's skills
deliver interactive React JSX artifacts rendered in Claude's artifact viewer.

- Skills MUST auto-activate via their `description` frontmatter field — descriptions MUST
  list concrete trigger phrases the user is likely to say
- Each `SKILL.md` MUST include valid YAML frontmatter with `name`, `description`, and
  `version` fields; missing frontmatter causes silent non-loading
- Skills that render interactive apps MUST store the app source in `references/*.jsx` and
  instruct the agent to present it as a React JSX artifact — never inline large JSX in SKILL.md
- Skills MUST be self-contained: they MUST NOT assume state from a prior skill invocation
  (storage initialization MUST handle the "first run" case gracefully)
- Commands are thin wrappers that invoke the corresponding skill — they MUST NOT duplicate
  the skill's logic

**Rationale**: The plugin's value is in interactive artifact apps. Keeping JSX in reference
files keeps SKILL.md readable and the artifact source maintainable. Broad trigger phrases
ensure users find the tool without memorizing exact command names.

### III. ITIL v4 Compliance

All change management workflows MUST conform to ITIL v4 Change Enablement practices.
Deviating from the standard undermines the plugin's purpose.

- Change Requests MUST follow the status flow: Draft → Pending CAB Approval → Approved by CAB / Rejected
- The CR schema MUST include all ITIL-required fields: change type (Standard/Normal/Emergency),
  risk assessment, implementation steps, rollback plan, validation criteria, and approver list
- Status transitions MUST be enforced — a CR MUST NOT skip states (e.g., Draft directly to
  Approved). **Exception**: Emergency change requests (changeType === "Emergency") MAY
  transition directly from Draft to "Approved by CAB" (auto-approved) and MUST set
  `retrospectiveReview: true`. The CAB reviews emergency changes post-implementation.
  This exception is intentional per ITIL v4 Change Enablement, which treats emergency
  changes as requiring expedited processing outside the standard CAB cycle.
- CAB review MUST be a separate skill/workflow from CR authoring — separation of duties
  between requester and approver is non-negotiable
- Word document exports MUST produce formal, print-ready documents suitable for
  CAB submission and audit trail

**Rationale**: Organizations adopt this plugin to enforce ITIL discipline. If the tool
allows shortcuts that bypass the change management process, it actively harms governance.

### IV. Persistent Storage via `window.storage`

All CR data MUST persist between sessions using `window.storage`. The storage schema
MUST be consistent across all skills that read or write CR data.

- The index key `cr_index` MUST be a JSON array of RFC IDs
- Individual CR records MUST be stored under `cr_{id}` as JSON strings
- All skills that modify CR data MUST update the `updatedAt` timestamp
- Storage reads MUST handle missing keys gracefully (first-run scenario)
- The `cab-review` skill MUST read and write the same storage keys as `itil-change-request` —
  no separate data stores

**Rationale**: Shared storage is the integration contract between the CR authoring and
CAB review skills. Diverging schemas or key conventions silently break cross-skill workflows.

### V. Simplicity & Incremental Complexity

Deliver the minimum component set that satisfies the requirement. Every component added
is a component that must be maintained, debugged, and documented.

- YAGNI: do not scaffold component types the current feature does not need
- The `plugin.json` manifest MUST remain lean — use auto-discovery; only add explicit paths
  when the default location genuinely does not work
- No helper abstractions until a second concrete reuse case exists
- Prefer a single well-scoped skill over multiple overlapping skills with ambiguous triggers
- Dependencies (npm packages, external binaries) MUST be justified by a current concrete
  need, not future flexibility

**Rationale**: Plugin complexity compounds — each hook, agent, and skill adds surface area
for breakage. The smallest plugin that works is the easiest to ship and maintain.

## Technology Stack

- **Manifest**: JSON (`plugin.json`) — semantic versioning, kebab-case name, minimal fields
- **Commands / Agents / Skills**: Markdown with YAML frontmatter
- **Hook configuration**: JSON (`hooks/hooks.json`)
- **Interactive apps**: React JSX artifacts (stored in `references/*.jsx`)
- **Data persistence**: `window.storage` (key-value, JSON-serialized)
- **Document export**: `docx` npm package via Node.js script, with template guidance
  in `references/docx-template.md`
- **Testing**: Manual Claude Code session verification for Markdown components;
  interactive artifact testing for JSX apps

- **Plugin name**: `"name": "ITIL-assistant"` (in `.claude-plugin/plugin.json`)
- **Component types in scope**: commands, skills, hooks — agents added only when needed

## Development Workflow

- All features MUST begin with a spec (`/speckit.specify`) before any planning or coding
- Implementation plans MUST include a Constitution Check gate (Principles I–V compliance)
- Before marking any skill or command complete, it MUST be triggered in an active Claude
  Code session and observed to behave as specified
- Interactive artifact apps MUST be tested end-to-end: create a CR, submit to CAB,
  approve/reject via cab-review, verify storage state
- Every PR MUST verify: correct file naming, correct directory placement, valid frontmatter,
  and consistent storage schema across skills
- Commits MUST use conventional commit format: `feat(ITIL-assistant):`, `fix(ITIL-assistant):`, etc.

## Governance

This constitution supersedes all other development practices and informal agreements. It is
the authoritative source of non-negotiable rules for the ITIL-assistant project.

**Amendment procedure**:
1. Propose amendment with rationale in a PR modifying this file
2. Run `/speckit.constitution` to propagate changes to dependent templates
3. Bump version according to semantic versioning rules (see below)
4. Update `LAST_AMENDED_DATE` to the date of merge

**Versioning policy**:
- MAJOR: Principle removed, renamed in a breaking way, or governance model restructured
- MINOR: New principle or section added; material expansion of existing guidance
- PATCH: Clarification, wording fix, typo, non-semantic refinement

**Compliance review**: All PRs and code reviews MUST verify compliance with Principles I–V.
Violations require an entry in the Complexity Tracking table before merge is permitted.

**Version**: 1.0.1 | **Ratified**: 2026-03-20 | **Last Amended**: 2026-03-21
