"""Pydantic models describing interview intelligence for a company."""

from datetime import datetime
from typing import Literal

from pydantic import BaseModel, Field

QuestionCategory = Literal["behavioral", "technical", "situational", "culture"]
QuestionSource = Literal["glassdoor", "reddit", "blind"]
RoundFormat = Literal["phone", "video", "take_home", "onsite", "panel"]


class Question(BaseModel):
    """A single interview question surfaced from a public source."""

    text: str = Field(..., description="The question text as reported.")
    category: QuestionCategory = Field(
        ..., description="Question category."
    )
    source: QuestionSource = Field(
        ..., description="Where the question was sourced from."
    )


class Round(BaseModel):
    """A single round in a company's interview process."""

    name: str = Field(..., description="Round name, e.g. 'Recruiter Screen'.")
    format: RoundFormat = Field(..., description="Interview format for this round.")
    duration_minutes: int | None = Field(
        None, description="Typical duration of the round in minutes."
    )
    questions: list[Question] = Field(
        default_factory=list, description="Questions reported for this round."
    )


class InterviewReport(BaseModel):
    """Aggregated interview intelligence for a company."""

    company_slug: str = Field(..., description="Slug of the company this report covers.")
    total_rounds: int = Field(..., ge=0, description="Number of interview rounds.")
    difficulty_rating: float = Field(
        ..., ge=1.0, le=5.0, description="Difficulty rating (1.0–5.0)."
    )
    offer_rate: float = Field(
        ..., ge=0.0, le=1.0, description="Reported offer rate (0.0–1.0)."
    )
    avg_process_days: int | None = Field(
        None, description="Average days from first contact to decision."
    )
    rounds: list[Round] = Field(
        default_factory=list, description="The interview rounds in order."
    )
    raw_source_count: int = Field(
        0, description="Number of raw source posts/pages aggregated."
    )
    fetched_at: datetime = Field(..., description="When this report was assembled.")
