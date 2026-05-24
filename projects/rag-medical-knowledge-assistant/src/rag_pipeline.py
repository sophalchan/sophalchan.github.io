from __future__ import annotations

from dataclasses import dataclass, asdict

from .generator import generate_answer
from .retriever import Retriever


@dataclass
class RAGResponse:
    question: str
    answer: str
    sources: list[dict]
    backend: str


class RAGPipeline:
    def __init__(self, retriever: Retriever | None = None) -> None:
        self.retriever = retriever or Retriever()

    def ask(self, question: str, top_k: int | None = None) -> RAGResponse:
        from .config import get_settings

        hits = self.retriever.retrieve(question, top_k=top_k)
        context = self.retriever.format_context(hits)
        answer = generate_answer(question, hits, context)

        sources = [
            {
                "title": h["metadata"]["title"],
                "category": h["metadata"]["category"],
                "doc_id": h["metadata"]["doc_id"],
                "score": round(h["score"], 4),
                "excerpt": h["text"][:240],
            }
            for h in hits
        ]

        return RAGResponse(
            question=question,
            answer=answer,
            sources=sources,
            backend=get_settings().llm_backend,
        )

    def to_dict(self, response: RAGResponse) -> dict:
        return asdict(response)
