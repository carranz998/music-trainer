from abc import ABC, abstractmethod
from typing import Any, Dict

from spotify_api_facade.credentials import spotify_api_credential
from spotify_api_facade.middleware.http_response_factory import \
    HTTP_Response_Factory
from spotify_api_facade.repositories import Token_Cache_File


class Spotify_Api_Request_Handler(ABC):
    def __init__(self) -> None:
        self._request_json: Dict[str, Any] = dict()
        self._response_json: Dict[str, Any] = dict()

    def request_to_spotify_api(self) -> Any:
        cached_response_json = self._get_cached_response_json()
        if cached_response_json:
            return cached_response_json

        self._request_json = self._set_request_json()

        url = self._set_url()
        http_method = self._set_http_method()

        self._response_json = self.__send_http_request(
            http_method, url, self._request_json
        )

        self._save_to_cache()

        self._response_json = self._postprocess_response_json()

        return self._response_json

    def __send_http_request(self, http_method: str, url: str, request_json: dict[str, Any]) -> Any:
        return HTTP_Response_Factory.request_to_server(http_method, url, request_json)

    def _save_to_cache(self) -> None:
        pass

    def _get_cached_response_json(self) -> Any | None:
        return None

    def _set_request_json(self) -> dict[str, Any]:
        spotify_api_token = Spotify_Api_Token()
        access_token, token_type = spotify_api_token.request_to_spotify_api()

        return {
            'headers': {
                'Authorization': f'{token_type} {access_token}'
            }
        }

    def _postprocess_request_json(self) -> Any:
        return self._request_json

    def _postprocess_response_json(self) -> Any:
        return self._response_json

    @abstractmethod
    def _set_url(self) -> str:
        pass

    @abstractmethod
    def _set_http_method(self) -> str:
        pass


class Spotify_Api_Token(Spotify_Api_Request_Handler):
    def __init__(self) -> None:
        self.token_cache_file = Token_Cache_File()

    def _set_url(self) -> str:
        return 'https://accounts.spotify.com/api/token'

    def _set_http_method(self) -> str:
        return 'post'

    def _get_cached_response_json(self) -> Any | None:
        return self.token_cache_file.read()

    def _set_request_json(self) -> dict[str, Any]:
        return {
            'data': {
                'grant_type': 'client_credentials'
            },
            'headers': {
                'Authorization': f'Basic {spotify_api_credential}'
            }
        }

    def _postprocess_response_json(self) -> Any:
        access_token = self._response_json['access_token']
        token_type = self._response_json['token_type']

        return access_token, token_type

    def _save_to_cache(self) -> None:
        self.token_cache_file.write(self._response_json)
