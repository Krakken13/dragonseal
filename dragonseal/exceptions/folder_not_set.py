class FolderNotSet(Exception):
    def __init__(self, folder: str, module: str):
        super().__init__(f"[{module}] Folder '{folder}' not set!")