from typing import Any

import networkx as nx
from data_scraping.similar_bands_ids_scraper import SimilarBandsIdsScraper
from algorithms.bfs import bfs


def bands_flowchart(source_band_id: int, target_band_id: int) -> list[Any] | dict[Any, list[Any]]:
    G_similar_bands = nx.Graph()
    similar_bands_scraper = SimilarBandsIdsScraper().scrap

    bfs(G_similar_bands, source_band_id, target_band_id, similar_bands_scraper)
    bands_flowchart_ids = nx.dijkstra_path(
        G_similar_bands, source_band_id, target_band_id
    )

    return bands_flowchart_ids
