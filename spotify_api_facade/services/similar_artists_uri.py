from typing import List

from spotify_api_facade.middleware import Similar_Artists_Uri


def get_similar_artists_uri(spotify_artist_id: str) -> List[str]:
    """
    Retrieves the similar artists' uri for a given artist.
    """

    similar_artists_uri: List[str] = Similar_Artists_Uri(spotify_artist_id) \
        .request_to_spotify_api()

    return similar_artists_uri
