# Claude Plugins — Developer Guide

## Repository Layout

```
plugins/<plugin-name>/          plugin source (one directory per plugin)
.claude-plugin/marketplace.json marketplace index listing all plugins
.github/scripts/                CI helper scripts (TypeScript, run via Bun)
.github/workflows/              GitHub Actions workflows
```

## Adding a New Plugin

1. Create `plugins/<plugin-name>/` with the standard plugin structure.
2. Add an entry to `.claude-plugin/marketplace.json`.
3. Validate frontmatter locally before pushing (see below).

### Required Plugin Structure

```
plugins/<plugin-name>/
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
