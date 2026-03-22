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

## Active Technologies
- Python 3.11+ + Flask, anthropic, chromadb, openai (embedding client) (RAG-assistant)
- ChromaDB (vector store), SQLite (registry) (RAG-assistant)
- Markdown (Claude Code plugin instruction files) + Claude Code plugin framework (commands/, skills/, agents/) (002-ea-project-management)
- JSON files (`engagement.json`) and directory structure (`EA-projects/`) (002-ea-project-management)

## Recent Changes
- RAG-assistant/001-rag-search-transparency: Added transparent RAG search — chunk panel, inspect prompt, inline citations
