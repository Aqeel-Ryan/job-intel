"""Scraper for the Glassdoor interview section."""

from types import ModuleType

from backend.scrapers.base import BaseScraper


class GlassdoorScraper(BaseScraper):
    """Extracts difficulty, offer rate, and interview questions from Glassdoor.

    Uses ``GLASSDOOR_BASE_URL`` from config for all requests.
    """

    def __init__(self, config: ModuleType) -> None:
        """Store config reference (see :class:`BaseScraper`)."""
        super().__init__(config)

    async def find_company_id(self, company_name: str) -> str | None:
        """Resolve a company name to its Glassdoor company id.

        Args:
            company_name: Company to resolve.

        Returns:
            The Glassdoor company id, or ``None`` if not found.
        """
        # TODO: query Glassdoor search and parse the resolved company id.
        raise NotImplementedError

    async def fetch_interview_page(self, company_id: str) -> str:
        """Fetch the raw HTML of a company's interview page.

        Args:
            company_id: Glassdoor company id.

        Returns:
            Raw HTML of the interview section.
        """
        # TODO: build the interview-page URL from config base and fetch it.
        raise NotImplementedError

    async def parse_interview_data(self, html: str) -> dict:
        """Parse difficulty, offer rate, and question texts from raw HTML.

        Args:
            html: Raw interview-page HTML.

        Returns:
            ``{"difficulty": float, "offer_rate": float, "questions": list[str]}``.
        """
        # TODO: parse the structured interview metrics out of the HTML.
        raise NotImplementedError

    async def scrape(self, company_name: str) -> dict:
        """Orchestrate Glassdoor interview-data retrieval.

        Args:
            company_name: Company to scrape.

        Returns:
            Parsed interview metrics and raw question texts.
        """
        # TODO: resolve id, fetch page, parse data.
        raise NotImplementedError
