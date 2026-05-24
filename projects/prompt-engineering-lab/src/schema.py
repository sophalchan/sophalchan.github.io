from __future__ import annotations

from enum import Enum
from typing import Any

from pydantic import BaseModel, Field


class Severity(str, Enum):
    low = "low"
    medium = "medium"
    high = "high"
    critical = "critical"


class SecurityTriageResult(BaseModel):
    incident_id: str
    severity: Severity
    summary: str = Field(..., max_length=280)
    recommended_actions: list[str] = Field(..., min_length=1, max_length=5)
    needs_escalation: bool


class MedicalSummaryResult(BaseModel):
    patient_context: str
    key_findings: list[str] = Field(..., min_length=1, max_length=6)
    follow_up_questions: list[str] = Field(default_factory=list, max_length=4)
    disclaimer: str = "Not clinical advice — for engineering demo only."


class EvaluationScore(BaseModel):
    prompt_id: str
    passed: bool
    score: float
    details: dict[str, Any]
