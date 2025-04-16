from pydantic import BaseModel
from typing import Optional

class CharacterBase(BaseModel):
    name: str
    description: Optional[str] = None
    role: Optional[str] = None
    affiliations: Optional[str] = None
    bounty: Optional[int] = None
    power_level: Optional[int] = None

class CharacterCreate(CharacterBase):
    pass  # same fields used for POST / create

class CharacterRead(CharacterBase):
    id: int

    class Config:
        orm_mode = True  # this allows SQLAlchemy → Pydantic conversion
