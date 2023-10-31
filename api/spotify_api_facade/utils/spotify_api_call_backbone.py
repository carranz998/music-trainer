from abc import ABC, abstractmethod
from typing import Any, Callable

import requests

from api.credentials import spotify_api_credential
from api.repositories import Token_Cache_File


class Spotify_Api_Call_Backbone(ABC):
    def __init__(self) -> None:
        self._url = None
        self._request_json = None
        self._response_json = None

    def request_to_spotify_api(self) -> Any:
        cached_response_json = self._get_cached_response_json()
        if cached_response_json:
            return cached_response_json

        self._url = self._build_url()
        http_method = self._select_http_method()

        self._request_json = self._build_request_json()
        self._request_json = self._postprocess_request_json()

        self._response_json = self.__send_http_request(http_method)
        self._save_to_cache()

        self._response_json = self._postprocess_response_json()

        return self._response_json

    def _save_to_cache(self) -> None:
        pass

    def _get_cached_response_json(self) -> Any | None:
        return None

    def _build_request_json(self) -> dict[str, Any]:
        access_token, token_type = Token().request_to_spotify_api()

        return {
            'headers': {
                'Authorization': f'{token_type} {access_token}'
            },
            'url': self._url
        }

    def __send_http_request(self, http_method: Callable) -> dict[str, Any]:
        return http_method(**self._request_json).json()

    def _postprocess_request_json(self) -> dict[str, Any]:
        return self._request_json

    def _postprocess_response_json(self) -> Any:
        return self._response_json

    @abstractmethod
    def _build_url(self) -> str:
        pass

    @abstractmethod
    def _select_http_method(self) -> Callable:
        pass


class Token(Spotify_Api_Call_Backbone):
    def __init__(self) -> None:
        self.token_cache_file = Token_Cache_File()

    def _build_url(self):
        return 'https://accounts.spotify.com/api/token'

    def _get_cached_response_json(self) -> Any | None:
        return self.token_cache_file.read()

    def _build_request_json(self) -> dict[str, Any]:
        return {
            'data': {
                'grant_type': 'client_credentials'
            },
            'headers': {
                'Authorization': f'Basic {spotify_api_credential}'
            },
            'url': self._url
        }

    def _select_http_method(self) -> Callable[..., Any]:
        return requests.post

    def _postprocess_response_json(self) -> Any:
        access_token = self._response_json['access_token']
        token_type = self._response_json['token_type']

        return access_token, token_type

    def _save_to_cache(self) -> None:
        self.token_cache_file.write(self._response_json)
