class FrameOutOfAnimation(Exception):
    def __init__(self, frame: int, folder: str, module: str):
        super().__init__(f"[{module}] Frame '{frame}' out of animation folder '{folder}'!")
