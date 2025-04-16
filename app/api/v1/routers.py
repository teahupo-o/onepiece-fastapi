from fastapi import APIRouter
from app.api.v1.endpoints import items, characters  # 👈 make sure to import characters

api_router = APIRouter()

api_router.include_router(items.router, prefix="/items", tags=["items"])
api_router.include_router(characters.router, prefix="/characters", tags=["characters"])  # 👈 register the character routes

