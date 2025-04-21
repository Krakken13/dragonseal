import asyncio
from abc import ABC, abstractmethod
from typing import Any, overload, Union, Generic
from pathlib import Path
from dragonseal.base.constants import T
from dragonseal.exceptions import FolderHaveAlreadyExists, FolderNotFound, FolderNotSet
from dragonseal.utils import path_error, extract_number


class FolderLoader(ABC, Generic[T]):
    @overload
    def __init__(self, std_dir: str, name: str, autocomplete: bool):
        ...

    @overload
    def __init__(self, std_dir: Path, name: str, autocomplete: bool):
        ...

    def __init__(self, std_dir: Union[str, Path], name: str, autocomplete: bool):
        std_dir = Path(std_dir)
        self.path = std_dir / name if std_dir.is_absolute() else Path(__file__).parent / std_dir / name
        path_error(self.path, self.__class__.__name__, empty_check=True)
        self.folders: dict[str, list[T]] = dict()
        self.active: str = str()
        self.active_value: list[T] = list()
        if autocomplete:
            asyncio.create_task(self.autocomplete())

    def __str__(self):
        return f"{self.__class__.__name__}: {self.path}"

    def __eq__(self, other: Any) -> bool:
        return self.path == other.path if isinstance(other, FolderLoader) else False

    async def autocomplete(self):
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
            self.set(name)

    def set(self, folder: str):
        if not self.has(folder):
            raise FolderNotFound(folder, self.__class__.__name__)
        self.active = folder

    def get_key(self) -> str:
        return self.active

    def get_value(self, folder: str = None) -> list[T]:
        return self.folders[self.active if folder is None else folder]

    def get_index(self, index: int, folder: str = None) -> T:
        return self.get_value(self.active if folder is None else folder)[index]

    def has(self, folder: str) -> bool:
        return folder in self.folders

    def folder_error(self, folder: str):
        if not folder:
            raise FolderNotSet(self.active, self.__class__.__name__)

        if not self.has(folder):
            raise FolderNotFound(self.active, self.__class__.__name__)

    @abstractmethod
    async def load(self, file: Path) -> T:
        ...
