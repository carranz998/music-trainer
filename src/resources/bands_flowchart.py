import networkx as nx
from data_scraping.similar_bands_ids_scraper import SimilarBandsIdsScraper
from flask import request
from flask_restful import Resource
from utils.bfs import bfs


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

        G_similar_bands = nx.Graph()
        similar_bands_scraper = SimilarBandsIdsScraper().scrap

        bfs(G_similar_bands, source_band_id, target_band_id, similar_bands_scraper)
        bands_flowchart_ids = nx.dijkstra_path(
            G_similar_bands, source_band_id, target_band_id
        )
        
        return {
            'data': bands_flowchart_ids,
            'code': 200
        }
