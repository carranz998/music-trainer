from flask import request

from data_scraping.bands_flowchart import scrap_bands_flowchart

from . import discover_bp


@discover_bp.route('/bands_flowchart')
def bands_flowchart():
    response = request.get_json()
    if not response:
        return {
            'data': [],
            'code': 400
        }

    source_band_id = response['source_band_id']
    target_band_id = response['target_band_id']

    bands_flowchart_ids = scrap_bands_flowchart(source_band_id, target_band_id)
    
    return {
        'data': bands_flowchart_ids,
        'code': 200
    }
