from typing import Any, Callable

import requests

from spotify_api_facade.utils.spotify_api_call_backbone import \
    Spotify_Api_Call_Backbone


class Artist_Name(Spotify_Api_Call_Backbone):
    def __init__(self, artist_id: str) -> None:
        self.artist_id = artist_id

    def _build_url(self) -> str:
        return f'https://api.spotify.com/v1/artists/{self.artist_id}'

    def _select_http_method(self) -> Callable[..., Any]:
        return requests.get

    def _postprocess_response_json(self) -> Any:
        return self._response_json['name']
