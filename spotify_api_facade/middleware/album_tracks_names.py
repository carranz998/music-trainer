from typing import Any

from spotify_api_facade.middleware.spotify_api_request_handler import \
    Spotify_Api_Request_Handler


class Album_Tracks_Names(Spotify_Api_Request_Handler):
    """
    Handles requests to the Spotify API to retrieve the names of tracks for a given album.
    """

    def __init__(self, spotify_album_id: str) -> None:
        self.spotify_album_id = spotify_album_id

    def _set_request_url(self) -> str:
        return f'https://api.spotify.com/v1/albums/{self.spotify_album_id}/tracks'

    def _set_http_method(self) -> str:
        return 'get'

    def _postprocess_response_json(self) -> Any:
        return [
            track_json['name']
            for track_json in self._response_json['items']
        ]
