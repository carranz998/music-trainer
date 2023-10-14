import flask

from api.algorithms import generate_items_flowchart
from api.blueprints import flowcharts_blueprint
from api.decorators import request_json_validator
from api.spotify_api_facade import SimilarArtistsUri


@flowcharts_blueprint.route('/artist_to_artist')
@request_json_validator({
    'source_artist_id': str,
    'target_artist_id': str
})
def generate_flowchart(source_artist_id: str, target_artist_id: str) -> tuple[flask.Response, int]:
    def similar_artists_gather(source_artist_id):
        return SimilarArtistsUri(source_artist_id).request_to_api()

    artists_uri_flowchart = generate_items_flowchart(
        source_artist_id,
        target_artist_id,
        similar_artists_gather
    )

    formatted_data = {
        'flowchart': artists_uri_flowchart
    }

    return flask.jsonify(formatted_data), 200
