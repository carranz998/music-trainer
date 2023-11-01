from functools import wraps
from typing import Any

import flask


def __request_is_json() -> None:
    if not flask.request.is_json:
        raise Exception('Invalid JSON')


def __validate_json_data(types_dict: dict[str, Any], json_data: dict[str, Any]) -> None:
    for key, expected_type in types_dict.items():
        if key not in json_data:
            raise Exception(f'Missing key {key} of type {expected_type}')

        if not isinstance(json_data[key], expected_type):
            raise Exception(f'Key {key} must be a {expected_type}')


def request_json_validator(types_dict: dict[str, Any]) -> tuple[flask.Response, int] | None:
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            try:
                __request_is_json()
                json_data = flask.request.get_json()
                __validate_json_data(types_dict, json_data)

            except Exception as exception:
                return flask.jsonify(str(exception)), 400

            return func(*args, **json_data, **kwargs)

        return wrapper

    return decorator
