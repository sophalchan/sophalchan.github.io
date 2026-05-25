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


def load_documents(path: Path) -> list[Document]:
    data = json.loads(path.read_text(encoding="utf-8"))
    return [Document(**item) for item in data]
