"""Tests for scripts/lib/embedder.py"""
import sys
import logging
from dataclasses import dataclass
from pathlib import Path
from unittest.mock import MagicMock, patch, call

import pytest

sys.path.insert(0, str(Path(__file__).parent.parent.parent / "scripts"))

from lib.embedder import EmbeddedChunk, EmbeddingError, embed_chunks
from lib.chunker import Chunk


# ---------------------------------------------------------------------------
# Minimal stand-ins
# ---------------------------------------------------------------------------

@dataclass
class EmbeddingConfig:
    api_base: str
    embedding_key_env: str
    model: str


def _make_config() -> EmbeddingConfig:
    return EmbeddingConfig(
        api_base="https://api.openai.com/v1",
        embedding_key_env="TEST_OPENAI_KEY",
        model="text-embedding-3-small",
    )


def _make_chunk(index: int = 0, source: str = "doc.txt") -> Chunk:
    text = f"Chunk number {index} with some text content."
    return Chunk(
        chunk_id=f"{source}::chunk::{index}",
        chunk_index=index,
        text=text,
        char_start=index * 50,
        char_end=index * 50 + len(text),
    )


def _make_embedding_response(vector: list[float], model: str) -> MagicMock:
    """Build a mock that mimics openai Embedding response shape."""
    embedding_obj = MagicMock()
    embedding_obj.embedding = vector
    response = MagicMock()
    response.data = [embedding_obj]
    response.model = model
    return response


@pytest.fixture
def logger() -> logging.Logger:
    return logging.getLogger("test_embedder")


@pytest.fixture(autouse=True)
def set_api_key(monkeypatch):
    monkeypatch.setenv("TEST_OPENAI_KEY", "sk-test-key")


# ---------------------------------------------------------------------------
# Successful embedding
# ---------------------------------------------------------------------------

class TestSuccessfulEmbedding:
    def test_returns_list_of_embedded_chunks(self, logger, monkeypatch):
        config = _make_config()
        chunks = [_make_chunk(0), _make_chunk(1)]
        vector = [0.1, 0.2, 0.3]

        mock_response = _make_embedding_response(vector, config.model)
        mock_client = MagicMock()
        mock_client.embeddings.create.return_value = mock_response

        with patch("lib.embedder.openai.OpenAI", return_value=mock_client):
            result = embed_chunks(chunks, config, logger)

        assert len(result) == 2
        assert all(isinstance(ec, EmbeddedChunk) for ec in result)

    def test_embedded_chunk_has_correct_chunk_id(self, logger, monkeypatch):
        config = _make_config()
        chunk = _make_chunk(0)
        vector = [0.1, 0.2, 0.3]

        mock_response = _make_embedding_response(vector, config.model)
        mock_client = MagicMock()
        mock_client.embeddings.create.return_value = mock_response

        with patch("lib.embedder.openai.OpenAI", return_value=mock_client):
            result = embed_chunks([chunk], config, logger)

        assert result[0].chunk_id == chunk.chunk_id

    def test_embedded_chunk_has_correct_text(self, logger, monkeypatch):
        config = _make_config()
        chunk = _make_chunk(0)
        vector = [0.1, 0.2, 0.3]

        mock_response = _make_embedding_response(vector, config.model)
        mock_client = MagicMock()
        mock_client.embeddings.create.return_value = mock_response

        with patch("lib.embedder.openai.OpenAI", return_value=mock_client):
            result = embed_chunks([chunk], config, logger)

        assert result[0].text == chunk.text

    def test_embedded_chunk_has_correct_model(self, logger, monkeypatch):
        config = _make_config()
        chunk = _make_chunk(0)
        vector = [0.1, 0.2, 0.3]

        mock_response = _make_embedding_response(vector, config.model)
        mock_client = MagicMock()
        mock_client.embeddings.create.return_value = mock_response

        with patch("lib.embedder.openai.OpenAI", return_value=mock_client):
            result = embed_chunks([chunk], config, logger)

        assert result[0].model == config.model

    def test_embedded_chunk_has_non_empty_vector(self, logger, monkeypatch):
        config = _make_config()
        chunk = _make_chunk(0)
        vector = [0.1, 0.2, 0.3]

        mock_response = _make_embedding_response(vector, config.model)
        mock_client = MagicMock()
        mock_client.embeddings.create.return_value = mock_response

        with patch("lib.embedder.openai.OpenAI", return_value=mock_client):
            result = embed_chunks([chunk], config, logger)

        assert len(result[0].vector) > 0
        assert result[0].vector == vector

    def test_empty_chunks_list_returns_empty_list(self, logger, monkeypatch):
        config = _make_config()
        mock_client = MagicMock()

        with patch("lib.embedder.openai.OpenAI", return_value=mock_client):
            result = embed_chunks([], config, logger)

        assert result == []
        mock_client.embeddings.create.assert_not_called()


# ---------------------------------------------------------------------------
# Retry behaviour
# ---------------------------------------------------------------------------

class TestRateLimitRetries:
    def test_rate_limit_retries_and_eventually_succeeds(self, logger, monkeypatch):
        """First 5 calls raise RateLimitError; 6th call succeeds."""
        import openai

        config = _make_config()
        chunk = _make_chunk(0)
        vector = [0.5, 0.6]

        success_response = _make_embedding_response(vector, config.model)

        # Build a RateLimitError instance (openai v1 signature)
        rate_limit_err = openai.RateLimitError(
            message="rate limited",
            response=MagicMock(status_code=429, headers={}),
            body=None,
        )

        mock_create = MagicMock(
            side_effect=[
                rate_limit_err,
                rate_limit_err,
                rate_limit_err,
                rate_limit_err,
                rate_limit_err,
                success_response,
            ]
        )
        mock_client = MagicMock()
        mock_client.embeddings.create = mock_create

        with patch("lib.embedder.openai.OpenAI", return_value=mock_client):
            with patch("lib.embedder.time.sleep"):
                result = embed_chunks([chunk], config, logger)

        assert len(result) == 1
        assert mock_create.call_count == 6

    def test_rate_limit_on_all_attempts_raises_embedding_error(self, logger, monkeypatch):
        """All 6 calls raise RateLimitError — should raise EmbeddingError."""
        import openai

        config = _make_config()
        chunk = _make_chunk(0)

        rate_limit_err = openai.RateLimitError(
            message="rate limited",
            response=MagicMock(status_code=429, headers={}),
            body=None,
        )

        mock_create = MagicMock(side_effect=rate_limit_err)
        mock_client = MagicMock()
        mock_client.embeddings.create = mock_create

        with patch("lib.embedder.openai.OpenAI", return_value=mock_client):
            with patch("lib.embedder.time.sleep"):
                with pytest.raises(EmbeddingError):
                    embed_chunks([chunk], config, logger)

    def test_sleep_is_called_between_retries(self, logger, monkeypatch):
        import openai

        config = _make_config()
        chunk = _make_chunk(0)
        vector = [0.1]

        success_response = _make_embedding_response(vector, config.model)
        rate_limit_err = openai.RateLimitError(
            message="rate limited",
            response=MagicMock(status_code=429, headers={}),
            body=None,
        )

        mock_create = MagicMock(side_effect=[rate_limit_err, rate_limit_err, success_response])
        mock_client = MagicMock()
        mock_client.embeddings.create = mock_create

        with patch("lib.embedder.openai.OpenAI", return_value=mock_client):
            with patch("lib.embedder.time.sleep") as mock_sleep:
                embed_chunks([chunk], config, logger)

        assert mock_sleep.call_count == 2


# ---------------------------------------------------------------------------
# Non-retryable errors
# ---------------------------------------------------------------------------

class TestNonRetryableErrors:
    def test_authentication_error_raises_embedding_error_immediately(self, logger, monkeypatch):
        import openai

        config = _make_config()
        chunk = _make_chunk(0)

        auth_err = openai.AuthenticationError(
            message="invalid api key",
            response=MagicMock(status_code=401, headers={}),
            body=None,
        )

        mock_create = MagicMock(side_effect=auth_err)
        mock_client = MagicMock()
        mock_client.embeddings.create = mock_create

        with patch("lib.embedder.openai.OpenAI", return_value=mock_client):
            with patch("lib.embedder.time.sleep") as mock_sleep:
                with pytest.raises(EmbeddingError):
                    embed_chunks([chunk], config, logger)

        # Must NOT retry — only one attempt
        assert mock_create.call_count == 1
        mock_sleep.assert_not_called()


# ---------------------------------------------------------------------------
# API key handling
# ---------------------------------------------------------------------------

class TestApiKeyHandling:
    def test_openai_client_constructed_with_key_from_env(self, logger, monkeypatch):
        config = _make_config()
        monkeypatch.setenv(config.embedding_key_env, "sk-env-secret-key")
        chunk = _make_chunk(0)
        vector = [0.1]

        mock_response = _make_embedding_response(vector, config.model)
        mock_client = MagicMock()
        mock_client.embeddings.create.return_value = mock_response

        with patch("lib.embedder.openai.OpenAI", return_value=mock_client) as mock_openai_cls:
            embed_chunks([chunk], config, logger)

        # Verify the constructor received the correct api_key
        init_kwargs = mock_openai_cls.call_args.kwargs
        assert init_kwargs.get("api_key") == "sk-env-secret-key"
