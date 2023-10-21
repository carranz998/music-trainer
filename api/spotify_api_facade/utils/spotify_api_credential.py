import base64
import os


def __get_credential() -> str:
    client_id = os.environ.get('SPOTIFY_CLIENT_ID')
    client_secret = os.environ.get('SPOTIFY_CLIENT_SECRET')

    return client_id + ':' + client_secret


def __encode_to_base64(data: str) -> str:
    return base64.b64encode(data.encode()).decode()


def __build_credential() -> str:
    raw_credential = __get_credential()
    encoded_credential = __encode_to_base64(raw_credential)

    return encoded_credential


spotify_api_credential = __build_credential()
