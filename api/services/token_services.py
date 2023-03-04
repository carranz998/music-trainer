import uuid
from datetime import datetime
from typing import Any

from flask import Blueprint, jsonify, request

from ..respositories import SQLAlchemyTokenRepository, TokenRepository
from ..services.encoders.sqlalchemy_model_encoder import convert_to_json

token_blueprint = Blueprint('tokens', __name__, url_prefix='/tokens')


class TokenService:
    def __init__(self, token_repository: TokenRepository) -> None:
        self.token_repository = token_repository

    def create_token(self, name: str, token: str, expiration_date: datetime) -> None:
        self.token_repository.create_token(name, token, expiration_date)

    def list_all_tokens(self) -> list[dict[str, Any]]:
        return self.token_repository.list_all_tokens()


@token_blueprint.route('/create', methods=['POST'])
def create_token() -> None:
    token_repository = SQLAlchemyTokenRepository()
    token_service = TokenService(token_repository)

    name = request.json['name']
    token = str(uuid.uuid4())
    expiration_date = datetime.fromisoformat(request.json['expiration_date'])

    token_service.create_token(name, token, expiration_date)

    return jsonify({'data': []}), 201


@token_blueprint.route('/list', methods=['POST'])
def list_all_tokens() -> list[dict[str, Any]]:
    token_repository = SQLAlchemyTokenRepository()
    token_service = TokenService(token_repository)

    data = list(map(convert_to_json, token_service.list_all_tokens()))

    return jsonify({'data': data}), 200
