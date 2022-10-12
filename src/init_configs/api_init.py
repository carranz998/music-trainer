from pathlib import Path

from flask import Flask
from flask_restful import Api

from init_configs.api_components.api_endpoints import ApiEndpoints
from init_configs.api_components.api_resources import ApiResources


def api_init(app: Flask, resources_directory_uri: Path) -> None:
    resources_module_name = resources_directory_uri.stem
    api = Api(app)

    for endpoint_name in ApiEndpoints.iterate(resources_directory_uri):
        resource_object = ApiResources.instantiate(resources_module_name, endpoint_name)
        api.add_resource(resource_object, endpoint_name)
    