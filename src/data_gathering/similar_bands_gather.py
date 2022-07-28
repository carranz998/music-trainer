from typing import Iterable, Iterator

import networkx as nx
from bs4 import BeautifulSoup


class SimilarBandsGather:
    @classmethod
    def gather(cls, G: nx.Graph, soup: BeautifulSoup, id_start_band: int) -> nx.Graph:
        rows_data = cls.__gather_row_data(soup)
        G = cls.__update_graph(G, id_start_band, rows_data)

        return G

    @classmethod
    def __gather_row_data(cls, soup: BeautifulSoup) -> Iterator[Iterable]:
        for link, span in zip(soup.find_all('a'), soup.find_all('span')):
            href = str(link.get('href'))
            data = str(href).split('/')

            name_band, id_band = data[4], int(data[5])
            score = int(span.text)

            yield id_band, name_band, score

    @classmethod
    def __update_graph(cls, G: nx.Graph, id_start_band: int, rows_data: Iterator[Iterable]) -> nx.Graph:
        for id_band, name_band, score in rows_data:
            G.add_node(id_band)
            nx.set_node_attributes(G, {id_band: name_band}, name='name_band')

            new_edge = (id_start_band, id_band)
            G.add_edge(*new_edge)
            nx.set_edge_attributes(G, {new_edge: {'score': score}})

        return G
