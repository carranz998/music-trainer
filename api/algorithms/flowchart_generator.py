from typing import Any, Callable

import networkx as nx

from api.algorithms.bidirectional_bfs import BidirectionalBFS


def generate_items_flowchart(source_item_id: Any, target_item_id: Any, get_neighbors: Callable):
    graph = __explore_graph(source_item_id, target_item_id, get_neighbors)
    shortest_path = __find_shortest_path(graph, source_item_id, target_item_id)

    return shortest_path


def __explore_graph(source_item_id: Any, target_item_id: Any, get_neighbors: Callable) -> nx.Graph:
    bidirectional_bfs = BidirectionalBFS()

    bidirectional_bfs \
        .explore(source_item_id, target_item_id, get_neighbors)

    return bidirectional_bfs.graph


def __find_shortest_path(graph: nx.Graph, source_item_id: Any, target_item_id: Any) -> list[Any]:
    return nx.dijkstra_path(graph, source_item_id, target_item_id)
