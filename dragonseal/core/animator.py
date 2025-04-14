import pygame as pg
from pathlib import Path
from dragonseal.base import FolderLoader


class Animator(FolderLoader[pg.Surface]):
    def __init__(self, name: str, animation_speed: int = 150, autocomplete: bool = True, animator_folder: str = "img"):
        super().__init__(animator_folder, name, autocomplete)
        self.animation_speed = animation_speed
        self.animation_timer: int = 0
        self.current_frame: int = 0
        self.paused: bool = False

    def load(self, file: Path) -> pg.Surface:
        return pg.image.load(file).convert_alpha()

    def animate(self, dt: int, flip_x=False, flip_y=False, loop=True, reverse=False) -> pg.Surface:
        self.folder_error(self.active)

        if not self.paused:
            self.animation_timer += dt
            if self.animation_timer >= self.animation_speed:
                self.animation_timer = 0
                self.current_frame += -1 if reverse else 1
                if self.current_frame >= len(self.folders[self.active]):
                    self.current_frame = 0 if loop else len(self.folders[self.active]) - 1
                elif self.current_frame < 0:
                    self.current_frame = len(self.folders[self.active]) - 1 if loop else 0
        return pg.transform.flip(self.folders[self.active][self.current_frame], flip_x, flip_y)


    def set_frame(self, frame: int):
        self.folder_error(self.active)

        if 0 <= frame < len(self.folders[self.active]):
            self.current_frame = frame

    def set_speed(self, speed: int):
        self.animation_speed = max(1, speed)

    def pause(self):
        self.paused = True

    def resume(self):
        self.paused = False

    def reset(self):
        self.current_frame = 0
        self.animation_timer = 0

    def stop(self):
        self.reset()
        self.pause()

    def is_playing(self) -> bool:
        return not self.paused

    def get_frame(self) -> int:
        return self.current_frame

    def get_frame_image(self, key: str) -> pg.Surface:
        return self.folders[key if key else self.active][self.current_frame]

    def get_speed(self) -> int:
        return self.animation_speed
