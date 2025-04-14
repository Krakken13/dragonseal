from pathlib import Path
from dragonseal.utils import path_check
from dragonseal.exceptions import PathError


def path_error(path: Path, module: str, empty_check: bool = False):
    if path_check(path, empty_check=empty_check):
        raise PathError(path, module, empty_check=empty_check)
