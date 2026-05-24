from __future__ import annotations

import json
import re
from typing import Any

from .schema import EvaluationScore, MedicalSummaryResult, SecurityTriageResult


def _extract_json_block(text: str) -> dict[str, Any]:
    match = re.search(r"\{.*\}", text, flags=re.DOTALL)
    if not match:
        raise ValueError("No JSON object found in model output")
    return json.loads(match.group(0))


def evaluate_security_triage(prompt_id: str, raw_output: str) -> EvaluationScore:
    details: dict[str, Any] = {}
    try:
        payload = _extract_json_block(raw_output)
        parsed = SecurityTriageResult.model_validate(payload)
        details["parsed"] = parsed.model_dump()

        checks = {
            "valid_json": True,
            "severity_present": parsed.severity in {"low", "medium", "high", "critical"},
            "summary_length_ok": len(parsed.summary.split()) <= 45,
            "has_actions": len(parsed.recommended_actions) >= 1,
            "critical_escalation": not parsed.needs_escalation or parsed.severity in {"high", "critical"},
        }
        score = sum(checks.values()) / len(checks)
        return EvaluationScore(
            prompt_id=prompt_id,
            passed=score >= 0.8,
            score=round(score, 3),
            details={"checks": checks, **details},
        )
    except Exception as exc:  # noqa: BLE001
        return EvaluationScore(
            prompt_id=prompt_id,
            passed=False,
            score=0.0,
            details={"error": str(exc), **details},
        )


def evaluate_medical_summary(prompt_id: str, raw_output: str) -> EvaluationScore:
    details: dict[str, Any] = {}
    try:
        payload = _extract_json_block(raw_output)
        parsed = MedicalSummaryResult.model_validate(payload)
        details["parsed"] = parsed.model_dump()

        checks = {
            "valid_json": True,
            "has_findings": len(parsed.key_findings) >= 1,
            "has_disclaimer": "not clinical advice" in parsed.disclaimer.lower(),
            "no_diagnosis_language": not re.search(r"\bdiagnos", raw_output, re.I),
        }
        score = sum(checks.values()) / len(checks)
        return EvaluationScore(
            prompt_id=prompt_id,
            passed=score >= 0.75,
            score=round(score, 3),
            details={"checks": checks, **details},
        )
    except Exception as exc:  # noqa: BLE001
        return EvaluationScore(
            prompt_id=prompt_id,
            passed=False,
            score=0.0,
            details={"error": str(exc), **details},
        )
