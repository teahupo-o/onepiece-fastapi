from pydantic import BaseModel
from typing import Optional

class PublisherBase(BaseModel):
    name: str
    country: Optional[str] = None

class PublisherCreate(PublisherBase):
    pass

class PublisherRead(PublisherBase):
    id: int

    class Config:
        orm_mode = True
