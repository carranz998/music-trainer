from abc import ABC, abstractmethod
from typing import Any

import requests
from bs4 import BeautifulSoup


class DataScraper(ABC):
    def scrap(self, resource_id: int) -> Any:
        url = self._build_url(resource_id)
        response_content = self.__request_page_content(url)
        response_soup = self.__response_soup(response_content)
        scraped_data = self._scrap_data(response_soup)

        return scraped_data

    def __request_page_content(self, url: str) -> bytes:
        return requests.get(url).content

    def __response_soup(self, response_content: bytes) -> BeautifulSoup:
        return BeautifulSoup(response_content, 'html.parser')

    @abstractmethod
    def _build_url(self, resource_id: int) -> str:
        pass

    @abstractmethod
    def _scrap_data(self, response_soup: BeautifulSoup) -> Any:
        pass
