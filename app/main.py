from fastapi import FastAPI
from app.core.database import Base, engine
from app.api.v1.routers import api_router

Base.metadata.create_all(bind=engine)

app = FastAPI(title="One PieceDB: Manga & Analytics API")
app.include_router(api_router, prefix="/api/v1")