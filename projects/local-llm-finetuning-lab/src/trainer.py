from __future__ import annotations

import json
from pathlib import Path

import torch
from datasets import Dataset
from transformers import DataCollatorForLanguageModeling, Trainer, TrainingArguments

from .config import TrainSettings, get_train_settings
from .data_loader import load_instruction_dataset
from .model_utils import (
    apply_lora,
    count_trainable_parameters,
    load_base_model,
    load_tokenizer,
)


def tokenize_dataset(dataset: Dataset, tokenizer, max_length: int) -> Dataset:
    def _tok(batch):
        return tokenizer(
            batch["text"],
            truncation=True,
            max_length=max_length,
            padding="max_length",
        )

    return dataset.map(_tok, batched=True, remove_columns=dataset.column_names)


def build_trainer(
    settings: TrainSettings,
    model,
    tokenizer,
    train_dataset: Dataset,
) -> Trainer:
    cfg = settings.method_config.get("training", {})
    args = TrainingArguments(
        output_dir=str(settings.output_dir),
        num_train_epochs=cfg.get("num_train_epochs", 1),
        per_device_train_batch_size=cfg.get("per_device_train_batch_size", 2),
        gradient_accumulation_steps=cfg.get("gradient_accumulation_steps", 4),
        learning_rate=cfg.get("learning_rate", 2e-4),
        warmup_ratio=cfg.get("warmup_ratio", 0.05),
        logging_steps=cfg.get("logging_steps", 5),
        save_steps=cfg.get("save_steps", 50),
        save_total_limit=2,
        report_to="none",
        fp16=torch.cuda.is_available(),
        gradient_checkpointing=cfg.get("gradient_checkpointing", False),
        remove_unused_columns=False,
    )

    collator = DataCollatorForLanguageModeling(tokenizer=tokenizer, mlm=False)
    return Trainer(
        model=model,
        args=args,
        train_dataset=train_dataset,
        data_collator=collator,
    )


def train_method(method: str) -> dict:
    settings = get_train_settings(method)
    settings.output_dir.mkdir(parents=True, exist_ok=True)

    tokenizer = load_tokenizer(settings.base_model)
    raw_ds = load_instruction_dataset(settings.data_path)
    train_ds = tokenize_dataset(raw_ds, tokenizer, settings.max_seq_length)

    if method == "qlora":
        model = load_base_model(settings.base_model, qlora=True)
        model = apply_lora(model, settings.method_config.get("lora", {}))
    elif method == "lora":
        model = load_base_model(settings.base_model, qlora=False)
        model = apply_lora(model, settings.method_config.get("lora", {}))
    elif method == "full":
        model = load_base_model(settings.base_model, qlora=False)
        if settings.method_config.get("training", {}).get("gradient_checkpointing"):
            model.gradient_checkpointing_enable()
    else:
        raise ValueError(f"Unknown method: {method}. Use lora, qlora, or full.")

    stats = count_trainable_parameters(model)
    trainer = build_trainer(settings, model, tokenizer, train_ds)
    trainer.train()

    save_dir = settings.output_dir / "final"
    save_dir.mkdir(parents=True, exist_ok=True)
    model.save_pretrained(save_dir)
    tokenizer.save_pretrained(save_dir)

    report = {
        "method": method,
        "base_model": settings.base_model,
        "output_dir": str(save_dir),
        "trainable_parameters": stats,
        "description": settings.method_config.get("description", ""),
    }
    (settings.output_dir / "training_report.json").write_text(
        json.dumps(report, indent=2), encoding="utf-8"
    )
    return report
