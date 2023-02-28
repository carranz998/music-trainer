from abc import ABC, abstractmethod
from datetime import datetime
from typing import Any

from .. import db
from ..models import TokenModel


class TokenRepository(ABC):
    @abstractmethod
    def create_token(self, name: str, token: str, expiration_date: datetime) -> None:
        pass

    @abstractmethod
    def list_all_tokens(self) -> list[dict[str, Any]]:
        pass


class SqlAlchemyTokenRepository(TokenRepository):
    def create_token(self, name: str, token: str, expiration_date: datetime) -> None:
        created_token = TokenModel(name, token, expiration_date)

        try:
            db.session.add(created_token)
            db.session.commit()

        except BaseException:
            db.session.rollback()

    def list_all_tokens(self) -> list[dict[str, Any]]:
        try:
            query = db.session.query(TokenModel).all()
            data = [row.serialize() for row in query]

            return data

        except BaseException:
            db.session.rollback()

            return None
