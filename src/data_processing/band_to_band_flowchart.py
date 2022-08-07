from typing import Any, Iterable

import networkx as nx


class BandToBandFlowchart:
    @classmethod
    def build(cls, G: nx.Graph, source_band_id: int, target_band_id: int) -> Iterable[Any]:
        shortest_path = list(nx.dijkstra_path(G, source_band_id, target_band_id))

        return shortest_path
