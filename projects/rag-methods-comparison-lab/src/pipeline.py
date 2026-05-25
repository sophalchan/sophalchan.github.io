from __future__ import annotations

import json
import os
from pathlib import Path

import yaml

from .chunking.strategies import (
    ChunkRecord,
    chunk_contextual,
    chunk_fixed_overlap,
    chunk_recursive_hierarchical,
    chunk_semantic_breakpoint,
    chunk_sentence_window,
)
from .documents import Document, load_documents
from .hybrid_search import HybridRetriever
from .vector_store import ChromaVectorDB

ROOT = Path(__file__).resolve().parents[1]
CONFIG_DIR = ROOT / "configs"

METHODS = (
    "fixed_overlap_chunking",
    "sentence_window_chunking",
    "recursive_hierarchical_chunking",
    "semantic_breakpoint_chunking",
    "contextual_retrieval",
    "vector_db_hybrid",
)


def load_config(method: str) -> dict:
    path = CONFIG_DIR / f"{method}.yaml"
    if not path.exists():
        raise FileNotFoundError(f"Missing config: {path}")
    return yaml.safe_load(path.read_text(encoding="utf-8"))


def build_chunks(method: str, documents: list[Document], cfg: dict) -> list[ChunkRecord]:
    c = cfg.get("chunking", {})
    strategy = c.get("strategy", method)

    if strategy == "fixed_overlap":
        return [
            ch
            for doc in documents
            for ch in chunk_fixed_overlap(
                doc, c.get("chunk_size_words", 28), c.get("overlap_words", 8)
            )
        ]

    if strategy == "sentence_window":
        return [
            ch
            for doc in documents
            for ch in chunk_sentence_window(
                doc, c.get("max_sentences", 2), c.get("sentence_overlap", 1)
            )
        ]

    if strategy == "recursive_hierarchical":
        return [
            ch
            for doc in documents
            for ch in chunk_recursive_hierarchical(
                doc,
                c.get("chunk_size_words", 32),
                c.get("separators"),
            )
        ]

    if strategy == "semantic_breakpoint":
        return [
            ch
            for doc in documents
            for ch in chunk_semantic_breakpoint(
                doc,
                c.get("max_sentences_per_chunk", 4),
                c.get("similarity_threshold", 0.55),
            )
        ]

    if strategy == "contextual_retrieval":
        return [
            ch
            for doc in documents
            for ch in chunk_contextual(
                doc,
                c.get("base_strategy", "sentence_window"),
                c.get("max_sentences", 2),
                c.get("sentence_overlap", 1),
                c.get("context_template"),
            )
        ]

    raise ValueError(f"Unknown chunking strategy '{strategy}' for method '{method}'")


def chunk_stats(chunks: list[ChunkRecord]) -> dict:
    if not chunks:
        return {"count": 0, "avg_tokens": 0, "strategies": []}
    tokens = [c.token_estimate for c in chunks]
    return {
        "count": len(chunks),
        "avg_tokens": round(sum(tokens) / len(tokens), 1),
        "min_tokens": min(tokens),
        "max_tokens": max(tokens),
        "strategies": sorted({c.chunking_strategy for c in chunks}),
    }


class RAGMethodPipeline:
    def __init__(self, method: str) -> None:
        if method not in METHODS:
            raise ValueError(f"Method must be one of {METHODS}")
        self.method = method
        self.cfg = load_config(method)
        self.persist = Path(os.getenv("CHROMA_PERSIST_DIR", ROOT / "chroma_db"))
        self.data_path = Path(
            os.getenv("DATA_PATH", ROOT / "data" / "knowledge_base" / "documents.json")
        )
        self.store = ChromaVectorDB(self.persist, self.cfg["vector_db"]["collection"])
        self._hybrid: HybridRetriever | None = None
        self._chunks: list[ChunkRecord] = []

    def build_index(self) -> dict:
        docs = load_documents(self.data_path)
        chunks = build_chunks(self.method, docs, self.cfg)
        self._chunks = chunks
        self.store.reset()
        count = self.store.upsert(chunks)
        if self.method == "vector_db_hybrid":
            self._hybrid = HybridRetriever(chunks, self.store, top_k=int(os.getenv("TOP_K", "4")))

        report = {
            "method": self.method,
            "description": self.cfg.get("description", ""),
            "chunks_indexed": count,
            "chunk_stats": chunk_stats(chunks),
            "collection": self.cfg["vector_db"]["collection"],
        }
        out_dir = Path(os.getenv("OUTPUT_DIR", ROOT / "outputs")) / self.method
        out_dir.mkdir(parents=True, exist_ok=True)
        (out_dir / "build_report.json").write_text(json.dumps(report, indent=2), encoding="utf-8")
        return report

    def retrieve(self, question: str, top_k: int | None = None) -> list[dict]:
        k = top_k or int(os.getenv("TOP_K", "4"))
        if self.method == "vector_db_hybrid":
            if self._hybrid is None:
                self.build_index()
            return self._hybrid.search(question)
        return self.store.query_vector(question, k)

    def answer(self, question: str, top_k: int | None = None) -> dict:
        hits = self.retrieve(question, top_k)
        lines = [
            f"**Method:** {self.method}",
            f"**Description:** {self.cfg.get('description', '')}",
            "",
            f"**Question:** {question}",
            "",
            "**Retrieved passages:**",
        ]
        for i, h in enumerate(hits, 1):
            meta = h["metadata"]
            strat = meta.get("chunking_strategy", "n/a")
            lines.append(
                f"{i}. [{meta['title']}] (strategy={strat}, {h.get('source', 'vector')}, "
                f"score={h['score']}) — {h['text']}"
            )
        return {
            "method": self.method,
            "question": question,
            "answer": "\n".join(lines),
            "sources": hits,
        }
