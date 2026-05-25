#!/usr/bin/env python3
"""Print chunking statistics without full index rebuild display."""
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from rich.console import Console
from rich.table import Table

from src.documents import load_documents
from src.pipeline import METHODS, build_chunks, chunk_stats, load_config
import os

console = Console()
data = Path(os.getenv("DATA_PATH", ROOT / "data" / "knowledge_base" / "documents.json"))
docs = load_documents(data)

table = Table(title="Chunking preview (before embedding)")
table.add_column("Method")
table.add_column("Chunks")
table.add_column("Avg tokens")
table.add_column("Strategy tag")

for method in METHODS:
    cfg = load_config(method)
    chunks = build_chunks(method, docs, cfg)
    cs = chunk_stats(chunks)
    table.add_row(method, str(cs["count"]), str(cs["avg_tokens"]), ", ".join(cs["strategies"]))

console.print(table)
