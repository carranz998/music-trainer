from abc import ABC, abstractmethod
from types import FunctionType
from typing import Any

import networkx as nx


class Graph_Exploration_Algorithm(ABC):
    def __init__(self, graph: nx.Graph, get_neighbors: FunctionType) -> None:
        """
        Attributes:
            graph (nx.Graph): The graph on which the algorithm operates.
            get_neighbors (FunctionType): A function that takes a node as input and returns its neighbors.
        """

        self.graph = graph
        self.get_neighbors = get_neighbors

    @abstractmethod
    def check_connection_between_nodes(self, source_node: Any, target_node: Any) -> bool:
        """
        Checks whether there is a connection between the source and target nodes in the graph.
        """

        pass
