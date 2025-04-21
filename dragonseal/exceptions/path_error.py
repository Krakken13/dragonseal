from pathlib import Path


class PathError(Exception):
    def __init__(self, path: Path, module: str, empty_check: bool = False):
        super().__init__(f"[{module}] Path '{path.name}' does not exist or isn't a folder" + (
            " or is empty" if empty_check else "") + "!" + str(path) + str(path.is_dir()) + str(bool(path.iterdir())) + str(path.exists()))
