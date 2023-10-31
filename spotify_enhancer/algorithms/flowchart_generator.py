from typing import Any, Callable

import networkx as nx

from spotify_enhancer.algorithms.bidirectional_bfs import Bidirectional_BFS


def generate_items_flowchart(source_item_id: Any, target_item_id: Any, get_neighbors: Callable):
    graph = __explore_graph(source_item_id, target_item_id, get_neighbors)
    shortest_path = __find_shortest_path(graph, source_item_id, target_item_id)

    return shortest_path


def __explore_graph(source_item_id: Any, target_item_id: Any, get_neighbors: Callable) -> nx.Graph:
    bidirectional_bfs = Bidirectional_BFS(nx.Graph(), get_neighbors)

    nodes_are_connected = bidirectional_bfs \
        .explore_for_connection(source_item_id, target_item_id)

    if not nodes_are_connected:
        raise Exception('nodes are not connected in the graph')

    return bidirectional_bfs.graph


def __find_shortest_path(graph: nx.Graph, source_item_id: Any, target_item_id: Any) -> list[Any]:
    return nx.dijkstra_path(graph, source_item_id, target_item_id)
