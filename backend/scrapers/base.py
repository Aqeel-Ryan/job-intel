"""Abstract base class shared by every scraper.

Subclasses implement ``scrape``; ``fetch`` provides a shared HTTP GET that
reads timeout, user-agent, and retry settings from config so no scraper
hardcodes them.
"""

from abc import ABC, abstractmethod
from types import ModuleType


class BaseScraper(ABC):
    """Common scraper behaviour: config access and retrying HTTP fetch."""

    def __init__(self, config: ModuleType) -> None:
        """Store a reference to the config module for all subclasses.

        Args:
            config: The imported ``config`` module (single source of truth).
        """
        self.config = config

    async def fetch(self, url: str) -> str:
        """HTTP GET a URL with retry + backoff, returning the response body.

        Reads ``REQUEST_TIMEOUT_S``, ``USER_AGENT``, ``REQUEST_MAX_RETRIES``,
        and ``REQUEST_BACKOFF_S`` from config. Retries on transient failures
        up to the configured maximum before raising.

        Args:
            url: Absolute URL to fetch.

        Returns:
            The response body as text.
        """
        # TODO: use the shared httpx client (backend.utils.http) with config-driven
        # timeout, user-agent header, retry count, and exponential backoff.
        raise NotImplementedError

    @abstractmethod
    async def scrape(self, company_name: str) -> dict:
        """Scrape this source for a company and return a raw signals dict.

        Args:
            company_name: The company to scrape data for.

        Returns:
            A source-specific dict of raw signals for downstream modules.
        """
        ...
