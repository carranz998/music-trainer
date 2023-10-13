from typing import Any, Callable, Iterator

import requests

from api.spotify_api_facade.spotify_api_call_backbone import \
    SpotifyApiCallBackbone


class AlbumTracksNames(SpotifyApiCallBackbone):
    def __init__(self, album_id: str) -> None:
        self.album_id = album_id

    def _build_url(self):
        return f'https://api.spotify.com/v1/albums/{self.album_id}/tracks'

    def _select_http_method(self) -> Callable[..., Any]:
        return requests.get

    def _postprocess_response_json(self):
        return [
            track_json['name']
            for track_json in self._response_json['items']
        ]
