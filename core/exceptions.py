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
