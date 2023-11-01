from typing import Any

import flask

from api.services import album_tracks_names, artist_to_artist


def __create_url_rule_config(view_func: Any) -> tuple[str, str, Any]:
    rule = f'/{view_func.__name__}'
    endpoint = f'{view_func.__name__}'

    return rule, endpoint, view_func


def __create_blueprint_configs(url_prefix_name: str) -> dict[str, str]:
    return {
        'name': url_prefix_name,
        'import_name': __name__,
        'url_prefix': f'/{url_prefix_name}'
    }


app = flask.Flask(__name__)

services_per_url_prefix = {
    'albums': [album_tracks_names],
    'flowcharts': [artist_to_artist]
}

for url_prefix, services in services_per_url_prefix.items():
    blueprint_configs = __create_blueprint_configs(url_prefix)
    blueprint = flask.Blueprint(**blueprint_configs)

    for service in services:
        rule, endpoint, view_func = __create_url_rule_config(service)
        blueprint.add_url_rule(rule, endpoint, view_func)

    app.register_blueprint(blueprint)


if __name__ == '__main__':
    app.run()
