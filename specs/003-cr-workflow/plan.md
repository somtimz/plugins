# Implementation Plan: Change Request Workflow

**Branch**: `003-cr-workflow` | **Date**: 2026-03-20 | **Spec**: [spec.md](spec.md)
**Input**: Feature specification from `/specs/003-cr-workflow/spec.md`

## Summary

Build the complete ITIL-assistant plugin with two skills (`itil-change-request`, `cab-review`), two slash commands (`/itil-cr`, `/cab-review`), and supporting reference files (JSX artifacts, docx template). The plugin manages the full ITIL v4 change request lifecycle: creation, submission, CAB review, approval/rejection, checklist tracking, and Word document export. All interactive UIs are React JSX artifacts rendered in Claude's artifact viewer, with data persisted via `window.storage`.

## Technical Context

**Language/Version**: Markdown (plugin instruction files) + React JSX (artifact apps) + Node.js (docx export scripts)
**Primary Dependencies**: Claude Code plugin framework (auto-discovery), React (artifact runtime), `docx` npm package (Word export)
**Storage**: `window.storage` (key-value, JSON-serialized) — browser-side persistence in Claude's artifact viewer
**Testing**: Manual Claude Code session verification — trigger each skill/command and verify artifact rendering and storage behavior
**Target Platform**: Claude Code (CLI + artifact viewer) on macOS, Linux, Windows (WSL)
**Project Type**: Claude Code plugin (Markdown instructions + JSX artifacts)
**Performance Goals**: N/A — single-user, local interaction
**Constraints**: All component files must follow Claude Code plugin conventions (kebab-case, correct directory placement, valid YAML frontmatter)
**Scale/Scope**: 2 skills, 2 commands, 2 JSX reference files, 1 docx template, ~1200 lines of JSX total

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

| Principle | Status | Notes |
|-----------|--------|-------|
| I. Standard Directory Layout | PASS | `skills/itil-change-request/SKILL.md`, `skills/cab-review/SKILL.md`, `commands/itil-cr.md`, `commands/cab-review.md` — all at plugin root, kebab-case |
| II. Skill-First Design | PASS | Two skills with broad trigger descriptions; commands are thin wrappers; JSX in `references/` not inlined |
| III. ITIL v4 Compliance | PASS | Status flow enforced (Draft → Pending → Approved/Rejected); emergency bypass documented; separation of duties (two skills); cabHistory for audit |
| IV. Persistent Storage | PASS | Shared `cr_index` + `cr_{id}` schema; both skills read/write same keys; `updatedAt` on every write; graceful empty-state handling |
| V. Simplicity | PASS | Minimum components: 2 skills, 2 commands, no agents, no hooks logic, no MCP servers |

No violations. Gate passes.

## Project Structure

### Documentation (this feature)

```text
specs/003-cr-workflow/
├── plan.md              # This file
├── research.md          # Phase 0 output
├── data-model.md        # Phase 1 output
├── quickstart.md        # Phase 1 output
├── contracts/           # Phase 1 output (storage contract)
└── tasks.md             # Phase 2 output (/speckit.tasks)
```

### Source Code (plugin root)

```text
plugins/ITIL-assistant/
├── .claude-plugin/
│   └── plugin.json                          # Plugin manifest
├── skills/
│   ├── itil-change-request/
│   │   ├── SKILL.md                         # Skill instructions + frontmatter
│   │   └── references/
│   │       ├── cr-app.jsx                   # CR management artifact (React JSX)
│   │       └── docx-template.md             # Word export template guide
│   └── cab-review/
│       ├── SKILL.md                         # Skill instructions + frontmatter
│       └── references/
│           └── cab-review-app.jsx           # CAB review artifact (React JSX)
├── commands/
│   ├── itil-cr.md                           # /itil-cr command
│   └── cab-review.md                        # /cab-review command
├── hooks/
│   └── hooks.json                           # Empty (no hooks needed)
├── README.md
├── LICENSE
└── .gitignore
```

**Structure Decision**: Claude Code plugin layout — all components at plugin root following convention-over-configuration. No `src/` or `tests/` directories needed; the deliverables are Markdown instruction files and JSX artifacts.

## Complexity Tracking

No violations to justify.
