from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.core.database import get_db
from app.models import Arc
from app.schemas.arc import ArcRead

router = APIRouter()

@router.get("/", response_model=List[ArcRead])
def list_arcs_by_manga(manga_id: int, db: Session = Depends(get_db)):
    arcs = db.query(Arc).filter(Arc.manga_id == manga_id).all()
    if not arcs:
        raise HTTPException(status_code=404, detail="No arcs found for this manga")
    return arcs
