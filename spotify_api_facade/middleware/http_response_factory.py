from typing import Any, Dict

from requests import get, post


class HTTP_Response_Factory:
    """
    Sends HTTP requests to a specified URL using any HTTP
    method and handle the JSON response from the server.
    """

    @staticmethod
    def request_to_server(http_method: str, url: str, request_json: Dict[str, Any]) -> Any:
        if http_method == 'get':
            return get(url, **request_json).json()
        elif http_method == 'post':
            return post(url, **request_json).json()
        else:
            return {}
