import networkx as nx
from data_pipeline.data_scraping.similar_bands_ids import SimilarBandsIds


class SimilarBandsGraph:
    @classmethod
    def build(cls, source_band_id: int, target_band_id: int) -> nx.Graph:
        G_similar_bands = nx.Graph()
        G_similar_bands.add_node(source_band_id)

        pending_pivot_bands_ids = [source_band_id]

        while pending_pivot_bands_ids:
            current_pivot_band_id = pending_pivot_bands_ids.pop(0)

            for similar_band_id in SimilarBandsIds.gather(current_pivot_band_id):
                if similar_band_id not in G_similar_bands.nodes:
                    G_similar_bands.add_edge(current_pivot_band_id, similar_band_id) 

                    if similar_band_id == target_band_id:
                        pending_pivot_bands_ids = []
                        break
                    else:
                        pending_pivot_bands_ids.append(similar_band_id)

        return G_similar_bands
