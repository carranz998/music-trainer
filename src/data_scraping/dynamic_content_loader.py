import time

from selenium import webdriver


class DynamicContentLoader:
    @classmethod
    def load_html(cls, url: str, chrome_web_driver: webdriver.Chrome, load_time: int=2) -> str:
        with chrome_web_driver:
            chrome_web_driver.get(url)
            time.sleep(load_time)

            return chrome_web_driver.page_source
