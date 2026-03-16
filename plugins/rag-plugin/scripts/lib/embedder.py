"""Embedder for the RAG ingestion pipeline."""
import logging
import os
import time
import random
from dataclasses import dataclass

import openai

from lib.chunker import Chunk

_MAX_RETRIES = 5  # total attempts = 6 (initial + 5 retries)
_MAX_DELAY = 30.0


@dataclass
class EmbeddedChunk:
    chunk_id: str
    text: str
    vector: list[float]
    model: str


class EmbeddingError(Exception):
    pass


def embed_chunks(chunks, config, logger: logging.Logger) -> list[EmbeddedChunk]:
    """Embed a list of Chunk objects using the configured OpenAI-compatible API.

    Parameters
    ----------
    chunks:
        Iterable of :class:`~lib.chunker.Chunk` objects to embed.
    config:
        An object with ``api_base``, ``api_key_env``, and ``model`` attributes.
    logger:
        A standard :class:`logging.Logger` used for diagnostic messages.

    Returns
    -------
    list[EmbeddedChunk]
        One :class:`EmbeddedChunk` per input chunk, in the same order.

    Raises
    ------
    EmbeddingError
        On authentication failure or when all retry attempts are exhausted.
    """
    if not chunks:
        return []

    client = openai.OpenAI(
        base_url=config.api_base,
        api_key=os.environ.get(config.api_key_env, ""),
    )

    results: list[EmbeddedChunk] = []

    for chunk in chunks:
        response = _embed_with_retry(client, chunk, config.model, logger)
        results.append(
            EmbeddedChunk(
                chunk_id=chunk.chunk_id,
                text=chunk.text,
                vector=response.data[0].embedding,
                model=config.model,
            )
        )

    return results


def _embed_with_retry(client, chunk: Chunk, model: str, logger: logging.Logger):
    """Call the embeddings API with exponential-backoff retry on rate limits."""
    last_exc: Exception | None = None

    for attempt in range(_MAX_RETRIES + 1):  # attempts 0 … 5
        try:
            return client.embeddings.create(model=model, input=chunk.text)
        except openai.AuthenticationError as exc:
            logger.error("Authentication error — not retrying: %s", exc)
            raise EmbeddingError(str(exc)) from exc
        except openai.RateLimitError as exc:
            last_exc = exc
            if attempt < _MAX_RETRIES:
                delay = min((2 ** attempt) + random.uniform(0, 1), _MAX_DELAY)
                logger.warning(
                    "Rate limit hit (attempt %d/%d). Sleeping %.2fs.",
                    attempt + 1,
                    _MAX_RETRIES + 1,
                    delay,
                )
                time.sleep(delay)
            # else: fall through to raise EmbeddingError below

    raise EmbeddingError(
        f"Embedding failed after {_MAX_RETRIES + 1} attempts due to rate limiting."
    ) from last_exc
