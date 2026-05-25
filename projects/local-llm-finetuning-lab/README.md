# Local LLM Fine-Tuning Lab

Step-by-step **local fine-tuning framework** comparing three methods used in production AI engineering:

| Method | Config | Best for |
|--------|--------|----------|
| **LoRA** | `configs/lora.yaml` | Low VRAM, fast iteration, frozen base model |
| **QLoRA** | `configs/qlora.yaml` | Large models on consumer GPUs (4-bit + adapters) |
| **Full fine-tuning** | `configs/full_finetune.yaml` | Small base models, maximum adaptation |

Default base model: **`distilgpt2`** (runs on CPU for demos). Swap to `TinyLlama/TinyLlama-1.1B-Chat-v1.0` or `microsoft/phi-2` when you have more GPU memory.

## Framework layout

```
local-llm-finetuning-lab/
├── configs/                 # YAML per method (hyperparameters)
├── data/                    # Instruction JSONL dataset
├── scripts/
│   ├── train.py             # Train one method: lora | qlora | full
│   ├── compare_methods.py   # Compare trainable parameter counts
│   └── inference_cli.py     # Test generation after training
└── src/
    ├── config.py            # Settings + YAML loader
    ├── data_loader.py       # Instruction → text formatting
    ├── model_utils.py       # LoRA / QLoRA model builders
    ├── trainer.py           # Hugging Face Trainer pipeline
    └── inference.py         # Load adapter and generate
```

## Quick start

```bash
cd projects/local-llm-finetuning-lab
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env

# Step 1 — Compare methods (no training yet)
python scripts/compare_methods.py

# Step 2 — Train with LoRA (works on CPU, slow but runnable)
python scripts/train.py lora

# Step 3 — Train with QLoRA (requires NVIDIA CUDA GPU)
python scripts/train.py qlora

# Step 4 — Full fine-tuning (small models only)
python scripts/train.py full

# Step 5 — Inference
python scripts/inference_cli.py "What are three benefits of LoRA?" --method lora
```

## Outputs

Each run saves to `outputs/<method>/`:

- `final/` — model + tokenizer (LoRA adapters or full weights)
- `training_report.json` — trainable parameter stats

## Scale to medical / production models

1. Replace `data/sample_instructions.jsonl` with de-identified instruction data.  
2. Set `BASE_MODEL` to your approved on-prem model in `.env`.  
3. Tune `configs/*.yaml` learning rates and `target_modules` for the architecture.  
4. Run **QLoRA** on GPU servers for 7B+ models; use **LoRA** for adapter sweeps.  

## Author

**Sophal Chan** — AI Engineering portfolio
