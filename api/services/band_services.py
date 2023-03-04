from typing import Any

from flask import Blueprint, jsonify, request

from data_scraping import BandNameScraper, scrap_bands_flowchart

from ..respositories import BandRepository
from ..respositories.band_repository import SQLAlchemyBandRepository
from ..services.encoders.sqlalchemy_model_encoder import convert_to_json

band_blueprint = Blueprint('bands', __name__, url_prefix='/bands')


class BandService:
    def __init__(self, band_repository: BandRepository) -> None:
        self.band_repository = band_repository

    def create_flowchart(self, bands_ids: list[int], **kwargs):
        self.band_repository.create_flowchart(bands_ids, **kwargs)

    def list_all_bands(self) -> list[dict[str, Any]]:
        return self.band_repository.list_all_bands()


@band_blueprint.route('/create_flowchart', methods=['POST'])
def create_flowchart():
    band_repository = SQLAlchemyBandRepository()
    band_service = BandService(band_repository)

    source_band_id = request.json['source_band_id']
    target_band_id = request.json['target_band_id']

    bands_ids = scrap_bands_flowchart(source_band_id, target_band_id)

    band_name_scraper = BandNameScraper()
    bands_names = list(map(band_name_scraper.scrap, bands_ids))

    band_service.create_flowchart(bands_ids, bands_names=bands_names)

    return jsonify({'data': []}), 201


@band_blueprint.route('/list', methods=['POST'])
def list_all_bands() -> list[dict[str, Any]]:
    band_repository = SQLAlchemyBandRepository()
    band_service = BandService(band_repository)

    data = list(map(convert_to_json, band_service.list_all_bands()))

    return jsonify({'data': data}), 200
