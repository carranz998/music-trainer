import networkx as nx

from data_gathering.similar_bands_gather import \
    SimilarBandsGather
from data_scraping.webpage_content import WebpageContent

if __name__ == '__main__':
    url_initial_band = 'https://www.metal-archives.com/bands/Meshuggah/21'
    data = url_initial_band.split('/')
    name_band, id_band = data[4], int(data[5])

    soup = WebpageContent.load(f'https://www.metal-archives.com/band/ajax-recommendations/id/{id_band}')

    G = nx.Graph()
    G.add_node(id_band)
    nx.set_node_attributes(G, {id_band: name_band}, name='name_band')
    G = SimilarBandsGather.gather(G, soup, id_band)
