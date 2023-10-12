import flask

albums_blueprint = flask.Blueprint(
    'albums',
    __name__,
    url_prefix='/albums'
)

flowcharts_blueprint = flask.Blueprint(
    'flowcharts',
    __name__,
    url_prefix='/flowcharts'
)
