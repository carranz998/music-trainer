from pathlib import Path

from flask import Flask
from flask_restful import Api

from app_components.api_endpoints import ApiEndpoints
from app_components.api_resources import ApiResources

if __name__ == "__main__":
    app = Flask(__name__)
    api = Api(app)

    resources_uri = Path('src\\resources')
    module_name = resources_uri.stem

    for endpoint_name in ApiEndpoints.iterate(resources_uri):
        ApiResources.add(api, module_name, endpoint_name)

    app.run(port=5000, debug=True)
