from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.core.database import get_db
from app.models import Publisher  # Assumes your Publisher model is defined in models.py
from app.schemas.publisher import PublisherCreate, PublisherRead

router = APIRouter()

@router.post("/", response_model=PublisherRead)
def create_publisher(publisher: PublisherCreate, db: Session = Depends(get_db)):
    db_publisher = Publisher(**publisher.dict())
    db.add(db_publisher)
    db.commit()
    db.refresh(db_publisher)
    return db_publisher

@router.get("/", response_model=List[PublisherRead])
def list_publishers(db: Session = Depends(get_db)):
    return db.query(Publisher).all()

@router.get("/{publisher_id}", response_model=PublisherRead)
def get_publisher(publisher_id: int, db: Session = Depends(get_db)):
    publisher = db.query(Publisher).filter(Publisher.id == publisher_id).first()
    if not publisher:
        raise HTTPException(status_code=404, detail="Publisher not found")
    return publisher

@router.put("/{publisher_id}", response_model=PublisherRead)
def update_publisher(publisher_id: int, updated_publisher: PublisherCreate, db: Session = Depends(get_db)):
    publisher = db.query(Publisher).filter(Publisher.id == publisher_id).first()
    if not publisher:
        raise HTTPException(status_code=404, detail="Publisher not found")
    for field, value in updated_publisher.dict().items():
        setattr(publisher, field, value)
    db.commit()
    db.refresh(publisher)
    return publisher

@router.delete("/{publisher_id}", status_code=204)
def delete_publisher(publisher_id: int, db: Session = Depends(get_db)):
    publisher = db.query(Publisher).filter(Publisher.id == publisher_id).first()
    if not publisher:
        raise HTTPException(status_code=404, detail="Publisher not found")
    db.delete(publisher)
    db.commit()
    return
