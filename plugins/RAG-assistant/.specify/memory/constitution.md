<!--
SYNC IMPACT REPORT
==================
Version change: 2.0.1 → 2.0.2 (PATCH — added Python file naming exception to Principle I;
clarifies that kebab-case applies to .md/.json component files; Python .py files use PEP 8 snake_case)

Modified principles:
  - None

Added sections:
  - None

Removed sections:
  - None

Templates reviewed:
  - .specify/templates/plan-template.md    ✅ no changes needed
  - .specify/templates/spec-template.md    ✅ no changes needed
  - .specify/templates/tasks-template.md   ✅ no changes needed
  - .specify/templates/constitution-template.md ✅ no changes needed

Follow-up TODOs:
  - None (all previously deferred items resolved)
-->

# RAG-plugin Constitution

## Core Principles

### I. Standard Directory Layout (Convention-Over-Configuration)

The plugin MUST follow the Claude Code standard directory structure exactly. Auto-discovery
depends on convention; deviating from it silently breaks component loading.

- `.claude-plugin/plugin.json` MUST exist and be the sole manifest — no metadata outside it
- Component directories (`commands/`, `agents/`, `skills/`, `hooks/`, scripts/) MUST live at
  the plugin root, NOT inside `.claude-plugin/`
- Only create directories for component types the plugin actually uses — no empty scaffolding
- All directory and file names MUST use kebab-case; no camelCase, no underscores, no spaces
- **Exception**: Python source files (`.py`) MUST follow PEP 8 snake_case naming conventions (`registry.py`, `test_config.py`). The kebab-case rule applies exclusively to plugin component files (`.md`, `.json`) and non-Python scripts.
- Commands → `.md` files in `commands/`; Agents → `.md` files in `agents/`;
  Skills → subdirectory per skill with a `SKILL.md` file (not README.md or any other name);
  Hooks → `hooks/hooks.json`; MCP servers → `.mcp.json` at plugin root

**Rationale**: Claude Code's auto-discovery is purely convention-based. A misnamed file or
wrongly-nested directory simply does not load — there is no error, just silent absence.
Strict layout compliance eliminates an entire class of integration bugs.

### II. Skill-First Design

Skills are the primary unit of reusable, context-triggered behavior. Every repeatable
workflow SHOULD be expressed as a skill before considering a command or agent.

- Skills MUST auto-activate via their `description` frontmatter field — if a description
  requires an exact incantation to trigger, it is too narrow; rewrite it
- Each `SKILL.md` MUST include valid YAML frontmatter with `name`, `description`, and
  `version` fields; missing frontmatter causes silent non-loading
- Skills MUST be self-contained: they MUST NOT assume state from a prior skill invocation
- Commands are for explicit user-invoked actions; agents are for autonomous sub-task
  delegation; skills are for reusable procedural guidance — use the right component type
- A skill MUST document exactly when it applies and when it does NOT in its description

**Rationale**: Skills are the mechanism for encoding expert workflows into the agent's
behavior without requiring users to invoke commands explicitly. Poorly scoped skill
descriptions cause under-triggering (missed activations) or over-triggering (noise).

### III. Test-First Development (NON-NEGOTIABLE)

All scripted logic (hook scripts, MCP server code, utility scripts) MUST have tests written
before implementation. Declarative files (Markdown, JSON manifests) MUST be validated
against a working Claude Code session before a feature is considered complete.

- Hook scripts MUST be tested in isolation before wiring into `hooks.json`
- MCP server tools MUST have contract tests covering inputs, outputs, and error paths
- Every skill MUST be manually triggered and verified in a Claude Code session as its
  acceptance test — "it looks right" is not a passing test
- Regression: if a component stops loading or stops triggering, a test or validation step
  MUST be added to catch it next time

**Rationale**: Plugin components fail silently (wrong frontmatter, wrong file name,
wrong path). Without explicit verification steps, broken components ship undetected.

### IV. Portability & Platform Parity

The plugin MUST run without modification on macOS, Linux, and Windows (WSL). Hardcoded
paths are a build-time defect, not a runtime concern.

- All intra-plugin path references in hooks, MCP configs, and scripts MUST use the
  `CLAUDE_PLUGIN_ROOT` environment variable — never hardcode absolute paths
- Scripts MUST use portable constructs (POSIX sh or Python 3.8+) — no bash-only syntax
  unless the plugin explicitly declares `bash` as a prerequisite
- Hook and MCP command invocations MUST use the form:
  `"command": "bash $CLAUDE_PLUGIN_ROOT/scripts/tool.sh"` — not `./scripts/tool.sh`
- External tool dependencies (node, python, jq, etc.) MUST be declared in the manifest
  and documented in the plugin README

**Rationale**: Plugins install in user-specific locations that vary by OS and installation
method. A path that works on the author's machine will silently break on any other system.

### V. Simplicity & Incremental Complexity

Deliver the minimum component set that satisfies the requirement. Every component added
is a component that must be maintained, debugged, and documented.

- YAGNI: do not scaffold component types the current feature does not need
- The `plugin.json` manifest MUST remain lean — use auto-discovery; only add explicit paths
  when the default location genuinely does not work
- No helper abstractions until a second concrete reuse case exists
- Prefer a single well-scoped skill over multiple overlapping skills with ambiguous triggers
- Dependencies (npm packages, pip packages, external binaries) MUST be justified by a
  current concrete need, not future flexibility

**Rationale**: Plugin complexity compounds — each hook, MCP server, and agent adds
surface area for breakage. The smallest plugin that works is the easiest to ship and
maintain.

## Technology Stack

- **Manifest**: JSON (`plugin.json`) — semantic versioning, kebab-case name, minimal fields
- **Commands / Agents / Skills**: Markdown with YAML frontmatter
- **Hook configuration**: JSON (`hooks/hooks.json`)
- **Hook & utility scripts**: POSIX sh or Python 3.8+ (portable; bash only if declared)
- **MCP servers**: Node.js (preferred) or Python; defined in `.mcp.json`
- **Testing**: Manual Claude Code session verification for Markdown components;
  unit tests (pytest / Jest) for any scripted logic

- **Plugin name**: `"name": "rag-plugin"` (in `.claude-plugin/plugin.json`)
- **Component types in scope**: commands, agents, skills, hooks, MCP servers — all five
  component directories MUST be present at plugin root

## Development Workflow

- All features MUST begin with a spec (`/speckit.specify`) before any planning or coding
- Implementation plans MUST include a Constitution Check gate (Principles I–V compliance)
- Before marking any skill or command complete, it MUST be triggered in an active Claude
  Code session and observed to behave as specified
- Every PR MUST verify: correct file naming, correct directory placement, valid frontmatter,
  and that all path references use `CLAUDE_PLUGIN_ROOT`
- Complexity violations MUST be documented in the plan's Complexity Tracking table and
  reviewed before implementation proceeds
- Commits MUST be atomic and reference the task ID from `tasks.md`

## Governance

This constitution supersedes all other development practices and informal agreements. It is
the authoritative source of non-negotiable rules for the RAG-plugin project.

**Amendment procedure**:
1. Propose amendment with rationale in a PR modifying this file
2. Run `/speckit.constitution` to propagate changes to dependent templates
3. Bump version according to semantic versioning rules (see header comment)
4. Update `LAST_AMENDED_DATE` to the date of merge

**Versioning policy**:
- MAJOR: Principle removed, renamed in a breaking way, or governance model restructured
- MINOR: New principle or section added; material expansion of existing guidance
- PATCH: Clarification, wording fix, typo, non-semantic refinement

**Compliance review**: All PRs and code reviews MUST verify compliance with Principles I–V.
Violations require an entry in the Complexity Tracking table before merge is permitted.

**Version**: 2.0.2 | **Ratified**: 2026-03-15 | **Last Amended**: 2026-03-15
