from utils.thread_safe_singleton import ThreadSafeSingleton


class WidgetData(metaclass=ThreadSafeSingleton):
    def __init__(self) -> None:
        self.source_band_url = ''
        self.target_band_url = ''

    @property
    def source_band_id(self) -> int:
        return self.__extract_band_id(self.source_band_url)

    @property
    def target_band_id(self) -> int:
        return self.__extract_band_id(self.target_band_url)

    def __extract_band_id(self, url: str) -> int:
        splitted_data = url.split('/')
        band_id = int(splitted_data[-1])

        return band_id