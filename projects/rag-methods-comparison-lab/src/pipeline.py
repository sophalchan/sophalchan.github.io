from __future__ import annotations

import os
from pathlib import Path

import yaml

from .documents import (
    Document,
    chunk_contextual,
    chunk_fixed,
    load_documents,
)
from .hybrid_search import HybridRetriever
from .vector_store import ChromaVectorDB

ROOT = Path(__file__).resolve().parents[1]
CONFIG_DIR = ROOT / "configs"

METHODS = ("fixed_chunking", "contextual_retrieval", "vector_db_hybrid")


def load_config(method: str) -> dict:
    path = CONFIG_DIR / f"{method}.yaml"
    return yaml.safe_load(path.read_text(encoding="utf-8"))


def build_chunks(method: str, documents: list[Document], cfg: dict) -> list:
    c = cfg.get("chunking", {})
    if method == "fixed_chunking":
        out = []
        for doc in documents:
            out.extend(
                chunk_fixed(doc, c.get("chunk_size_words", 24), c.get("overlap_words", 6))
            )
        return out
    if method == "contextual_retrieval":
        tpl = c.get(
            "context_template",
            "Document: {title} ({category}). Summary: {summary}\nChunk:\n",
        )
        out = []
        for doc in documents:
            out.extend(
                chunk_contextual(
                    doc,
                    c.get("chunk_size_words", 24),
                    c.get("overlap_words", 4),
                    tpl,
                )
            )
        return out
    if method == "vector_db_hybrid":
        out = []
        for doc in documents:
            out.extend(
                chunk_fixed(doc, c.get("chunk_size_words", 28), c.get("overlap_words", 5))
            )
        return out
    raise ValueError(f"Unknown method: {method}")


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
        collection = self.cfg["vector_db"]["collection"]
        self.store = ChromaVectorDB(self.persist, collection)
        self._hybrid: HybridRetriever | None = None
        self._chunks = []

    def build_index(self) -> int:
        docs = load_documents(self.data_path)
        chunks = build_chunks(self.method, docs, self.cfg)
        self._chunks = chunks
        self.store.reset()
        count = self.store.upsert(chunks)
        if self.method == "vector_db_hybrid":
            self._hybrid = HybridRetriever(
                chunks, self.store, top_k=int(os.getenv("TOP_K", "4"))
            )
        return count

    def retrieve(self, question: str, top_k: int | None = None) -> list[dict]:
        k = top_k or int(os.getenv("TOP_K", "4"))
        if self.method == "vector_db_hybrid":
            if self._hybrid is None:
                docs = load_documents(self.data_path)
                self._chunks = build_chunks(self.method, docs, self.cfg)
                self._hybrid = HybridRetriever(self._chunks, self.store, top_k=k)
            return self._hybrid.search(question)
        return self.store.query_vector(question, k)

    def answer(self, question: str, top_k: int | None = None) -> dict:
        hits = self.retrieve(question, top_k)
        lines = [
            f"Method: **{self.method}** — {self.cfg.get('description', '')}",
            "",
            f"**Question:** {question}",
            "",
            "**Retrieved context:**",
        ]
        for i, h in enumerate(hits, 1):
            meta = h["metadata"]
            lines.append(
                f"{i}. [{meta['title']}] ({h.get('source', 'vector')}, score={h['score']}) — {h['text']}"
            )
        return {
            "method": self.method,
            "question": question,
            "answer": "\n".join(lines),
            "sources": hits,
        }
