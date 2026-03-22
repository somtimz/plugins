# ChromaDB Developer Guide

## Introduction

ChromaDB is an open-source embedding database designed for AI applications. It stores documents alongside their vector embeddings and provides fast similarity search. ChromaDB can run entirely in-process (no server required) or as a persistent local database.

## Installation

```bash
pip install chromadb
```

## Basic Usage

### Create a persistent client

```python
import chromadb

client = chromadb.PersistentClient(path=".chroma-store")
```

### Create or get a collection

```python
collection = client.get_or_create_collection(
    name="my-documents",
    metadata={"hnsw:space": "cosine"},
)
```

### Add documents

```python
collection.add(
    ids=["doc-1", "doc-2"],
    documents=["First document text", "Second document text"],
    embeddings=[[0.1, 0.2, ...], [0.3, 0.4, ...]],  # pre-computed
    metadatas=[{"source": "file_a.txt"}, {"source": "file_b.txt"}],
)
```

### Query

```python
results = collection.query(
    query_embeddings=[[0.1, 0.2, ...]],
    n_results=5,
    include=["documents", "metadatas", "distances"],
)
```

## Collections and Metadata

Each collection stores:
- **ids**: unique string identifiers per embedding
- **embeddings**: float vectors (must be consistent dimensionality)
- **documents**: optional raw text associated with each embedding
- **metadatas**: optional dict of filterable key-value pairs

## Filtering

ChromaDB supports metadata filtering using the `where` parameter:

```python
results = collection.query(
    query_embeddings=query_vec,
    n_results=10,
    where={"source": {"$eq": "annual-report.pdf"}},
)
```

Supported operators: `$eq`, `$ne`, `$gt`, `$gte`, `$lt`, `$lte`, `$in`, `$nin`.

## Model Consistency

If you re-embed documents with a different model, the new vectors will be incompatible with existing ones. Best practice: store the embedding model name in the collection metadata and validate it on startup.

```python
collection = client.get_or_create_collection(
    name="docs",
    metadata={"embedding_model": "text-embedding-3-small"},
)
stored_model = collection.metadata.get("embedding_model")
if stored_model and stored_model != current_model:
    raise ValueError(f"Model mismatch: store={stored_model}, config={current_model}")
```

## Deleting Documents

```python
collection.delete(ids=["doc-1", "doc-2"])
```

For re-ingestion workflows, always delete old chunks before inserting updated ones to avoid stale data.

## Performance Tips

- Use `PersistentClient` for any data that must survive process restarts.
- Keep collection count low — one collection per use case is usually optimal.
- For large corpora (>100k chunks), consider batching `add()` calls in chunks of 500–1000.
