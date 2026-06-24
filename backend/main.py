"""FastAPI application entry point for Job Intel.

Wires CORS (origins from config), the three route routers, a startup hook that
initialises the cache store and LLM client, and a health check.
"""

import config
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from backend.api.dependencies import set_cache_store, set_llm_client
from backend.api.routes import company_router, score_router, tracker_router
from backend.cache.store import CacheStore
from backend.llm.client import LLMClient

app = FastAPI(title=config.APP_NAME, version=config.APP_VERSION)

app.add_middleware(
    CORSMiddleware,
    allow_origins=config.CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(company_router)
app.include_router(score_router)
app.include_router(tracker_router)


@app.on_event("startup")
async def on_startup() -> None:
    """Initialise process-wide singletons (cache store, LLM client).

    Builds the :class:`CacheStore` and :class:`LLMClient` from config and
    registers them with the dependency-injection providers.
    """
    set_cache_store(CacheStore(config))
    set_llm_client(LLMClient(config))


@app.get("/health")
async def health() -> dict:
    """Health check.

    Returns:
        ``{"status": "ok", "version": APP_VERSION}``.
    """
    return {"status": "ok", "version": config.APP_VERSION}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(
        "backend.main:app",
        host=config.BACKEND_HOST,
        port=config.BACKEND_PORT,
        reload=config.DEBUG,
    )
