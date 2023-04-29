import spotify_api_facade

for track_name in spotify_api_facade.album_tracks('1CICQQAxvXbayxDF5jJETJ'):
    print(track_name)
