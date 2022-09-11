"""
Файл для работы с главным героем игры
Реализован класс главного героя с единственным конструктором.
Герой может прыгать, двигаться и стрелять.
"""
from arcade import Sprite, SpriteList
from constants import (
    HERO_JUMP,
    HERO_SLOWDOWN,
    HERO_SPEED,
    HERO_START_X,
    HERO_START_Y,
    SCALE,
)


class Hero(Sprite):
    """Главный герой"""

    def __init__(self):
        """Конструктор для главного героя"""
        super().__init__(
            "assets/dynamic_pics/hero.piskel.png",
            SCALE,
            center_x=HERO_START_X,
            center_y=HERO_START_Y,
        )
        self.is_moved = False
        self.speed = HERO_SPEED
        self.change_x = 0
        self.change_y = 0
        self.slowdown = HERO_SLOWDOWN

    def on_update(self, delta_time: float = 1 / 60, walls: SpriteList = SpriteList()):
        """Обновляет движение героя"""
        if not self.is_moved:
            self.change_x /= self.slowdown

        self.__jump(walls)

    def __jump(self, walls: SpriteList):
        """Заставляет героя прыгать"""
        for wall in walls:
            if (
                self.bottom <= wall.top < self.top
                and self.right > wall.left
                and self.left < wall.right
            ):
                self.change_y = HERO_JUMP

    def shoot(self):
        """Игрок стреляет в указанное направление"""