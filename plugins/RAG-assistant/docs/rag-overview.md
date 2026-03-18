# Retrieval-Augmented Generation (RAG) Overview

## What is RAG?

Retrieval-Augmented Generation (RAG) is an AI architecture pattern that combines a retrieval system with a generative language model. Instead of relying solely on knowledge encoded in model weights during training, RAG allows the model to query an external knowledge base at inference time and ground its responses in retrieved documents.

## Core Components

### 1. Document Ingestion Pipeline
The ingestion pipeline processes raw documents (PDFs, Word files, Markdown, plain text) into chunks, embeds each chunk using an embedding model, and stores the resulting vectors in a vector database alongside the original text.

### 2. Vector Store
A vector store (such as ChromaDB, Pinecone, or Weaviate) indexes embedding vectors for fast approximate nearest-neighbour (ANN) search. At query time, the user's question is embedded and the top-k most semantically similar chunks are retrieved.

### 3. Language Model (LLM)
The retrieved chunks are injected into the LLM's context window as grounding material. The model is instructed to answer the user's question using only the provided context, reducing hallucination.

## Key Benefits

- **Freshness**: The knowledge base can be updated without retraining the model.
- **Traceability**: Responses can be traced back to source documents.
- **Cost efficiency**: Smaller, cheaper models can outperform larger models when given relevant context.
- **Privacy**: Documents never leave your infrastructure (with a local vector store and self-hosted LLM).

## Chunking Strategy

Chunk size and overlap significantly affect retrieval quality:

| Setting | Effect |
|---------|--------|
| Larger chunks | More context per result, but noisier matches |
| Smaller chunks | Precise matches, but less surrounding context |
| Higher overlap | Better boundary coverage, more storage |

A typical starting point is `chunk_size=1000`, `chunk_overlap=200` (character-based).

## Embedding Models

Common embedding models and their trade-offs:

| Model | Dimensions | Notes |
|-------|-----------|-------|
| `text-embedding-3-small` | 1536 | Best cost/quality ratio for most use cases |
| `text-embedding-3-large` | 3072 | Higher accuracy, 2× cost |
| `text-embedding-ada-002` | 1536 | Legacy, superseded by 3-small |

## Limitations

- Retrieval quality is bounded by the embedding model's semantic understanding.
- Very long documents must be chunked, which can split context across chunk boundaries.
- Duplicate or near-duplicate documents inflate the index without adding value — deduplication is essential.
