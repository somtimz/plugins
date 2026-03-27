# Claude Plugins — Developer Guide

## Repository Layout

```
<plugin-name>/          plugin source (one directory per plugin)
.claude-plugin/marketplace.json marketplace index listing all plugins
.github/scripts/                CI helper scripts (TypeScript, run via Bun)
.github/workflows/              GitHub Actions workflows
```

## Adding a New Plugin

1. Create `<plugin-name>/` at the repo root with the standard plugin structure.
2. Add an entry to `.claude-plugin/marketplace.json`.
3. Validate frontmatter locally before pushing (see below).

### Required Plugin Structure

```
<plugin-name>/
├── .claude-plugin/plugin.json   # required: name, version, description, author
├── README.md                    # required
├── LICENSE                      # required
├── .gitignore                   # recommended
├── agents/                      # agent .md files
├── commands/                    # slash command .md files
├── skills/                      # skill directories (each with SKILL.md)
├── hooks/hooks.json             # optional lifecycle hooks
└── templates/                   # optional document templates
```

### `plugin.json` Required Fields

```json
{
  "name": "kebab-case-name",
  "version": "0.1.0",
  "description": "One-line description",
  "author": { "name": "...", "email": "..." }
}
```

## Frontmatter Rules

All `agents/*.md`, `commands/*.md`, and `skills/*/SKILL.md` files must have valid YAML frontmatter. The CI workflow (`validate-frontmatter.yml`) enforces this on every PR using `.github/scripts/validate-frontmatter.ts`.

**Agent frontmatter** — required fields: `name`, `description`, `model`, `color`

**Command frontmatter** — required fields: `name`, `description`

**Skill frontmatter** — required fields: `name`, `description`, `version`

## CI Workflows

| Workflow | Trigger | Purpose |
|---|---|---|
| `validate-frontmatter.yml` | PR touching agents/skills/commands | Validates YAML frontmatter |
| `close-external-prs.yml` | Any PR opened | Closes PRs from non-maintainers |

## Versioning

Plugins use semantic versioning (`MAJOR.MINOR.PATCH`). Bump `version` in both `plugin.json` and the skill `SKILL.md` frontmatter when releasing changes.

## Commit Style

Use conventional commits:

```
feat(plugin-name): add ...
fix(plugin-name): correct ...
docs(plugin-name): update ...
chore: ...
```

## Response Formatting

When displaying answers to questions or presenting any multi-item information:

- **Use bullet points** for lists of facts, options, steps, or items — never run them together as prose
- **Use numbered lists** when sequence or priority matters (steps, ranked options)
- **Use a table** when comparing two or more items across the same attributes
- **Bold the lead word or phrase** of each bullet to make it scannable at a glance
- Keep each bullet to one clear idea; split compound thoughts into separate bullets
- Use plain prose only for single-sentence answers or narrative explanations where no list is appropriate

## Active Technologies
- Python 3.11+ + Flask, anthropic, chromadb, openai (embedding client) (RAG-assistant)
- ChromaDB (vector store), SQLite (registry) (RAG-assistant)
- Python 3.11+ + python-docx, python-pptx (ea-assistant artifact generation scripts)
- Markdown (Claude Code plugin instruction files) + Claude Code plugin framework (commands/, skills/, agents/) (ea-assistant, RAG-assistant, ITIL-assistant)
- JSON files (`engagement.json`) and directory structure (`EA-projects/`) (ea-assistant)
- React JSX (artifact apps for interview UI and brainstorm pad) — rendered as Claude artifacts or written to disk as standalone HTML (ea-assistant)
- `window.localStorage` (key-value, JSON-serialized) — browser-side persistence in Claude's artifact viewer (ITIL-assistant)

## Recent Changes
- ea-assistant v0.9.0: Motivation framework — Architecture Vision restructured with §2 Business Drivers (DRV-NNN), §3 Goals (G-NNN), §4 Objectives (OBJ-NNN), §5 Issues (ISS-NNN), §6 Problems (PRB-NNN), §7 Strategic Direction Summary (Strategies + Metrics); 15 sections total; ID scheme reference and section markers in Phase A interview
- ea-assistant v0.9.0: `/ea-grill` command — deep-review any artifact using grill-me skills with auto-skill selection by artifact type (9 skills); review output saved to `reviews/` folder
- ea-assistant v0.9.0: EA concepts expanded from 5 to 8 (added Objective, Issue, Problem); `/ea-new` collects `engagementType`; `/ea-publish` pre-publish compliance check; Requirements Register Motivation field for traceability; research agent integration during interviews
- grill-me v0.4.0: Consolidated to 9 skills — added software-design, infra-design, artifact, diagram; premortem dual Generate/Review mode; removed redundant strategy and boardroom skills
- ea-assistant v0.8.0: Artifact compliance check — three-tier rule set (frontmatter, template structure, artifact-specific); compliance prompt on every artifact load (achieve compliance / accept as-is / view details); complianceNote frontmatter field; non-standard artifact flag in /ea-status and /ea-publish
- ea-assistant v0.8.0: Shortcuts reference shown at interview start; `?`/`help` contextual help (artifact purpose, phase context, concept hint, opt-out reminder); `concepts` quick reference for Principle/Goal/Strategy/Plan/Risk
- ea-assistant v0.8.0: Opt-out tracking — `opt-out` (question) and `opt-out artifact`; ⊘ answer state marker; engagement.json optOuts[] array with reason/timestamp; flagged in /ea-status, /ea-publish, and session log
- ea-assistant v0.8.0: Interview session tracking — step 0 collects facilitator/participants; prior session summary on new session start; session-log.md per engagement; next-logical-step inference (5-rule priority); facilitator/participants in interview note frontmatter
- ea-assistant v0.8.0: Interview quality — ea-concepts.md canonical reference (Principle/Goal/Strategy/Plan/Risk with TOGAF/ArchiMate alignment, disambiguation checklist); cross-topic detection step 7b with 10-artifact signal map; concept-check prompt step 7c
- ea-assistant v0.7.0: Decision Register — `/ea-decisions` command aggregates Appendix A3 rows from all artifacts into a cross-artifact register; governance states (Provisional/Awaiting/Verified/Voted/Fiat/Returned); A3 Decision Log appendix added to 5 key templates; filter flags (--audience, --owner, --domain, --authority, --cost, --impact, --risk, --subject, --status); audience presets (executive/architect/business/technical); inline status mode
- ea-assistant v0.7.0: Business Model Canvas template (Phase B) with BMC interview question bank (27 questions, output routing, facilitation notes); corporate vs project requirements distinction — scope field, edit protection, Waived status with justification enforcement, sync auto-tagging, backward-compatible migration; scaffolding-map reference added
- repo: Flattened plugin directory structure — all plugins now live at repo root instead of inside `plugins/` subfolder
- ea-assistant v0.6.0: Interview mode selection (Text default, Web, Display); markdown checklists on enumerated questions; Phase F Migration Planning interview; version display in `/ea-help` and `/ea-status`; governance framework reference with diagrams; `/ea-brainstorm` command; `/ea-publish` command (replaces `/ea-merge`)
- ea-assistant v0.5.0: ITIL-assistant plugin added; ADM governance framework added; interview UI React artifacts for web mode
- ea-assistant v0.4.0: Artifact generation (Word/PPTX/Mermaid), phase interview question bank, requirements analyst agent, ADM reference material; togaf-adm plugin retired and merged
- RAG-assistant v0.1.0: Transparent RAG search — chunk panel, inspect prompt, inline citations
- ITIL-assistant v0.1.0: Change Request management and CAB review workflow with React artifact UI
