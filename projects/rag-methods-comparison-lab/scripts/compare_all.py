#!/usr/bin/env python3
"""Build all six RAG indexes and compare retrieval on one question."""
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from rich.console import Console
from rich.table import Table
from rich.panel import Panel

from src.pipeline import METHODS, RAGMethodPipeline

console = Console()
QUESTION = "How do sentence chunking and semantic breakpoints improve RAG retrieval?"


def main():
    stats_table = Table(title="Chunking statistics per method")
    stats_table.add_column("Method")
    stats_table.add_column("Chunks")
    stats_table.add_column("Avg tokens")
    stats_table.add_column("Min–Max tokens")

    for method in METHODS:
        console.print(f"[bold cyan]Indexing {method}...[/bold cyan]")
        report = RAGMethodPipeline(method).build_index()
        cs = report["chunk_stats"]
        stats_table.add_row(
            method,
            str(cs["count"]),
            str(cs["avg_tokens"]),
            f"{cs.get('min_tokens', 0)}–{cs.get('max_tokens', 0)}",
        )

    console.print(stats_table)
    console.print(f"\n[bold]Query:[/bold] {QUESTION}\n")

    for method in METHODS:
        result = RAGMethodPipeline(method).answer(QUESTION)
        console.print(Panel(result["answer"], title=method, border_style="green"))


if __name__ == "__main__":
    main()
