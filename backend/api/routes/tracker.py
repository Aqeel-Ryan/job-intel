"""CRUD routes for the application tracker (kanban stage management)."""

from datetime import date

from fastapi import APIRouter, Depends
from pydantic import BaseModel, Field

from backend.api.dependencies import get_cache_store
from backend.cache.store import CacheStore

router = APIRouter(prefix="/tracker", tags=["tracker"])


class TrackedApplication(BaseModel):
    """A single tracked job application."""

    id: int = Field(..., description="Unique record id.")
    company_slug: str = Field(..., description="Slug of the company applied to.")
    role_title: str = Field(..., description="Title of the role.")
    applied_date: date = Field(..., description="Date the application was submitted.")
    stage: str = Field(
        ..., description="Current kanban stage (e.g. 'Applied', 'Screening')."
    )


class CreateTrackedApplication(BaseModel):
    """Body for creating a tracked application."""

    company_slug: str = Field(..., description="Slug of the company applied to.")
    role_title: str = Field(..., description="Title of the role.")
    applied_date: date = Field(..., description="Date the application was submitted.")
    stage: str = Field(..., description="Initial kanban stage.")


class UpdateStage(BaseModel):
    """Body for updating a tracked application's stage."""

    stage: str = Field(..., description="The new kanban stage.")


@router.get("", response_model=list[TrackedApplication])
async def list_tracker(
    cache: CacheStore = Depends(get_cache_store),
) -> list[TrackedApplication]:
    """List all tracked applications.

    Args:
        cache: Injected cache store (also backs tracker persistence).

    Returns:
        All tracked application records.
    """
    # TODO: read all tracker rows from the store.
    raise NotImplementedError


@router.post("", response_model=TrackedApplication)
async def create_tracker_item(
    body: CreateTrackedApplication,
    cache: CacheStore = Depends(get_cache_store),
) -> TrackedApplication:
    """Create a new tracked application.

    Args:
        body: The application to create.
        cache: Injected cache store.

    Returns:
        The created :class:`TrackedApplication` (with assigned id).
    """
    # TODO: insert and return the created record.
    raise NotImplementedError


@router.patch("/{item_id}", response_model=TrackedApplication)
async def update_tracker_stage(
    item_id: int,
    body: UpdateStage,
    cache: CacheStore = Depends(get_cache_store),
) -> TrackedApplication:
    """Update the stage of a tracked application.

    Args:
        item_id: Id of the record to update.
        body: The new stage.
        cache: Injected cache store.

    Returns:
        The updated :class:`TrackedApplication`.
    """
    # TODO: update the stage column for item_id and return the record.
    raise NotImplementedError


@router.delete("/{item_id}")
async def delete_tracker_item(
    item_id: int,
    cache: CacheStore = Depends(get_cache_store),
) -> dict:
    """Delete a tracked application.

    Args:
        item_id: Id of the record to delete.
        cache: Injected cache store.

    Returns:
        ``{"deleted": item_id}`` on success.
    """
    # TODO: delete the row for item_id.
    raise NotImplementedError
