#!/usr/bin/env python3
"""Compare trainable parameter counts across LoRA, QLoRA, and full fine-tuning."""

from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from rich.console import Console
from rich.table import Table

from src.config import get_train_settings
from src.model_utils import apply_lora, count_trainable_parameters, load_base_model

console = Console()


def compare() -> list[dict]:
    rows = []
    settings_lora = get_train_settings("lora")
    base_id = settings_lora.base_model

    # LoRA
    m = load_base_model(base_id, qlora=False)
    m = apply_lora(m, settings_lora.method_config.get("lora", {}))
    rows.append({"method": "lora", **count_trainable_parameters(m), "notes": "PEFT adapters only"})

    # QLoRA (parameter count on adapter side; base frozen in 4-bit)
    try:
        settings_q = get_train_settings("qlora")
        mq = load_base_model(base_id, qlora=True)
        mq = apply_lora(mq, settings_q.method_config.get("lora", {}))
        rows.append({
            "method": "qlora",
            **count_trainable_parameters(mq),
            "notes": "4-bit base + LoRA (CUDA)",
        })
    except RuntimeError as exc:
        rows.append({
            "method": "qlora",
            "trainable": 0,
            "total": 0,
            "trainable_percent": 0,
            "notes": str(exc),
        })

    # Full
    mf = load_base_model(base_id, qlora=False)
    rows.append({"method": "full", **count_trainable_parameters(mf), "notes": "All parameters trainable"})

    return rows


def main() -> None:
    rows = compare()
    out = ROOT / "outputs" / "method_comparison.json"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(rows, indent=2), encoding="utf-8")

    table = Table(title="Fine-tuning method comparison")
    table.add_column("Method")
    table.add_column("Trainable")
    table.add_column("Total")
    table.add_column("% Trainable")
    table.add_column("Notes")

    for r in rows:
        table.add_row(
            r["method"],
            str(r.get("trainable", "n/a")),
            str(r.get("total", "n/a")),
            str(r.get("trainable_percent", "n/a")),
            r.get("notes", ""),
        )

    console.print(table)
    console.print(f"\nSaved: {out}")


if __name__ == "__main__":
    main()
