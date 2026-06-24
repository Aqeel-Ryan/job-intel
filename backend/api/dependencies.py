"""FastAPI dependency-injection providers (cache store, LLM client).

These are wired into route handlers via ``fastapi.Depends``. Singletons are
created at startup (see ``backend.main``) and handed out here.
"""

from backend.cache.store import CacheStore
from backend.llm.client import LLMClient

# Process-wide singletons, populated by the FastAPI startup event in main.py.
_cache_store: CacheStore | None = None
_llm_client: LLMClient | None = None


def set_cache_store(store: CacheStore) -> None:
    """Register the process-wide cache store (called at startup).

    Args:
        store: The initialised :class:`CacheStore` singleton.
    """
    global _cache_store
    _cache_store = store


def set_llm_client(client: LLMClient) -> None:
    """Register the process-wide LLM client (called at startup).

    Args:
        client: The initialised :class:`LLMClient` singleton.
    """
    global _llm_client
    _llm_client = client


def get_cache_store() -> CacheStore:
    """FastAPI dependency: return the shared cache store.

    Returns:
        The :class:`CacheStore` singleton.
    """
    # TODO: assert initialised and return _cache_store.
    raise NotImplementedError


def get_llm_client() -> LLMClient:
    """FastAPI dependency: return the shared LLM client.

    Returns:
        The :class:`LLMClient` singleton.
    """
    # TODO: assert initialised and return _llm_client.
    raise NotImplementedError
