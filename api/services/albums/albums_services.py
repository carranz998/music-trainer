import flask

import spotify_api_facade

albums_blueprint = flask.Blueprint('albums', __name__, url_prefix='/albums')


@albums_blueprint.route('/tracks_names')
def retrieve_tracks_names():
    album_id = flask.request.json['album_id']

    album_tracks_names = spotify_api_facade.album_tracks(album_id)

    formatted_data = {
        'album_tracks': album_tracks_names
    }

    return flask.jsonify({'data': formatted_data}), 200
