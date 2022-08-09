from typing import Iterator

from web_browser_management.chrome_web_driver import ChromeWebDriver


class BrowserWindow:
    def __init__(self) -> None:
        self.driver = ChromeWebDriver.build()

    def close_window(self) -> None:
        for handle in self.driver.window_handles:
            self.driver.switch_to.window(handle)
            self.driver.close()
        
    def open_window(self, url: str) -> None:
        self.driver.execute_script(f'window.open("{url}")')
    
    def get_tabs_url(self) -> Iterator[str]:
        for handle in self.driver.window_handles:
            self.driver.switch_to.window(handle)
            tab_url = self.driver.current_url

            yield tab_url
