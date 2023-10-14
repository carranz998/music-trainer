from functools import wraps
from typing import Any

import flask


def __request_is_json() -> tuple[flask.Response, int] | None:
    if not flask.request.is_json:
        return flask.jsonify({'error': 'Invalid JSON'}), 400

    return None


def __validate_json_data(types_dict: dict[str, Any], json_data: dict[str, Any]) -> tuple[flask.Response, int] | None:
    for key, expected_type in types_dict.items():
        if key not in json_data:
            return flask.jsonify({'error': f'Missing key {key} of type {expected_type}'}), 400

        if not isinstance(json_data[key], expected_type):
            return flask.jsonify({'error': f'Key {key} must be a {expected_type}'}), 400

    return None


def request_json_validator(types_dict: dict[str, Any]) -> tuple[flask.Response, int] | None:
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            error_response = __request_is_json()
            if error_response:
                return error_response

            json_data = flask.request.get_json()

            error_response = __validate_json_data(types_dict, json_data)
            if error_response:
                return error_response

            return func(*args, **json_data, **kwargs)

        return wrapper

    return decorator
