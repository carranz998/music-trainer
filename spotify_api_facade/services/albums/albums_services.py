import requests

from ..tokens.tokens_services import retrieve_access_token


def album_tracks(album_id: str) -> tuple[str]:
    access_token, token_type = retrieve_access_token()

    authorization_options = {
        'url': f'https://api.spotify.com/v1/albums/{album_id}/tracks',
        'headers': {
            'Authorization': f'{token_type} {access_token}'
        }
    }

    response = requests.get(
        authorization_options['url'],
        headers=authorization_options['headers']
    )

    return tuple(
        track_json['name']
        for track_json in response.json()['items']
    )
