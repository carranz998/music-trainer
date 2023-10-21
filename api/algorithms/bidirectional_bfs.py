from typing import Any, Callable

import networkx as nx


class Bidirectional_BFS:
    def __init__(self, graph: nx.Graph, get_neighbors: Callable) -> None:
        self.graph = graph
        self.get_neighbors = get_neighbors

    def explore_for_connection(self, source_node: Any, target_node: Any) -> bool:
        if source_node == target_node:
            return True

        forward_pending_nodes = [source_node]
        forward_visited = {source_node}

        backward_pending_nodes = [target_node]
        backward_visited = {target_node}

        while backward_pending_nodes and forward_pending_nodes:
            nodes_are_connected = self \
                .__search(forward_pending_nodes, forward_visited, backward_visited)

            if nodes_are_connected:
                return True

            nodes_are_connected = self \
                .__search(backward_pending_nodes, backward_visited, forward_visited)

            if nodes_are_connected:
                return True

        return False

    def __search(self, pending_nodes: list, visited_set: set, opposite_visited_set: set) -> bool:
        current_node = pending_nodes.pop(0)

        for neighbor_node in self.get_neighbors(current_node):
            if neighbor_node not in visited_set:
                self.graph.add_edge(current_node, neighbor_node)
                visited_set.add(neighbor_node)

                if neighbor_node in opposite_visited_set:
                    return True

                pending_nodes.append(neighbor_node)

        return False
