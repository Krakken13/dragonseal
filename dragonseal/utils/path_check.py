from pathlib import Path


def path_check(path: Path, empty_check: bool = False) -> bool:
    return not (path.is_dir() and path.exists() and True if not empty_check else not path.iterdir())
