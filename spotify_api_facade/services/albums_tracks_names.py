from spotify_api_facade.middleware.album_tracks_names import Album_Tracks_Names


def get_album_tracks_names(spotify_album_id: str) -> list[str]:
    album_tracks_names = Album_Tracks_Names(spotify_album_id)
    spotify_api_response: list[str] = album_tracks_names \
        .request_to_spotify_api()

    return spotify_api_response
