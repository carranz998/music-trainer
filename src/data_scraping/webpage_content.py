from bs4 import BeautifulSoup

from data_scraping.chrome_web_driver import ChromeWebDriver
from data_scraping.dynamic_content_loader import DynamicContentLoader


class WebpageContent:
    @classmethod
    def load(cls, url: str) -> BeautifulSoup:
        chrome_web_driver = ChromeWebDriver.build()
        html = DynamicContentLoader.load_html(url, chrome_web_driver)
        soup = BeautifulSoup(html, 'html.parser')

        return soup
