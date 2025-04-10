import pygame as pg
from pathlib import Path
from dragonseal.exceptions import *
from dragonseal.core.extract_number import extract_number


class Animator:
    def __init__(self, name: str, animation_speed: int = 150, autocomplete: bool = True, animator_folder: str = "img"):
        self.path = Path(__file__).parent / animator_folder / name
        self.active: str = str()
        self.animations: dict[str, list[pg.Surface]] = dict()
        if not self.path.exists() or not self.path.is_dir():
            raise AnimatorFolderNotFoundOrIsNotDir(self.path)
        if autocomplete:
            for folder in self.path.iterdir():
                if folder.is_dir():
                    self.new(folder)
        self.animation_speed = animation_speed
        self.animation_timer: int = 0
        self.current_frame: int = 0
        self.paused: bool = False

    def __str__(self) -> str:
        return f"Animator: {self.path}"

    def __eq__(self, other) -> bool:
        return self.path == other.path

    def new(self, folder: str):
        if folder in self.animations:
            raise AnimationHaveAlreadyExists(folder)
        self.animations[folder]: list[pg.Surface] = list()
        path = self.path / folder
        if not path.exists() or not path.is_dir() or not path.iterdir():
            raise AnimationFolderNotFoundOrIsNotDirOrEmpty(str(path))
        for frame in sorted(path.iterdir(), key=extract_number):
            self.animations[folder].append(pg.image.load(frame).convert_alpha())
        if not self.active:
            self.active = folder

    def animate(self, dt: int, flip_x=False, flip_y=False, loop=True, reverse=False) -> pg.Surface:
        if not self.active or self.active not in self.animations:
            raise AnimationNotSet()

        if not self.paused:
            self.animation_timer += dt
            if self.animation_timer >= self.animation_speed:
                self.animation_timer = 0
                self.current_frame += -1 if reverse else 1
                if self.current_frame >= len(self.animations[self.active]):
                    self.current_frame = 0 if loop else len(self.animations[self.active]) - 1
                elif self.current_frame < 0:
                    self.current_frame = len(self.animations[self.active]) - 1 if loop else 0
        return pg.transform.flip(self.animations[self.active][self.current_frame], flip_x, flip_y)

    def set(self, animation_type: str, frame: int = 0):
        if self.has_animation(animation_type):
            self.active = animation_type
            self.animation_timer = 0
            self.current_frame = frame
        else:
            raise AnimationNotFound(animation_type)

    def set_frame(self, frame: int):
        if 0 <= frame < len(self.animations[self.active]):
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

    def has_animation(self, animation_type: str) -> bool:
        return animation_type in self.animations

    def is_playing(self) -> bool:
        return not self.paused

    def get_frame(self) -> int:
        return self.current_frame

    def get_speed(self) -> int:
        return self.animation_speed

    def get_active_animation(self) -> str:
        return self.active


if __name__ == "__main__":
    animator = Animator("animator")
