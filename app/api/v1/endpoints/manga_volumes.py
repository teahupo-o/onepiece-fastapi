from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.core.database import get_db
from app.models import Volume
from app.schemas.volume import VolumeRead

router = APIRouter()

@router.get("/", response_model=List[VolumeRead])
def list_volumes_by_manga(manga_id: int, db: Session = Depends(get_db)):
    volumes = db.query(Volume).filter(Volume.manga_id == manga_id).all()
    if not volumes:
        raise HTTPException(status_code=404, detail="No volumes found for this manga")
    return volumes
