from typing import Any

from spotify_api_facade.utils.spotify_api_call_backbone import \
    Spotify_Api_Call_Backbone


class __Album_Tracks_Names(Spotify_Api_Call_Backbone):
    def __init__(self, spotify_album_id: str) -> None:
        self.spotify_album_id = spotify_album_id

    def _set_url(self) -> str:
        return f'https://api.spotify.com/v1/albums/{self.spotify_album_id}/tracks'

    def _set_http_method(self) -> str:
        return 'get'

    def _postprocess_response_json(self) -> Any:
        return [
            track_json['name']
            for track_json in self._response_json['items']
        ]


def get_album_tracks_names(spotify_album_id: str) -> list[str]:
    album_tracks_names = __Album_Tracks_Names(spotify_album_id)
    spotify_api_response: list[str] = album_tracks_names \
        .request_to_spotify_api()

    return spotify_api_response
