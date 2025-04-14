import pygame as pg
from pathlib import Path


class Document:
    def __init__(self, name: str, autocomplete: bool = True, document_folder: str = "doc"):
        self.path = Path(__file__).parent / document_folder / name
        self.documents: dict[str, list[Path]] = dict()
        if not self.path.exists():
            pass
        if autocomplete:
            pass
