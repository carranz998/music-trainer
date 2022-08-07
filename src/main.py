from data_gathering.similar_bands_graph import SimilarBandsGraph
from data_processing.band_to_band_flowchart import BandToBandFlowchart
from data_scraping.band_data import BandData

if __name__ == '__main__':
    source_band_id, target_band_id = 21, 119

    G_expanded = SimilarBandsGraph.build_expanded_graph(source_band_id, target_band_id)
    bands_flowchart_ids = BandToBandFlowchart.build(G_expanded, source_band_id, target_band_id)
    bands_flowchart_names = map(BandData.scrap_name, bands_flowchart_ids)

    print(*bands_flowchart_names, sep=' -> ')
