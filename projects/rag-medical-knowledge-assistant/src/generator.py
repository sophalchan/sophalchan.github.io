from __future__ import annotations

import requests

from .config import get_settings

SYSTEM_PROMPT = """You are a medical IT and AI engineering assistant.
Answer ONLY using the provided context. If the context is insufficient, say you do not know.
Cite sources by title. Never invent HIPAA rules or clinical advice."""


def _extractive_answer(question: str, hits: list[dict]) -> str:
    if not hits:
        return "No relevant policy documents were found for this question."

    lines = [
        "Based on retrieved internal policy excerpts:",
        "",
    ]
    for hit in hits[:3]:
        meta = hit["metadata"]
        lines.append(f"• **{meta['title']}** — {hit['text']}")
    lines.append("")
    lines.append(f"*(Question: {question})*")
    return "\n".join(lines)


def _ollama_generate(question: str, context: str) -> str:
    settings = get_settings()
    prompt = (
        f"{SYSTEM_PROMPT}\n\n"
        f"Context:\n{context}\n\n"
        f"Question: {question}\n\nAnswer:"
    )
    response = requests.post(
        f"{settings.ollama_host.rstrip('/')}/api/generate",
        json={"model": settings.ollama_model, "prompt": prompt, "stream": False},
        timeout=120,
    )
    response.raise_for_status()
    return response.json()["response"].strip()


def _openai_generate(question: str, context: str) -> str:
    settings = get_settings()
    if not settings.openai_api_key:
        raise ValueError("OPENAI_API_KEY is required when LLM_BACKEND=openai")

    headers = {
        "Authorization": f"Bearer {settings.openai_api_key}",
        "Content-Type": "application/json",
    }
    payload = {
        "model": settings.openai_model,
        "messages": [
            {"role": "system", "content": SYSTEM_PROMPT},
            {
                "role": "user",
                "content": f"Context:\n{context}\n\nQuestion: {question}",
            },
        ],
        "temperature": 0.2,
    }
    response = requests.post(
        f"{settings.openai_base_url.rstrip('/')}/chat/completions",
        headers=headers,
        json=payload,
        timeout=120,
    )
    response.raise_for_status()
    return response.json()["choices"][0]["message"]["content"].strip()


def generate_answer(question: str, hits: list[dict], context: str) -> str:
    backend = get_settings().llm_backend

    if backend == "extractive":
        return _extractive_answer(question, hits)
    if backend == "ollama":
        return _ollama_generate(question, context)
    if backend == "openai":
        return _openai_generate(question, context)
    raise ValueError(f"Unknown LLM_BACKEND: {backend}")
