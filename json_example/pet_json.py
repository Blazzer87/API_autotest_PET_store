from pydantic import BaseModel


class PetJSON (BaseModel):
    id: int
    category: dict
    name: str
    photoUrls: list
    tags: list
    status: str
