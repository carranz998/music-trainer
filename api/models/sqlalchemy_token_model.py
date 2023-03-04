from datetime import datetime

from sqlalchemy import Column, DateTime, Integer, String

from ..postgresql_db import Base


class SQLAlchemyTokenModel(Base):
    __tablename__ = 'tokens'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    token = Column(String, nullable=False)
    expiration_date = Column(DateTime, nullable=False)

    def __init__(self, name: str, token: str, expiration_date: datetime) -> None:
        self.name = name
        self.token = token
        self.expiration_date = expiration_date
