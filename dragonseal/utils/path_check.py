from pathlib import Path


def path_check(path: Path, empty_check: bool = False) -> bool:
    return path.is_dir() and path.iterdir()
