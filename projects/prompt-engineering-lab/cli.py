#!/usr/bin/env python3
"""Prompt Engineering Lab — CLI for running and comparing prompts."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT))

from rich.console import Console
from rich.table import Table

from src.runner import PromptRunner

console = Console()


def main() -> None:
    parser = argparse.ArgumentParser(description="Prompt Engineering Lab CLI")
    sub = parser.add_subparsers(dest="command", required=True)

    run_cmd = sub.add_parser("run", help="Run a single prompt template")
    run_cmd.add_argument("prompt_id")
    run_cmd.add_argument("--source", default="Splunk ES")
    run_cmd.add_argument("--alert-type", default="Suspicious PowerShell")
    run_cmd.add_argument("--hostname", default="WS-CLINICAL-07")
    run_cmd.add_argument("--details", default="Encoded command line with outbound connection")
    run_cmd.add_argument("--json", action="store_true")

    compare_cmd = sub.add_parser("compare", help="A/B compare prompt variants")
    compare_cmd.add_argument("prompt_ids", nargs="+")
    compare_cmd.add_argument("--source", default="Elastic SIEM")
    compare_cmd.add_argument("--alert-type", default="Possible ransomware")
    compare_cmd.add_argument("--hostname", default="EHR-APP-02")
    compare_cmd.add_argument("--details", default="Mass file rename activity detected")

    args = parser.parse_args()
    runner = PromptRunner()

    if args.command == "run":
        variables = {
            "source": args.source,
            "alert_type": args.alert_type,
            "hostname": args.hostname,
            "details": args.details,
        }
        result = runner.run(args.prompt_id, variables)
        if args.json:
            console.print_json(json.dumps({
                "prompt_id": result.prompt_id,
                "technique": result.technique,
                "score": result.evaluation.score,
                "passed": result.evaluation.passed,
                "output": result.raw_output,
            }))
            return

        console.print(f"\n[bold]Prompt:[/bold] {result.prompt_id} ({result.technique})")
        console.print(f"[bold]Score:[/bold] {result.evaluation.score} — passed={result.evaluation.passed}")
        console.print("\n[bold]Rendered user prompt:[/bold]")
        console.print(result.user[:600] + ("..." if len(result.user) > 600 else ""))
        console.print("\n[bold]Output:[/bold]")
        console.print(result.raw_output)
        return

    variables = {
        "source": args.source,
        "alert_type": args.alert_type,
        "hostname": args.hostname,
        "details": args.details,
    }
    results = runner.compare(args.prompt_ids, variables)
    table = Table(title="Prompt A/B Comparison")
    table.add_column("Prompt ID")
    table.add_column("Technique")
    table.add_column("Score")
    table.add_column("Passed")

    for r in results:
        table.add_row(r.prompt_id, r.technique, str(r.evaluation.score), str(r.evaluation.passed))

    console.print(table)


if __name__ == "__main__":
    main()
