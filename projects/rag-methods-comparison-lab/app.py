"""Flask API — compare RAG methods: fixed chunking, contextual retrieval, vector DB hybrid."""

from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT))

from flask import Flask, jsonify, request

from src.pipeline import METHODS, RAGMethodPipeline

app = Flask(__name__)
pipelines = {m: RAGMethodPipeline(m) for m in METHODS}


@app.get("/health")
def health():
    return jsonify({"status": "ok", "methods": list(METHODS)})


@app.post("/build/<method>")
def build(method: str):
    if method not in METHODS:
        return jsonify({"error": f"method must be one of {METHODS}"}), 400
    n = pipelines[method].build_index()
    return jsonify({"method": method, "chunks_indexed": n})


@app.post("/ask")
def ask():
    body = request.get_json(silent=True) or {}
    question = (body.get("question") or "").strip()
    method = body.get("method", "fixed_chunking")
    if not question:
        return jsonify({"error": "question required"}), 400
    if method not in METHODS:
        return jsonify({"error": f"method must be one of {METHODS}"}), 400
    return jsonify(pipelines[method].answer(question))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8090, debug=True)
