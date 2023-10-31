from typing import Any, Callable

import requests

from spotify_api_facade.utils.spotify_api_call_backbone import \
    Spotify_Api_Call_Backbone


class __Artist_Name(Spotify_Api_Call_Backbone):
    def __init__(self, artist_id: str) -> None:
        self.artist_id = artist_id

    def _build_url(self) -> str:
        return f'https://api.spotify.com/v1/artists/{self.artist_id}'

    def _select_http_method(self) -> Callable[..., Any]:
        return requests.get

    def _postprocess_response_json(self) -> Any:
        return self._response_json['name']


def get_artist_name(spotify_artist_id: str) -> str:
    artist_name = __Artist_Name(spotify_artist_id)
    spotify_api_response = artist_name.request_to_spotify_api()

    return spotify_api_response
