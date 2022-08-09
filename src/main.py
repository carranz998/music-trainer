from data_gathering.similar_bands_graph import SimilarBandsGraph
from data_processing.band_to_band_flowchart import BandToBandFlowchart
from data_scraping.band_data import BandData
from gui.main_frame import MainFrame
from gui.main_frame_values import MainFrameValues

if __name__ == '__main__':
    main_frame = MainFrame()
    source_band_id, target_band_id = MainFrameValues().source_band_id, MainFrameValues().target_band_id

    G_expanded = SimilarBandsGraph.build_expanded_graph(source_band_id, target_band_id)
    bands_flowchart_ids = BandToBandFlowchart.build(G_expanded, source_band_id, target_band_id)
    bands_flowchart_names = map(BandData.scrap_name, bands_flowchart_ids)

    print(*bands_flowchart_names, sep=' -> ')
