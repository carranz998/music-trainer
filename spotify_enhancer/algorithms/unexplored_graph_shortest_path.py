from typing import Any, List

import networkx as nx

from spotify_enhancer.algorithms.graph_exploration_algorithm import \
    Graph_Exploration_Algorithm


class Unexplored_Graph_Shortest_Path:
    def __init__(self, graph_exploration_algorithm: Graph_Exploration_Algorithm) -> None:
        """
        Parameters:
            graph_exploration_algorithm (Graph_Exploration_Algorithm):
                The graph exploration algorithm to be used for checking connections in the graph.
        """

        self.graph_exploration_algorithm = graph_exploration_algorithm

    def find_shortest_path(self, source_item_id: Any, target_item_id: Any) -> List[Any]:
        """
        Finds the shortest path between the source and target nodes in the graph.
        """

        nodes_are_connected = self.graph_exploration_algorithm \
            .check_connection_between_nodes(source_item_id, target_item_id)

        if not nodes_are_connected:
            return []

        graph = self.graph_exploration_algorithm.graph

        shortest_path: List[Any] = nx \
            .dijkstra_path(graph, source_item_id, target_item_id)

        return shortest_path
