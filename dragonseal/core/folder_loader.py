from abc import ABC, abstractmethod
from pathlib import Path
from dragonseal.exceptions import (
    FolderHaveAlreadyExists
)
from dragonseal.utils.path_error import path_error
from dragonseal.utils.extract_number import extract_number
from typing import Any


class FolderLoader(ABC):
    def __init__(self, std_dir: str, name: str ):
        self.path = Path(__file__).parent / std_dir / name
        self.folders = dict[str, list]

    def new(self, folder: str):
        if self.has(folder):
            raise FolderHaveAlreadyExists(folder, self.path.name)

        path = self.path / folder
        if path_error(path, empty_check=True):
            raise

    def has(self, folder: str) -> bool:
        return folder in self.folders

    @abstractmethod
    def load(self):
        pass
