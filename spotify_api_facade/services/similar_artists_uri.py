from spotify_api_facade.middleware import Similar_Artists_Uri


def get_similar_artists_uri(spotify_artist_id: str) -> list[str]:
    """
    Retrieves the similar artists' uri for a given artist.
    """

    similar_artists_uri: list[str] = Similar_Artists_Uri(spotify_artist_id) \
        .request_to_spotify_api()

    return similar_artists_uri
