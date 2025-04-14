from abc import ABC, abstractmethod
from pathlib import Path
from dragonseal.exceptions import (
    FolderHaveAlreadyExists,
    FolderNotFound,
    PathError
)
from dragonseal.utils import (
    path_check,
    path_error,
    extract_number
)
from typing import Any


class FolderLoader(ABC):
    def __init__(self, std_dir: str, name: str):
        self.path = Path(__file__).parent / std_dir / name
        path_error(self.path, self.__class__.__name__, empty_check=True)
        self.folders: dict[str, list[Any]] = dict()
        self.active: str = str()

    def __eq__(self, other: Any) -> bool:
        return self.path == other.path if isinstance(other, FolderLoader) else False

    def new(self, folder: str):
        if self.has(folder):
            raise FolderHaveAlreadyExists(folder, self.__class__.__name__)

        path = self.path / folder
        path_error(path, self.__class__.__name__, empty_check=True)
        self.folders[folder] = [self.load(file) for file in sorted(path.iterdir(), key=extract_number)]
        if not self.active:
            self.active = folder

    def set(self, folder: str):
        if not self.has(folder):
            raise FolderNotFound(folder, self.__class__.__name__)
        self.active = folder

    def get(self) -> str:
        return self.active

    def has(self, folder: str) -> bool:
        return folder in self.folders

    @abstractmethod
    def load(self, file: Path) -> Any:
        pass
