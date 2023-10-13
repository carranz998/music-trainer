from abc import ABC, abstractmethod
from typing import Any, Callable

import requests

from api.spotify_api_facade.utils.credentials import (
    access_token_parameters_uri, authorization_credentials)
from api.spotify_api_facade.utils.file_management import (file_exists,
                                                          is_expired,
                                                          read_json, save)


class SpotifyApiCallBackbone(ABC):
    def __init__(self) -> None:
        self._url = None
        self._request_json = None
        self._response_json = None

    def request_to_spotify_api(self) -> None:
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

    def _get_cached_response_json(self):
        return None

    def _build_request_json(self) -> dict[str, Any]:
        access_token, token_type = Token().request_to_spotify_api()

        return {
            'url': self._url,
            'headers': {
                'Authorization': f'{token_type} {access_token}'
            }
        }

    def __send_http_request(self, requests_method: Callable) -> dict[str, Any]:
        return requests_method(**self._request_json).json()

    def _postprocess_request_json(self) -> dict[str, Any]:
        return self._request_json

    def _postprocess_response_json(self) -> dict[str, Any]:
        return self._response_json

    @abstractmethod
    def _build_url(self) -> str:
        pass

    @abstractmethod
    def _select_http_method(self) -> Callable:
        pass


class Token(SpotifyApiCallBackbone):
    def _build_url(self):
        return 'https://accounts.spotify.com/api/token'

    def _get_cached_response_json(self):
        if file_exists(access_token_parameters_uri):
            access_token_parameters = read_json(access_token_parameters_uri)
            access_token = access_token_parameters['access_token']
            expiration_date = access_token_parameters['expiration_date']
            token_type = access_token_parameters['token_type']

            if not is_expired(expiration_date):
                print('cached')
                return access_token, token_type
        print('not cached')
        return None

    def _build_request_json(self):
        return {
            'url': self._url,
            'headers': {
                'Authorization': f'Basic {authorization_credentials}'
            },
            'data': {
                'grant_type': 'client_credentials'
            }
        }

    def _select_http_method(self) -> Callable[..., Any]:
        return requests.post

    def _postprocess_response_json(self):
        access_token = self._response_json['access_token']
        token_type = self._response_json['token_type']

        save(self._response_json)

        return access_token, token_type
