from typing import Any

from bs4 import BeautifulSoup, Tag

from data_scraping.abstract_data_scraper import AbstractDataScraper


class SimilarBandsIdsScraper(AbstractDataScraper):
    def _build_url(self, resource_id: int) -> str:
        return f'https://www.metal-archives.com/band/ajax-recommendations/id/{resource_id}'

    def _scrap_data(self, response_soup: BeautifulSoup) -> Any:
        similar_bands_ids = map(self.__extract_band_id, response_soup.find_all('a'))
        valid_bands_ids = filter(lambda band_id: band_id >= 0, similar_bands_ids)

        return valid_bands_ids

    def __extract_band_id(self, similar_band_hyperlink: Tag) -> int:
        splitted_url = str(similar_band_hyperlink.get('href')).split('/')

        try:
            return int(splitted_url[5])
        except ValueError:
            return -1
