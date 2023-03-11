"""
Реализация монстров.
Появляются через определённое количество платформ
Монстры прыгают на одном месте (на платформе)
При соприкосновение героя с монстром не с верху герой умирает (падает вниз)
"""
from arcade import Sprite
from game_platforms import Platform


class Monster(Sprite):
    def __init__(self, file: str, platform: Platform):
        """Конструктор для монстров"""
        super().__init__(file, center_x=platform.center_x, center_y=platform.center_y + 250,
                         hit_box_algorithm="Detailed")
        self.__platform = platform

    def on_update(self, delta_time: float = 1 / 60):
        """Обновляет движение монстра"""
        gravity = 25
        self.change_y -= gravity * delta_time

        self.center_y += self.change_y

        self.__jump()

    # TODO дописать код для прыжка монстра (делали в конце урока, надо вспомнить и повторить)
    def __jump(self):
        """Заставляет монстра прыгать"""
        if self.bottom <= self.__platform.top:


class Penguin(Monster):
    """
    Дописать
    """

    def __init__(self, platform: Platform):
        super().__init__("assets\\dynamic_pics\\Monster_penguin.png", platform)


class Zombie(Monster):
    """
    Дописать
    """

    def __init__(self, platform: Platform):
        super().__init__("assets\\dynamic_pics\\zombie.png", platform)


class Penguin2(Monster):
    """
    Дописать
    """

    def __init__(self, platform: Platform):
        super().__init__("assets\\dynamic_pics\\penguin.png", platform)
