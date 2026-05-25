from __future__ import annotations

import re
from dataclasses import dataclass

import numpy as np

from ..documents import Document


@dataclass
class ChunkRecord:
    chunk_id: str
    doc_id: str
    title: str
    category: str
    text: str
    embed_text: str
    chunking_strategy: str
    chunk_index: int
    token_estimate: int


def _estimate_tokens(text: str) -> int:
    return max(1, len(text.split()))


def _make_record(
    doc: Document,
    index: int,
    text: str,
    embed_text: str,
    strategy: str,
) -> ChunkRecord:
    return ChunkRecord(
        chunk_id=f"{doc.id}__{strategy}__{index}",
        doc_id=doc.id,
        title=doc.title,
        category=doc.category,
        text=text.strip(),
        embed_text=embed_text.strip(),
        chunking_strategy=strategy,
        chunk_index=index,
        token_estimate=_estimate_tokens(text),
    )


def _split_words(text: str, size: int, overlap: int) -> list[str]:
    words = text.split()
    if len(words) <= size:
        return [text]
    chunks: list[str] = []
    start = 0
    while start < len(words):
        end = min(start + size, len(words))
        chunks.append(" ".join(words[start:end]))
        if end >= len(words):
            break
        start = max(end - overlap, start + 1)
    return chunks


def split_sentences(text: str) -> list[str]:
    parts = re.split(r"(?<=[.!?])\s+", text.strip())
    return [p.strip() for p in parts if p.strip()]


def chunk_fixed_overlap(
    doc: Document,
    chunk_size_words: int = 28,
    overlap_words: int = 8,
) -> list[ChunkRecord]:
    """Fixed-size word windows with sliding overlap (baseline)."""
    records = []
    for i, piece in enumerate(_split_words(doc.text, chunk_size_words, overlap_words)):
        records.append(_make_record(doc, i, piece, piece, "fixed_overlap"))
    return records


def chunk_sentence_window(
    doc: Document,
    max_sentences: int = 2,
    sentence_overlap: int = 1,
) -> list[ChunkRecord]:
    """Group sentences into windows; overlap sentences between consecutive chunks."""
    sentences = split_sentences(doc.text)
    if not sentences:
        return [_make_record(doc, 0, doc.text, doc.text, "sentence_window")]

    records = []
    step = max(1, max_sentences - sentence_overlap)
    idx = 0
    for start in range(0, len(sentences), step):
        window = sentences[start : start + max_sentences]
        if not window:
            break
        piece = " ".join(window)
        records.append(_make_record(doc, idx, piece, piece, "sentence_window"))
        idx += 1
        if start + max_sentences >= len(sentences):
            break
    return records


def chunk_recursive_hierarchical(
    doc: Document,
    chunk_size_words: int = 32,
    separators: list[str] | None = None,
) -> list[ChunkRecord]:
    """Recursive split: try paragraph breaks, then sentences, then words (LangChain-style)."""
    seps = separators or ["\n\n", "\n", ". ", " "]

    def _recurse(text: str, sep_idx: int) -> list[str]:
        text = text.strip()
        if not text:
            return []
        if _estimate_tokens(text) <= chunk_size_words:
            return [text]
        if sep_idx >= len(seps):
            return _split_words(text, chunk_size_words, 4)

        sep = seps[sep_idx]
        parts = text.split(sep) if sep != " " else text.split()
        parts = [p.strip() for p in parts if p.strip()]
        if len(parts) <= 1:
            return _recurse(text, sep_idx + 1)

        merged: list[str] = []
        buffer = ""
        for part in parts:
            candidate = f"{buffer}{sep}{part}".strip() if buffer else part
            if _estimate_tokens(candidate) <= chunk_size_words:
                buffer = candidate
            else:
                if buffer:
                    merged.extend(_recurse(buffer, sep_idx + 1))
                buffer = part
        if buffer:
            merged.extend(_recurse(buffer, sep_idx + 1))
        return merged

    records = []
    for i, piece in enumerate(_recurse(doc.text, 0)):
        records.append(_make_record(doc, i, piece, piece, "recursive_hierarchical"))
    return records


def chunk_semantic_breakpoint(
    doc: Document,
    max_sentences_per_chunk: int = 4,
    similarity_threshold: float = 0.55,
) -> list[ChunkRecord]:
    """Semantic chunking: break when adjacent sentence-group embedding similarity drops."""
    sentences = split_sentences(doc.text)
    if len(sentences) <= 1:
        return [_make_record(doc, 0, doc.text, doc.text, "semantic_breakpoint")]

    try:
        from ..embeddings import embed
    except ImportError:
        return chunk_sentence_window(doc, max_sentences_per_chunk, 1)

    vectors = np.array(embed(sentences))
    groups: list[list[str]] = [[sentences[0]]]

    for i in range(1, len(sentences)):
        prev_vec = vectors[i - 1]
        curr_vec = vectors[i]
        sim = float(np.dot(prev_vec, curr_vec) / (np.linalg.norm(prev_vec) * np.linalg.norm(curr_vec) + 1e-9))
        current_group = groups[-1]
        if sim < similarity_threshold or len(current_group) >= max_sentences_per_chunk:
            groups.append([sentences[i]])
        else:
            current_group.append(sentences[i])

    records = []
    for idx, group in enumerate(groups):
        piece = " ".join(group)
        records.append(_make_record(doc, idx, piece, piece, "semantic_breakpoint"))
    return records


def chunk_contextual(
    doc: Document,
    base_strategy: str = "sentence_window",
    max_sentences: int = 2,
    sentence_overlap: int = 1,
    context_template: str | None = None,
) -> list[ChunkRecord]:
    """Contextual retrieval: enrich each chunk with document context before embedding."""
    if base_strategy == "fixed_overlap":
        base = chunk_fixed_overlap(doc)
    elif base_strategy == "recursive_hierarchical":
        base = chunk_recursive_hierarchical(doc)
    else:
        base = chunk_sentence_window(doc, max_sentences, sentence_overlap)

    tpl = context_template or (
        "Document: {title} | Category: {category}\n"
        "Summary: {summary}\n"
        "Passage:\n"
    )
    summary = doc.text[:160] + ("..." if len(doc.text) > 160 else "")
    prefix = tpl.format(title=doc.title, category=doc.category, summary=summary)

    records = []
    for i, chunk in enumerate(base):
        records.append(
            _make_record(
                doc,
                i,
                chunk.text,
                prefix + chunk.text,
                "contextual_retrieval",
            )
        )
    return records
