import pygame as pg
import re
from pathlib import Path


def extract_number(p: Path):
    match = re.search(r'\d+', p.stem)
    return int(match.group()) if match else 0


class Animator:
    def __init__(self, name: str, animation_speed: int = 150):
        self.name = name
        self.animation_speed = animation_speed
        self.animations = dict()
        self.active = str()
        self.animation_timer = 0
        self.current_frame = 0
        self.paused = False

    def new(self, folder: str):
        self.animations[folder] = list()
        path = Path(f"img/{self.name}/{folder}/")
        for frame in sorted(path.iterdir(), key=extract_number):
            self.animations[folder].append(pg.image.load(frame).convert_alpha())

    def animate(self, dt: int, flip_x=False, flip_y=False, loop=True, reverse=False) -> pg.Surface:
        if not self.active or self.active not in self.animations:
            return pg.Surface((1, 1), pg.SRCALPHA)

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

    def set(self, animation_type: str):
        if self.has_animation(animation_type):
            self.active = animation_type
            self.reset()
        elif not self.active:
            self.active = next(iter(self.animations))
        else:
            print(f"[Animator] couldn't find animation {animation_type}")

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
