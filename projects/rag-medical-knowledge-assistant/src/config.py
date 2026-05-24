from __future__ import annotations

import os
from dataclasses import dataclass
from pathlib import Path

from dotenv import load_dotenv

load_dotenv()

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_KB = ROOT / "data" / "knowledge_base" / "medical_it_policies.json"


@dataclass(frozen=True)
class Settings:
    chroma_persist_dir: Path
    embedding_model: str
    collection_name: str
    llm_backend: str
    ollama_host: str
    ollama_model: str
    openai_api_key: str
    openai_base_url: str
    openai_model: str
    top_k: int
    knowledge_base_path: Path


def get_settings() -> Settings:
    return Settings(
        chroma_persist_dir=Path(os.getenv("CHROMA_PERSIST_DIR", ROOT / "chroma_db")),
        embedding_model=os.getenv(
            "EMBEDDING_MODEL", "sentence-transformers/all-MiniLM-L6-v2"
        ),
        collection_name=os.getenv("COLLECTION_NAME", "medical_knowledge"),
        llm_backend=os.getenv("LLM_BACKEND", "extractive").lower(),
        ollama_host=os.getenv("OLLAMA_HOST", "http://localhost:11434"),
        ollama_model=os.getenv("OLLAMA_MODEL", "llama3.2"),
        openai_api_key=os.getenv("OPENAI_API_KEY", ""),
        openai_base_url=os.getenv("OPENAI_BASE_URL", "https://api.openai.com/v1"),
        openai_model=os.getenv("OPENAI_MODEL", "gpt-4o-mini"),
        top_k=int(os.getenv("TOP_K", "4")),
        knowledge_base_path=Path(os.getenv("KNOWLEDGE_BASE_PATH", DEFAULT_KB)),
    )
