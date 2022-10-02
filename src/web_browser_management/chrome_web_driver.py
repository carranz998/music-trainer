from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


class ChromeWebDriver:
    @classmethod
    def build(cls) -> webdriver.Chrome:
        return webdriver.Chrome(
            options=cls.__build_options(),
            service=cls.__build_service()
        )

    @classmethod
    def __build_options(cls) -> Options:
        options = Options()
        options.add_argument('start-maximized')

        return options

    @classmethod
    def __build_service(cls) -> Service:
        chrome_driver_manager = ChromeDriverManager().install()
        service = Service(chrome_driver_manager)

        return service
