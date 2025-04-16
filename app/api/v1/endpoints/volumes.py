from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.core.database import get_db
from app.models import Volume
from app.schemas.volume import VolumeCreate, VolumeRead

router = APIRouter()

@router.post("/", response_model=VolumeRead)
def create_volume(volume: VolumeCreate, db: Session = Depends(get_db)):
    db_volume = Volume(**volume.dict())
    db.add(db_volume)
    db.commit()
    db.refresh(db_volume)
    return db_volume

@router.get("/", response_model=List[VolumeRead])
def list_volumes(db: Session = Depends(get_db)):
    return db.query(Volume).all()

@router.get("/{volume_id}", response_model=VolumeRead)
def get_volume(volume_id: int, db: Session = Depends(get_db)):
    volume = db.query(Volume).filter(Volume.id == volume_id).first()
    if not volume:
        raise HTTPException(status_code=404, detail="Volume not found")
    return volume

@router.put("/{volume_id}", response_model=VolumeRead)
def update_volume(volume_id: int, updated_volume: VolumeCreate, db: Session = Depends(get_db)):
    volume = db.query(Volume).filter(Volume.id == volume_id).first()
    if not volume:
        raise HTTPException(status_code=404, detail="Volume not found")
    for field, value in updated_volume.dict().items():
        setattr(volume, field, value)
    db.commit()
    db.refresh(volume)
    return volume

@router.delete("/{volume_id}", status_code=204)
def delete_volume(volume_id: int, db: Session = Depends(get_db)):
    volume = db.query(Volume).filter(Volume.id == volume_id).first()
    if not volume:
        raise HTTPException(status_code=404, detail="Volume not found")
    db.delete(volume)
    db.commit()
    return
