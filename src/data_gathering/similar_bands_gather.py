import networkx as nx
from bs4 import BeautifulSoup


class SimilarBandsGather:
    @classmethod
    def gather(cls, G: nx.Graph, soup: BeautifulSoup, id_start_band: int) -> nx.Graph:
        for link, span in zip(soup.find_all('a'), soup.find_all('span')):
            href = str(link.get('href'))
            data = str(href).split('/')

            try:
                name_band, id_band = data[4], int(data[5])
                score = int(span.text)
                G.add_node(id_band)
                nx.set_node_attributes(G, {id_band: name_band}, name='band_name')
                G.add_edge(id_start_band, id_band)

                attrs = {(id_start_band, id_band): {'score': score}}
                nx.set_edge_attributes(G, attrs)

            except ValueError:
                pass

        return G
