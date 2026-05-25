#!/usr/bin/env python3
"""Build all three indexes and query the same question for side-by-side comparison."""
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from rich.console import Console
from rich.panel import Panel

from src.pipeline import METHODS, RAGMethodPipeline

console = Console()
QUESTION = "How does contextual retrieval improve RAG chunk quality?"


def main():
    for method in METHODS:
        console.print(f"[bold cyan]Building {method}...[/bold cyan]")
        RAGMethodPipeline(method).build_index()

    console.print(f"\n[bold]Comparing methods for:[/bold] {QUESTION}\n")
    for method in METHODS:
        result = RAGMethodPipeline(method).answer(QUESTION)
        console.print(Panel(result["answer"], title=method, border_style="green"))


if __name__ == "__main__":
    main()
