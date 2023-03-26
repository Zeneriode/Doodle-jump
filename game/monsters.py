"""
Реализация монстров.
Появляются через определённое количество платформ
Монстры прыгают на одном месте (на платформе)
При соприкосновение героя с монстром не с верху герой умирает (падает вниз)
"""
from arcade import Sprite
from constants import MONSTER_JUMP, G
from game_platforms import Platform


class Monster(Sprite):
    def __init__(self, file: str, platform: Platform):
        """Конструктор для монстров"""
        super().__init__(
            file,
            center_x=platform.center_x,
            center_y=platform.center_y + 250,
            hit_box_algorithm="Detailed",
        )
        self.__platform = platform

    def on_update(self, delta_time: float = 1 / 60):
        """Обновляет движение монстра"""
        self.change_y -= G * delta_time

        self.center_y += self.change_y

        self.__jump()

    def __jump(self):
        """Заставляет монстра прыгать"""
        if self.bottom <= self.__platform.top:
            self.change_y = MONSTER_JUMP


class Penguin(Monster):
    """
    Дописать # TODO дописать документацию для подклассов
    """

    def __init__(self, platform: Platform):
        super().__init__("assets\\dynamic_pics\\Monster_penguin.png", platform)


class Zombie(Monster):
    """
    Дописать # TODO дописать документацию для подклассов
    """

    def __init__(self, platform: Platform):
        super().__init__("assets\\dynamic_pics\\zombie.png", platform)


class Penguin2(Monster):
    """
    Дописать # TODO дописать документацию для подклассов
    """

    def __init__(self, platform: Platform):
        super().__init__("assets\\dynamic_pics\\penguin.png", platform)
