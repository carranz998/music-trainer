from typing import Any

from utils.thread_safe_singleton import ThreadSafeSingleton


class DataCollector(metaclass=ThreadSafeSingleton):
    def __init__(self) -> None:
        self.data = dict()
    
    def add(self, key: Any, value: Any) -> None:
        try:
            self.data[key].append(value)
        except KeyError:
            self.data[key] = [value]
