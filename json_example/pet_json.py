from typing import Optional
from pydantic import BaseModel



class Category(BaseModel):
    id: int
    name: str

class Tag(BaseModel):
    id: Optional[int] = None
    name: Optional[str] = None

class PetJsonModel (BaseModel):
    id: int
    category: Category
    name: str
    photoUrls: Optional[list[str]] = None
    tags: list[Tag]
    status: str


