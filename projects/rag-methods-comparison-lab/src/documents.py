from __future__ import annotations

import json
from dataclasses import dataclass
from pathlib import Path


@dataclass
class Document:
    id: str
    title: str
    category: str
    text: str


@dataclass
class ChunkRecord:
    chunk_id: str
    doc_id: str
    title: str
    category: str
    text: str
    embed_text: str


def load_documents(path: Path) -> list[Document]:
    data = json.loads(path.read_text(encoding="utf-8"))
    return [Document(**item) for item in data]


def _split_words(text: str, size: int, overlap: int) -> list[str]:
    words = text.split()
    if len(words) <= size:
        return [text]
    chunks = []
    start = 0
    while start < len(words):
        end = min(start + size, len(words))
        chunks.append(" ".join(words[start:end]))
        if end >= len(words):
            break
        start = max(end - overlap, start + 1)
    return chunks


def chunk_fixed(doc: Document, chunk_size: int, overlap: int) -> list[ChunkRecord]:
    records = []
    for i, piece in enumerate(_split_words(doc.text, chunk_size, overlap)):
        records.append(
            ChunkRecord(
                chunk_id=f"{doc.id}__{i}",
                doc_id=doc.id,
                title=doc.title,
                category=doc.category,
                text=piece,
                embed_text=piece,
            )
        )
    return records


def chunk_contextual(
    doc: Document,
    chunk_size: int,
    overlap: int,
    context_template: str,
) -> list[ChunkRecord]:
    summary = doc.text[:120] + ("..." if len(doc.text) > 120 else "")
    prefix = context_template.format(
        title=doc.title, category=doc.category, summary=summary
    )
    records = []
    for i, piece in enumerate(_split_words(doc.text, chunk_size, overlap)):
        records.append(
            ChunkRecord(
                chunk_id=f"{doc.id}__ctx_{i}",
                doc_id=doc.id,
                title=doc.title,
                category=doc.category,
                text=piece,
                embed_text=prefix + piece,
            )
        )
    return records
