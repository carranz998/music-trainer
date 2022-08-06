from typing import Iterable

import networkx as nx
from data_gathering.band_data import BandData
from data_gathering.similar_bands import SimilarBands


class BandsFlowchart:
	@classmethod
	def build(cls, source_band_id: int, target_band_id: int) -> Iterable[str]:
		G_brute_force = cls.__build_brute_force_graph(source_band_id, target_band_id)
		shortest_path = list(nx.dijkstra_path(G_brute_force, source_band_id, target_band_id))

		band_flowchart = [BandData.scrap_name(band_id) for band_id in shortest_path]

		return band_flowchart

	@classmethod
	def __build_brute_force_graph(cls, source_band_id: int, target_band_id: int) -> nx.Graph:
		G_bands_flowchart = nx.Graph()
		G_bands_flowchart.add_node(source_band_id)

		current_band_id = source_band_id
		next_band_id = current_band_id

		while current_band_id != target_band_id:
			for similar_band_id in SimilarBands.gather(next_band_id):
				G_bands_flowchart.add_edge(current_band_id, similar_band_id)

				next_band_id = similar_band_id
				
				if similar_band_id == target_band_id:
					current_band_id = target_band_id
					break

			current_band_id = next_band_id

		return G_bands_flowchart
