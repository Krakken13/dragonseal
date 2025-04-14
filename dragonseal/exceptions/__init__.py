from dragonseal.exceptions.path_error import PathError
from dragonseal.exceptions.folder_not_found import FolderNotFound


class AnimationNotFound(Exception):
    def __init__(self, animation):
        super().__init__(f"[Animator] Animation '{animation}' not found!")


class AnimationNotSet(Exception):
    def __init__(self):
        super().__init__(f"[Animator] Animation not set!")


class AnimatorFolderNotFoundOrIsNotDir(Exception):
    def __init__(self, folder):
        super().__init__(f"[Animator] Animator Folder '{folder}' not found or isn't a directory!")


class AnimationFolderNotFoundOrIsNotDirOrEmpty(Exception):
    def __init__(self, folder):
        super().__init__(f"[Animator] Animation Folder '{folder}' not found or isn't a directory or empty!")


class AnimationHaveAlreadyExists(Exception):
    def __init__(self, animation):
        super().__init__(f"[Animator] Animation has already been created for '{animation}'!")


class FolderHaveAlreadyExists(Exception):
    def __init__(self, folder: str, module: str, ):
        super().__init__(f"[{module}] Folder '{folder}' already exists!")
