import json
from abc import ABC, abstractmethod
from datetime import datetime
from typing import Any

from ..db import session
from ..models import TokenModel
from .encoders.sqlalchemy_model_encoder import SqlAlchemyModelEncoder


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
            session.add(created_token)
            session.commit()

        except BaseException:
            session.rollback()

    def list_all_tokens(self) -> list[dict[str, Any]]:
        try:
            all_tokens = session.query(TokenModel).all()

            data = [
                json.loads(json.dumps(row, cls=SqlAlchemyModelEncoder))
                for row in all_tokens
            ]

            return data

        except BaseException:
            return None
