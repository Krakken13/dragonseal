class Scene:
    def __init__(self, manager, **kwargs):
        self.manager = manager
        self.data = kwargs

    def update(self, dt):
        pass

    def draw(self, screen):
        pass

    def handle_event(self, event):
        pass
