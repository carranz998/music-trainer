from typing import Any, Iterable

import networkx as nx
from data_gathering.similar_bands import SimilarBands


class BandsFlowchart:
	@classmethod
	def generate_flowchart(cls, source_band_id: int, target_band_id: int) -> Iterable[int]:
		G_expanded = cls.__generate_expanded_graph(source_band_id, target_band_id) 
		flowchart = cls.__calculate_shortest_path(G_expanded, source_band_id, target_band_id)
		
		return flowchart

	@classmethod
	def __generate_expanded_graph(cls, source_band_id: int, target_band_id: int) -> nx.Graph:
		G_expanded = nx.Graph()
		G_expanded.add_node(source_band_id)

		queue = [source_band_id]
		
		while queue:
			current_band_id = queue.pop(0)

			for similar_band_id in SimilarBands.gather(current_band_id):
				if similar_band_id not in G_expanded.nodes:
					G_expanded.add_edge(current_band_id, similar_band_id) 
					
					if similar_band_id == target_band_id:
						queue = []
						break
					else:
						queue.append(similar_band_id)

		return G_expanded

	@classmethod
	def __calculate_shortest_path(cls, G: nx.Graph, source_band_id: int, target_band_id: int) -> Iterable[Any]:
		shortest_path = list(nx.dijkstra_path(G, source_band_id, target_band_id))

		return shortest_path
