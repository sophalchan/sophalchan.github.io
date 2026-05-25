# Advanced RAG Methods Comparison Lab

Compare **six RAG pipelines** emphasizing **advanced chunking** and **vector database retrieval** — inspired by [Pinecone chunking strategies](https://www.pinecone.io/learn/chunking-strategies/) and semantic/recursive approaches (Kamradt, LangChain).

## Six methods

| # | Method | Technique |
|---|--------|-----------|
| 1 | **fixed_overlap_chunking** | Word windows + **sliding overlap** |
| 2 | **sentence_window_chunking** | **Sentence boundaries** + overlapping sentence windows |
| 3 | **recursive_hierarchical_chunking** | **Recursive** split: `\n\n` → `\n` → `. ` → words |
| 4 | **semantic_breakpoint_chunking** | **Embedding similarity** drops = chunk boundary |
| 5 | **contextual_retrieval** | Prepend **document + summary** to each chunk embedding |
| 6 | **vector_db_hybrid** | **Chroma** vectors + **BM25** + **RRF** fusion |

## Quick start

```bash
cd projects/rag-methods-comparison-lab
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt

# Preview chunk counts before embedding
python scripts/chunk_stats.py

# Build + query one method
python scripts/build_index.py sentence_window_chunking
python scripts/query.py semantic_breakpoint_chunking "What is semantic chunking?"

# Compare all six
python scripts/compare_all.py
```

## Framework

```
configs/                    # YAML hyperparameters per method
src/chunking/strategies.py  # All chunking implementations
src/vector_store.py         # ChromaDB
src/hybrid_search.py        # BM25 + RRF
src/pipeline.py             # build_index / retrieve / answer
scripts/                    # CLI tools
```

## Outputs

`outputs/<method>/build_report.json` — chunk count, avg/min/max tokens, collection name.

**Author:** Sophal Chan
