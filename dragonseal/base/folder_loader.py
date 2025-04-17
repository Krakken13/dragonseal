from abc import ABC, abstractmethod
from typing import Any, overload, Union, Generic
from pathlib import Path
from dragonseal.base import T
from dragonseal.exceptions import FolderHaveAlreadyExists, FolderNotFound, FolderNotSet
from dragonseal.utils import path_error, extract_number


class FolderLoader(ABC, Generic[T]):
    def __init__(self, std_dir: str, name: str, autocomplete: bool):
        self.path = Path(__file__).parent / std_dir / name
        path_error(self.path, self.__class__.__name__, empty_check=True)
        self.folders: dict[str, list[T]] = dict()
        self.active: str = str()
        if autocomplete:
            self.autocomplete()

    def __str__(self):
        return f"{self.__class__.__name__}: {self.path}"

    def __eq__(self, other: Any) -> bool:
        return self.path == other.path if isinstance(other, FolderLoader) else False

    def autocomplete(self):
        for folder in sorted(self.path.iterdir(), key=extract_number):
            if path_error(folder, self.__class__.__name__, empty_check=True):
                self.new(folder)

    @overload
    def new(self, folder: str):
        ...

    @overload
    def new(self, folder: Path):
        ...

    def new(self, folder: Union[str, Path]):
        name = folder if isinstance(folder, str) else folder.name

        if self.has(name):
            raise FolderHaveAlreadyExists(name, self.__class__.__name__)

        path = self.path / folder if isinstance(folder, str) else folder
        path_error(path, self.__class__.__name__, empty_check=True)
        self.folders[name] = [self.load(file) for file in sorted(path.iterdir(), key=extract_number)]
        if not self.active:
            self.active = name

    def set(self, folder: str):
        if not self.has(folder):
            raise FolderNotFound(folder, self.__class__.__name__)
        self.active = folder

    def get_key(self) -> str:
        return self.active

    def get_value(self, key: str) -> list[T]:
        return self.folders[key if key else self.active]

    def get_index(self, index: int, key: str) -> T:
        return self.get_value(key if key and self.has(key) else self.active)[index]

    def has(self, folder: str) -> bool:
        return folder in self.folders

    def folder_error(self, folder: str):
        if not folder:
            raise FolderNotSet(self.active, self.__class__.__name__)

        if not self.has(folder):
            raise FolderNotFound(self.active, self.__class__.__name__)

    @abstractmethod
    def load(self, file: Path) -> T:
        ...
