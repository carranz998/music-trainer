from typing import Iterator

import requests

from ...utils.http_request_facade import (build_authorization_options,
                                          send_http_request)
from ..tokens.tokens_services import with_token


@with_token
def retrieve_similar_artists_uri(access_token: str, token_type: str, artist_id: str) -> Iterator[str]:
    url = f'https://api.spotify.com/v1/artists/{artist_id}/related-artists'

    options = build_authorization_options(url, access_token, token_type)
    response_json = send_http_request(requests.get, options)

    for artist_json in response_json['artists']:
        yield artist_json['uri'].split(':')[-1]
