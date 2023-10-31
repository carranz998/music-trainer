from flask import Flask

from spotify_enhancer.blueprints import albums_blueprint, flowcharts_blueprint
from spotify_enhancer.services import album_tracks_names, artist_to_artist

app = Flask(__name__)
app.register_blueprint(albums_blueprint)
app.register_blueprint(flowcharts_blueprint)

if __name__ == '__main__':
    app.run()
