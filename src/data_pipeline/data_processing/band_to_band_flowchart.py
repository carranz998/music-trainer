from typing import Any, Iterable

import networkx as nx


class BandToBandFlowchart:
    @classmethod
    def build(cls, G_similar_bands: nx.Graph, source_band_id: int, target_band_id: int) -> Iterable[Any]:
        shortest_path = nx.dijkstra_path(G_similar_bands, source_band_id, target_band_id)

        return shortest_path
