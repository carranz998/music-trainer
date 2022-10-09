from pathlib import Path
from typing import Iterator

from utils.camel_case import camel_case
from utils.module import Module


class ApiEndpoints:
    @classmethod
    def iterate(cls, endpoints_module_uri: Path) -> Iterator[str]:
        return map(cls.__convert_to_endpoint, Module.file_iterator(endpoints_module_uri))

    @classmethod
    def __convert_to_endpoint(cls, filename: str) -> str:
        return f'/{camel_case(filename)}'
