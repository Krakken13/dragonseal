import pygame as pg
import pytest
from pathlib import Path
from dragonseal import Animator

pg.init()
pg.display.set_mode((1, 1))


def test_animator_load_and_animate(tmp_path: Path):
    img_path = tmp_path / "img" / "player" / "idle"
    img_path.mkdir(parents=True)

    for i in range(3):
        surface = pg.Surface((10, 10))
        surface.fill((i * 40, i * 40, i * 40))
        pg.image.save(surface, img_path / f"{i}.png")

    animator = Animator(name="player", animator_folder=tmp_path / "img", autocomplete=False)
    animator.new("idle")

    assert animator.get_frame() == 0
    assert animator.get_key() == "idle"

    frame_before = animator.animate(dt=animator.get_speed(), loop=True)
    assert isinstance(frame_before, pg.Surface)

    animator.set_frame(2)
    assert animator.get_frame() == 2

    frame_after = animator.animate(dt=animator.get_speed(), loop=True)
    assert frame_after is not None
