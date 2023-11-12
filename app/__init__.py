from flask import Flask

from api_blueprint_scraper import scrap_blueprints_routes


def create_app() -> Flask:
    app = Flask(__name__)

    for blueprint in scrap_blueprints_routes('app/resources'):
        app.register_blueprint(blueprint)

    return app
