#!/usr/bin/env python3
"""Train a local LLM with LoRA, QLoRA, or full fine-tuning."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from rich.console import Console
from rich.table import Table

from src.trainer import train_method

console = Console()

METHODS = {
    "lora": "LoRA — low-rank adapters on frozen base weights",
    "qlora": "QLoRA — 4-bit quantized base + LoRA (CUDA GPU)",
    "full": "Full fine-tuning — all weights updated (small models)",
}


def main() -> None:
    parser = argparse.ArgumentParser(description="Local LLM fine-tuning lab")
    parser.add_argument(
        "method",
        choices=list(METHODS.keys()),
        help="Fine-tuning method",
    )
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()

    console.print(f"[bold]Training:[/bold] {args.method} — {METHODS[args.method]}")
    report = train_method(args.method)

    if args.json:
        console.print_json(json.dumps(report, indent=2))
        return

    table = Table(title="Training complete")
    table.add_column("Field")
    table.add_column("Value")
    table.add_row("Method", report["method"])
    table.add_row("Base model", report["base_model"])
    table.add_row("Output", report["output_dir"])
    table.add_row("Trainable params", str(report["trainable_parameters"]["trainable"]))
    table.add_row("Total params", str(report["trainable_parameters"]["total"]))
    table.add_row("Trainable %", f"{report['trainable_parameters']['trainable_percent']}%")
    console.print(table)


if __name__ == "__main__":
    main()
