from typing import Iterator

import flask

from spotify_api_facade.services import Artist_Name, Similar_Artists_Uri
from spotify_enhancer.algorithms import generate_items_flowchart
from spotify_enhancer.blueprints import flowcharts_blueprint
from spotify_enhancer.decorators import request_json_validator


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

    flowchart = __get_additional_artist_data(artists_uri_flowchart)

    return flask.jsonify({'flowchart': flowchart}), 200


def __get_additional_artist_data(artists_uri_flowchart: list[str]) -> Iterator[dict]:
    additional_artist_data = []

    for i, spotify_artist_id in enumerate(artists_uri_flowchart, start=1):
        artist_name = Artist_Name(spotify_artist_id)
        spotify_api_response = artist_name.request_to_spotify_api()

        artist_data = {
            'listening_order': i,
            'spotify_artist_id': spotify_artist_id,
            'spotify_artist_name': spotify_api_response
        }

        additional_artist_data.append(artist_data)

    return additional_artist_data


def __get_similar_artists_uri(spotify_artist_id) -> list[str]:
    similar_artists_uri = Similar_Artists_Uri(spotify_artist_id)
    spotify_api_response = similar_artists_uri.request_to_spotify_api()

    return spotify_api_response
