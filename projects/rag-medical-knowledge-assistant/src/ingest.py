from __future__ import annotations

import json
from dataclasses import dataclass
from pathlib import Path
from typing import Iterator


@dataclass
class Document:
    id: str
    title: str
    category: str
    text: str


@dataclass
class Chunk:
    chunk_id: str
    doc_id: str
    title: str
    category: str
    text: str


def load_documents(path: Path) -> list[Document]:
    raw = json.loads(path.read_text(encoding="utf-8"))
    return [
        Document(
            id=item["id"],
            title=item["title"],
            category=item["category"],
            text=item["text"],
        )
        for item in raw
    ]


def chunk_text(text: str, chunk_size: int = 320, overlap: int = 48) -> list[str]:
    words = text.split()
    if len(words) <= chunk_size:
        return [text]

    chunks: list[str] = []
    start = 0
    while start < len(words):
        end = min(start + chunk_size, len(words))
        chunks.append(" ".join(words[start:end]))
        if end == len(words):
            break
        start = max(end - overlap, start + 1)
    return chunks


def build_chunks(documents: list[Document]) -> Iterator[Chunk]:
    for doc in documents:
        for idx, piece in enumerate(chunk_text(doc.text)):
            yield Chunk(
                chunk_id=f"{doc.id}__chunk_{idx}",
                doc_id=doc.id,
                title=doc.title,
                category=doc.category,
                text=piece,
            )
