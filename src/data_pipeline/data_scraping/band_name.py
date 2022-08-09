from bs4 import BeautifulSoup
from web_browser_management.webpage_content import WebpageContent


class BandName:
    @classmethod
    def gather(cls, band_id: int) -> str:
        band_url = cls.__get_band_url(band_id)
        band_soup = WebpageContent.load(band_url)

        band_name = cls.__scrap_band_name(band_soup)

        return band_name

    @classmethod
    def __get_band_url(cls, band_id: int) -> str:
        band_url = f'https://www.metal-archives.com/bands//{band_id}'

        return band_url

    @classmethod
    def __scrap_band_name(cls, band_soup: BeautifulSoup) -> str:
        found_band_name = band_soup.find('h1', class_='band_name')
        band_name = found_band_name.text if found_band_name else ''

        return band_name
