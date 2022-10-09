from pathlib import Path
from typing import Iterator, Type


class Module:
    @classmethod
    def file_iterator(cls, module_uri: Path) -> Iterator[str]:
        return (Path(python_file).stem for python_file in module_uri.glob('[!_]*.py'))
        
    @classmethod
    def instantiate_class(cls, module_name: str, class_name: str) -> Type:
        return getattr(__import__(module_name), class_name)
