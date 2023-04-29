from typing import Iterator

import requests

from ..tokens.extractor import retrieve_access_token


def album_tracks(album_id: str) -> Iterator[str]:
    access_token, token_type = retrieve_access_token()

    auth_options = {
        'url': f'https://api.spotify.com/v1/albums/{album_id}/tracks',
        'headers': {
            'Authorization': f'{token_type} {access_token}'
        }
    }

    response = requests.get(
        auth_options['url'],
        headers=auth_options['headers']
    )

    for song_json in response.json()['items']:
        yield song_json['name']
