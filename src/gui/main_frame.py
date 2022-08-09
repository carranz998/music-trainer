import tkinter as tk

from dynamic_web_scraper.chrome_web_driver import ChromeWebDriver
from dynamic_web_scraper.webpage_content import WebpageContent
from gui.main_frame_values import MainFrameValues

class MainFrame:
    def __init__(self) -> None:
        self.parent = tk.Tk()
        source_band_button = tk.Button(text='Capture source band', command=self.capture_source_url)
        source_band_button.pack()

        target_band_button = tk.Button(text='Capture target band', command=self.capture_target_url)
        target_band_button.pack()

        confirm_button = tk.Button(text='Confirm', command=self.quit)
        confirm_button.pack()

        self.base_url = 'https://www.metal-archives.com/'
        self.driver = ChromeWebDriver.build()
        self.driver.execute_script(f'window.open("{self.base_url}")')

        self.parent.mainloop()

    def quit(self):
        for handle in self.driver.window_handles:
            self.driver.switch_to.window(handle)
            self.driver.close()

        self.parent.destroy()
    
    def capture_source_url(self) -> None:
        for handle in self.driver.window_handles:
            self.driver.switch_to.window(handle)

            tab_url = self.driver.current_url
            if self.base_url in tab_url:
                MainFrameValues().source_band_url = tab_url

    def capture_target_url(self) -> None:
        for handle in self.driver.window_handles:
            self.driver.switch_to.window(handle)

            tab_url = self.driver.current_url
            if self.base_url in tab_url:
                MainFrameValues().target_band_url = tab_url
