from typing import Any

from bs4 import BeautifulSoup

from data_scraping.abstract_data_scraper import AbstractDataScraper


class BandNameScraper(AbstractDataScraper):
    def _build_url(self, resource_id: int) -> str:
        return f'https://www.metal-archives.com/bands//{resource_id}'

    def _scrap_data(self, response_soup: BeautifulSoup) -> Any:
        found_band_name = response_soup.find('h1', class_='band_name')
        band_name = found_band_name.text if found_band_name else ''

        return band_name
