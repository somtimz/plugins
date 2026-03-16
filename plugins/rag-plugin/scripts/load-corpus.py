import os
import textwrap
import requests

# List of (filename, url) pairs to download
FILES = [
    # OpenAI Cookbook (LLM usage and patterns)
    (
        "openai_cookbook_embeddings.md",
        "https://raw.githubusercontent.com/openai/openai-cookbook/main/examples/Embeddings_in_JavaScript.ipynb"
    ),
    (
        "openai_cookbook_rag.md",
        "https://raw.githubusercontent.com/openai/openai-cookbook/main/examples/rag/rag_with_openai.ipynb"
    ),

    # LangChain docs (RAG / LLM orchestration)
    (
        "langchain_rag.md",
        "https://raw.githubusercontent.com/langchain-ai/langchain/master/docs/docs/use_cases/question_answering/how_to/rag.ipynb"
    ),
    (
        "langchain_llm_integration.md",
        "https://raw.githubusercontent.com/langchain-ai/langchain/master/docs/docs/how_to/llms.ipynb"
    ),

    # Hugging Face Transformers docs (LLM models & usage)
    (
        "hf_transformers_index.md",
        "https://raw.githubusercontent.com/huggingface/transformers/main/README.md"
    ),
    (
        "hf_transformers_generation.md",
        "https://raw.githubusercontent.com/huggingface/transformers/main/docs/source/en/generation_strategies.md"
    ),

    # A few model-related READMEs (LLM model cards / usage)
    (
        "llama_index_readme.md",
        "https://raw.githubusercontent.com/jerryjliu/llama_index/main/README.md"
    ),
    (
        "mistral_ai_readme.md",
        "https://raw.githubusercontent.com/mistralai/mistral-src/main/README.md"
    ),
]

CORPUS_DIR = ".my-files"

def ensure_dir(path: str):
    if not os.path.exists(path):
        os.makedirs(path, exist_ok=True)


def download_file(name: str, url: str, out_dir: str):
    print(f"Downloading {name} from {url} ...")
    try:
        resp = requests.get(url, timeout=30)
        resp.raise_for_status()
    except Exception as e:
        print(f"  ERROR: failed to download {url} : {e}")
        return

    # Some of these are notebooks (.ipynb) – you may want to keep them raw
    # or strip JSON metadata here. For now we store raw content.
    out_path = os.path.join(out_dir, name)
    with open(out_path, "wb") as f:
        f.write(resp.content)
    print(f"  Saved to {out_path} ({len(resp.content)} bytes)")


def main():
    ensure_dir(CORPUS_DIR)
    print(f"Saving corpus into: {os.path.abspath(CORPUS_DIR)}\n")

    for fname, url in FILES:
        download_file(fname, url, CORPUS_DIR)

    print("\nDone. Example next steps for RAG:")
    print(textwrap.dedent(
        f"""
        - List documents in {CORPUS_DIR}/
        - Convert .ipynb or large markdown to plain text if needed
        - Chunk each file (e.g., 500–1000 tokens per chunk)
        - Embed and store chunks in your vector database
        """
    ))


if __name__ == "__main__":
    main()