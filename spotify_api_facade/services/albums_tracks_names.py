from typing import List

from spotify_api_facade.middleware import Album_Tracks_Names


def get_album_tracks_names(spotify_album_id: str) -> List[str]:
    """
    Retrieves the tracks names for a given album.
    """

    album_tracks_names: List[str] = Album_Tracks_Names(spotify_album_id) \
        .request_to_spotify_api()

    return album_tracks_names
