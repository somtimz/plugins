"""Source discovery helpers for the RAG ingestion pipeline — T018"""
from __future__ import annotations

import os
from dataclasses import dataclass
from pathlib import Path


@dataclass
class SourceFile:
    origin_path: str
    source_name: str
    file_size_bytes: int


def discover_local(path: str, supported_formats: list[str]) -> list[SourceFile]:
    """Discover ingestion candidates under *path*.

    Parameters
    ----------
    path:
        A file path or directory path to scan.
    supported_formats:
        List of file extensions (without leading dot, e.g. ``["txt", "md"]``)
        to include when scanning a directory.

    Returns
    -------
    list[SourceFile]
        Ordered list of discovered source files.  For a single-file path the
        list always contains exactly that file regardless of its extension.
        For a directory the list contains all files whose extension (lower-cased,
        without leading dot) is in *supported_formats*, discovered recursively.
    """
    p = Path(path)

    if p.is_file():
        return [
            SourceFile(
                origin_path=str(p),
                source_name=str(p),
                file_size_bytes=p.stat().st_size,
            )
        ]

    supported = {fmt.lower() for fmt in supported_formats}
    results: list[SourceFile] = []

    for root, _dirs, files in os.walk(str(p)):
        for filename in files:
            ext = Path(filename).suffix.lstrip(".").lower()
            if ext in supported:
                full_path = os.path.join(root, filename)
                results.append(
                    SourceFile(
                        origin_path=full_path,
                        source_name=full_path,
                        file_size_bytes=os.path.getsize(full_path),
                    )
                )

    return results
