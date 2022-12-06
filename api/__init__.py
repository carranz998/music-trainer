from flask import Flask

from api.functionalities.discover import discover_bp

app = Flask(__name__)

app.register_blueprint(discover_bp)
