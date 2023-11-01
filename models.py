from database import Base
from datetime import datetime
from sqlalchemy import (
    Column,
    DateTime,
    Enum,
    Integer,
    String
)
from schemas import PetType


class Pet(Base):
    __tablename__ = 'pets'

    id: int = Column(Integer, primary_key=True, index=True)
    name: str = Column(String, nullable=False)
    age: int = Column(Integer, nullable=False)
    type: PetType = Column(Enum(PetType), nullable=False)
    created_at: datetime = Column(DateTime, default=datetime.now)
