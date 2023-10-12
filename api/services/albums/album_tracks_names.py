import flask

from api.blueprints import albums_blueprint
from api.spotify_api_facade import AlbumTracksNames


@albums_blueprint.route('/tracks_names')
def album_tracks_names():
    album_id = flask.request.json['album_id']

    album_tracks_names = AlbumTracksNames(album_id).request_to_spotify_api()

    formatted_data = {
        'album_tracks_names': list(album_tracks_names)
    }

    return flask.jsonify(formatted_data), 200
