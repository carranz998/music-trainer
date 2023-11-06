from typing import Any

from spotify_api_facade.middleware.spotify_api_request_handler import \
    Spotify_Api_Request_Handler


class Artist_Name(Spotify_Api_Request_Handler):
    """
    Handles requests to the Spotify API to retrieve the names of a given artist.
    """

    def __init__(self, spotify_artist_id: str) -> None:
        self.spotify_artist_id = spotify_artist_id

    def _set_request_url(self) -> str:
        return f'https://api.spotify.com/v1/artists/{self.spotify_artist_id}'

    def _set_http_method(self) -> str:
        return 'get'

    def _postprocess_response_json(self) -> Any:
        return self._response_json['name']
