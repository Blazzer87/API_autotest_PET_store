from pydantic import BaseModel


class ValidatePetJson (BaseModel):
    id: int
    category: dict
    name: str
    photoUrls: list
    tags: list
    status: str
