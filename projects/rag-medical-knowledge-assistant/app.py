"""Flask API for the medical IT RAG assistant."""

from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT))

from flask import Flask, jsonify, request

from src.rag_pipeline import RAGPipeline

app = Flask(__name__)
pipeline = RAGPipeline()


@app.get("/health")
def health():
    return jsonify({"status": "ok", "service": "medical-rag-assistant"})


@app.post("/ask")
def ask():
    payload = request.get_json(silent=True) or {}
    question = payload.get("question", "").strip()
    if not question:
        return jsonify({"error": "question is required"}), 400

    top_k = payload.get("top_k")
    response = pipeline.ask(question, top_k=top_k)
    return jsonify(pipeline.to_dict(response))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
