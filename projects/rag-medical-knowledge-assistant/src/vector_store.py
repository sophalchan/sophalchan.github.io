from __future__ import annotations

import chromadb
from chromadb.config import Settings as ChromaSettings

from .config import Settings, get_settings
from .embeddings import embed_texts
from .ingest import Chunk, build_chunks, load_documents


class VectorStore:
    def __init__(self, settings: Settings | None = None) -> None:
        self.settings = settings or get_settings()
        self.settings.chroma_persist_dir.mkdir(parents=True, exist_ok=True)
        self.client = chromadb.PersistentClient(
            path=str(self.settings.chroma_persist_dir),
            settings=ChromaSettings(anonymized_telemetry=False),
        )
        self.collection = self.client.get_or_create_collection(
            name=self.settings.collection_name,
            metadata={"hnsw:space": "cosine"},
        )

    def reset(self) -> None:
        self.client.delete_collection(self.settings.collection_name)
        self.collection = self.client.get_or_create_collection(
            name=self.settings.collection_name,
            metadata={"hnsw:space": "cosine"},
        )

    def upsert_chunks(self, chunks: list[Chunk]) -> int:
        if not chunks:
            return 0

        texts = [c.text for c in chunks]
        embeddings = embed_texts(texts)
        self.collection.upsert(
            ids=[c.chunk_id for c in chunks],
            documents=texts,
            embeddings=embeddings,
            metadatas=[
                {
                    "doc_id": c.doc_id,
                    "title": c.title,
                    "category": c.category,
                }
                for c in chunks
            ],
        )
        return len(chunks)

    def query(self, question: str, top_k: int | None = None) -> list[dict]:
        k = top_k or self.settings.top_k
        query_vec = embed_texts([question])[0]
        result = self.collection.query(
            query_embeddings=[query_vec],
            n_results=k,
            include=["documents", "metadatas", "distances"],
        )

        hits: list[dict] = []
        for idx in range(len(result["ids"][0])):
            hits.append(
                {
                    "chunk_id": result["ids"][0][idx],
                    "text": result["documents"][0][idx],
                    "metadata": result["metadatas"][0][idx],
                    "score": 1 - result["distances"][0][idx],
                }
            )
        return hits


def build_index_from_kb(settings: Settings | None = None) -> int:
    cfg = settings or get_settings()
    store = VectorStore(cfg)
    store.reset()
    documents = load_documents(cfg.knowledge_base_path)
    chunks = list(build_chunks(documents))
    return store.upsert_chunks(chunks)
