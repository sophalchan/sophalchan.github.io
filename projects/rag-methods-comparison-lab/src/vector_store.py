from __future__ import annotations

from pathlib import Path

import chromadb
from chromadb.config import Settings as ChromaSettings

from .chunking.strategies import ChunkRecord
from .embeddings import embed


class ChromaVectorDB:
    def __init__(self, persist_dir: Path, collection_name: str) -> None:
        persist_dir.mkdir(parents=True, exist_ok=True)
        self.client = chromadb.PersistentClient(
            path=str(persist_dir),
            settings=ChromaSettings(anonymized_telemetry=False),
        )
        self.collection_name = collection_name
        self.collection = self.client.get_or_create_collection(
            name=collection_name,
            metadata={"hnsw:space": "cosine"},
        )

    def reset(self) -> None:
        try:
            self.client.delete_collection(self.collection_name)
        except Exception:  # noqa: BLE001
            pass
        self.collection = self.client.get_or_create_collection(
            name=self.collection_name,
            metadata={"hnsw:space": "cosine"},
        )

    def upsert(self, chunks: list[ChunkRecord]) -> int:
        if not chunks:
            return 0
        texts = [c.embed_text for c in chunks]
        vectors = embed(texts)
        self.collection.upsert(
            ids=[c.chunk_id for c in chunks],
            documents=[c.text for c in chunks],
            embeddings=vectors,
            metadatas=[
                {
                    "doc_id": c.doc_id,
                    "title": c.title,
                    "category": c.category,
                    "chunking_strategy": c.chunking_strategy,
                    "chunk_index": c.chunk_index,
                    "token_estimate": c.token_estimate,
                }
                for c in chunks
            ],
        )
        return len(chunks)

    def query_vector(self, question: str, top_k: int) -> list[dict]:
        qvec = embed([question])[0]
        res = self.collection.query(
            query_embeddings=[qvec],
            n_results=top_k,
            include=["documents", "metadatas", "distances"],
        )
        hits = []
        for i in range(len(res["ids"][0])):
            hits.append(
                {
                    "chunk_id": res["ids"][0][i],
                    "text": res["documents"][0][i],
                    "metadata": res["metadatas"][0][i],
                    "score": round(1 - res["distances"][0][i], 4),
                    "source": "vector",
                }
            )
        return hits
