from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


class ChromeWebDriver:
    @classmethod
    def build(cls) -> webdriver.Chrome:
        options = Options()
        options.add_argument('start-maximized')

        chrome_driver_manager = ChromeDriverManager().install()
        driver = webdriver.Chrome(service=Service(chrome_driver_manager), options=options)

        return driver
