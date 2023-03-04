from flask import Flask

from .services import band_blueprint, token_blueprint

app = Flask(__name__)

app.register_blueprint(band_blueprint)
app.register_blueprint(token_blueprint)
