"""
Файл для реализации платформ.
В файле созданы высший класс для всех платформ и 2 класса конкретных платформ.
"""
from arcade import Sprite
from constants import SCALE


class Platform(Sprite):
    """Высший класс платформ"""

    def __init__(self, file: str, center_x: float, center_y: float):
        """Конструктор для платформ"""
        super().__init__(file, SCALE, center_x=center_x, center_y=center_y, hit_box_algorithm="Detailed")


class Trampoline(Platform):
    """Платформа с батутом"""

    def __init__(self, center_x: float, center_y: float):
        """Базовый конструктор для платформы с батутом"""
        super().__init__(
            "assets/dynamic_pics/platform-trampoline.piskel.png", center_x, center_y
        )


class SimplePlatform(Platform):
    """Обычная платформа"""

    def __init__(self, center_x: float, center_y: float):
        """Базовый конструктор для обычной платформы"""
        super().__init__("assets/static_pics/platform.png", center_x, center_y)


class PlatformJump(Platform):
    """Платформа с пружинкой"""

    def __init__(self, center_x: float, center_y: float):
        super().__init__(
            "assets/dynamic_pics/platformjump.piskel.png", center_x, center_y
        )
