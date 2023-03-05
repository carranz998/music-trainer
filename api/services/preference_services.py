from typing import Any

from flask import Blueprint, jsonify, request

from ..respositories import (PreferenceRepository,
                             SQLAlchemyPreferencesRepository)
from ..services.encoders.sqlalchemy_model_encoder import convert_to_json

preference_blueprint = Blueprint(
    'preferences', __name__, url_prefix='/preferences'
)


class PreferenceService:
    def __init__(self, preference_repository: PreferenceRepository) -> None:
        self.preference_repository = preference_repository

    def create_preference(self, token_id: int, band_id: int, preference_level: int):
        self.preference_repository.create_preference(
            token_id, band_id, preference_level
        )

    def list_all_preferences(self) -> list[dict[str, Any]]:
        return self.preference_repository.list_all_preferences()


@preference_blueprint.route('/create', methods=['POST'])
def create_preference() -> None:
    preference_repository = SQLAlchemyPreferencesRepository()
    preference_service = PreferenceService(preference_repository)

    token_id = request.json['token_id']
    band_id = request.json['band_id']
    preference_level = request.json['preference_level']

    preference_service.create_preference(token_id, band_id, preference_level)

    return jsonify({'data': []}), 201


@preference_blueprint.route('/list', methods=['POST'])
def list_all_preferences() -> list[dict[str, Any]]:
    preference_repository = SQLAlchemyPreferencesRepository()
    preference_service = PreferenceService(preference_repository)

    data = list(map(convert_to_json, preference_service.list_all_preferences()))

    return jsonify({'data': data}), 200
