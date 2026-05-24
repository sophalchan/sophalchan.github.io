from __future__ import annotations

from .config import get_settings
from .vector_store import VectorStore


class Retriever:
    def __init__(self, store: VectorStore | None = None) -> None:
        self.store = store or VectorStore()
        self.settings = get_settings()

    def retrieve(self, question: str, top_k: int | None = None) -> list[dict]:
        return self.store.query(question, top_k=top_k or self.settings.top_k)

    @staticmethod
    def format_context(hits: list[dict]) -> str:
        blocks: list[str] = []
        for i, hit in enumerate(hits, start=1):
            meta = hit["metadata"]
            blocks.append(
                f"[Source {i}] {meta['title']} ({meta['category']})\n{hit['text']}"
            )
        return "\n\n".join(blocks)
