from __future__ import annotations

from functools import lru_cache

from sentence_transformers import SentenceTransformer

from .config import get_settings


@lru_cache(maxsize=1)
def get_embedding_model() -> SentenceTransformer:
    settings = get_settings()
    return SentenceTransformer(settings.embedding_model)


def embed_texts(texts: list[str]) -> list[list[float]]:
    model = get_embedding_model()
    vectors = model.encode(texts, show_progress_bar=False, normalize_embeddings=True)
    return vectors.tolist()
