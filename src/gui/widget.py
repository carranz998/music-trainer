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

        source_band_button = tk.Button(text='Capture source band', command=self.__capture_source_url)
        target_band_button = tk.Button(text='Capture target band', command=self.__capture_target_url)
        confirm_button = tk.Button(text='Confirm', command=self.__quit)

        source_band_button.pack()
        target_band_button.pack()
        confirm_button.pack()

        return root_window

    def __capture_source_url(self) -> None:
        for tab_url in self.browser_window.get_tabs_url():
            if self.base_url in tab_url:
                DataCollector().add('source_band_id', self.__extract_band_id(tab_url))

    def __capture_target_url(self) -> None:
        for tab_url in self.browser_window.get_tabs_url():
            if self.base_url in tab_url:
                DataCollector().add('target_band_id', self.__extract_band_id(tab_url))

    def __extract_band_id(self, url: str) -> int:
        splitted_data = url.split('/')
        band_id = int(splitted_data[-1])

        return band_id

    def __quit(self) -> None:
        self.browser_window.close_window()
        self.root_window.destroy()
