import tkinter as tk

from utils.data_collector import DataCollector
from web_browser_management.browser_window import BrowserWindow


class Widget:
    def __init__(self) -> None:
        self.base_url = 'https://www.metal-archives.com/'

        self.browser_window = BrowserWindow()
        self.browser_window.open_window(self.base_url)
        
        self.root_window = self.__build_widget_components()
        self.root_window.mainloop()
    
    def __build_widget_components(self) -> tk.Tk:
        root_window = tk.Tk()

        tk.Button(
            text='Capture source band',
            command=lambda: self.__save_band_id('source_band_id')
        ).pack()

        tk.Button(
            text='Capture target band',
            command=lambda: self.__save_band_id('target_band_id')
        ).pack()

        tk.Button(
            text='Confirm',
            command=self.__quit
        ).pack()

        return root_window

    def __save_band_id(self, key: str) -> None:
        for tab_url in self.browser_window.get_tabs_url():
            if self.base_url in tab_url:
                DataCollector().add(key, self.__extract_band_id(tab_url))

    def __extract_band_id(self, url: str) -> int:
        splitted_data = url.split('/')
        band_id = int(splitted_data[-1])

        return band_id

    def __quit(self) -> None:
        self.browser_window.close_window()
        self.root_window.destroy()
