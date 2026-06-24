"""Scraper for LinkedIn — company headcount, industry, and recent postings."""

from types import ModuleType

from backend.scrapers.base import BaseScraper


class LinkedInScraper(BaseScraper):
    """Pulls company metadata and recent job postings from LinkedIn.

    Uses the RapidAPI proxy key from config when direct access is blocked.
    """

    def __init__(self, config: ModuleType) -> None:
        """Store config reference (see :class:`BaseScraper`)."""
        super().__init__(config)

    async def fetch_company_page(self, company_name: str) -> dict:
        """Fetch the company page for employee count and industry.

        Args:
            company_name: Company to look up.

        Returns:
            ``{"employee_count": int | None, "industry": str | None}``.
        """
        # TODO: resolve the company's LinkedIn page and parse headcount + industry.
        raise NotImplementedError

    async def fetch_job_postings(self, company_name: str, limit: int) -> list[dict]:
        """Fetch the most recent job postings with their apply URLs.

        Args:
            company_name: Company to fetch postings for.
            limit: Maximum number of postings to return.

        Returns:
            A list of posting dicts (title, posted date, apply URL, ...).
        """
        # TODO: query recent postings, capping at ``limit``.
        raise NotImplementedError

    async def scrape(self, company_name: str) -> dict:
        """Orchestrate company-page and postings retrieval.

        Args:
            company_name: Company to scrape.

        Returns:
            Combined company metadata and recent postings.
        """
        # TODO: combine fetch_company_page and fetch_job_postings.
        raise NotImplementedError
