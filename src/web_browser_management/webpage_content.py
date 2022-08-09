import time

from bs4 import BeautifulSoup
from selenium import webdriver

from web_browser_management.chrome_web_driver import ChromeWebDriver


class WebpageContent:
    @classmethod
    def load(cls, url: str) -> BeautifulSoup:
        chrome_web_driver = ChromeWebDriver.build()
        page_dynamic_content = cls.__load_dynamic_content(url, chrome_web_driver)

        soup = BeautifulSoup(page_dynamic_content, 'html.parser')

        return soup

    @classmethod
    def __load_dynamic_content(cls, url: str, chrome_web_driver: webdriver.Chrome, load_time: int=2) -> str:
        with chrome_web_driver:
            chrome_web_driver.get(url)
            time.sleep(load_time)

            page_dynamic_content = chrome_web_driver.page_source

        return page_dynamic_content
