import base64
import os
from dataclasses import dataclass


@dataclass
class ApiCredentials:
    def __init__(self):
        client_id = os.environ.get('SPOTIFY_CLIENT_ID')
        client_secret = os.environ.get('SPOTIFY_CLIENT_SECRET')

        self.authorization_credentials = self.__encode_to_base64(
            client_id + ':' + client_secret
        )

    def __encode_to_base64(self, data: str) -> str:
        return base64.b64encode(data.encode()).decode()
