from arcade import Sprite
from game.constants import SCALE


class Platform(Sprite):
    """Платформа"""

    def __init__(self, file: str, center_x: int, center_y: int):
        """Конструктор для платформ"""
        super().__init__(file, SCALE)
        self.center_x = center_x
        self.center_y = center_y


class Trampoline(Platform):
    """Платформа с батутом"""

    def __init__(self, center_x: int, center_y: int):
        super().__init__("assets/dynamic_pics/platform-trampoline.piskel.png", center_x, center_y)


class SimplePlatform(Platform):
    """Обычная платформа"""

    def __init__(self, center_x: int, center_y: int):
        super().__init__("assets/static_pics/platform.png", center_x, center_y)
