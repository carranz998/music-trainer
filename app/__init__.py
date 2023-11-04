from flask import Flask

from app.configs import identify_resources


def create_app() -> Flask:
    app = Flask(__name__)
    identify_resources(app)

    return app
