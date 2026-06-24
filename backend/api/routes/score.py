"""Routes for the chance-score breakdown."""

from fastapi import APIRouter, Depends
from pydantic import BaseModel, Field

from backend.api.dependencies import get_cache_store
from backend.cache.store import CacheStore
from backend.models.company import ChanceScore

router = APIRouter(prefix="/score", tags=["score"])


class RecalculateRequest(BaseModel):
    """Body for a score recalculation request."""

    job_description: str = Field(..., description="The target role's job description.")
    resume_text: str = Field(..., description="The applicant's resume text.")


@router.get("/{company_slug}", response_model=ChanceScore)
async def get_score(
    company_slug: str,
    cache: CacheStore = Depends(get_cache_store),
) -> ChanceScore:
    """Return the cached chance score, or recalculate if absent.

    Args:
        company_slug: Slug of the company to score.
        cache: Injected cache store.

    Returns:
        The :class:`ChanceScore` for the company.
    """
    # TODO: read score from cache; recalculate via ChanceScorer on miss.
    raise NotImplementedError


@router.post("/{company_slug}/recalculate", response_model=ChanceScore)
async def recalculate_score(
    company_slug: str,
    body: RecalculateRequest,
    cache: CacheStore = Depends(get_cache_store),
) -> ChanceScore:
    """Recalculate the chance score against a supplied JD and resume.

    Args:
        company_slug: Slug of the company to score.
        body: The job description and resume text to score against.
        cache: Injected cache store.

    Returns:
        The recomputed :class:`ChanceScore`.
    """
    # TODO: load profile + interview report, run ChanceScorer.calculate, cache, return.
    raise NotImplementedError
