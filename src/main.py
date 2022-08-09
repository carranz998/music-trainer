from data_pipeline.data_gathering.similar_bands_graph import SimilarBandsGraph
from data_pipeline.data_processing.band_to_band_flowchart import BandToBandFlowchart
from data_pipeline.data_scraping.band_name import BandName
from gui.widget import Widget
from gui.widget_data import WidgetData

if __name__ == '__main__':
    widget = Widget()
    source_band_id, target_band_id = WidgetData().source_band_id, WidgetData().target_band_id

    G_expanded = SimilarBandsGraph.build(source_band_id, target_band_id)
    bands_flowchart_ids = BandToBandFlowchart.build(G_expanded, source_band_id, target_band_id)
    bands_flowchart_names = map(BandName.gather, bands_flowchart_ids)

    print(*bands_flowchart_names, sep=' -> ')
