class AnimationNotFound(Exception):
    def __init__(self, animation):
        super().__init__(f"[Animator] Animation '{animation}' not found!")


class AnimationNotSet(Exception):
    def __init__(self):
        super().__init__(f"[Animator] Animation not set!")
