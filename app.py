import flask

from api.services import album_tracks_names, artist_to_artist
from blueprint_manager import Blueprint_Manager

app = flask.Flask(__name__)

services_per_url_prefix = {
    'albums': [album_tracks_names],
    'flowcharts': [artist_to_artist]
}

blueprint_manager = Blueprint_Manager(app, services_per_url_prefix)
blueprint_manager.register_blueprints()


if __name__ == '__main__':
    app.run()
