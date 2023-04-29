import os

from spotify_api_facade.utils.format_conversions import encode_to_base64

client_id = os.environ.get('CLIENT_ID')
client_secret = os.environ.get('CLIENT_SECRET')
authorization_credentials = encode_to_base64(client_id + ':' + client_secret)

access_token_parameters_uri = 'spotify_api_facade/services/tokens/access_token_parameters.json'

__all__ = [
    'retrieve_access_token'
]
