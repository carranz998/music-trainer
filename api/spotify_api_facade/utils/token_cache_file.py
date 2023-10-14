import json
import os
from datetime import datetime, timedelta
from typing import Any


class TokenCacheFile:
    def __init__(self) -> None:
        current_file_path = os.path.abspath(__file__)
        directory_name = os.path.dirname(current_file_path)
        file_name = 'access_token_parameters.json'

        self.file_uri = os.path.join(directory_name, file_name)

    def read(self) -> tuple[str, str] | None:
        if self.__file_exists():
            token_parameters = self.__read_json()
            expiration_date = token_parameters['expiration_date']

            if not self.__is_expired(expiration_date):
                access_token = token_parameters['access_token']
                token_type = token_parameters['token_type']

                return access_token, token_type

        return None

    def write(self, token_parameters: dict[str, Any]) -> None:
        expires_in = token_parameters['expires_in']
        expiration_date = self.__calculate_expiration_date(expires_in)

        token_parameters['expiration_date'] = expiration_date
        del token_parameters['expires_in']

        self.__write_json(token_parameters)

    def __calculate_expiration_date(self, duration_seconds: int) -> datetime:
        current_date = datetime.now().replace(microsecond=0)
        duration_seconds = timedelta(seconds=duration_seconds)

        expiration_date = current_date + duration_seconds

        return expiration_date

    def __file_exists(self) -> bool:
        return os.path.exists(self.file_uri)

    def __is_expired(self, expiration_date: str) -> bool:
        expiration_date = datetime.strptime(
            expiration_date, '%Y-%m-%d %H:%M:%S'
        )

        is_expired = datetime.now() > expiration_date

        return is_expired

    def __read_json(self) -> dict[str, Any]:
        with open(self.file_uri, 'r') as fp:
            return json.load(fp)

    def __write_json(self, data: dict[str, Any]) -> None:
        with open(self.file_uri, 'w') as fp:
            json.dump(data, fp, indent=4, sort_keys=True, default=str)
