# Medical IT RAG Knowledge Assistant

Retrieval-Augmented Generation (RAG) pipeline for **medical IT, HIPAA compliance, and local LLM deployment** policy Q&A. Built for AI engineering workflows where answers must be **grounded in approved documents** with source citations.

## Features

- Document ingestion and chunking from JSON knowledge base
- Local embeddings via `sentence-transformers/all-MiniLM-L6-v2`
- Persistent vector store with **ChromaDB**
- Three generator backends: **extractive** (default), **Ollama**, **OpenAI-compatible**
- Flask REST API (`POST /ask`) and CLI query tool

## Quick Start

```bash
cd projects/rag-medical-knowledge-assistant
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt
cp .env.example .env
python scripts/build_index.py
python scripts/query_cli.py "What are HIPAA audit logging requirements?"
```

## API

```bash
python app.py
curl -X POST http://localhost:8080/ask \
  -H "Content-Type: application/json" \
  -d '{"question": "How should we deploy local LLMs for medical NLP?"}'
```

## Project Structure

```
rag-medical-knowledge-assistant/
├── app.py                      # Flask API
├── data/knowledge_base/          # Source documents (JSON)
├── scripts/
│   ├── build_index.py          # Step 1: embed + index
│   └── query_cli.py            # Step 2: CLI queries
└── src/
    ├── ingest.py               # Load + chunk documents
    ├── embeddings.py           # Sentence-transformer encoder
    ├── vector_store.py         # ChromaDB persistence
    ├── retriever.py            # Top-k semantic search
    ├── generator.py            # LLM / extractive answer
    └── rag_pipeline.py         # End-to-end orchestration
```

## Configuration

| Variable | Default | Description |
|----------|---------|-------------|
| `LLM_BACKEND` | `extractive` | `extractive`, `ollama`, or `openai` |
| `EMBEDDING_MODEL` | `all-MiniLM-L6-v2` | Hugging Face embedding model |
| `TOP_K` | `4` | Retrieved chunks per query |
| `OLLAMA_HOST` | `http://localhost:11434` | Local Ollama endpoint |

## Author

**Sophal Chan** — AI Engineering & Cybersecurity portfolio
