from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.models import Character
from app.schemas.character import CharacterCreate, CharacterRead
from typing import List, Optional

router = APIRouter()


@router.post("/", response_model=CharacterRead)
def create_character(character: CharacterCreate, db: Session = Depends(get_db)):
    db_character = Character(**character.dict())
    db.add(db_character)
    db.commit()
    db.refresh(db_character)
    return db_character


@router.get("/{character_id}", response_model=CharacterRead)
def read_character(character_id: int, db: Session = Depends(get_db)):
    db_character = db.query(Character).filter(Character.id == character_id).first()
    if not db_character:
        raise HTTPException(status_code=404, detail="Character not found")
    return db_character


@router.get("/", response_model=List[CharacterRead])
def list_characters(
        db: Session = Depends(get_db),
        role: Optional[str] = Query(None, description="Filter by character role"),
        min_bounty: Optional[int] = Query(None, description="Minimum bounty value"),
        max_bounty: Optional[int] = Query(None, description="Maximum bounty value"),
        skip: int = Query(0, ge=0, description="Number of records to skip"),
        limit: int = Query(100, ge=1, description="Maximum number of records to return")
):
    query = db.query(Character)

    if role:
        query = query.filter(Character.role == role)
    if min_bounty is not None:
        query = query.filter(Character.bounty >= min_bounty)
    if max_bounty is not None:
        query = query.filter(Character.bounty <= max_bounty)

    return query.offset(skip).limit(limit).all()
