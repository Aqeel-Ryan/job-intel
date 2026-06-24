"""Pydantic models describing a company, its predicted ATS, and chance score."""

from datetime import datetime
from typing import Literal

from pydantic import BaseModel, Field

DetectionMethod = Literal["url_fingerprint", "size_inference", "llm_extraction"]
ScoreCategory = Literal["Reach", "Match", "Safe"]


class ATSPrediction(BaseModel):
    """Prediction of which Applicant Tracking System a company uses."""

    vendor: str = Field(..., description="ATS vendor name, e.g. 'Greenhouse'.")
    confidence: float = Field(
        ..., ge=0.0, le=1.0, description="Confidence in the prediction (0.0–1.0)."
    )
    tier: Literal[1, 2, 3] = Field(
        ..., description="ATS tier: 1=enterprise, 2=mid-market, 3=SMB."
    )
    detection_method: DetectionMethod = Field(
        ..., description="How the vendor was detected."
    )
    raw_signals: list[str] = Field(
        default_factory=list,
        description="Raw signals (URLs, text snippets) the prediction was based on.",
    )


class SignalScore(BaseModel):
    """One signal's contribution to the overall chance score."""

    name: str = Field(..., description="Signal name, matching a SCORE_WEIGHTS key.")
    raw_score: float = Field(
        ..., ge=0.0, le=1.0, description="Raw signal score before weighting (0.0–1.0)."
    )
    weight: float = Field(..., description="Weight applied to this signal.")
    weighted_contribution: float = Field(
        ..., description="raw_score * weight — the signal's contribution to the total."
    )
    evidence: str = Field(
        ..., description="Human-readable explanation of why this score was assigned."
    )


class ChanceScore(BaseModel):
    """Overall 0–100 chance score with a per-signal breakdown."""

    overall: int = Field(..., ge=0, le=100, description="Overall chance score (0–100).")
    breakdown: list[SignalScore] = Field(
        default_factory=list, description="Per-signal scores that sum to the overall."
    )
    category: ScoreCategory = Field(
        ..., description="Derived bucket: Reach, Match, or Safe."
    )
    generated_at: datetime = Field(
        ..., description="When this score was computed."
    )


class CompanyProfile(BaseModel):
    """Full aggregated profile for a single company."""

    name: str = Field(..., description="Company display name.")
    slug: str = Field(..., description="URL-safe identifier derived from the name.")
    employee_count: int | None = Field(
        None, description="Approximate employee headcount."
    )
    revenue_range: str | None = Field(
        None, description="Revenue range, e.g. '$10M–$50M'."
    )
    funding_stage: str | None = Field(
        None, description="Funding stage, matching a FUNDING_STAGE_SCORES key."
    )
    industry: str | None = Field(None, description="Primary industry / sector.")
    hq_location: str | None = Field(None, description="Headquarters location.")
    careers_url: str | None = Field(None, description="Company careers page URL.")
    ats_prediction: ATSPrediction | None = Field(
        None, description="Predicted ATS vendor for this company."
    )
    chance_score: ChanceScore | None = Field(
        None, description="Computed chance score for the applicant."
    )
    fetched_at: datetime = Field(..., description="When this profile was assembled.")
