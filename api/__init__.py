from flask import Flask

from .services import token_blueprint

app = Flask(__name__)


app.register_blueprint(token_blueprint)
