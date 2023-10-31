import flask

from spotify_api_facade.services import get_album_tracks_names
from spotify_enhancer.blueprints import albums_blueprint
from spotify_enhancer.decorators import request_json_validator


@albums_blueprint.route('/album_tracks_names')
@request_json_validator({
    'spotify_album_id': str
})
def album_tracks_names(spotify_album_id: str) -> tuple[flask.Response, int]:
    try:
        album_tracks_names = get_album_tracks_names(spotify_album_id)

    except KeyError:
        return flask.jsonify({'error': 'there is no album in spotify with that id'}), 400

    return flask.jsonify({'album_tracks_names': album_tracks_names}), 200
