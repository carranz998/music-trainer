from flask import Blueprint, jsonify, request

import spotify_api_facade

albums_blueprint = Blueprint('albums', __name__, url_prefix='/albums')


@albums_blueprint.route('/tracks_names')
def retrieve_tracks_names():
    album_id = request.json['album_id']

    tracks_names = list(spotify_api_facade.album_tracks(album_id))

    return jsonify({'data': tracks_names}), 200
