from flask import Flask

from api.services.albums.albums_services import albums_blueprint
from api.services.flowcharts.flowcharts_services import flowcharts_blueprint

app = Flask(__name__)
app.register_blueprint(albums_blueprint)
app.register_blueprint(flowcharts_blueprint)

if __name__ == '__main__':
    app.run()
