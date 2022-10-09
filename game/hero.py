"""
Файл для работы с главным героем игры
Реализован класс главного героя с единственным конструктором.
Герой может прыгать, двигаться и стрелять.
"""
from arcade import Sprite, SpriteList
from constants import (
    HERO_JUMP,
    HERO_PLATFORMJUMP,
    HERO_SCALE,
    HERO_SLOWDOWN,
    HERO_SPEED,
    HERO_START_X,
    HERO_START_Y,
    HERO_TRAMPOLINE,
)
from game_platforms import PlatformJump, SimplePlatform, Trampoline


class Hero(Sprite):
    """Главный герой"""

    def __init__(self):
        """Конструктор для главного героя"""
        super().__init__(
            "assets/dynamic_pics/hero.piskel.png",
            HERO_SCALE,
            center_x=HERO_START_X,
            center_y=HERO_START_Y,
        )
        self.max_height = self.center_y
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
        self.max_height = max(self.max_height, self.center_y)

    def __jump(self, walls: SpriteList):
        """Заставляет героя прыгать"""
        for wall in walls:
            if (
                self.bottom <= wall.top < self.top
                and self.right > wall.left
                and self.left < wall.right
            ):
                if isinstance(wall, SimplePlatform):
                    self.change_y = HERO_JUMP
                elif isinstance(wall, PlatformJump):
                    self.change_y = HERO_PLATFORMJUMP
                elif isinstance(wall, Trampoline):
                    self.change_y = HERO_TRAMPOLINE
                """Указываем с какой силой герой должен отпрыгнутьот той или иной платформы"""
    def shoot(self):
        """Игрок стреляет в указанное направление"""
