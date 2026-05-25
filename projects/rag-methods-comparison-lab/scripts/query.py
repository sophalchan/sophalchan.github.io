#!/usr/bin/env python3
import argparse
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from src.pipeline import METHODS, RAGMethodPipeline


def main():
    p = argparse.ArgumentParser()
    p.add_argument("method", choices=METHODS)
    p.add_argument("question")
    p.add_argument("--json", action="store_true")
    args = p.parse_args()

    pipe = RAGMethodPipeline(args.method)
    result = pipe.answer(args.question)
    if args.json:
        print(json.dumps(result, indent=2))
    else:
        print(result["answer"])


if __name__ == "__main__":
    main()
