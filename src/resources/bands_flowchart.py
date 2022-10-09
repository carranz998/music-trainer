from flask_restful import Resource


class BandsFlowchart(Resource):
    def get(self):
        return {'band': 'flowchart'}
            