"""Scraper for the Crunchbase API — revenue, funding, and headcount."""

from types import ModuleType

from backend.scrapers.base import BaseScraper


class CrunchbaseScraper(BaseScraper):
    """Calls the Crunchbase API for firmographic data.

    Uses ``CRUNCHBASE_BASE_URL`` and ``CRUNCHBASE_API_KEY`` from config.
    """

    def __init__(self, config: ModuleType) -> None:
        """Store config reference (see :class:`BaseScraper`)."""
        super().__init__(config)

    async def fetch_org(self, company_name: str) -> dict | None:
        """Fetch the Crunchbase organization record for a company.

        Args:
            company_name: Company to look up.

        Returns:
            The raw organization record, or ``None`` if not found.
        """
        # TODO: call the Crunchbase organizations endpoint with the API key.
        raise NotImplementedError

    async def scrape(self, company_name: str) -> dict:
        """Return normalized firmographic signals.

        Args:
            company_name: Company to scrape.

        Returns:
            ``{"employee_count": int | None, "funding_stage": str | None,
            "revenue_range": str | None}``.
        """
        # TODO: fetch_org then normalize into the signals dict above.
        raise NotImplementedError
