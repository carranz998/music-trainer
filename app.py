from flask import Flask
from api.services.albums.albums_services import albums_blueprint

app = Flask(__name__)
app.register_blueprint(albums_blueprint)

if __name__ == '__main__':
    app.run()
