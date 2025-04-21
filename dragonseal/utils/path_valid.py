from pathlib import Path

def path_valid(path: Path) -> bool:
    return path.exists() and path.is_dir()