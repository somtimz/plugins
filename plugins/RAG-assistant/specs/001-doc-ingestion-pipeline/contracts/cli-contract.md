# Contract: Pipeline CLI Interface

**Feature**: 001-doc-ingestion-pipeline
**Contract type**: Command-line interface
**Entrypoint**: `$CLAUDE_PLUGIN_ROOT/scripts/ingest.py`

## Purpose

The ingestion pipeline is invoked as a Python script from within a Claude Code session
(guided by the skill) or directly from the terminal. This document defines the stable
CLI contract that the skill's instructions depend on.

## Invocation

```bash
# Use all sources defined in config (normal usage)
python "$CLAUDE_PLUGIN_ROOT/scripts/ingest.py" [--config <CONFIG_PATH>]

# Override with a one-off local path (bypasses [[sources]] in config)
python "$CLAUDE_PLUGIN_ROOT/scripts/ingest.py" --source <PATH> [--config <CONFIG_PATH>]
```

## Arguments

| Argument | Required | Default | Description |
|----------|----------|---------|-------------|
| `--source PATH` | No | — | Override: ingest a single local file or directory, ignoring `[[sources]]` in config |
| `--config PATH` | No | `.rag-plugin.toml` (CWD) | Path to the TOML configuration file |

**Source resolution rules**:
1. If `--source` is provided → process only that local path; ignore `[[sources]]` in config
2. If `--source` is not provided → process all sources defined in `[[sources]]`
3. If neither `--source` nor `[[sources]]` exists → fatal error, exit code 1

## Exit Codes

| Code | Meaning |
|------|---------|
| `0` | Pipeline completed; all discovered documents processed (some may have been skipped or failed — check stdout summary) |
| `1` | Pipeline aborted due to a fatal error (config missing/invalid, vector store unreachable, no source specified) |

## Standard Output (stdout)

On success, the pipeline prints a per-source and aggregate completion summary:

```
RAG Ingestion Pipeline — Complete
==================================
Config      : .rag-plugin.toml
Started     : 2026-03-15T10:00:00
Completed   : 2026-03-15T10:01:15

Source: local-docs (local: ./docs/)
  Discovered : 8  |  Succeeded : 7  |  Skipped : 1  |  Failed : 0

Source: sharepoint-reports (sharepoint: /Shared Documents/Reports)
  Discovered : 5  |  Succeeded : 5  |  Skipped : 0  |  Failed : 0

─────────────────────────────────────────
Total discovered : 13
  Succeeded      : 12
  Skipped        : 1
  Failed         : 0
```

The summary also shows per-document deduplication stats:

```
  Skipped (unchanged) : 4   ← same hash, already in registry
  Skipped (duplicate) : 1   ← same hash seen earlier in this run
```

On source-level failure (auth error, unreachable):

```
Source: sharepoint-reports — FAILED (auth_failed)
  Authentication failed. Re-run after re-exporting SP_TENANT_ID and SP_CLIENT_ID,
  or re-authenticate via device flow.
```

On partial document failure, failed documents are listed per source:

```
Source: local-docs — failures:
  - ./docs/corrupted.txt  — UnicodeDecodeError: 'utf-8' codec can't decode byte
```

## Standard Error (stderr)

Fatal errors (config missing, store unreachable, model mismatch) are written to stderr before exit code 1:

```
ERROR: Configuration file not found: .rag-plugin.toml
Run the skill to create it, or pass --config to specify a different path.
```

```
ERROR: Embedding model mismatch. The vector store was created with model
'text-embedding-3-small' but the config specifies 'nomic-embed-text'.
To switch models, delete .rag-store/ and .rag-registry.db, then re-run the pipeline.
```

## Stability Guarantee

Arguments and exit codes are stable within a major plugin version. Output format to
stdout is informational and MUST NOT be parsed by scripts — it is for human reading only.
Machine-readable output will be added in a future version if needed.
