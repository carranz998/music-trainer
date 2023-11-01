from typing import Iterator

import flask

from api.decorators import request_json_validator
from spotify_api_facade import get_artist_name, get_similar_artists_uri
from spotify_enhancer import get_artist_to_artist_flowchart


@request_json_validator({
    'source_spotify_artist_id': str,
    'target_spotify_artist_id': str
})
def artist_to_artist(source_spotify_artist_id: str, target_spotify_artist_id: str) -> tuple[flask.Response, int]:
    artists_uri_flowchart = get_artist_to_artist_flowchart(
        source_spotify_artist_id,
        target_spotify_artist_id,
        get_similar_artists_uri
    )

    flowchart = list(__get_additional_artist_data(artists_uri_flowchart))

    return flask.jsonify({'flowchart': flowchart}), 200


def __get_additional_artist_data(artists_uri_flowchart: list[str]) -> Iterator[dict]:
    for i, spotify_artist_id in enumerate(artists_uri_flowchart, start=1):
        artist_name = get_artist_name(spotify_artist_id)

        yield {
            'artist_name': artist_name,
            'listening_order': i,
            'spotify_artist_id': spotify_artist_id
        }
