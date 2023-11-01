from datetime import datetime

from sqlalchemy import (
    Column,
    DateTime,
    Enum,
    Integer,
    String
)

from api.schemas import PetType
from db.database import Base


class Pet(Base):
    __tablename__ = 'pets'

    id: int = Column(Integer, primary_key=True, index=True)
    name: str = Column(String, nullable=False)
    age: int = Column(Integer, nullable=False)
    type: PetType = Column(Enum(PetType), nullable=False)
    created_at: datetime = Column(DateTime, default=datetime.now)
