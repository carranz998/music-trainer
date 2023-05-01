from typing import Any, Callable

import networkx as nx

from .bfs import bfs


def generate_items_flowchart(source_item_id: Any, target_item_id: Any, similar_items_gather: Callable):
    G_similar_items = nx.Graph()

    bfs(G_similar_items, source_item_id, target_item_id, similar_items_gather)
    items_flowchart = nx.dijkstra_path(
        G_similar_items, source_item_id, target_item_id
    )

    return items_flowchart
    