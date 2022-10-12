from algorithms.bands_flowchart import bands_flowchart
from flask import request
from flask_restful import Resource


class BandsFlowchart(Resource):
    def get(self):
        response = request.get_json()
        if not response:
            return {
                'data': [],
                'code': 400
            }

        source_band_id = response['source_band_id']
        target_band_id = response['target_band_id']

        bands_flowchart_ids = bands_flowchart(source_band_id, target_band_id)
        
        return {
            'data': bands_flowchart_ids,
            'code': 200
        }
