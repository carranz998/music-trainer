from abc import ABC, abstractmethod
from typing import Any, Callable

from api.spotify_api_facade.services.tokens.tokens_services import \
    get_access_token


class SpotifyApiCallBackbone(ABC):
    def __init__(self) -> None:
        self._url = None
        self._request_json = None
        self._response_json = None

    def request_to_spotify_api(self) -> None:
        self._url = self._build_url()
        http_method = self._select_http_method()

        self._request_json = self.__build_request_json()
        self._request_json = self._postprocess_request_json()

        self._response_json = self.__send_http_request(http_method)
        self._response_json = self._postprocess_response_json()

        return self._response_json

    def __build_request_json(self) -> dict[str, Any]:
        access_token, token_type = get_access_token()

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
