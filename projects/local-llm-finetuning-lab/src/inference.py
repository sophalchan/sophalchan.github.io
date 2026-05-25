from __future__ import annotations

from pathlib import Path

import torch
from peft import PeftModel
from transformers import AutoModelForCausalLM, AutoTokenizer


def generate(
    base_model: str,
    adapter_path: str | None,
    prompt: str,
    max_new_tokens: int = 120,
) -> str:
    adapter_path_obj = Path(adapter_path) if adapter_path else None
    tokenizer_source = (
        str(adapter_path_obj) if adapter_path_obj and adapter_path_obj.exists() else base_model
    )
    tokenizer = AutoTokenizer.from_pretrained(tokenizer_source)
    if tokenizer.pad_token is None:
        tokenizer.pad_token = tokenizer.eos_token

    if adapter_path_obj and adapter_path_obj.exists():
        base = AutoModelForCausalLM.from_pretrained(base_model)
        model = PeftModel.from_pretrained(base, str(adapter_path_obj))
    else:
        model = AutoModelForCausalLM.from_pretrained(base_model)

    model.eval()
    device = "cuda" if torch.cuda.is_available() else "cpu"
    model.to(device)

    inputs = tokenizer(prompt, return_tensors="pt").to(device)
    with torch.no_grad():
        out = model.generate(
            **inputs,
            max_new_tokens=max_new_tokens,
            do_sample=True,
            temperature=0.7,
            top_p=0.9,
            pad_token_id=tokenizer.eos_token_id,
        )
    return tokenizer.decode(out[0], skip_special_tokens=True)
