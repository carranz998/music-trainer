from utils.thread_safe_singleton import ThreadSafeSingleton


class MainFrameValues(metaclass=ThreadSafeSingleton):
    def __init__(self) -> None:
        self.source_band_url = ''
        self.target_band_url = ''

    @property
    def source_band_id(self):
        splitted_data = self.source_band_url.split('/')
        band_id = int(splitted_data[-1])

        return band_id

    @property
    def target_band_id(self):
        splitted_data = self.target_band_url.split('/')
        band_id = int(splitted_data[-1])

        return band_id