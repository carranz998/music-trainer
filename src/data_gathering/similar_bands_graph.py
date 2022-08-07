import networkx as nx
from data_scraping.similar_bands import SimilarBands


class SimilarBandsGraph:
    @classmethod
    def build_expanded_graph(cls, source_band_id: int, target_band_id: int) -> nx.Graph:
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
