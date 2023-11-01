from datetime import datetime
from enum import Enum
from typing import List

from pydantic import BaseModel, Field


class PetType(Enum):
    dog = 'dog'
    cat = 'cat'


class PetBaseModel(BaseModel):
    name: str = Field(max_length=16)
    age: int = Field(ge=0)
    type: PetType

    class Config:
        from_attributes = True


class PetList(PetBaseModel):
    id: int
    created_at: datetime

    class Config:
        from_attributes = True


class PetListWithCount(BaseModel):
    count: int
    items: List[PetList]


class DeletePetModel(BaseModel):
    ids: List[int] = [1, 2, 3]
