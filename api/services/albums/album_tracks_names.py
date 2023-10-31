import flask

from api.blueprints import albums_blueprint
from api.decorators import request_json_validator
from api.spotify_api_facade import Album_Tracks_Names


@albums_blueprint.route('/album_tracks_names')
@request_json_validator({
    'spotify_album_id': str
})
def album_tracks_names(spotify_album_id: str) -> tuple[flask.Response, int]:
    album_tracks_names = Album_Tracks_Names(spotify_album_id)

    try:
        spotify_api_response = album_tracks_names.request_to_spotify_api()

    except KeyError:
        return flask.jsonify({'error': 'there is no album in spotify with that id'}), 400

    return flask.jsonify({'album_tracks_names': spotify_api_response}), 200
