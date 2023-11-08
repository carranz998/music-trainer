from spotify_api_facade.middleware import Artist_Name


def get_artist_name(spotify_artist_id: str) -> str:
    """
    Retrieves the name for a given artist.
    """

    artist_name: str = Artist_Name(spotify_artist_id).request_to_spotify_api()

    return artist_name
