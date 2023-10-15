from typing import Any, Callable, Iterator

import requests

from api.spotify_api_facade.utils.spotify_api_call_backbone import \
    SpotifyApiCallBackbone


class ArtistName(SpotifyApiCallBackbone):
    def __init__(self, artist_id: str) -> None:
        self.artist_id = artist_id

    def _build_url(self) -> str:
        return f'https://api.spotify.com/v1/artists/{self.artist_id}'

    def _select_http_method(self) -> Callable[..., Any]:
        return requests.get

    def _postprocess_response_json(self) -> Any:
        return self._response_json['name']
