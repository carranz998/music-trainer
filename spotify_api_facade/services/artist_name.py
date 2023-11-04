from typing import Any

from spotify_api_facade.utils.spotify_api_request_handler import \
    Spotify_Api_Request_Handler


class __Artist_Name(Spotify_Api_Request_Handler):
    def __init__(self, artist_id: str) -> None:
        self.artist_id = artist_id

    def _set_url(self) -> str:
        return f'https://api.spotify.com/v1/artists/{self.artist_id}'

    def _set_http_method(self) -> str:
        return 'get'

    def _postprocess_response_json(self) -> Any:
        return self._response_json['name']


def get_artist_name(spotify_artist_id: str) -> str:
    artist_name = __Artist_Name(spotify_artist_id)
    spotify_api_response: str = artist_name.request_to_spotify_api()

    return spotify_api_response
