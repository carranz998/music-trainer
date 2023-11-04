from typing import Any

from spotify_api_facade.utils.spotify_api_call_backbone import \
    Spotify_Api_Call_Backbone


class __Similar_Artists_Uri(Spotify_Api_Call_Backbone):
    def __init__(self, artist_id: str) -> None:
        self.artist_id = artist_id

    def _set_url(self) -> str:
        return f'https://api.spotify.com/v1/artists/{self.artist_id}/related-artists'

    def _set_http_method(self) -> str:
        return 'get'

    def _postprocess_response_json(self) -> Any:
        return [
            artist_json['uri'].split(':')[-1]
            for artist_json in self._response_json['artists']
        ]


def get_similar_artists_uri(spotify_artist_id: str) -> list[str]:
    similar_artists_uri = __Similar_Artists_Uri(spotify_artist_id)
    spotify_api_response: list[str] = similar_artists_uri \
        .request_to_spotify_api()

    return spotify_api_response
