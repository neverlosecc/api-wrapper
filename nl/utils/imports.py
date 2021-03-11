from importlib import import_module
from pathlib import Path
from typing import Any
from typing import List

from pydantic import BaseModel


class ImportedModule(BaseModel):
    module: Any
    name: str


def import_all_modules(
        name: str, path: Path = Path(__file__).parent, except_files=None
) -> List:
    result = list()
    if not except_files:
        except_files = []
    except_files.append('__init__')
    for file in path.iterdir():
        if file.is_dir():
            result = [*result, *import_all_modules(name, file)]
            continue

        if file.name.split('.')[1] != 'py':
            continue
        if file.name.split('.')[0] in except_files:
            continue

        file_name = file.name.split('.')[0]
        additional_path = (
            str(file.absolute()).split('.py')[0].split(name.split('.')[-1])
        )

        if len(additional_path) < 1:
            additional_path = ''
        else:
            windows_path = additional_path[1].split('\\', maxsplit=1)
            linux_path = additional_path[1].split('/', maxsplit=1)

            additional_path = windows_path if len(
                windows_path) > 1 else linux_path
            additional_path = ''.join(
                (
                    additional_path[1].replace('\\', '.').replace('/', '.')
                    if len(additional_path) > 1
                    else ''
                ).split('.')[:-1]
            )
        if additional_path not in ['', ' ']:
            additional_path += '.'
        file_name = additional_path + file_name

        imported = import_module(name + '.' + file_name)
        item = ImportedModule(module=imported, name=file_name)
        result.append(item)

    return result
