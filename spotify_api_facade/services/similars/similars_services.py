import requests

from ..tokens.tokens_services import with_token


@with_token
def retrieve_similar_artists_uri(access_token: str, token_type: str, artist_id: str) -> tuple[str]:
    authorization_options = {
        'url': f'https://api.spotify.com/v1/artists/{artist_id}/related-artists',
        'headers': {
            'Authorization': f'{token_type} {access_token}'
        }
    }

    response = requests.get(
        url=authorization_options['url'],
        headers=authorization_options['headers']
    )

    similar_artists_uri = []

    for a in response.json()['artists']:
        uri = a['uri'].split(':')[-1]
        
        similar_artists_uri.append(uri)

    return similar_artists_uri
