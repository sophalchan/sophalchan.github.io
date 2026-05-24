from __future__ import annotations

from pathlib import Path
from typing import Any

import yaml
from jinja2 import Environment, StrictUndefined


class PromptTemplateEngine:
    def __init__(self, prompts_dir: Path | None = None) -> None:
        root = Path(__file__).resolve().parents[1]
        self.prompts_dir = prompts_dir or (root / "prompts")
        self.env = Environment(undefined=StrictUndefined, trim_blocks=True, lstrip_blocks=True)

    def load_yaml(self, filename: str) -> dict[str, Any]:
        path = self.prompts_dir / filename
        return yaml.safe_load(path.read_text(encoding="utf-8"))

    def render(self, template_str: str, variables: dict[str, Any]) -> str:
        template = self.env.from_string(template_str)
        return template.render(**variables).strip()

    def render_prompt(self, prompt_id: str, variables: dict[str, Any]) -> dict[str, str]:
        catalog = self.load_yaml("templates.yaml")
        if prompt_id not in catalog["prompts"]:
            raise KeyError(f"Unknown prompt_id: {prompt_id}")

        spec = catalog["prompts"][prompt_id]
        system = self.render(spec.get("system", ""), variables) if spec.get("system") else ""
        user = self.render(spec["user"], variables)

        if spec.get("few_shot_file"):
            shots = self.load_yaml(spec["few_shot_file"]).get("examples", [])
            shot_block = self._format_few_shot(shots)
            user = f"{shot_block}\n\n---\n\n{user}"

        return {"system": system, "user": user, "technique": spec.get("technique", "basic")}

    @staticmethod
    def _format_few_shot(examples: list[dict[str, str]]) -> str:
        lines = ["Few-shot examples:"]
        for i, ex in enumerate(examples, start=1):
            lines.append(f"\nExample {i} input:\n{ex['input']}")
            lines.append(f"Example {i} output:\n{ex['output']}")
        return "\n".join(lines)
