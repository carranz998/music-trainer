import base64


def __encode_to_base64(data: str) -> str:
    return base64.b64encode(data.encode()).decode()


client_id = '168b2708dfef4bc394caa012fc723677'
client_secret = '25ac584b1195459f97f00a0a52e0527f'

authorization_credentials = __encode_to_base64(client_id + ':' + client_secret)
access_token_parameters_uri = 'api/spotify_api_facade/access_token_parameters.json'
