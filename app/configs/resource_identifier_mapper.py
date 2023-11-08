from types import FunctionType
from typing import Tuple

from flask import Blueprint, Flask

from app.resources import artist_to_artist, tracks_names


def __create_blueprint(url_prefix: str) -> Blueprint:
    return Blueprint(url_prefix, __name__, url_prefix=f'/{url_prefix}')


def __create_url_rule_config(view_func: FunctionType) -> Tuple[str, str, FunctionType]:
    rule = f'/{view_func.__name__}'
    endpoint = f'{view_func.__name__}'
    return rule, endpoint, view_func


services_per_url_prefix = {
    'albums': [tracks_names],
    'flowcharts': [artist_to_artist]
}


def identify_resources(app: Flask) -> None:
    for url_prefix, services in services_per_url_prefix.items():
        blueprint = __create_blueprint(url_prefix)

        for service in services:
            rule, endpoint, view_func = __create_url_rule_config(service)
            blueprint.add_url_rule(rule, endpoint, view_func)

        app.register_blueprint(blueprint)
