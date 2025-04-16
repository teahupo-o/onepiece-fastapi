from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.core.database import get_db
from app.models import Character
from app.schemas.character import CharacterRead

router = APIRouter()

@router.get("/", response_model=List[CharacterRead])
def list_characters_by_manga(manga_id: int, db: Session = Depends(get_db)):
    # Query characters linked to the given manga_id
    characters = db.query(Character).filter(Character.manga_id == manga_id).all()
    if characters is None:
        raise HTTPException(status_code=404, detail="No characters found for this manga")
    return characters
