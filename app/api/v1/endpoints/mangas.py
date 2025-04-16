from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.core.database import get_db
from app.models import Manga
from app.schemas.manga import MangaCreate, MangaRead

router = APIRouter()

@router.post("/", response_model=MangaRead)
def create_manga(manga: MangaCreate, db: Session = Depends(get_db)):
    db_manga = Manga(**manga.dict())
    db.add(db_manga)
    db.commit()
    db.refresh(db_manga)
    return db_manga

@router.get("/", response_model=List[MangaRead])
def list_mangas(db: Session = Depends(get_db)):
    return db.query(Manga).all()

@router.get("/{manga_id}", response_model=MangaRead)
def get_manga(manga_id: int, db: Session = Depends(get_db)):
    manga = db.query(Manga).filter(Manga.id == manga_id).first()
    if not manga:
        raise HTTPException(status_code=404, detail="Manga not found")
    return manga

@router.put("/{manga_id}", response_model=MangaRead)
def update_manga(manga_id: int, updated_data: MangaCreate, db: Session = Depends(get_db)):
    manga = db.query(Manga).filter(Manga.id == manga_id).first()
    if not manga:
        raise HTTPException(status_code=404, detail="Manga not found")
    for field, value in updated_data.dict().items():
        setattr(manga, field, value)
    db.commit()
    db.refresh(manga)
    return manga

@router.delete("/{manga_id}", status_code=204)
def delete_manga(manga_id: int, db: Session = Depends(get_db)):
    manga = db.query(Manga).filter(Manga.id == manga_id).first()
    if not manga:
        raise HTTPException(status_code=404, detail="Manga not found")
    db.delete(manga)
    db.commit()
    return
