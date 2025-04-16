from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.core.database import get_db
from app.models import Arc
from app.schemas.arc import ArcCreate, ArcRead

router = APIRouter()

@router.post("/", response_model=ArcRead)
def create_arc(arc: ArcCreate, db: Session = Depends(get_db)):
    db_arc = Arc(**arc.dict())
    db.add(db_arc)
    db.commit()
    db.refresh(db_arc)
    return db_arc

@router.get("/", response_model=List[ArcRead])
def list_arcs(db: Session = Depends(get_db)):
    return db.query(Arc).all()

@router.get("/{arc_id}", response_model=ArcRead)
def get_arc(arc_id: int, db: Session = Depends(get_db)):
    arc = db.query(Arc).filter(Arc.id == arc_id).first()
    if not arc:
        raise HTTPException(status_code=404, detail="Arc not found")
    return arc

@router.put("/{arc_id}", response_model=ArcRead)
def update_arc(arc_id: int, updated_arc: ArcCreate, db: Session = Depends(get_db)):
    arc = db.query(Arc).filter(Arc.id == arc_id).first()
    if not arc:
        raise HTTPException(status_code=404, detail="Arc not found")
    for field, value in updated_arc.dict().items():
        setattr(arc, field, value)
    db.commit()
    db.refresh(arc)
    return arc

@router.delete("/{arc_id}", status_code=204)
def delete_arc(arc_id: int, db: Session = Depends(get_db)):
    arc = db.query(Arc).filter(Arc.id == arc_id).first()
    if not arc:
        raise HTTPException(status_code=404, detail="Arc not found")
    db.delete(arc)
    db.commit()
    return
