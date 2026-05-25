from __future__ import annotations

import json
from pathlib import Path

from datasets import Dataset


def format_instruction(example: dict) -> str:
    instruction = example.get("instruction", "").strip()
    inp = example.get("input", "").strip()
    output = example.get("output", "").strip()

    if inp:
        prompt = f"### Instruction:\n{instruction}\n\n### Input:\n{inp}\n\n### Response:\n{output}"
    else:
        prompt = f"### Instruction:\n{instruction}\n\n### Response:\n{output}"
    return prompt + "<|endoftext|>"


def load_instruction_dataset(path: Path) -> Dataset:
    rows: list[dict] = []
    for line in path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if line:
            rows.append(json.loads(line))

    texts = [{"text": format_instruction(row)} for row in rows]
    return Dataset.from_list(texts)
