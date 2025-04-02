import pygame as pg
import importlib


class SceneManager:
    def __init__(self):
        self.scene = None
        self.global_data = {}

    def change_scene(self, scene_name, **kwargs):
        try:
            module = importlib.import_module(f"scenes.{scene_name}")
            self.scene = module.Scene(self, **kwargs)
        except ModuleNotFoundError:
            print(f"[SceneManager] Scene '{scene_name}' not found!")

    def update(self, dt):
        if self.scene:
            self.scene.update(dt)

    def draw(self, screen):
        if self.scene:
            self.scene.draw(screen)

    def handle_event(self, event):
        if self.scene:
            self.scene.handle_event(event)
