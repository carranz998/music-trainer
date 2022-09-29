import itertools

import networkx as nx

from data_scraping.band_name_scraper import BandNameScraper
from data_scraping.similar_bands_ids_scraper import SimilarBandsIdsScraper
from gui.widget import Widget
from utils.bfs import bfs
from utils.data_collector import DataCollector

if __name__ == '__main__':
    widget = Widget()

    source_bands_ids = DataCollector().data['source_band_id']
    target_bands_ids = DataCollector().data['target_band_id']

    G_similar_bands = nx.Graph()

    similar_bands_scraper = SimilarBandsIdsScraper().scrap
    band_name_scraper = BandNameScraper().scrap

    for source_band_id, target_band_id in itertools.product(source_bands_ids, target_bands_ids):
        bfs(G_similar_bands, source_band_id, target_band_id, similar_bands_scraper)
        bands_flowchart_ids = nx.dijkstra_path(G_similar_bands, source_band_id, target_band_id)

        bands_flowchart_names = map(band_name_scraper, bands_flowchart_ids)

        print(*bands_flowchart_names, sep=' -> ')
