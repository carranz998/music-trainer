from typing import Any, Callable


def build_authorization_options(url: str, access_token: str, token_type: str) -> dict[str, Any]:
    return {
        'url': url,
        'headers': {
            'Authorization': f'{token_type} {access_token}'
        }
    }


def send_http_request(requests_method: Callable, options: dict[str, Any]) -> dict[str, Any]:
    return requests_method(**options).json()
