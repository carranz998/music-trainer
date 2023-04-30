from datetime import datetime, timedelta
from typing import Any

import requests

from ...utils.file_management import file_exists, read_json, write_in_json
from . import access_token_parameters_uri, authorization_credentials


def retrieve_access_token() -> dict[str, Any]:
    if file_exists(access_token_parameters_uri):
        access_token_parameters = read_json(access_token_parameters_uri)
        access_token = access_token_parameters['access_token']
        expiration_date = access_token_parameters['expiration_date']
        token_type = access_token_parameters['token_type']

        if not __is_expired(expiration_date):
            return access_token, token_type

    access_token_parameters = __request_to_server()
    __save(access_token_parameters)

    access_token = access_token_parameters['access_token']
    token_type = access_token_parameters['token_type']

    return access_token, token_type


def __request_to_server() -> dict[str, Any]:
    authorization_options = {
        'url': 'https://accounts.spotify.com/api/token',
        'headers': {
            'Authorization': 'Basic ' + authorization_credentials
        },
        'form': {
            'grant_type': 'client_credentials'
        }
    }

    response = requests.post(
        url=authorization_options['url'],
        headers=authorization_options['headers'],
        data=authorization_options['form']
    )

    return response.json()


def __is_expired(expiration_date: str) -> bool:
    expiration_date = datetime.strptime(expiration_date, '%Y-%m-%d %H:%M:%S')
    is_expired = datetime.now() > expiration_date

    return is_expired


def __calculate_expiration_date(duration_seconds: int) -> datetime:
    current_date = datetime.now().replace(microsecond=0)
    duration_seconds = timedelta(seconds=duration_seconds)

    expiration_date = current_date + duration_seconds

    return expiration_date


def __save(access_token_parameters: dict[str, Any]) -> None:
    expires_in = access_token_parameters['expires_in']
    expiration_date = __calculate_expiration_date(expires_in)
    access_token_parameters['expiration_date'] = expiration_date

    del access_token_parameters['expires_in']

    write_in_json(access_token_parameters_uri, access_token_parameters)
