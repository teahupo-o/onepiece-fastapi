from pydantic import BaseModel
from typing import Optional

class ArcBase(BaseModel):
    arc_name: str
    description: Optional[str] = None
    start_chapter: int
    end_chapter: int

class ArcCreate(ArcBase):
    manga_id: int  # This links an arc to a manga

class ArcRead(ArcBase):
    id: int
    manga_id: int

    class Config:
        orm_mode = True
