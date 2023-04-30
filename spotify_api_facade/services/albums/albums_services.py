import requests

from ..tokens.tokens_services import with_token


@with_token
def retrieve_album_tracks_names(access_token: str, token_type: str, album_id: str) -> tuple[str]:
    authorization_options = {
        'url': f'https://api.spotify.com/v1/albums/{album_id}/tracks',
        'headers': {
            'Authorization': f'{token_type} {access_token}'
        }
    }

    response = requests.get(
        url=authorization_options['url'],
        headers=authorization_options['headers']
    )

    album_tracks_names = tuple(
        track_json['name']
        for track_json in response.json()['items']
    )

    return album_tracks_names
