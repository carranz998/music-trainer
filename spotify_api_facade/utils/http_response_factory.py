from typing import Any

from requests import get, post


class HTTP_Response_Factory:
    @staticmethod
    def request_to_server(http_method: str, url: str, request_json: dict[str, Any]) -> Any:
        if http_method == 'get':
            return get(url, **request_json).json()
        elif http_method == 'post':
            return post(url, **request_json).json()
        else:
            return {}
