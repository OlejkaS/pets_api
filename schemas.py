from datetime import datetime
from enum import Enum
from pydantic import BaseModel, Field
from typing import List


class PetType(Enum):
    dog = 'dog'
    cat = 'cat'


class PetBaseModel(BaseModel):
    name: str = Field(max_length=16)
    age: int = Field(ge=0)
    type: str


class PetListModel(PetBaseModel):
    id: int
    created_at: datetime = datetime.now()


class PetListWithCount(BaseModel):
    count: int
    items: List[PetListModel]


class DeletePetModel(BaseModel):
    ids: List[int] = [1, 2, 3]
