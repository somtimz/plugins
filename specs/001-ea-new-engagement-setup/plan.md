# Implementation Plan: EA New Engagement Setup

**Branch**: `001-ea-new-engagement-setup` | **Date**: 2026-03-19 | **Spec**: [spec.md](./spec.md)
**Input**: Feature specification from `/specs/001-ea-new-engagement-setup/spec.md`

## Summary

Enhance the existing `/ea-new` command with three capabilities: richer
engagement metadata (engagement type, target end date, architecture
domains), smarter UX (confirmation summary with edit-before-save), and
TOGAF-aware scaffolding (auto-generate Preliminary phase starter
artifacts based on engagement type and domain selection). The command
file at `commands/ea-new.md` will be updated, the engagement lifecycle
skill will be extended, and a new scaffolding mapping configuration
will be added.

## Technical Context

**Language/Version**: Markdown (Claude Code plugin command definitions)
**Primary Dependencies**: Claude Code plugin framework, existing
  `ea-engagement-lifecycle` skill, existing artifact templates
**Storage**: JSON files (`engagement.json` per engagement), Markdown
  artifact files in `artifacts/`
**Testing**: Manual verification via `/ea-new` invocation
**Target Platform**: Claude Code CLI with plugin support
**Project Type**: Claude Code plugin (Markdown command + skill files)
**Performance Goals**: Engagement creation completes within 2 minutes
  of user interaction
**Constraints**: Must be backward-compatible with any existing
  engagements created by the current `/ea-new` command
**Scale/Scope**: Single-user CLI tool, one engagement at a time

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

| Principle | Status | Notes |
|-----------|--------|-------|
| I. Framework Fidelity | PASS | Engagement types map to documented TOGAF ADM tailoring patterns. ADM phases use standard names. Domain-to-phase mapping follows TOGAF convention (B=Business, C-Data=Data, C-App=Application, D=Technology). |
| II. User-Sourced Content | PASS | Scaffolded artifacts use `🤖 AI Draft — Review required` markers. Unanswered fields use `⚠️ Not answered`. No content is silently fabricated. |
| III. Plugin Architecture | PASS | Changes are scoped to `commands/ea-new.md`, `skills/ea-engagement-lifecycle/`, and `templates/`. Frontmatter remains valid. Version bump in `plugin.json`. |
| IV. Engagement Isolation | PASS | Each engagement remains in its own `EA-projects/{slug}/` directory. No cross-engagement reads or writes. |
| V. Template-Driven Artifacts | PASS | Scaffolded artifacts are generated from existing templates in `templates/`. New artifact types require new templates first. |
| Development Workflow | PASS | Backward-compatible: existing `engagement.json` files without new fields (`engagementType`, `architectureDomains`, `targetEndDate`) are handled gracefully by defaulting. |

**Gate result**: PASS — all principles satisfied. Proceed to Phase 0.

## Project Structure

### Documentation (this feature)

```text
specs/001-ea-new-engagement-setup/
├── plan.md              # This file
├── research.md          # Phase 0 output
├── data-model.md        # Phase 1 output
├── quickstart.md        # Phase 1 output
├── contracts/           # Phase 1 output
└── tasks.md             # Phase 2 output (/speckit.tasks)
```

### Source Code (plugin directory)

```text
plugins/ea-assistant/
├── commands/
│   └── ea-new.md                          # MODIFY: enhanced command definition
├── skills/
│   └── ea-engagement-lifecycle/
│       ├── SKILL.md                       # MODIFY: add domain/type guidance
│       └── references/
│           ├── adm-phase-guide.md         # NO CHANGE
│           ├── engagement-patterns.md     # NO CHANGE
│           └── scaffolding-map.md         # NEW: type+domain → artifact mapping
├── templates/
│   ├── architecture-principles.md         # NO CHANGE (used by scaffolding)
│   └── stakeholder-map.md                # NO CHANGE (used by scaffolding)
└── .claude-plugin/
    └── plugin.json                        # MODIFY: version bump
```

**Structure Decision**: This is an enhancement to an existing Claude Code
plugin. All changes are within the `plugins/ea-assistant/` directory.
No new top-level directories are needed. The main deliverable is an
updated command file (`ea-new.md`) supported by a new reference file
(`scaffolding-map.md`) that defines which artifacts are scaffolded for
each engagement type and domain combination.

## Complexity Tracking

> No constitution violations. No complexity justification needed.
