from api.spotify_api_facade.utils.format_conversions import encode_to_base64

client_id = '168b2708dfef4bc394caa012fc723677'
client_secret = '25ac584b1195459f97f00a0a52e0527f'
authorization_credentials = encode_to_base64(client_id + ':' + client_secret)

access_token_parameters_uri = 'api/spotify_api_facade/services/tokens/access_token_parameters.json'

__all__ = [
    'retrieve_access_token'
]
