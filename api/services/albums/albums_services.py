import flask

import spotify_api_facade

albums_blueprint = flask.Blueprint(
    'albums',
    __name__,
    url_prefix='/albums'
)


@albums_blueprint.route('/tracks_names')
def retrieve_album_tracks_names():
    album_id = flask.request.json['album_id']

    album_tracks_names = spotify_api_facade \
        .retrieve_album_tracks_names(album_id)

    formatted_data = {
        'album_tracks_names': list(album_tracks_names)
    }

    output_json = flask.jsonify(formatted_data), 200

    return output_json
