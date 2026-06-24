"""Interview intelligence — aggregate scraped text and LLM-extract structure."""

from types import ModuleType

from backend.llm.client import LLMClient
from backend.models.interview import InterviewReport


class InterviewIntel:
    """Merges scraped interview text and extracts a structured report via LLM."""

    def __init__(self, config: ModuleType, llm_client: LLMClient) -> None:
        """Store config and the LLM client.

        Args:
            config: The config module.
            llm_client: Wrapper around the Anthropic SDK.
        """
        self.config = config
        self.llm_client = llm_client

    async def aggregate(self, glassdoor_data: dict, reddit_data: dict) -> str:
        """Merge raw scraped text from all interview sources into one blob.

        Args:
            glassdoor_data: Output of ``GlassdoorScraper.scrape``.
            reddit_data: Output of ``RedditScraper.scrape``.

        Returns:
            A single concatenated text blob for LLM extraction.
        """
        # TODO: concatenate and lightly clean the source texts.
        raise NotImplementedError

    async def extract(self, raw_text: str, company_name: str) -> InterviewReport:
        """Send aggregated text to the LLM and parse a structured report.

        Loads the ``extract_interview`` prompt and uses the LLM client's
        JSON completion to populate an :class:`InterviewReport`.

        Args:
            raw_text: Aggregated interview text from :meth:`aggregate`.
            company_name: Company the report is for (used in the prompt).

        Returns:
            A populated :class:`InterviewReport`.
        """
        # TODO: render the prompt, call llm_client.complete_json, validate into model.
        raise NotImplementedError

    async def get_report(
        self, company_name: str, glassdoor_data: dict, reddit_data: dict
    ) -> InterviewReport:
        """Aggregate then extract — the public entry point.

        Args:
            company_name: Company the report is for.
            glassdoor_data: Output of ``GlassdoorScraper.scrape``.
            reddit_data: Output of ``RedditScraper.scrape``.

        Returns:
            A populated :class:`InterviewReport`.
        """
        # TODO: aggregate(...) then extract(...).
        raise NotImplementedError
