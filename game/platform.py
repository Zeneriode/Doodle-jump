from arcade import Sprite

from constants import (
    SCALE,
    PLATFORM_CENTER_X,
    PLATFORM_CENTER_Y
)


class Platform(Sprite):
    """Платформа"""

    def __init__(self):
        """Конструктор для платформ"""
        super().__init__("assets/static_pics/floor.png", SCALE)
        self.center_x = PLATFORM_CENTER_X
        self.center_y = PLATFORM_CENTER_Y
