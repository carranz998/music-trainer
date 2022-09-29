from typing import Any

from utils.thread_safe_singleton import ThreadSafeSingleton


class DataCollector(metaclass=ThreadSafeSingleton):
    def __init__(self) -> None:
        self.data = dict()
    
    def add(self, key: Any, value: Any) -> None:
        if key not in self.data.keys():
            self.data[key] = [value]
        else:
            self.data[key].append(value)

    def reset(self) -> None:
        self.data = dict()
