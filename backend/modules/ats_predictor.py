"""ATS vendor classification.

Matches observed job-posting URLs against the fingerprint table in config, and
falls back to size-based tier inference. No vendor names are hardcoded here —
they are all read from ``ATS_URL_FINGERPRINTS`` and ``ATS_TIER_MAP``.
"""

from types import ModuleType

from backend.models.company import ATSPrediction


class ATSPredictor:
    """Predicts a company's ATS vendor and tier from public signals."""

    def __init__(self, config: ModuleType) -> None:
        """Load the fingerprint and tier tables from config.

        Args:
            config: The config module (provides ``ATS_URL_FINGERPRINTS``,
                ``ATS_TIER_MAP``, ``COMPANY_SIZE_TIER_MAP``,
                ``ENTERPRISE_TIER_THRESHOLD``).
        """
        self.config = config
        self.fingerprints = config.ATS_URL_FINGERPRINTS
        self.tier_map = config.ATS_TIER_MAP

    def predict_from_urls(self, urls: list[str]) -> ATSPrediction | None:
        """Match URLs against the fingerprint table to identify the vendor.

        Iterates ``ATS_URL_FINGERPRINTS`` (never hardcoding vendor names) and
        returns the highest-confidence match.

        Args:
            urls: Outbound job-posting URLs harvested from a careers page.

        Returns:
            An :class:`ATSPrediction` with ``detection_method='url_fingerprint'``,
            or ``None`` if no fingerprint matched.
        """
        # TODO: for each vendor in self.fingerprints, test its patterns against urls;
        # set tier from self.tier_map and confidence from match strength.
        raise NotImplementedError

    def predict_from_company_size(self, employee_count: int) -> ATSPrediction:
        """Infer a likely ATS tier from company headcount.

        Uses ``COMPANY_SIZE_TIER_MAP`` and ``ENTERPRISE_TIER_THRESHOLD``.

        Args:
            employee_count: Approximate employee headcount.

        Returns:
            An :class:`ATSPrediction` with ``detection_method='size_inference'``.
        """
        # TODO: bucket employee_count via COMPANY_SIZE_TIER_MAP /
        # ENTERPRISE_TIER_THRESHOLD into a tier and a low-confidence prediction.
        raise NotImplementedError

    def predict(
        self, careers_signals: dict, linkedin_signals: dict
    ) -> ATSPrediction:
        """Run both prediction methods and return the highest-confidence one.

        Args:
            careers_signals: Output of ``CareersPageScraper.scrape``.
            linkedin_signals: Output of ``LinkedInScraper.scrape``.

        Returns:
            The best available :class:`ATSPrediction`.
        """
        # TODO: try predict_from_urls first; fall back to predict_from_company_size.
        raise NotImplementedError
