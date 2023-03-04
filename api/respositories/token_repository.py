from abc import ABC, abstractmethod
from datetime import datetime

from ..postgresql_db import session
from ..models import SQLAlchemyTokenModel


class TokenRepository(ABC):
    @abstractmethod
    def create_token(self, name: str, token: str, expiration_date: datetime) -> None:
        pass

    @abstractmethod
    def list_all_tokens(self):
        pass


class SQLAlchemyTokenRepository(TokenRepository):
    def create_token(self, name: str, token: str, expiration_date: datetime) -> None:
        created_token = SQLAlchemyTokenModel(name, token, expiration_date)

        try:
            session.add(created_token)
            session.commit()

        except BaseException:
            session.rollback()

    def list_all_tokens(self):
        try:
            return session.query(SQLAlchemyTokenModel).all()

        except BaseException:
            return None
