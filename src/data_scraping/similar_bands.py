from typing import Iterator

from bs4 import BeautifulSoup

from dynamic_web_scraper.webpage_content import WebpageContent


class SimilarBands:
    @classmethod
    def gather(cls, band_id: int) -> Iterator[int]:
        url = cls.__get_band_url(band_id)
        soup = WebpageContent.load(url)

        return cls.__scrap_similar_bands_ids(soup)

    @classmethod
    def __scrap_similar_bands_ids(cls, soup: BeautifulSoup) -> Iterator[int]:
        similar_bands_ids = map(cls.__extract_band_id, soup.find_all('a'))
        similar_bands_ids = filter(lambda x: x >= 0, similar_bands_ids)

        return similar_bands_ids

    @classmethod
    def __get_band_url(cls, band_id: int) -> str:
        url = f'https://www.metal-archives.com/band/ajax-recommendations/id/{band_id}'

        return url

    @classmethod
    def __extract_band_id(cls, band_url: BeautifulSoup) -> int:
        href = str(band_url.get('href'))
        data = str(href).split('/')

        try:
            return int(data[5])
        except ValueError:
            return -1
