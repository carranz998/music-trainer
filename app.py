from flask import Flask
from api.services.albums.album_tracks import albums_blueprint

app = Flask(__name__)
app.register_blueprint(albums_blueprint)

if __name__ == '__main__':
    app.run()
