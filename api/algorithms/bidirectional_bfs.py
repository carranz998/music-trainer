from typing import Any, Callable

import networkx as nx


class BidirectionalBFS:
    def __init__(self) -> None:
        self.G = nx.Graph()

        self.forward_pending_nodes = list()
        self.forward_visited = set()
        self.forward_parents = dict()

        self.backward_pending_nodes = list()
        self.backward_visited = set()
        self.backward_parents = dict()

        self.get_neighbors = None

    def search(self, source_node: Any, target_node: Any, get_neighbors: Callable):
        if source_node == target_node:
            return [source_node]

        self.get_neighbors = get_neighbors
        self.__init_pivots(source_node, target_node)

        while self.backward_pending_nodes and self.forward_pending_nodes:
            path = self.__forward_search()
            if path:
                return path

            path = self.__backward_search()
            if path:
                return path

    def __forward_search(self):
        forward_current_node = self.forward_pending_nodes.pop(0)
        for neighbor_node in self.get_neighbors(forward_current_node):
            if neighbor_node not in self.forward_visited:
                self.G.add_edge(forward_current_node, neighbor_node)
                self.forward_visited.add(neighbor_node)
                self.forward_parents[neighbor_node] = forward_current_node

                if neighbor_node in self.backward_visited:
                    return self.__create_path(neighbor_node)

                self.forward_pending_nodes.append(neighbor_node)

        return []

    def __backward_search(self):
        backward_current_node = self.backward_pending_nodes.pop(0)
        for neighbor_node in self.get_neighbors(backward_current_node):
            if neighbor_node not in self.backward_visited:
                self.G.add_edge(backward_current_node, neighbor_node)
                self.backward_visited.add(neighbor_node)
                self.backward_parents[neighbor_node] = backward_current_node

                if neighbor_node in self.forward_visited:
                    return self.__create_path(neighbor_node)

                self.backward_pending_nodes.append(neighbor_node)

        return []

    def __init_pivots(self, source_node: Any, target_node: Any):
        self.forward_pending_nodes = [source_node]
        self.forward_visited = {source_node}
        self.forward_parents = {source_node: None}

        self.backward_pending_nodes = [target_node]
        self.backward_visited = {target_node}
        self.backward_parents = {target_node: None}

    def __create_path(self, neighbor_node):
        meeting_node = neighbor_node

        forward_path = self.__reconstruct_path(
            self.forward_parents, meeting_node)
        backward_path = self.__reconstruct_path(
            self.backward_parents, meeting_node, reverse=True
        )

        return forward_path + backward_path

    def __reconstruct_path(self, parents, meeting_node, reverse=False):
        path = []
        current_node = meeting_node

        while current_node is not None:
            path.append(current_node)
            current_node = parents[current_node]

        return path[::-1] if reverse else path
