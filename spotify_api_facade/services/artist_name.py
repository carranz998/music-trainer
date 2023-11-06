from spotify_api_facade.middleware.artist_name import Artist_Name


def get_artist_name(spotify_artist_id: str) -> str:
    artist_name = Artist_Name(spotify_artist_id)
    spotify_api_response: str = artist_name.request_to_spotify_api()

    return spotify_api_response
