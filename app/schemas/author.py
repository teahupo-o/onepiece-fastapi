from pydantic import BaseModel
from datetime import date
from typing import Optional

class AuthorBase(BaseModel):
    name: str
    nationality: Optional[str] = None
    biography: Optional[str] = None
    birthdate: Optional[date] = None

class AuthorCreate(AuthorBase):
    pass

class AuthorRead(AuthorBase):
    id: int

    class Config:
        orm_mode = True
