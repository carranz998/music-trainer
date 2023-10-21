from typing import Any, Callable

import requests

from api.spotify_api_facade.utils.spotify_api_call_backbone import \
    Spotify_Api_Call_Backbone


class Album_Tracks_Names(Spotify_Api_Call_Backbone):
    def __init__(self, album_id: str) -> None:
        self.album_id = album_id

    def _build_url(self) -> str:
        return f'https://api.spotify.com/v1/albums/{self.album_id}/tracks'

    def _select_http_method(self) -> Callable[..., Any]:
        return requests.get

    def _postprocess_response_json(self) -> Any:
        return [
            track_json['name']
            for track_json in self._response_json['items']
        ]
