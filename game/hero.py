"""
Файл для работы с главным героем игры
Реализован класс главного героя с единственным конструктором.
Герой может прыгать, двигаться и стрелять.
"""
from arcade import Sprite, SpriteList, load_texture
from constants import (
    HERO_JUMP,
    HERO_PLATFORMJUMP,
    HERO_SLOWDOWN,
    HERO_SPEED,
    HERO_START_X,
    HERO_START_Y,
    HERO_TRAMPOLINE,
    SCALE,
    G,
)
from game_platforms import PlatformJump, SimplePlatform, Trampoline


class Hero(Sprite):
    """Главный герой"""

    def __init__(self):
        """Конструктор для главного героя"""
        super().__init__(
            "assets/dynamic_pics/hero.piskel.down.png",
            SCALE,
            hit_box_algorithm="Detailed",
        )
        self.change_x = 0
        self.change_y = 0
        self.center_x = HERO_START_X
        self.center_y = HERO_START_Y
        self.max_height = self.center_y
        self.is_moved = False
        self.speed = HERO_SPEED
        self.slowdown = HERO_SLOWDOWN
        self.alive = True
        self.__load_textures()

    def __load_textures(self):
        """Текстуры для динамических картинок(параметры для картинокк)"""
        texture_facing_left = load_texture(
            "assets/dynamic_pics/hero.piskel.down.png", flipped_horizontally=True
        )
        self.textures.append(texture_facing_left)

        texture_facing_right_short_legs = load_texture(
            "assets/dynamic_pics/hero.piskel.up.png"
        )
        self.textures.append(texture_facing_right_short_legs)

        texture_facing_left_short_legs = load_texture(
            "assets/dynamic_pics/hero.piskel.up.png", flipped_horizontally=True
        )
        self.textures.append(texture_facing_left_short_legs)

    def __update_animation(self):
        """отвечает за анимацию в игре"""
        face_to_left = self.change_x < 0

        short_legs = self.change_y >= 0

        self.texture = self.textures[face_to_left + short_legs * 2]

    def on_update(self, delta_time: float = 1 / 60, walls: SpriteList = SpriteList()):
        """Обновляет движение героя"""
        self.change_y -= G * delta_time
        if self.alive:
            self.__update_animation()

            self.__jump(walls)

        if not self.is_moved:
            self.change_x /= self.slowdown

        self.center_x += self.change_x
        self.center_y += self.change_y

        self.max_height = max(self.max_height, self.center_y)

    def __jump(self, walls: SpriteList):
        """Заставляет героя прыгать"""
        for wall in walls:
            if (
                self.bottom <= wall.top < self.bottom + 30
                and self.right > wall.left + 70
                and self.left < wall.right - 20
                and self.change_y < 0
            ):
                """Указываем с какой силой герой должен отпрыгнуть от той или иной платформы"""
                if isinstance(wall, SimplePlatform):
                    self.change_y = HERO_JUMP
                elif isinstance(wall, PlatformJump):
                    self.change_y = HERO_PLATFORMJUMP
                elif isinstance(wall, Trampoline):
                    self.change_y = HERO_TRAMPOLINE

    def shoot(self):
        """Игрок стреляет в указанное направление"""
