"""
Реализация монстров.
(Где и когда появляются)
(Основные действия - что могут белать)
Некоторые монстры могут выдерживать несколько ударов
С какой силой монстр отпрыгивает от плаформы?
Смерть злодея - падает вниз
Как двигаются монстры?
"""
# TODO дописать описание файла
# TODO подправить размеры картинок с пингвинами
from arcade import Sprite


class Monster(Sprite):
    def __init__(self, file: str, center_x: float, center_y: float):
        """Конструктор для монстров"""
        super().__init__(file, center_x=center_x, center_y=center_y, hit_box_algorithm="Detailed")


class Penguin(Monster):
    """
    Дописать
    """
    def __init__(self, center_x: float, center_y: float):
        super().__init__("assets\\dynamic_pics\\Monster_penguin.png", center_x, center_y)


class Zombie(Monster):
    """
    Дописать
    """
    def __init__(self, center_x: float, center_y: float):
        super().__init__("assets\\dynamic_pics\\zombie.png", center_x, center_y)


class Penguin2(Monster):
    """
    Дописать
    """
    def __init__(self, center_x: float, center_y: float):
        super().__init__("assets\\dynamic_pics\\penguin.png", center_x, center_y)
