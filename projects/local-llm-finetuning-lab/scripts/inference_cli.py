#!/usr/bin/env python3
"""Generate text from a fine-tuned adapter or base model."""

from __future__ import annotations

import argparse
import os
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from src.inference import generate


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("prompt", help="Instruction or prompt text")
    parser.add_argument("--method", default="lora", choices=["lora", "qlora", "full"])
    parser.add_argument("--base-model", default=os.getenv("BASE_MODEL", "distilgpt2"))
    parser.add_argument("--adapter-dir", default=None)
    args = parser.parse_args()

    adapter = args.adapter_dir or str(ROOT / "outputs" / args.method / "final")
    formatted = f"### Instruction:\n{args.prompt}\n\n### Response:\n"

    text = generate(args.base_model, adapter if Path(adapter).exists() else None, formatted)
    print(text)


if __name__ == "__main__":
    main()
