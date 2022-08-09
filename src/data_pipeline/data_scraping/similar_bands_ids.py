from typing import Iterator

from bs4 import BeautifulSoup, Tag
from web_browser_management.webpage_content import WebpageContent


class SimilarBandsIds:
    @classmethod
    def gather(cls, pivot_band_id: int) -> Iterator[int]:
        similar_bands_url = cls.__get_similar_bands_url(pivot_band_id)
        similar_bands_soup = WebpageContent.load(similar_bands_url)
        
        similar_bands_ids = cls.__scrap_similar_bands_ids(similar_bands_soup)

        return similar_bands_ids

    @classmethod
    def __extract_band_id(cls, similar_band_hyperlink: Tag) -> int:
        similar_band_url = str(similar_band_hyperlink.get('href'))
        splitted_url = str(similar_band_url).split('/')

        try:
            band_id = int(splitted_url[5])
        except ValueError:
            band_id = -1

        return band_id

    @classmethod
    def __get_similar_bands_url(cls, pivot_band_id: int) -> str:
        similar_bands_url = f'https://www.metal-archives.com/band/ajax-recommendations/id/{pivot_band_id}'

        return similar_bands_url

    @classmethod
    def __scrap_similar_bands_ids(cls, similar_bands_soup: BeautifulSoup) -> Iterator[int]:
        similar_bands_ids = map(cls.__extract_band_id, similar_bands_soup.find_all('a'))
        similar_bands_ids = filter(lambda band_id: band_id >= 0, similar_bands_ids)

        return similar_bands_ids
