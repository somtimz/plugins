# Implementation Plan: EA Project Management

**Branch**: `002-ea-project-management` | **Date**: 2026-03-20 | **Spec**: [spec.md](./spec.md)
**Input**: Feature specification from `/specs/002-ea-project-management/spec.md`

## Summary

Enhance the `/ea-open` and `/ea-status` commands to provide richer engagement information (type, domains, dates, phase-by-phase breakdown), add inline editing of engagement metadata, phase statuses, and artifact statuses via `/ea-open` next actions, and add archive/delete/restore capabilities for engagement lifecycle management.

## Technical Context

**Language/Version**: Markdown (Claude Code plugin instruction files)
**Primary Dependencies**: Claude Code plugin framework (commands/, skills/, agents/)
**Storage**: JSON files (`engagement.json`) and directory structure (`EA-projects/`)
**Testing**: Manual validation — invoke commands and verify output/file changes
**Target Platform**: Claude Code CLI plugin
**Project Type**: Claude Code plugin (Markdown instruction files, not executable code)
**Performance Goals**: N/A (conversational plugin, no runtime)
**Constraints**: Must maintain backward compatibility with pre-v0.2.0 engagements
**Scale/Scope**: 2 command files to modify (`ea-open.md`, `ea-status.md`), 1 skill file to update (`SKILL.md`)

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

| Principle | Status | Notes |
|-----------|--------|-------|
| I. Framework Fidelity | PASS | All changes align with TOGAF 10 ADM phases, Zachman classification, ArchiMate notation |
| II. User-Sourced Content (NON-NEGOTIABLE) | PASS | No content generation — this feature is about viewing and editing existing metadata |
| III. Plugin Architecture | PASS | Changes are to command `.md` files and skill `.md` files only |
| IV. Engagement Isolation | PASS | Each engagement remains in its own directory; archive uses `.archive/` subdirectory |
| V. Template-Driven Artifacts | PASS | No template changes needed; artifact metadata editing only touches `engagement.json` |

All gates pass. No violations to justify.

## Project Structure

### Documentation (this feature)

```text
specs/002-ea-project-management/
├── plan.md              # This file
├── research.md          # Phase 0 output
├── data-model.md        # Phase 1 output
├── quickstart.md        # Phase 1 output
├── contracts/           # Phase 1 output
└── tasks.md             # Phase 2 output (/speckit.tasks)
```

### Source Code (repository root)

```text
plugins/ea-assistant/
├── commands/
│   ├── ea-open.md       # MODIFY: enhanced picklist, summary, next actions with edit/archive/delete
│   └── ea-status.md     # MODIFY: enhanced dashboard with type, domains, dates, N/A-aware progress, archive section
├── skills/
│   └── ea-engagement-lifecycle/
│       └── SKILL.md     # MODIFY: document new status value "Completed", archive/restore lifecycle, editing workflows
└── .claude-plugin/
    └── plugin.json      # MODIFY: version bump 0.2.0 → 0.3.0
```

**Structure Decision**: This feature modifies existing command and skill files. No new files are created. The plugin structure remains unchanged.
