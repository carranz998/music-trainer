from functools import wraps
from typing import Any, Dict, List

from flask import request


class Request_Json_Validator:
    def __init__(self, types_dict: Dict[str, Any]) -> None:
        self.types_dict = types_dict

    def __call__(self, func: Any) -> Any:
        @wraps(func)
        def wrapper(*args: List[Any], **kwargs: Dict[str, Any]) -> Any:
            self.__request_is_json()
            json_data: Any = request.get_json()
            self.__validate_json_data(self.types_dict, json_data)

            return func(*args, **json_data, **kwargs)

        return wrapper

    @staticmethod
    def __request_is_json() -> None:
        if not request.is_json:
            raise Exception('Invalid JSON')

    @staticmethod
    def __validate_json_data(types_dict: Dict[str, Any], json_data: Dict[str, Any]) -> None:
        for key, expected_type in types_dict.items():
            if key not in json_data:
                raise Exception(f'Missing key {key} of type {expected_type}')

            if not isinstance(json_data[key], expected_type):
                raise Exception(f'Key {key} must be a {expected_type}')
