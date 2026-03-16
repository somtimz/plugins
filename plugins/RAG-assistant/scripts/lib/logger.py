"""Pipeline logger — T007"""
from __future__ import annotations

import logging
from pathlib import Path

_LOGGER_NAME = "rag_pipeline"
_FORMAT = "%(asctime)s [%(levelname)s] %(message)s"
_DATE_FORMAT = "%Y-%m-%d %H:%M:%S"


def init_logger(log_path: str) -> logging.Logger:
    """Initialise and return the pipeline logger.

    Creates (or opens) a log file at *log_path*.  The logger uses the format::

        YYYY-MM-DD HH:MM:SS [LEVEL] message

    Calling this function more than once with the same path is safe — duplicate
    handlers are removed before adding a new one.
    """
    logger = logging.getLogger(_LOGGER_NAME)
    logger.setLevel(logging.DEBUG)

    # Remove any previously attached handlers to prevent duplicate output.
    logger.handlers.clear()

    Path(log_path).parent.mkdir(parents=True, exist_ok=True)
    handler = logging.FileHandler(log_path, encoding="utf-8")
    handler.setLevel(logging.DEBUG)
    formatter = logging.Formatter(_FORMAT, datefmt=_DATE_FORMAT)
    handler.setFormatter(formatter)
    logger.addHandler(handler)

    # Prevent propagation to the root logger (avoids stderr bleed-through).
    logger.propagate = False

    return logger
