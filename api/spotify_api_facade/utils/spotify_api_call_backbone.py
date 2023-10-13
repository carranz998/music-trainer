from abc import ABC, abstractmethod
from typing import Any, Callable

import requests

from api.spotify_api_facade.utils.api_credentials import ApiCredentials
from api.spotify_api_facade.utils.token_cache_file import TokenCacheFile


class SpotifyApiCallBackbone(ABC):
    def __init__(self) -> None:
        self._url = None
        self._request_json = None
        self._response_json = None

    def request_to_api(self) -> Any:
        cached_response_json = self._get_cached_response_json()
        if cached_response_json:
            return cached_response_json

        self._url = self._build_url()
        http_method = self._select_http_method()

        self._request_json = self._build_request_json()
        self._request_json = self._postprocess_request_json()

        self._response_json = self.__send_http_request(http_method)
        self._response_json = self._postprocess_response_json()

        return self._response_json

    def _get_cached_response_json(self) -> Any | None:
        return None

    def _build_request_json(self) -> dict[str, Any]:
        access_token, token_type = Token().request_to_api()

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


class Token(SpotifyApiCallBackbone):
    def __init__(self) -> None:
        self.token_cache_file = TokenCacheFile()

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
                'Authorization': f'Basic {ApiCredentials().authorization_credentials}'
            },
            'url': self._url
        }

    def _select_http_method(self) -> Callable[..., Any]:
        return requests.post

    def _postprocess_response_json(self) -> Any:
        access_token = self._response_json['access_token']
        token_type = self._response_json['token_type']

        self.token_cache_file.write(self._response_json)

        return access_token, token_type