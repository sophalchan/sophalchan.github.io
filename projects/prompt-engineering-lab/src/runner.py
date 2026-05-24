from __future__ import annotations

from dataclasses import dataclass

from .evaluator import evaluate_medical_summary, evaluate_security_triage
from .mock_llm import MOCK_HANDLERS
from .schema import EvaluationScore
from .template_engine import PromptTemplateEngine


@dataclass
class RunResult:
    prompt_id: str
    technique: str
    system: str
    user: str
    raw_output: str
    evaluation: EvaluationScore


class PromptRunner:
    def __init__(self, engine: PromptTemplateEngine | None = None) -> None:
        self.engine = engine or PromptTemplateEngine()

    def run(self, prompt_id: str, variables: dict, use_mock: bool = True) -> RunResult:
        bundle = self.engine.render_prompt(prompt_id, variables)

        if use_mock:
            handler = MOCK_HANDLERS.get(prompt_id)
            if not handler:
                raise KeyError(f"No mock handler registered for {prompt_id}")
            raw = handler(bundle)
        else:
            raise NotImplementedError(
                "Live LLM integration: set use_mock=False and wire OpenAI/Ollama client"
            )

        evaluation = self._evaluate(prompt_id, raw)
        return RunResult(
            prompt_id=prompt_id,
            technique=bundle["technique"],
            system=bundle["system"],
            user=bundle["user"],
            raw_output=raw,
            evaluation=evaluation,
        )

    def compare(self, prompt_ids: list[str], variables: dict) -> list[RunResult]:
        return [self.run(pid, variables) for pid in prompt_ids]

    @staticmethod
    def _evaluate(prompt_id: str, raw: str) -> EvaluationScore:
        if prompt_id.startswith("security"):
            return evaluate_security_triage(prompt_id, raw)
        if prompt_id.startswith("medical"):
            return evaluate_medical_summary(prompt_id, raw)
        return EvaluationScore(prompt_id=prompt_id, passed=True, score=1.0, details={})
