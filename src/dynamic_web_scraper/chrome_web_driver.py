from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


class ChromeWebDriver:
    @classmethod
    def build(cls) -> webdriver.Chrome:
        driver = webdriver.Chrome(options=cls.__set_options(), service=cls.__set_service())

        return driver

    @classmethod
    def __set_options(cls) -> Options:
        options = Options()
        options.add_argument('start-maximized')

        return options

    @classmethod
    def __set_service(cls) -> Service:
        chrome_driver_manager = ChromeDriverManager().install()
        service = Service(chrome_driver_manager)

        return service
