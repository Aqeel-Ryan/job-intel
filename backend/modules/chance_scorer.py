"""Weighted 0–100 chance-scoring model.

Reads ``SCORE_WEIGHTS`` and all sub-maps from config. Validates that the
weights sum to 1.0 on init and raises ``ValueError`` otherwise.
"""

from types import ModuleType

from backend.models.company import (
    ATSPrediction,
    ChanceScore,
    CompanyProfile,
    SignalScore,
)
from backend.models.interview import InterviewReport

# Floating-point tolerance for the weights-sum-to-1.0 invariant.
_WEIGHT_SUM_TOLERANCE = 1e-9


class ChanceScorer:
    """Computes a weighted chance score from independent signal scorers."""

    def __init__(self, config: ModuleType) -> None:
        """Load weights and sub-maps from config; validate the weights.

        Args:
            config: The config module (provides ``SCORE_WEIGHTS``,
                ``FUNDING_STAGE_SCORES``, ``POSTING_RECENCY_SCORE_MAP``,
                ``POSTING_STALE_SCORE``, ``SCORE_CATEGORY_THRESHOLDS``).

        Raises:
            ValueError: If ``SCORE_WEIGHTS`` does not sum to 1.0.
        """
        self.config = config
        self.weights = config.SCORE_WEIGHTS
        total = sum(self.weights.values())
        if abs(total - 1.0) > _WEIGHT_SUM_TOLERANCE:
            raise ValueError(
                f"SCORE_WEIGHTS must sum to 1.0, got {total}"
            )

    def score_role_match(
        self, job_description: str, resume_text: str
    ) -> SignalScore:
        """Score how well the resume matches the job description.

        Args:
            job_description: The target role's job description text.
            resume_text: The applicant's resume text.

        Returns:
            A :class:`SignalScore` for the ``role_match`` signal.
        """
        # TODO: compute semantic / keyword overlap; weight via SCORE_WEIGHTS.
        raise NotImplementedError

    def score_ats_parse_risk(self, ats_prediction: ATSPrediction) -> SignalScore:
        """Score the risk that the ATS mis-parses the resume.

        Args:
            ats_prediction: The predicted ATS for the company.

        Returns:
            A :class:`SignalScore` for the ``ats_parse_risk`` signal.
        """
        # TODO: map ATS tier to a parse-risk raw score; weight via SCORE_WEIGHTS.
        raise NotImplementedError

    def score_offer_rate(self, interview_report: InterviewReport) -> SignalScore:
        """Score based on the company's reported offer rate.

        Args:
            interview_report: Aggregated interview intelligence.

        Returns:
            A :class:`SignalScore` for the ``glassdoor_offer_rate`` signal.
        """
        # TODO: use interview_report.offer_rate; weight via SCORE_WEIGHTS.
        raise NotImplementedError

    def score_interview_difficulty(
        self, interview_report: InterviewReport
    ) -> SignalScore:
        """Score based on interview difficulty (easier → higher chance).

        Args:
            interview_report: Aggregated interview intelligence.

        Returns:
            A :class:`SignalScore` for the ``interview_difficulty`` signal.
        """
        # TODO: invert difficulty_rating (1–5) into a 0–1 score; weight it.
        raise NotImplementedError

    def score_company_size_fit(self, employee_count: int) -> SignalScore:
        """Score how favourable the company size is for the applicant.

        Args:
            employee_count: Approximate employee headcount.

        Returns:
            A :class:`SignalScore` for the ``company_size_fit`` signal.
        """
        # TODO: map headcount to a fit raw score; weight via SCORE_WEIGHTS.
        raise NotImplementedError

    def score_funding_stage(self, funding_stage: str) -> SignalScore:
        """Score based on the company's funding stage.

        Args:
            funding_stage: A key into ``FUNDING_STAGE_SCORES``.

        Returns:
            A :class:`SignalScore` for the ``funding_stage`` signal.
        """
        # TODO: look up FUNDING_STAGE_SCORES (default to 'unknown'); weight it.
        raise NotImplementedError

    def score_posting_recency(self, days_since_posted: int) -> SignalScore:
        """Score based on how recently the role was posted.

        Args:
            days_since_posted: Days since the posting went live.

        Returns:
            A :class:`SignalScore` for the ``posting_recency`` signal.
        """
        # TODO: bucket days_since_posted via POSTING_RECENCY_SCORE_MAP, falling
        # back to POSTING_STALE_SCORE; weight via SCORE_WEIGHTS.
        raise NotImplementedError

    def score_monoculture_risk(self, ats_prediction: ATSPrediction) -> SignalScore:
        """Score exposure to ATS-monoculture risk (see README).

        Args:
            ats_prediction: The predicted ATS for the company.

        Returns:
            A :class:`SignalScore` for the ``monoculture_risk`` signal.
        """
        # TODO: derive monoculture exposure from ATS tier; weight via SCORE_WEIGHTS.
        raise NotImplementedError

    def calculate(
        self,
        profile: CompanyProfile,
        interview_report: InterviewReport,
        job_description: str,
        resume_text: str,
    ) -> ChanceScore:
        """Run every signal scorer, apply weights, and assemble the score.

        Args:
            profile: The :class:`CompanyProfile` being scored.
            interview_report: Aggregated interview intelligence.
            job_description: The target role's job description text.
            resume_text: The applicant's resume text.

        Returns:
            A :class:`ChanceScore` with ``overall`` (0–100), the per-signal
            ``breakdown``, and a ``category`` derived from
            ``SCORE_CATEGORY_THRESHOLDS``.
        """
        # TODO: call each score_* method, sum weighted_contribution * 100, and
        # derive category from config.SCORE_CATEGORY_THRESHOLDS.
        raise NotImplementedError
