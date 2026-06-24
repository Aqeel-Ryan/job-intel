"""Shared httpx client with retry and rate limiting.

Reads ``REQUEST_TIMEOUT_S``, ``USER_AGENT``, ``REQUEST_MAX_RETRIES``, and
``REQUEST_BACKOFF_S`` from config — scrapers must not configure their own.
"""

from types import ModuleType

import httpx


def build_client(config: ModuleType) -> httpx.AsyncClient:
    """Construct a shared async httpx client from config settings.

    Args:
        config: The config module (provides ``REQUEST_TIMEOUT_S``,
            ``USER_AGENT``).

    Returns:
        A configured :class:`httpx.AsyncClient` with the timeout and
        user-agent header from config.
    """
    # TODO: httpx.AsyncClient(timeout=config.REQUEST_TIMEOUT_S,
    #   headers={"User-Agent": config.USER_AGENT}).
    raise NotImplementedError


async def get_with_retry(
    client: httpx.AsyncClient, url: str, config: ModuleType
) -> httpx.Response:
    """GET a URL, retrying with exponential backoff on transient failures.

    Args:
        client: The shared httpx client from :func:`build_client`.
        url: Absolute URL to fetch.
        config: The config module (provides ``REQUEST_MAX_RETRIES``,
            ``REQUEST_BACKOFF_S``).

    Returns:
        The successful :class:`httpx.Response`.

    Raises:
        httpx.HTTPError: If all retries are exhausted.
    """
    # TODO: loop up to REQUEST_MAX_RETRIES, sleeping REQUEST_BACKOFF_S * 2**attempt
    # between transient failures (timeouts, 429, 5xx); raise on exhaustion.
    raise NotImplementedError
