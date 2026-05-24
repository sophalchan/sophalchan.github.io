#!/usr/bin/env python3
"""Example: structured medical note summarization prompt."""

from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from src.runner import PromptRunner


def main() -> None:
    runner = PromptRunner()
    variables = {
        "clinical_note": (
            "De-identified demo: Patient presented for follow-up imaging review. "
            "Prior knee radiograph available. Engineering team requested ROI metadata "
            "and texture feature pipeline status for OA staging experiment."
        ),
    }
    result = runner.run("medical_summary_structured", variables)
    print(result.raw_output)
    print(f"\nEvaluation score: {result.evaluation.score}")


if __name__ == "__main__":
    main()
