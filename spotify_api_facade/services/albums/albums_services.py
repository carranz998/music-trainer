import requests

from ...utils.http_request_facade import (build_authorization_options,
                                          send_http_request)
from ..tokens.tokens_services import with_token


@with_token
def retrieve_album_tracks_names(access_token: str, token_type: str, album_id: str) -> tuple[str]:
    url = f'https://api.spotify.com/v1/albums/{album_id}/tracks'

    options = build_authorization_options(url, access_token, token_type)
    response_json = send_http_request(requests.get, options)

    album_tracks_names = tuple(
        track_json['name']
        for track_json in response_json['items']
    )

    return album_tracks_names
