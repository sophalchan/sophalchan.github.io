from __future__ import annotations

import torch
from peft import LoraConfig, PeftModel, get_peft_model, prepare_model_for_kbit_training
from transformers import (
    AutoModelForCausalLM,
    AutoTokenizer,
    BitsAndBytesConfig,
)


def count_trainable_parameters(model) -> dict:
    trainable = sum(p.numel() for p in model.parameters() if p.requires_grad)
    total = sum(p.numel() for p in model.parameters())
    pct = 100 * trainable / total if total else 0
    return {
        "trainable": trainable,
        "total": total,
        "trainable_percent": round(pct, 4),
    }


def default_lora_targets(model) -> list[str]:
    """Pick common attention projection module names per architecture."""
    names = {n.split(".")[-1] for n, _ in model.named_modules()}
    candidates = [
        ["q_proj", "k_proj", "v_proj", "o_proj"],
        ["c_attn", "c_proj"],
        ["query", "key", "value", "dense"],
    ]
    for group in candidates:
        if all(t in names for t in group):
            return group
    # fallback: any module with proj/attn in name
    return [n for n in names if "proj" in n or "attn" in n][:4] or list(names)[:2]


def load_tokenizer(model_id: str):
    tokenizer = AutoTokenizer.from_pretrained(model_id)
    if tokenizer.pad_token is None:
        tokenizer.pad_token = tokenizer.eos_token
    return tokenizer


def load_base_model(model_id: str, qlora: bool = False):
    if qlora:
        if not torch.cuda.is_available():
            raise RuntimeError(
                "QLoRA requires a CUDA GPU. Use --method lora or full on CPU, "
                "or run on a machine with NVIDIA drivers installed."
            )
        bnb_config = BitsAndBytesConfig(
            load_in_4bit=True,
            bnb_4bit_quant_type="nf4",
            bnb_4bit_compute_dtype=torch.bfloat16,
            bnb_4bit_use_double_quant=True,
        )
        model = AutoModelForCausalLM.from_pretrained(
            model_id,
            quantization_config=bnb_config,
            device_map="auto",
        )
        model = prepare_model_for_kbit_training(model)
        return model

    model = AutoModelForCausalLM.from_pretrained(model_id)
    return model


def apply_lora(model, lora_cfg: dict) -> PeftModel:
    targets = lora_cfg.get("target_modules")
    if not targets or targets == ["auto"]:
        targets = default_lora_targets(model)

    config = LoraConfig(
        r=lora_cfg.get("r", 16),
        lora_alpha=lora_cfg.get("lora_alpha", 32),
        lora_dropout=lora_cfg.get("lora_dropout", 0.05),
        target_modules=targets,
        bias="none",
        task_type="CAUSAL_LM",
    )
    return get_peft_model(model, config)


def load_model_for_inference(base_model: str, adapter_path: str | None = None):
    tokenizer = load_tokenizer(base_model)
    if adapter_path:
        base = AutoModelForCausalLM.from_pretrained(base_model)
        model = PeftModel.from_pretrained(base, adapter_path)
    else:
        model = AutoModelForCausalLM.from_pretrained(adapter_path or base_model)
    model.eval()
    return model, tokenizer
