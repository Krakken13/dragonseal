from pathlib import Path
from dragonseal.utils.path_valid import path_valid
from dragonseal.exceptions import PathError


def path_error(path: Path, module: str, empty_check: bool = False):
    is_filled = bool(path.iterdir()) if empty_check else True
    if not path_valid(path) or not is_filled:
        raise PathError(path, module, empty_check=empty_check)
