"""Scraper for a company careers page — extracts ATS URL fingerprints."""

from types import ModuleType

from backend.scrapers.base import BaseScraper


class CareersPageScraper(BaseScraper):
    """Locates a company's careers page and harvests outbound job-posting URLs.

    The harvested URLs are matched against ``ATS_URL_FINGERPRINTS`` downstream
    to identify the ATS vendor.
    """

    def __init__(self, config: ModuleType) -> None:
        """Store config reference (see :class:`BaseScraper`)."""
        super().__init__(config)

    async def find_careers_url(self, company_name: str) -> str | None:
        """Search for the company's careers/jobs page URL.

        Args:
            company_name: Company to find a careers page for.

        Returns:
            The careers page URL, or ``None`` if it could not be located.
        """
        # TODO: search engine / homepage crawl to locate the careers page.
        raise NotImplementedError

    async def extract_ats_signals(self, careers_url: str) -> list[str]:
        """Return all outbound job-posting URLs found on the careers page.

        Args:
            careers_url: The careers page to parse.

        Returns:
            A list of outbound apply/job URLs (raw ATS signals).
        """
        # TODO: fetch the page and extract anchor hrefs pointing at job postings.
        raise NotImplementedError

    async def scrape(self, company_name: str) -> dict:
        """Orchestrate careers-page discovery and signal extraction.

        Args:
            company_name: Company to scrape.

        Returns:
            ``{"careers_url": str | None, "ats_signals": list[str]}``.
        """
        # TODO: call find_careers_url then extract_ats_signals.
        raise NotImplementedError
