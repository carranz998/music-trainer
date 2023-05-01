import flask

import spotify_api_facade
from ...utils.algorithms.flowchart_generator import generate_items_flowchart

flowcharts_blueprint = flask.Blueprint(
    'flowcharts',
    __name__,
    url_prefix='/flowcharts'
)


@flowcharts_blueprint.route('/artist_to_artist')
def generate_flowchart():
    source_artist_id = flask.request.json['source_artist_id']
    target_artist_id = flask.request.json['target_artist_id']

    similar_artists_gather = spotify_api_facade \
        .retrieve_similar_artists_uri

    artists_uri_flowchart = generate_items_flowchart(
        source_artist_id,
        target_artist_id,
        similar_artists_gather
    )

    formatted_data = {
        'flowchart': artists_uri_flowchart
    }

    output_json = flask.jsonify(formatted_data), 200

    return output_json
