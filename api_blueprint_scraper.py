import ast
import importlib
import os
from types import FunctionType
from typing import Any, Iterator, List, Tuple

from flask import Blueprint


class HTTP_Resources_Tree:
    def __init__(self, base_directory_path: str) -> None:
        self.__base_directory_path = base_directory_path

    def build(self) -> dict[str, List[FunctionType]]:
        scheme: dict[str, List[FunctionType]] = dict()

        for file in self.__yield_python_files():
            leaf_directory_name = self.__extract_last_directory(file)
            scheme[leaf_directory_name] = []

            for f in self.__extract_public_functions(file):
                file = file.replace('/', '.')
                file = os.path.splitext(file)[0]

                function = self.__import_function(file, f)

                scheme[leaf_directory_name].append(function)

        return scheme

    def __import_function(self, module_name: str, function_name: str) -> Any:
        module = importlib.import_module(module_name)
        function = getattr(module, function_name)

        return function

    def __yield_python_files(self) -> Iterator[str]:
        for root, _, files in os.walk(self.__base_directory_path):
            for file in files:
                if not file.startswith('_') and file.endswith('.py'):
                    yield os.path.join(root, file)

    def __extract_public_functions(self, file_path: str) -> Iterator[str]:
        with open(file_path, 'r') as file:
            tree = ast.parse(file.read())

        for node in ast.walk(tree):
            if isinstance(node, ast.FunctionDef):
                if not node.name.startswith('_'):
                    yield node.name

    def __extract_last_directory(self, path: str) -> str:
        path_components = path.split(os.path.sep)
        last_directory = path_components[-2]

        return last_directory


def __create_blueprint(url_prefix: str) -> Blueprint:
    return Blueprint(url_prefix, __name__, url_prefix=f'/{url_prefix}')


def __create_url_rule_config(view_func: FunctionType) -> Tuple[str, str, FunctionType]:
    rule = f'/{view_func.__name__}'
    endpoint = f'{view_func.__name__}'
    return rule, endpoint, view_func


def scrap_blueprints_routes(base_directory_path: str) -> Iterator[Blueprint]:
    scheme = HTTP_Resources_Tree(base_directory_path).build()

    for url_prefix, services in scheme.items():
        blueprint = __create_blueprint(url_prefix)

        for service in services:
            rule, endpoint, view_func = __create_url_rule_config(service)
            blueprint.add_url_rule(rule, endpoint, view_func)

        yield blueprint
