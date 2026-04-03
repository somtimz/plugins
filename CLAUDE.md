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
├── hooks/hooks.json             # optional lifecycle hooks — must be `{"hooks":{}}`, not `{}`
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

## Plugins & Marketplace

When working with plugins — listing, deduplicating, checking status — always look in the installed plugins directory (`~/.claude/plugins/`), not the source repo. Use `claude plugins list` or read `~/.claude/plugins/` directly.

## Repository Structure

This is a monorepo. When pushing new packages or plugins to GitHub, always confirm the correct subdirectory placement (e.g., `RAG-assistant/`, `ea-assistant/`) before committing. Don't assume flat layout.

## Tools & CLIs

- **spec-kit** — CLI tool installed via `uv`. Invoke as `uv run spec-kit <command>`. It is NOT a Claude Code plugin or marketplace item.

## Development Environment

This user is on Windows/WSL2. Before editing text files (especially YAML, JSON, Markdown), be aware that CRLF line endings can cause silent failures — particularly in YAML frontmatter and plugin config files. If an edit fails to apply correctly, check line endings.

## Testing & Verification

- After any fix to plugin configs or UI components, verify the fix actually worked — don't just say "fixed". For JSON: parse it. For plugin installs: run the command and show output.
- For web UI components (React, HTML), always test rendering in the browser before marking complete. UI rendering failures have occurred silently multiple times.
- After bulk multi-file changes, maintain and show a checklist. Mark each file complete only after verifying it. Don't batch-complete without evidence.

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

Plugins use semantic versioning (`MAJOR.MINOR.PATCH`). When releasing changes, bump `version` in `plugin.json` and in **all** `skills/*/SKILL.md` frontmatter files for that plugin.

## Change Workflow

### When to use a PR

Use a **feature branch + PR** for:
- Any new feature or capability spanning multiple files or sessions
- Changes to agent behaviour, skill logic, or interview flows
- New templates, commands, or skills
- Anything that warrants a review before merging

Process:
1. Create a branch: `git checkout -b feat/short-description`
2. Plan the change — outline what files will be touched and why before writing code
3. Implement in focused commits
4. Validate frontmatter: `~/.bun/bin/bun .github/scripts/validate-frontmatter.ts <plugin>/`
5. Open a PR: `gh pr create` with a clear summary and test plan
6. Merge only after review

### When to commit directly to main

Direct commits to `main` are acceptable for:
- Single-file bug fixes and typo corrections
- Version bumps, README updates, changelog entries
- QA fixes and small doc-only changes within a single session

### Validation before any commit

Always run frontmatter validation before committing changes to `agents/`, `skills/`, or `commands/`:

```bash
~/.bun/bin/bun .github/scripts/validate-frontmatter.ts <plugin>/
```

## Commit Style

Use conventional commits:

```
feat(plugin-name): add ...
fix(plugin-name): correct ...
docs(plugin-name): update ...
chore: ...
```

## Active Technologies

Use these existing stacks before introducing new dependencies:
- Python 3.11+ + Flask, anthropic, chromadb, openai (embedding client) (RAG-assistant)
- ChromaDB (vector store), SQLite (registry) (RAG-assistant)
- Python 3.11+ + python-docx, python-pptx (ea-assistant artifact generation scripts)
- Markdown (Claude Code plugin instruction files) + Claude Code plugin framework (commands/, skills/, agents/) (ea-assistant, RAG-assistant, ITIL-assistant)
- JSON files (`engagement.json`) and directory structure (`EA-projects/`) (ea-assistant)
- React JSX (artifact apps for interview UI and brainstorm pad) — rendered as Claude artifacts or written to disk as standalone HTML (ea-assistant)
- `window.localStorage` (key-value, JSON-serialized) — browser-side persistence in Claude's artifact viewer (ITIL-assistant)
