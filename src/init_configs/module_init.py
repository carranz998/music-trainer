import os
from pathlib import Path

from utils.module import Module


def module_init(module_uri: Path) -> None:
    module_name = module_uri.stem

    init_path = os.path.join(module_uri, '__init__.py')
    __erase_file_contents(init_path)

    with open(init_path, 'w') as f:
        for filename in Module.file_iterator(module_uri):
            camel = __snake_to_camel(filename)
            class_name = camel[0].capitalize() + camel[1:]
            string = f'from {module_name}.{filename} import {class_name}\n'
            f.write(string)

def __erase_file_contents(filepath: str) -> None:
    open(filepath, 'w').close()

def __snake_to_camel(word: str) -> str:
        return ''.join(x.capitalize() or '_' for x in word.split('_'))
