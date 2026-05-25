from __future__ import annotations

import os
from dataclasses import dataclass
from pathlib import Path

import yaml
from dotenv import load_dotenv

load_dotenv()

ROOT = Path(__file__).resolve().parents[1]
CONFIG_DIR = ROOT / "configs"

METHOD_CONFIG_FILES = {
    "lora": "lora.yaml",
    "qlora": "qlora.yaml",
    "full": "full_finetune.yaml",
}


@dataclass(frozen=True)
class TrainSettings:
    base_model: str
    data_path: Path
    output_dir: Path
    max_seq_length: int
    method: str
    method_config: dict


def load_method_config(method: str) -> dict:
    filename = METHOD_CONFIG_FILES.get(method)
    if not filename:
        raise ValueError(f"Unknown method: {method}. Use: lora, qlora, full")
    path = CONFIG_DIR / filename
    return yaml.safe_load(path.read_text(encoding="utf-8"))


def get_train_settings(method: str) -> TrainSettings:
    return TrainSettings(
        base_model=os.getenv("BASE_MODEL", "distilgpt2"),
        data_path=Path(os.getenv("DATA_PATH", ROOT / "data" / "sample_instructions.jsonl")),
        output_dir=Path(os.getenv("OUTPUT_DIR", ROOT / "outputs")) / method,
        max_seq_length=int(os.getenv("MAX_SEQ_LENGTH", "256")),
        method=method,
        method_config=load_method_config(method),
    )
