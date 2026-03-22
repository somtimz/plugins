"""Tests for scripts/lib/logger.py — T005"""
import logging
import re
from pathlib import Path

import pytest
import sys
sys.path.insert(0, str(Path(__file__).parent.parent.parent / "scripts"))

from lib.logger import init_logger


class TestLoggerCreation:
    def test_creates_log_file(self, tmp_path):
        log_path = str(tmp_path / "pipeline.log")
        logger = init_logger(log_path)
        logger.info("test entry")
        assert Path(log_path).exists()

    def test_returns_logger_instance(self, tmp_path):
        log_path = str(tmp_path / "pipeline.log")
        logger = init_logger(log_path)
        assert isinstance(logger, logging.Logger)

    def test_default_path_used_when_none(self, tmp_path, monkeypatch):
        monkeypatch.chdir(tmp_path)
        logger = init_logger(str(tmp_path / ".rag-pipeline.log"))
        logger.info("default path test")
        assert (tmp_path / ".rag-pipeline.log").exists()


class TestLogEntryFormat:
    LOG_PATTERN = re.compile(
        r"^\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2} \[(DEBUG|INFO|WARNING|ERROR|CRITICAL)\] .+$"
    )

    def test_info_entry_format(self, tmp_path):
        log_path = str(tmp_path / "pipeline.log")
        logger = init_logger(log_path)
        logger.info("ingesting document")
        lines = Path(log_path).read_text().strip().splitlines()
        assert lines, "log file should not be empty"
        assert self.LOG_PATTERN.match(lines[-1]), f"Unexpected format: {lines[-1]}"

    def test_error_entry_format(self, tmp_path):
        log_path = str(tmp_path / "pipeline.log")
        logger = init_logger(log_path)
        logger.error("something failed")
        lines = Path(log_path).read_text().strip().splitlines()
        assert "[ERROR]" in lines[-1]

    def test_warning_entry_format(self, tmp_path):
        log_path = str(tmp_path / "pipeline.log")
        logger = init_logger(log_path)
        logger.warning("large file detected")
        lines = Path(log_path).read_text().strip().splitlines()
        assert "[WARNING]" in lines[-1]

    def test_multiple_entries_all_formatted(self, tmp_path):
        log_path = str(tmp_path / "pipeline.log")
        logger = init_logger(log_path)
        logger.info("step 1")
        logger.info("step 2")
        logger.error("step 3 failed")
        lines = [l for l in Path(log_path).read_text().strip().splitlines() if l]
        assert len(lines) == 3
        for line in lines:
            assert self.LOG_PATTERN.match(line), f"Bad format: {line}"


class TestLoggerBehavior:
    def test_does_not_suppress_on_success(self, tmp_path):
        log_path = str(tmp_path / "pipeline.log")
        logger = init_logger(log_path)
        logger.info("success message")
        content = Path(log_path).read_text()
        assert "success message" in content

    def test_multiple_init_calls_do_not_duplicate_handlers(self, tmp_path):
        log_path = str(tmp_path / "pipeline.log")
        logger1 = init_logger(log_path)
        logger2 = init_logger(log_path)
        logger2.info("single entry")
        lines = [l for l in Path(log_path).read_text().strip().splitlines() if l]
        assert len(lines) == 1, f"Expected 1 line, got {len(lines)}: {lines}"
