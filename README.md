# Claude Plugins

A curated collection of Claude Code plugins maintained by [@somtimz](https://github.com/somtimz).

## Plugins

| Plugin | Description | Version |
|---|---|---|
| [ea-assistant](./plugins/ea-assistant/) | End-to-end Enterprise Architecture engagement management (TOGAF 10, Zachman, ArchiMate) | 0.1.0 |
| [rag-plugin](./plugins/rag-plugin/) | Local RAG pipeline — ingest documents into ChromaDB, conversational web UI for cited Q&A and ingestion management | 0.1.0 |

## Installation

Install any plugin directly in Claude Code:

```bash
/plugin install https://github.com/somtimz/plugins/tree/main/plugins/<plugin-name>
```

## Repository Structure

```
plugins/
└── <plugin-name>/
    ├── .claude-plugin/plugin.json   # plugin manifest
    ├── agents/                      # subagent definitions
    ├── commands/                    # slash commands
    ├── skills/                      # skill files
    ├── hooks/                       # lifecycle hooks
    ├── templates/                   # document templates
    └── README.md
.claude-plugin/marketplace.json      # marketplace index
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
