from pydantic import BaseModel
from typing import Optional

class MangaBase(BaseModel):
    title: str
    synopsis: Optional[str] = None
    ongoing: Optional[bool] = True
    author_id: Optional[int] = None
    publisher_id: Optional[int] = None

class MangaCreate(MangaBase):
    pass

class MangaRead(MangaBase):
    id: int

    class Config:
        orm_mode = True
