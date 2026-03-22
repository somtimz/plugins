"""RAG Ingestion Pipeline — T016/T019/T022

Invocation:
    python scripts/ingest.py --source <PATH> [--config <PATH>]
    python scripts/ingest.py [--config <PATH>]

Exit codes:
    0  — completed (some documents may have been skipped/failed; check stdout)
    1  — fatal error (config invalid, store unreachable, model mismatch, no source)
"""
from __future__ import annotations

import argparse
import sys
import datetime
from pathlib import Path

# Ensure scripts/ is on sys.path so `lib.*` imports work when the script is
# called from any working directory.
sys.path.insert(0, str(Path(__file__).parent))

import chromadb

from lib.config import load_config, ConfigError, LocalSourceConfig
from lib.logger import init_logger
from lib.sources import discover_local
from lib.store import (
    get_or_create_collection,
    check_model_consistency,
    ModelMismatchError,
)
from lib.registry import open_registry, create_schema
from lib.pipeline import SourceResult, run_ingestion

_DEFAULT_CONFIG = ".rag-plugin.toml"


def _print_full_summary(
    config_path: str,
    started: datetime.datetime,
    completed: datetime.datetime,
    results: list[SourceResult],
) -> None:
    total_disc = sum(r.discovered for r in results)
    total_succ = sum(r.succeeded for r in results)
    total_skip = sum(r.skipped for r in results)
    total_fail = sum(r.failed for r in results)
    total_unchanged = sum(r.skipped_unchanged for r in results)
    total_dup = sum(r.skipped_duplicate for r in results)

    print("RAG Ingestion Pipeline — Complete")
    print("==================================")
    print(f"Config      : {config_path}")
    print(f"Started     : {started.isoformat(timespec='seconds')}")
    print(f"Completed   : {completed.isoformat(timespec='seconds')}")

    for r in results:
        print()
        if r.status != "ok":
            print(f"Source: {r.label} — FAILED ({r.status})")
            if r.error_message:
                print(f"  {r.error_message}")
        else:
            print(f"Source: {r.label}")
            print(
                f"  Discovered : {r.discovered}  |  Succeeded : {r.succeeded}"
                f"  |  Skipped : {r.skipped}  |  Failed : {r.failed}"
            )
            if r.skipped_unchanged or r.skipped_duplicate:
                print(f"  Skipped (unchanged) : {r.skipped_unchanged}"
                      f"   ← same hash, already in registry")
                print(f"  Skipped (duplicate) : {r.skipped_duplicate}"
                      f"   ← same hash seen earlier in this run")
            if r.failed_docs:
                print(f"\nSource: {r.label} — failures:")
                for doc_path, reason in r.failed_docs:
                    print(f"  - {doc_path}  — {reason}")

    print()
    print("─────────────────────────────────────────")
    print(f"Total discovered : {total_disc}")
    print(f"  Succeeded      : {total_succ}")
    print(f"  Skipped        : {total_skip}")
    if total_unchanged or total_dup:
        print(f"  Skipped (unchanged) : {total_unchanged}")
        print(f"  Skipped (duplicate) : {total_dup}")
    print(f"  Failed         : {total_fail}")


# ---------------------------------------------------------------------------
# CLI entry point
# ---------------------------------------------------------------------------

def main() -> int:
    parser = argparse.ArgumentParser(
        prog="ingest.py",
        description="RAG document ingestion pipeline",
    )
    parser.add_argument(
        "--source",
        metavar="PATH",
        default=None,
        help="Local file or directory to ingest (overrides [[sources]] in config)",
    )
    parser.add_argument(
        "--config",
        metavar="PATH",
        default=_DEFAULT_CONFIG,
        help=f"Path to TOML config (default: {_DEFAULT_CONFIG})",
    )
    args = parser.parse_args()

    config_path = args.config
    started = datetime.datetime.now()

    # --- Load config ---
    try:
        cfg = load_config(config_path)
    except ConfigError as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1

    # --- Initialise logger ---
    logger = init_logger(cfg.pipeline.log_path)
    logger.info("Pipeline started — config=%s", config_path)

    # --- Open ChromaDB and check model consistency ---
    try:
        chroma_client = chromadb.PersistentClient(path=cfg.vector_store.path)
        collection = get_or_create_collection(
            chroma_client,
            cfg.vector_store.collection,
            cfg.embedding.model,
        )
        check_model_consistency(collection, cfg.embedding.model)
    except ModelMismatchError as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        logger.error("Model mismatch abort: %s", exc)
        return 1
    except Exception as exc:
        print(f"ERROR: Could not connect to vector store: {exc}", file=sys.stderr)
        logger.error("Vector store init failed: %s", exc)
        return 1

    # --- Open registry ---
    try:
        reg_conn = open_registry(cfg.pipeline.registry_path)
    except Exception as exc:
        print(f"ERROR: Could not open registry: {exc}", file=sys.stderr)
        logger.error("Registry init failed: %s", exc)
        return 1

    # --- Resolve source(s) ---
    if args.source is None and not cfg.sources:
        print(
            "ERROR: No --source specified and no [[sources]] defined in config.",
            file=sys.stderr,
        )
        logger.error("No source to process — aborting")
        return 1

    if args.source is not None:
        # --source override: wrap as a single LocalSourceConfig
        source_path = args.source
        p = Path(source_path)
        if not p.exists():
            print(f"ERROR: Source path does not exist: {source_path}", file=sys.stderr)
            logger.error("Source path not found: %s", source_path)
            return 1
        sources = [LocalSourceConfig(name="_cli_source", type="local", path=source_path)]
    else:
        sources = cfg.sources

    results = run_ingestion(sources, cfg, logger, chroma_client, collection, reg_conn)

    reg_conn.close()

    completed = datetime.datetime.now()
    total_disc = sum(r.discovered for r in results)
    total_succ = sum(r.succeeded for r in results)
    total_skip = sum(r.skipped for r in results)
    total_fail = sum(r.failed for r in results)
    logger.info(
        "Pipeline complete — discovered=%d succeeded=%d skipped=%d failed=%d",
        total_disc, total_succ, total_skip, total_fail,
    )

    _print_full_summary(config_path, started, completed, results)
    return 0


if __name__ == "__main__":
    sys.exit(main())
