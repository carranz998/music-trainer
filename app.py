from flask import Flask

from api.blueprints import albums_blueprint, flowcharts_blueprint
from api.services import album_tracks_names, artist_to_artist

app = Flask(__name__)
app.register_blueprint(albums_blueprint)
app.register_blueprint(flowcharts_blueprint)

if __name__ == '__main__':
    app.run()
