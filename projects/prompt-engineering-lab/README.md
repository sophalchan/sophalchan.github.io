# Prompt Engineering Lab

Structured **prompt engineering** toolkit for AI engineering workflows: Jinja2 templates, few-shot examples, chain-of-thought instructions, **Pydantic schema validation**, and **A/B prompt comparison** with automated scoring.

## Features

- YAML prompt catalog with reusable variables
- Techniques: zero-shot JSON, few-shot, chain-of-thought
- Mock LLM for offline demos (no API key required)
- Evaluators for cybersecurity triage and medical summary JSON outputs
- Rich CLI for single runs and A/B comparisons

## Quick Start

```bash
cd projects/prompt-engineering-lab
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

python cli.py run security_triage_v1
python cli.py compare security_triage_v1 security_triage_cot_v2
python examples/run_security_triage.py
python examples/run_medical_summary.py
```

## Project Structure

```
prompt-engineering-lab/
├── cli.py
├── prompts/
│   ├── templates.yaml
│   └── few_shot_cyber_analyst.yaml
├── examples/
│   ├── run_security_triage.py
│   └── run_medical_summary.py
└── src/
    ├── template_engine.py    # Jinja2 rendering
    ├── schema.py             # Pydantic output schemas
    ├── evaluator.py          # JSON + rule scoring
    ├── mock_llm.py           # Offline demo responses
    └── runner.py             # Orchestration + A/B compare
```

## Prompt Catalog

| ID | Technique | Use case |
|----|-----------|----------|
| `security_triage_v1` | Zero-shot JSON | SOC alert triage |
| `security_triage_cot_v2` | Chain-of-thought + few-shot | Higher-quality triage |
| `medical_summary_structured` | Structured output | De-identified note summary |

## Author

**Sophal Chan** — AI Engineering & Cybersecurity portfolio
