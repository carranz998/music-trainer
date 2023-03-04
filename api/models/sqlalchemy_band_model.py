from sqlalchemy import Column, Integer, String

from ..postgresql_db import Base


class SQLAlchemyBandModel(Base):
    __tablename__ = 'bands'

    id = Column(Integer, primary_key=True, autoincrement=False)
    name = Column(String, nullable=False)

    def __init__(self, id: int, name: str) -> None:
        self.id = id
        self.name = name
