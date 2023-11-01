import flask

from api.services import album_tracks_names, artist_to_artist

app = flask.Flask(__name__)

albums_blueprint = flask.Blueprint(
    'albums', __name__, url_prefix='/albums'
)

flowcharts_blueprint = flask.Blueprint(
    'flowcharts', __name__, url_prefix='/flowcharts'
)

albums_blueprint.add_url_rule(
    '/album_tracks_names', 'album_tracks_names', album_tracks_names
)

flowcharts_blueprint.add_url_rule(
    '/artist_to_artist', 'artist_to_artist', artist_to_artist
)

app.register_blueprint(albums_blueprint)
app.register_blueprint(flowcharts_blueprint)

if __name__ == '__main__':
    app.run()
