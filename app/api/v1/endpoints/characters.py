from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.models import Character
from app.schemas.character import CharacterCreate, CharacterRead
from typing import List

router = APIRouter()

# POST /characters → Create character
@router.post("/", response_model=CharacterRead)
def create_character(character: CharacterCreate, db: Session = Depends(get_db)):
    db_character = Character(**character.dict())
    db.add(db_character)
    db.commit()
    db.refresh(db_character)
    return db_character

# GET /characters/{id} → Get one character
@router.get("/{character_id}", response_model=CharacterRead)
def read_character(character_id: int, db: Session = Depends(get_db)):
    db_character = db.query(Character).filter(Character.id == character_id).first()
    if not db_character:
        raise HTTPException(status_code=404, detail="Character not found")
    return db_character

# GET /characters → List all characters
@router.get("/", response_model=List[CharacterRead])
def list_characters(db: Session = Depends(get_db)):
    return db.query(Character).all()

@router.put("/{character_id}", response_model=CharacterRead)
def update_character(character_id: int, updated_data: CharacterCreate, db: Session = Depends(get_db)):
    db_character = db.query(Character).filter(Character.id == character_id).first()
    if not db_character:
        raise HTTPException(status_code=404, detail="Character not found")
    for key, value in updated_data.dict().items():
        setattr(db_character, key, value)
    db.commit()
    db.refresh(db_character)
    return db_character

@router.delete("/{character_id}", status_code=204)
def delete_character(character_id: int, db: Session = Depends(get_db)):
    db_character = db.query(Character).filter(Character.id == character_id).first()
    if not db_character:
        raise HTTPException(status_code=404, detail="Character not found")
    db.delete(db_character)
    db.commit()
    return