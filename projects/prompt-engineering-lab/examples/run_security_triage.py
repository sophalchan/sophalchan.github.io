#!/usr/bin/env python3
"""Example: compare zero-shot vs chain-of-thought security triage prompts."""

from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from src.runner import PromptRunner


def main() -> None:
    runner = PromptRunner()
    variables = {
        "source": "Elastic SIEM",
        "alert_type": "Data exfiltration pattern",
        "hostname": "PACS-ARCHIVE-01",
        "details": "Large outbound transfer to unknown cloud storage after hours",
    }

    results = runner.compare(
        ["security_triage_v1", "security_triage_cot_v2"],
        variables,
    )

    for r in results:
        print("=" * 60)
        print(f"Prompt: {r.prompt_id} | technique={r.technique}")
        print(f"Score: {r.evaluation.score} | passed={r.evaluation.passed}")
        print(r.raw_output)


if __name__ == "__main__":
    main()
