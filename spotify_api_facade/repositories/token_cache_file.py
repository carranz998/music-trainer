import json
import os
from datetime import datetime, timedelta
from typing import Any, Dict, Tuple


class Token_Cache_File:
    def __init__(self) -> None:
        self.file_uri = os.environ.get('ACCESS_TOKEN_PARAMETERS_PATH')

    def read(self) -> Tuple[str, str] | None:
        if self.__file_exists():
            token_parameters = self.__read_json()
            expiration_date = token_parameters['expiration_date']

            if not self.__is_expired(expiration_date):
                access_token = token_parameters['access_token']
                token_type = token_parameters['token_type']

                return access_token, token_type

        return None

    def write(self, token_parameters: Dict[str, Any]) -> None:
        expires_in = token_parameters['expires_in']
        expiration_date = self.__calculate_expiration_date(expires_in)

        token_parameters['expiration_date'] = expiration_date
        del token_parameters['expires_in']

        self.__write_json(token_parameters)

    def __calculate_expiration_date(self, duration_seconds: int) -> datetime:
        current_date = datetime.now().replace(microsecond=0)
        duration_timedelta = timedelta(seconds=duration_seconds)

        expiration_date = current_date + duration_timedelta

        return expiration_date

    def __file_exists(self) -> bool:
        if self.file_uri is None:
            return False

        return os.path.exists(self.file_uri)

    def __is_expired(self, expiration_date_str: str) -> bool:
        date_format = '%Y-%m-%d %H:%M:%S'
        expiration_date = datetime.strptime(expiration_date_str, date_format)

        is_expired = datetime.now() > expiration_date

        return is_expired

    def __read_json(self) -> Any:
        if self.file_uri is None:
            raise Exception()

        with open(self.file_uri, 'r') as fp:
            return json.load(fp)

    def __write_json(self, data: Dict[str, Any]) -> None:
        if self.file_uri is None:
            raise Exception()

        with open(self.file_uri, 'w') as fp:
            json.dump(data, fp, indent=4, sort_keys=True, default=str)
