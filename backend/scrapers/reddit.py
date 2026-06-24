"""Scraper for Reddit — interview experience posts."""

from types import ModuleType

from backend.scrapers.base import BaseScraper


class RedditScraper(BaseScraper):
    """Searches relevant subreddits for interview-experience posts.

    Uses ``REDDIT_BASE_URL`` from config for all requests.
    """

    def __init__(self, config: ModuleType) -> None:
        """Store config reference (see :class:`BaseScraper`)."""
        super().__init__(config)

    async def search_interview_posts(self, company_name: str) -> list[dict]:
        """Search subreddits for posts about interviewing at the company.

        Args:
            company_name: Company to search for.

        Returns:
            A list of post dicts (title, body, subreddit, score, url, ...).
        """
        # TODO: query Reddit search across relevant subreddits.
        raise NotImplementedError

    async def scrape(self, company_name: str) -> dict:
        """Return raw Reddit interview-experience signals.

        Args:
            company_name: Company to scrape.

        Returns:
            ``{"posts": list[dict]}``.
        """
        # TODO: wrap search_interview_posts.
        raise NotImplementedError
