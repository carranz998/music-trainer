import networkx as nx

from data_gathering.similar_bands_gather import \
    SimilarBandsGather
from data_scraping.webpage_content import WebpageContent

if __name__ == '__main__':
    url_initial_band = 'https://www.metal-archives.com/bands/Meshuggah/21'
    data = url_initial_band.split('/')
    name_band, id_band = data[4], int(data[5])

    soup = WebpageContent.load('https://www.metal-archives.com/band/ajax-recommendations/id/21')

    G = nx.Graph()
    G.add_node(21)
    nx.set_node_attributes(G, {id_band: name_band}, name='name_band')
    G = SimilarBandsGather.gather(G, soup, 21)
