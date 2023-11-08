from typing import Any, Dict, Iterator, List, Tuple

from flask import Response, jsonify

from app.decorators import Request_Json_Validator
from spotify_api_facade import get_artist_name, get_similar_artists_uri
from spotify_enhancer import get_artist_to_artist_flowchart


@Request_Json_Validator({
    'source_spotify_artist_id': str,
    'target_spotify_artist_id': str
})
def artist_to_artist(source_spotify_artist_id: str, target_spotify_artist_id: str) -> Tuple[Response, int]:
    artists_uri_flowchart = get_artist_to_artist_flowchart(
        source_spotify_artist_id,
        target_spotify_artist_id,
        get_similar_artists_uri
    )

    flowchart = list(__get_additional_artist_data(artists_uri_flowchart))

    return jsonify({'flowchart': flowchart}), 200


def __get_additional_artist_data(artists_uri_flowchart: List[str]) -> Iterator[Dict[str, Any]]:
    for i, spotify_artist_id in enumerate(artists_uri_flowchart, start=1):
        yield {
            'artist_name': get_artist_name(spotify_artist_id),
            'listening_order': i,
            'spotify_artist_id': spotify_artist_id
        }
