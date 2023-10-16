from typing import Any, Callable

import networkx as nx


class BidirectionalBFS:
    def __init__(self) -> None:
        self.graph = nx.Graph()
        self.get_neighbors = None

    def explore(self, source_node: Any, target_node: Any, get_neighbors: Callable) -> bool:
        if source_node == target_node:
            return True

        self.get_neighbors = get_neighbors

        forward_pending_nodes = [source_node]
        forward_visited = {source_node}
        backward_pending_nodes = [target_node]
        backward_visited = {target_node}

        while backward_pending_nodes and forward_pending_nodes:
            forward_search_finished = self \
                .__search(forward_pending_nodes, forward_visited, backward_visited)

            if forward_search_finished:
                return True

            backward_search_finished = self \
                .__search(backward_pending_nodes, backward_visited, forward_visited)

            if backward_search_finished:
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
