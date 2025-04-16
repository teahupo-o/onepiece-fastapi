from fastapi import APIRouter
from app.api.v1.endpoints import characters, manga

api_router = APIRouter()

api_router.include_router(characters.router, prefix="/characters", tags=["characters"])

api_router.include_router(manga.router, prefix="/manga", tags=["manga"])
