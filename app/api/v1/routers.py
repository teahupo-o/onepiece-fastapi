from fastapi import APIRouter
from app.api.v1.endpoints import (
    characters,
    mangas,
    volumes,
    arcs,
    authors,
    publishers
)

api_router = APIRouter()

api_router.include_router(characters.router, prefix="/characters", tags=["characters"])
api_router.include_router(mangas.router, prefix="/mangas", tags=["mangas"])
api_router.include_router(volumes.router, prefix="/volumes", tags=["volumes"])
api_router.include_router(arcs.router, prefix="/arcs", tags=["arcs"])
api_router.include_router(authors.router, prefix="/authors", tags=["authors"])
api_router.include_router(publishers.router, prefix="/publishers", tags=["publishers"])
