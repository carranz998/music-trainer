from pathlib import Path

from init_configs.api_init import api_init
from init_configs.app_init import app_init
from init_configs.module_init import module_init

if __name__ == "__main__":
    resources_directory_uri = Path('src\\resources')

    app = app_init(__name__)
    module_init(resources_directory_uri)
    api_init(app, resources_directory_uri)

    app.run(port=5000, debug=True)
