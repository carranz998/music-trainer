import networkx as nx
from bs4 import BeautifulSoup


class SimilarBandsGather:
    @classmethod
    def gather(cls, G: nx.Graph, soup: BeautifulSoup, id_start_band: int) -> nx.Graph:
        for link in soup.find_all('a'):
            href = str(link.get('href'))
            data = str(href).split('/')

            try:
                name_band, id_band = data[4], int(data[5])
                G.add_node(id_band)
                nx.set_node_attributes(G, {id_band: name_band}, name='band_name')
                G.add_edge(id_start_band, id_band)
            except ValueError:
                pass

        return G
