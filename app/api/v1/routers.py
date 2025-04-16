from fastapi import APIRouter
from app.api.v1.endpoints import (
    characters,
    mangas,
    volumes,
    arcs,
    authors,
    publishers,
    manga_characters,
    manga_volumes,
    manga_arcs,
    analytics
)

api_router = APIRouter()

api_router.include_router(characters.router, prefix="/characters", tags=["characters"])
api_router.include_router(mangas.router, prefix="/mangas", tags=["mangas"])
api_router.include_router(volumes.router, prefix="/volumes", tags=["volumes"])
api_router.include_router(arcs.router, prefix="/arcs", tags=["arcs"])
api_router.include_router(authors.router, prefix="/authors", tags=["authors"])
api_router.include_router(publishers.router, prefix="/publishers", tags=["publishers"])

# Nested endpoints
api_router.include_router(
    manga_characters.router,
    prefix="/mangas/{manga_id}/characters",
    tags=["manga_characters"]
)

api_router.include_router(
    manga_volumes.router,
    prefix="/mangas/{manga_id}/volumes",
    tags=["manga_volumes"]
)
api_router.include_router(
    manga_arcs.router,
    prefix="/mangas/{manga_id}/arcs",
    tags=["manga_arcs"]
)

# Analytics endpoints
api_router.include_router(analytics.router, prefix="/analytics", tags=["analytics"])
