import uuid
from datetime import datetime

from flask import Blueprint, jsonify, request

from ..respositories import TokenRepository
from ..respositories.token_repository import SqlAlchemyTokenRepository

token_blueprint = Blueprint('tokens', __name__, url_prefix='/tokens')


class TokenService:
    def __init__(self, token_repository: TokenRepository) -> None:
        self.token_repository = token_repository

    def create_token(self, name: str, token: str, expiration_date: datetime) -> None:
        self.token_repository.create_token(
            name, token, expiration_date
        )

    def list_all_tokens(self):
        return self.token_repository.list_all_tokens()


@token_blueprint.route('/create', methods=['POST'])
def create_token():
    token_repository = SqlAlchemyTokenRepository()
    token_service = TokenService(token_repository)

    name = request.json['name']
    token = str(uuid.uuid4())
    expiration_date = datetime.fromisoformat(request.json['expiration_date'])

    token_service.create_token(name, token, expiration_date)

    return jsonify({'data': []}), 201


@token_blueprint.route('/list', methods=['POST'])
def list_all_tokens():
    token_repository = SqlAlchemyTokenRepository()
    token_service = TokenService(token_repository)

    all_tokens = token_service.list_all_tokens()

    return jsonify({'data': all_tokens}), 200
