from typing import Any

import flask


class Blueprint_Manager:
    def __init__(self, app: flask.Flask, services_per_url_prefix: dict[str, list]) -> None:
        self.app = app
        self.services_per_url_prefix = services_per_url_prefix

    def __create_url_rule_config(self, view_func: Any) -> tuple[str, str, Any]:
        rule = f'/{view_func.__name__}'
        endpoint = f'{view_func.__name__}'
        return rule, endpoint, view_func

    def __create_blueprint_configs(self, url_prefix_name: str) -> dict[str, str]:
        return {
            'name': url_prefix_name,
            'import_name': __name__,
            'url_prefix': f'/{url_prefix_name}'
        }

    def register_blueprints(self):
        for url_prefix, services in self.services_per_url_prefix.items():
            blueprint_configs = self.__create_blueprint_configs(url_prefix)
            blueprint = flask.Blueprint(**blueprint_configs)

            for service in services:
                rule, endpoint, view_func = self \
                    .__create_url_rule_config(service)
                blueprint.add_url_rule(rule, endpoint, view_func)

            self.app.register_blueprint(blueprint)
