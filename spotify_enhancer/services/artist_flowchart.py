from typing import Any, List

import networkx as nx

from spotify_enhancer.algorithms import (Bidirectional_BFS,
                                         Unexplored_Graph_Shortest_Path)


def generate_artist_flowchart(
    source_spotify_artist_id: str,
    target_spotify_artist_id: str,
    get_neighbors: Any
) -> List[str]:
    """
    Generates a flowchart representing the shortest path between two Spotify artist IDs.
    """

    graph = nx.Graph()
    bidirectional_bfs = Bidirectional_BFS(graph, get_neighbors)

    flowchart: List[str] = Unexplored_Graph_Shortest_Path(bidirectional_bfs) \
        .find_shortest_path(source_spotify_artist_id, target_spotify_artist_id)

    return flowchart
