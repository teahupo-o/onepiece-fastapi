from pydantic import BaseModel
from typing import Optional
from datetime import date

class VolumeBase(BaseModel):
    volume_number: int
    title: str
    cover_image: Optional[str] = None
    release_date: Optional[date] = None

class VolumeCreate(VolumeBase):
    manga_id: int  # This field links a volume to a manga

class VolumeRead(VolumeBase):
    id: int
    manga_id: int

    class Config:
        orm_mode = True
