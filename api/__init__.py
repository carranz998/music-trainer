from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

from .services import token_blueprint

app = Flask(__name__)


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
db.init_app(app)

with app.app_context():
    db.create_all()

app.register_blueprint(token_blueprint)
