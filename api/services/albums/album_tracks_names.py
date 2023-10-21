import flask

from api.blueprints import albums_blueprint
from api.decorators import request_json_validator
from api.spotify_api_facade import Album_Tracks_Names


@albums_blueprint.route('/tracks_names')
@request_json_validator({
    'album_id': str
})
def album_tracks_names(album_id: str) -> tuple[flask.Response, int]:
    album_tracks_names = Album_Tracks_Names(album_id).request_to_api()
    formatted_data = {'album_tracks_names': album_tracks_names}

    return flask.jsonify(formatted_data), 200
