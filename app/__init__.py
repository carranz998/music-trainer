from flask import Flask

from app.configs import identify_resources


def create_app():
    app = Flask(__name__)

    identify_resources(app)

    return app
