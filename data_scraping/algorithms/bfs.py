from typing import Any, Callable

import networkx as nx


def bfs(G: nx.Graph, source_node: Any, target_node: Any, get_neighbors: Callable) -> None:
    G.add_node(source_node)
    pending_nodes = [source_node]

    while pending_nodes:
        current_node = pending_nodes.pop(0)

        for neighbor_node in get_neighbors(current_node):
            if neighbor_node not in G.nodes:
                G.add_edge(current_node, neighbor_node)

                if neighbor_node == target_node:
                    pending_nodes = []
                    break
                else:
                    pending_nodes.append(neighbor_node)
