#!/usr/bin/env python3
import argparse
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from src.pipeline import METHODS, RAGMethodPipeline


def main():
    p = argparse.ArgumentParser()
    p.add_argument("method", choices=METHODS)
    args = p.parse_args()
    pipe = RAGMethodPipeline(args.method)
    n = pipe.build_index()
    print(f"Built index for [{args.method}]: {n} chunks → collection '{pipe.cfg['vector_db']['collection']}'")


if __name__ == "__main__":
    main()
