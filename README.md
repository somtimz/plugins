# Claude Plugins

A curated collection of plugins for Claude Code and OpenCode maintained by [@somtimz](https://github.com/somtimz).

## Plugins

| Plugin | Description | Version |
|---|---|---|
| [ea-assistant](./ea-assistant/) | End-to-end Enterprise Architecture engagement management (TOGAF 10, Zachman, ArchiMate) with artifact generation, phase interviews, Decision Register, session tracking, opt-out tracking, and artifact compliance checking | 0.8.0 |
| [RAG-assistant](./RAG-assistant/) | Conversational RAG assistant — ingests documents into ChromaDB, web UI for cited Q&A and ingestion management | 0.1.0 |
| [research-agent](./research-agent/) | Lead Research Analyst agent — evidence-based deep research with confidence scoring, contradiction detection, and executive-ready synthesis | 0.1.0 |
| [grill-me](./grill-me/) | Nine interview skills for stress-testing strategies, decisions, risks, and designs | 0.4.0 |
| [ITIL-assistant](./ITIL-assistant/) | ITIL v4 Change Management assistant — create, manage, and review Change Requests with CAB approval workflow | 0.1.0 |

## Installation

### Claude Code — add as marketplace

In Claude Code, add this repo as a marketplace to browse and install all plugins:

```
/marketplace add https://github.com/somtimz/plugins
```

Or install a single plugin directly:

```bash
/plugin install https://github.com/somtimz/plugins/tree/main/<plugin-name>
```

### OpenCode — install skills

OpenCode has no marketplace mechanism, but all 21 skills are format-compatible. Clone the repo and run the install script to symlink skills into OpenCode's discovery path:

```bash
git clone https://github.com/somtimz/plugins.git
cd plugins
bash install-opencode.sh
# Uninstall: bash install-opencode.sh --uninstall
```

The script symlinks all skills into `~/.config/opencode/skills/`. Set `OPENCODE_SKILLS_DIR` to override the target directory. Restart OpenCode after installing.

**Skills available for OpenCode:**

| Skill | Plugin |
|---|---|
| `archimate-notation` | ea-assistant |
| `ea-artifact-templates` | ea-assistant |
| `ea-document-ingestion` | ea-assistant |
| `ea-engagement-lifecycle` | ea-assistant |
| `ea-generation` | ea-assistant |
| `ea-requirements-management` | ea-assistant |
| `ea-interview-ui` | ea-assistant |
| `zachman-framework` | ea-assistant |
| `doc-ingestion-pipeline` | RAG-assistant |
| `rag-chat` | RAG-assistant |
| `itil-change-request` | ITIL-assistant |
| `cab-review` | ITIL-assistant |
| `grill-me-stress-test` | grill-me |
| `grill-me-premortem` | grill-me |
| `grill-me-decision` | grill-me |
| `grill-me-design` | grill-me |
| `grill-me-software-design` | grill-me |
| `grill-me-infra-design` | grill-me |
| `grill-me-artifact` | grill-me |
| `grill-me-diagram` | grill-me |
| `grill-me-boardroom-strategy` | grill-me |

## Repository Structure

```
<plugin-name>/
├── .claude-plugin/plugin.json   # plugin manifest
├── agents/                      # subagent definitions
├── commands/                    # slash commands
├── skills/                      # skill files
├── hooks/                       # lifecycle hooks
├── templates/                   # document templates
└── README.md
.claude-plugin/marketplace.json  # marketplace index
.github/
    scripts/validate-frontmatter.ts  # CI frontmatter validator
    workflows/
        validate-frontmatter.yml     # runs on every PR
        close-external-prs.yml       # maintainer-only contributions
```

## Contributing

This repo accepts contributions from maintainers only. To propose a new plugin or report an issue, open a GitHub issue.

## License

Each plugin carries its own license. See the `LICENSE` file in each plugin directory.
