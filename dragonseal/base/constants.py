from enum import Enum, auto
from typing import TypeVar

T = TypeVar("T")


class LoadMode(Enum):
    EAGER = auto()
    LAZY = auto()
    PRELOAD = auto()
