from spotify_api_facade.middleware.similar_artists_uri import \
    Similar_Artists_Uri


def get_similar_artists_uri(spotify_artist_id: str) -> list[str]:
    similar_artists_uri = Similar_Artists_Uri(spotify_artist_id)
    spotify_api_response: list[str] = similar_artists_uri \
        .request_to_spotify_api()

    return spotify_api_response
