from __future__ import annotations

from rank_bm25 import BM25Okapi

from .chunking.strategies import ChunkRecord
from .vector_store import ChromaVectorDB


def tokenize(text: str) -> list[str]:
    return text.lower().split()


def reciprocal_rank_fusion(rankings: list[list[str]], k: int = 60) -> list[tuple[str, float]]:
    scores: dict[str, float] = {}
    for ranking in rankings:
        for rank, doc_id in enumerate(ranking):
            scores[doc_id] = scores.get(doc_id, 0) + 1 / (k + rank + 1)
    return sorted(scores.items(), key=lambda x: x[1], reverse=True)


class HybridRetriever:
    def __init__(self, chunks: list[ChunkRecord], vector_db: ChromaVectorDB, top_k: int = 4) -> None:
        self.chunks = {c.chunk_id: c for c in chunks}
        self.chunk_list = chunks
        self.vector_db = vector_db
        self.top_k = top_k
        self.bm25 = BM25Okapi([tokenize(c.embed_text) for c in chunks])

    def search(self, question: str) -> list[dict]:
        vector_hits = self.vector_db.query_vector(question, self.top_k * 2)
        vector_ranking = [h["chunk_id"] for h in vector_hits]

        bm25_scores = self.bm25.get_scores(tokenize(question))
        bm25_ranked = sorted(
            range(len(self.chunk_list)),
            key=lambda i: bm25_scores[i],
            reverse=True,
        )[: self.top_k * 2]
        bm25_ranking = [self.chunk_list[i].chunk_id for i in bm25_ranked]

        fused = reciprocal_rank_fusion([vector_ranking, bm25_ranking])[: self.top_k]

        hits = []
        for chunk_id, rrf_score in fused:
            chunk = self.chunks[chunk_id]
            vec_score = next(
                (h["score"] for h in vector_hits if h["chunk_id"] == chunk_id), 0.0
            )
            hits.append(
                {
                    "chunk_id": chunk_id,
                    "text": chunk.text,
                    "metadata": {
                        "doc_id": chunk.doc_id,
                        "title": chunk.title,
                        "category": chunk.category,
                        "chunking_strategy": chunk.chunking_strategy,
                    },
                    "score": round(rrf_score, 4),
                    "vector_score": vec_score,
                    "source": "hybrid_rrf",
                }
            )
        return hits
