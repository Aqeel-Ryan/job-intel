"""Routes for fetching a full company profile."""

from fastapi import APIRouter, Depends

from backend.api.dependencies import get_cache_store, get_llm_client
from backend.cache.store import CacheStore
from backend.llm.client import LLMClient
from backend.models.company import CompanyProfile

router = APIRouter(prefix="/company", tags=["company"])


@router.get("/{company_name}", response_model=CompanyProfile)
async def get_company(
    company_name: str,
    cache: CacheStore = Depends(get_cache_store),
    llm: LLMClient = Depends(get_llm_client),
) -> CompanyProfile:
    """Return the full profile for a company, running the pipeline if needed.

    Triggers the full pipeline: scrape all sources, predict the ATS, calculate
    the chance score, extract interview intel, and cache the result. Returns a
    cached profile when one exists and is within TTL.

    Args:
        company_name: Company to profile.
        cache: Injected cache store.
        llm: Injected LLM client.

    Returns:
        The assembled :class:`CompanyProfile`.
    """
    # TODO: check cache; on miss run scrapers -> ATSPredictor -> InterviewIntel ->
    # ChanceScorer, build CompanyProfile, cache, and return.
    raise NotImplementedError


@router.get("/{company_name}/refresh", response_model=CompanyProfile)
async def refresh_company(
    company_name: str,
    cache: CacheStore = Depends(get_cache_store),
    llm: LLMClient = Depends(get_llm_client),
) -> CompanyProfile:
    """Re-run the full pipeline for a company, bypassing the cache.

    Args:
        company_name: Company to profile.
        cache: Injected cache store.
        llm: Injected LLM client.

    Returns:
        The freshly assembled :class:`CompanyProfile`.
    """
    # TODO: same as get_company but skip the cache read; write the fresh result.
    raise NotImplementedError
