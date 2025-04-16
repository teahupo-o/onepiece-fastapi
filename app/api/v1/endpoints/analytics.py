from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from sqlalchemy import func
from typing import List
from app.core.database import get_db
from app.models import Character
from app.schemas.character import CharacterRead

router = APIRouter()

@router.get("/average-bounty", response_model=float)
def average_bounty(manga_id: int = Query(..., description="ID of the manga"), db: Session = Depends(get_db)):
    """
    Returns the average bounty of all characters for a given Manga.
    """
    avg = db.query(func.avg(Character.bounty)).filter(Character.manga_id == manga_id).scalar()
    if avg is None:
        raise HTTPException(status_code=404, detail="No characters found for the given manga")
    return avg

@router.get("/top-characters", response_model=List[CharacterRead])
def top_characters(
    manga_id: int = Query(..., description="ID of the manga"),
    limit: int = Query(5, ge=1, description="Number of top characters to return"),
    db: Session = Depends(get_db)
):
    """
    Returns the top characters by bounty for a given Manga.
    """
    top_chars = db.query(Character).filter(Character.manga_id == manga_id).order_by(Character.bounty.desc()).limit(limit).all()
    if not top_chars:
        raise HTTPException(status_code=404, detail="No characters found for the given manga")
    return top_chars
