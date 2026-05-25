# RAG Methods Comparison Lab

Compare **three RAG architectures** on the same knowledge base:

| Method | Key idea | Storage |
|--------|----------|---------|
| **fixed_chunking** | Traditional overlapping word chunks | Chroma vector DB |
| **contextual_retrieval** | Prepend document context to each chunk before embedding | Chroma vector DB |
| **vector_db_hybrid** | Vector DB + BM25 keyword search fused with RRF | Chroma + sparse index |

## Quick start

```bash
cd projects/rag-methods-comparison-lab
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt

python scripts/build_index.py fixed_chunking
python scripts/build_index.py contextual_retrieval
python scripts/build_index.py vector_db_hybrid

python scripts/query.py fixed_chunking "What is contextual retrieval?"
python scripts/compare_all.py
```

## Framework layout

```
configs/           # YAML per RAG method
data/              # Shared JSON knowledge base
src/
  documents.py     # Chunking strategies
  vector_store.py  # ChromaDB
  hybrid_search.py # BM25 + RRF for hybrid method
  pipeline.py      # Unified build + retrieve + answer
scripts/           # build_index, query, compare_all
app.py             # Flask API
```

## API

```bash
python app.py
curl -X POST http://localhost:8090/build/fixed_chunking
curl -X POST http://localhost:8090/ask -H "Content-Type: application/json" \
  -d '{"method":"vector_db_hybrid","question":"How does hybrid search work?"}'
```

**Author:** Sophal Chan
