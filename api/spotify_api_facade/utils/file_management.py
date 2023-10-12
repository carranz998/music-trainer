import json
import os
from typing import Any


def create_empty_json(uri: str) -> None:
    open(uri, 'w').close()


def file_exists(uri: str) -> bool:
    return os.path.exists(uri)


def read_json(uri: str) -> dict[str, Any]:
    with open(uri, 'r') as fp:
        return json.load(fp)


def write_in_json(uri: str, data: dict[str, Any]) -> None:
    with open(uri, 'w') as fp:
        json.dump(data, fp, indent=4, sort_keys=True, default=str)
