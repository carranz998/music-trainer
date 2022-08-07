from data_gathering.band_data import BandData
from data_structures.bands_flowchart import BandsFlowchart

if __name__ == '__main__':
    bands_flowchart_ids = BandsFlowchart.generate_flowchart(source_band_id=34361, target_band_id=125)
    bands_flowchart_names = map(BandData.scrap_name, bands_flowchart_ids)

    print(*bands_flowchart_names, sep=" -> ")
