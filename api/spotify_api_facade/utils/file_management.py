import json
import os
from datetime import datetime, timedelta
from typing import Any

from api.spotify_api_facade.utils.credentials import \
    access_token_parameters_uri


def calculate_expiration_date(duration_seconds: int) -> datetime:
    current_date = datetime.now().replace(microsecond=0)
    duration_seconds = timedelta(seconds=duration_seconds)

    expiration_date = current_date + duration_seconds

    return expiration_date


def save(access_token_parameters: dict[str, Any]) -> None:
    expires_in = access_token_parameters['expires_in']
    expiration_date = calculate_expiration_date(expires_in)
    access_token_parameters['expiration_date'] = expiration_date

    del access_token_parameters['expires_in']

    write_in_json(access_token_parameters_uri, access_token_parameters)


def read_json(uri: str) -> dict[str, Any]:
    with open(uri, 'r') as fp:
        return json.load(fp)


def file_exists(uri: str) -> bool:
    return os.path.exists(uri)


def write_in_json(uri: str, data: dict[str, Any]) -> None:
    with open(uri, 'w') as fp:
        json.dump(data, fp, indent=4, sort_keys=True, default=str)


def is_expired(expiration_date: str) -> bool:
    expiration_date = datetime.strptime(expiration_date, '%Y-%m-%d %H:%M:%S')
    is_expired = datetime.now() > expiration_date

    return is_expired
