from flask_restful import Resource


class BandsCluster(Resource):
    def get(self):
        return {'band': 'cluster'}