#!/usr/bin/env python3
"""Build or rebuild the Chroma vector index from the knowledge base."""

from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from src.vector_store import build_index_from_kb  # noqa: E402


def main() -> None:
    count = build_index_from_kb()
    print(f"Index built successfully — {count} chunks indexed.")


if __name__ == "__main__":
    main()
