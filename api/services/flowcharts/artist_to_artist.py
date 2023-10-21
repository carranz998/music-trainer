from typing import Iterator

import flask

from api.algorithms import generate_items_flowchart
from api.blueprints import flowcharts_blueprint
from api.decorators import request_json_validator
from api.spotify_api_facade import Artist_Name, Similar_Artists_Uri


@flowcharts_blueprint.route('/artist_to_artist')
@request_json_validator({
    'source_artist_id': str,
    'target_artist_id': str
})
def artist_to_artist(source_artist_id: str, target_artist_id: str) -> tuple[flask.Response, int]:
    artists_uri_flowchart = generate_items_flowchart(
        source_artist_id,
        target_artist_id,
        __get_similar_artists_uri
    )

    flowchart = list(__get_additional_artist_data(artists_uri_flowchart))
    formatted_data = {'flowchart': flowchart}

    return flask.jsonify(formatted_data), 200


def __get_additional_artist_data(artists_uri_flowchart: list[str]) -> Iterator[dict]:
    for i, artist_id in enumerate(artists_uri_flowchart, start=1):
        yield {
            'artist_id': artist_id,
            'artist_name': Artist_Name(artist_id).request_to_api(),
            'listening_order': i
        }


def __get_similar_artists_uri(artist_id) -> list[str]:
    return Similar_Artists_Uri(artist_id).request_to_api()
