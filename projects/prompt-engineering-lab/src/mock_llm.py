from __future__ import annotations

import json
from typing import Callable

from .schema import EvaluationScore


def mock_security_triage(prompt_bundle: dict[str, str]) -> str:
    """Deterministic mock LLM for offline demos and unit tests."""
    user = prompt_bundle["user"].lower()
    severity = "critical" if "ransomware" in user or "exfiltration" in user else "medium"
    payload = {
        "incident_id": "INC-2026-0042",
        "severity": severity,
        "summary": "Suspicious activity detected in SIEM alerts requiring analyst review.",
        "recommended_actions": [
            "Isolate affected host from network",
            "Preserve logs for 72 hours",
            "Notify IR lead within 30 minutes",
        ],
        "needs_escalation": severity in {"high", "critical"},
    }
    return json.dumps(payload, indent=2)


def mock_medical_summary(prompt_bundle: dict[str, str]) -> str:
    payload = {
        "patient_context": "De-identified engineering demo note",
        "key_findings": [
            "Structured prompt returned JSON successfully",
            "Findings limited to provided context",
        ],
        "follow_up_questions": [
            "Which imaging modality was referenced?",
            "Was prior authorization documented?",
        ],
        "disclaimer": "Not clinical advice — for engineering demo only.",
    }
    return json.dumps(payload, indent=2)


MOCK_HANDLERS: dict[str, Callable[[dict[str, str]], str]] = {
    "security_triage_v1": mock_security_triage,
    "security_triage_cot_v2": mock_security_triage,
    "medical_summary_structured": mock_medical_summary,
}
