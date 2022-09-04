from arcade import Sprite, SpriteList
from constants import (
    SCALE,
    HERO_START_X,
    HERO_START_Y,
    HERO_JUMP,
    HERO_SLOWDOWN
)


class Hero(Sprite):
    """Главный герой"""

    def __init__(self):
        """Конструктор для главного героя"""
        super().__init__("assets/dynamic_pics/hero.piskel.png", SCALE)
        self.center_x = HERO_START_X
        self.center_y = HERO_START_Y
        self.is_moved = False

    def on_update(self, delta_time: float = 1 / 60, walls: SpriteList = SpriteList()):
        """Обновляет движение героя"""
        if not self.is_moved:
            self.change_x /= HERO_SLOWDOWN

        self.__jump(walls)

    def __jump(self, walls: SpriteList):
        """Заставляет героя прыгать"""
        for wall in walls:
            if self.bottom <= wall.top < self.top and \
                    self.right > wall.left and self.left < wall.right:
                self.change_y = HERO_JUMP

    def shoot(self):
        pass
