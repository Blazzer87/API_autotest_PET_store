from typing import Optional, Literal
from pydantic import BaseModel


class Category(BaseModel):
    id: Optional[int] = None
    name: Optional[str] = None

class Tag(BaseModel):
    id: Optional[int] = None
    name: Optional[str] = None

class PetJsonModel (BaseModel):
    id: int
    category: Optional[Category]
    name: str
    photoUrls: Optional[list[str]] = None
    tags: list[Tag]
    status: str

class StatusMessageModel(BaseModel):
    code: Literal[200]
    type: Literal['unknown']
    message: str


