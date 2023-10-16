from typing import Any, Callable

import networkx as nx


class BidirectionalBFS:
    def __init__(self) -> None:
        self.graph = nx.Graph()

        self.forward_pending_nodes = list()
        self.forward_visited = set()

        self.backward_pending_nodes = list()
        self.backward_visited = set()

        self.get_neighbors = None

    def __init_pivots(self, source_node: Any, target_node: Any) -> None:
        self.forward_pending_nodes = [source_node]
        self.forward_visited = {source_node}

        self.backward_pending_nodes = [target_node]
        self.backward_visited = {target_node}

    def explore(self, source_node: Any, target_node: Any, get_neighbors: Callable) -> bool:
        if source_node == target_node:
            return True

        self.get_neighbors = get_neighbors
        self.__init_pivots(source_node, target_node)

        while self.backward_pending_nodes and self.forward_pending_nodes:
            forward_search_finished = self.__forward_search()
            if forward_search_finished:
                return True

            backward_search_finished = self.__backward_search()
            if backward_search_finished:
                return True

        return False

    def __forward_search(self) -> bool:
        forward_current_node = self.forward_pending_nodes.pop(0)

        for neighbor_node in self.get_neighbors(forward_current_node):
            if neighbor_node not in self.forward_visited:

                self.graph.add_edge(forward_current_node, neighbor_node)
                self.forward_visited.add(neighbor_node)

                if neighbor_node in self.backward_visited:
                    return True

                self.forward_pending_nodes.append(neighbor_node)

        return False

    def __backward_search(self) -> bool:
        backward_current_node = self.backward_pending_nodes.pop(0)

        for neighbor_node in self.get_neighbors(backward_current_node):
            if neighbor_node not in self.backward_visited:

                self.graph.add_edge(backward_current_node, neighbor_node)
                self.backward_visited.add(neighbor_node)

                if neighbor_node in self.forward_visited:
                    return True

                self.backward_pending_nodes.append(neighbor_node)

        return False
