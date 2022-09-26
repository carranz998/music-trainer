import time

import networkx as nx

from data_scraping.band_name import BandName
from data_scraping.similar_bands_ids import SimilarBandsIds
from gui.widget import Widget
from gui.widget_data import WidgetData
from utils.bfs import bfs

if __name__ == '__main__':
    widget = Widget()
    source_band_id, target_band_id = WidgetData().source_band_id, WidgetData().target_band_id

    G_similar_bands = nx.Graph()

    bfs(G_similar_bands, source_band_id, target_band_id, SimilarBandsIds.gather)
    bands_flowchart_ids = nx.dijkstra_path(G_similar_bands, source_band_id, target_band_id)

    bands_flowchart_names = map(BandName.gather, bands_flowchart_ids)

    print(*bands_flowchart_names, sep=' -> ')

    widget = Widget()
    source_band_id, target_band_id = WidgetData().source_band_id, WidgetData().target_band_id

    bfs(G_similar_bands, source_band_id, target_band_id, SimilarBandsIds.gather)
    bands_flowchart_ids = nx.dijkstra_path(G_similar_bands, source_band_id, target_band_id)

    bands_flowchart_names = map(BandName.gather, bands_flowchart_ids)

    print(*bands_flowchart_names, sep=' -> ')
