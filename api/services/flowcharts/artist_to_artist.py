from typing import Iterator

import flask

from api.algorithms import generate_items_flowchart
from api.blueprints import flowcharts_blueprint
from api.decorators import request_json_validator
from api.spotify_api_facade import Artist_Name, Similar_Artists_Uri


@flowcharts_blueprint.route('/artist_to_artist')
@request_json_validator({
    'source_spotify_artist_id': str,
    'target_spotify_artist_id': str
})
def artist_to_artist(source_spotify_artist_id: str, target_spotify_artist_id: str) -> tuple[flask.Response, int]:
    artists_uri_flowchart = generate_items_flowchart(
        source_spotify_artist_id,
        target_spotify_artist_id,
        __get_similar_artists_uri
    )

    flowchart = list(__get_additional_artist_data(artists_uri_flowchart))

    return flask.jsonify({'flowchart': flowchart}), 200


def __get_additional_artist_data(artists_uri_flowchart: list[str]) -> Iterator[dict]:
    for i, spotify_artist_id in enumerate(artists_uri_flowchart, start=1):
        yield {
            'spotify_artist_id': spotify_artist_id,
            'spotify_artist_name': Artist_Name(spotify_artist_id).request_to_spotify_api(),
            'listening_order': i
        }


def __get_similar_artists_uri(spotify_artist_id) -> list[str]:
    return Similar_Artists_Uri(spotify_artist_id).request_to_spotify_api()
