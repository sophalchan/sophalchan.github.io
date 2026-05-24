#!/usr/bin/env python3
"""CLI for asking questions against the medical IT RAG index."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from src.rag_pipeline import RAGPipeline  # noqa: E402


def main() -> None:
    parser = argparse.ArgumentParser(description="Query the medical IT RAG assistant")
    parser.add_argument("question", help="Natural-language question")
    parser.add_argument("--top-k", type=int, default=None)
    parser.add_argument("--json", action="store_true", help="Print JSON response")
    args = parser.parse_args()

    pipeline = RAGPipeline()
    response = pipeline.ask(args.question, top_k=args.top_k)

    if args.json:
        print(json.dumps(pipeline.to_dict(response), indent=2))
        return

    print(f"\nQ: {response.question}\n")
    print(response.answer)
    print("\nSources:")
    for src in response.sources:
        print(f"  - {src['title']} ({src['category']}) score={src['score']}")


if __name__ == "__main__":
    main()
