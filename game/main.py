"""
Главный файл игры - реализация класса окна.
Окно генерирует сцену для уровня.
Файл запускает игру, запуск используется для тестирования.
"""
from random import randint
from typing import Type, Union

from arcade import (
    Camera,
    Scene,
    Window,
    close_window,
    color,
    key,
    run,
    set_background_color,
)
from constants import CAMERA_SHIFT, COUNT_PLATFORMS, DECREASE_PLATFORMS_LEVEL_1
from game_platforms import Platform, PlatformJump, SimplePlatform, Trampoline
from hero import Hero
from numpy import array
from numpy.linalg import norm
from numpy.random import choice
from monsters import Penguin, Zombie, Penguin2
from pyglet.math import Vec2


class MyWindow(Window):
    """Главное окно в игре"""

    def __init__(self, background: tuple[int, int, int] = color.PURPLE_NAVY):
        """Конструктор для создания обычного окна"""
        super().__init__(fullscreen=True)

        self.hero: Hero = ...
        self.scene: Scene = ...
        self.camera: Camera = ...
        self.number_of_platforms: int = 0
        self.count_platforms: int = 0

        set_background_color(background)

    def setup(self):
        """Загружает и создает все необходимые объекты для игры/уровня/режима"""
        self.hero = Hero()

        self.scene = Scene()
        self.scene.add_sprite("Players", self.hero)
        self.scene.add_sprite_list("Walls", True)
        self.scene.add_sprite_list("Monsters")
        self.scene.add_sprite("Walls", SimplePlatform(1200, 570))
        self.scene.add_sprite("Walls", SimplePlatform(650, 190))
        self.scene.add_sprite("Walls", SimplePlatform(200, 250))
        self.number_of_platforms = 3
        self.count_platforms = COUNT_PLATFORMS
        self.camera = Camera(self.width, self.height)
        self.camera.move(
            Vec2(0, self.hero.center_y - self.camera.viewport_height / CAMERA_SHIFT)
        )

    def on_draw(self):
        """Прорисовка всех объектов и структур на экране"""
        self.clear()
        self.camera.use()
        self.scene.draw()

    def on_key_press(self, symbol: int, modifiers: int):
        """Выполняет команды, связанные с кнопками. Вызывается при нажатии на любую клавишу"""
        # Выход из игры
        if symbol == key.ESCAPE:
            close_window()
            return

        # движение вправо и влево
        if symbol in (key.D, key.RIGHT):
            self.hero.change_x = self.hero.speed
            self.hero.is_moved = True
        elif symbol in (key.A, key.LEFT):
            self.hero.change_x = -self.hero.speed
            self.hero.is_moved = True

    def on_key_release(self, symbol: int, modifiers: int):
        """Выполняет команды, связанные с кнопками. Вызывается при отжатии клавиш"""
        # замедление при бездействии
        self.hero.is_moved = False

    def camera_under_control(self):
        """Смещаем камеру, когда главному герою это нужно"""
        # Камера поднимается за героем, вниз камера не опускается
        if self.hero.change_y > 0 and self.hero.center_y >= self.hero.max_height:
            self.camera.move(
                Vec2(0, self.hero.center_y - self.camera.viewport_height / CAMERA_SHIFT)
            )

    def new_platforms(self):
        """Добавляет нужные платформы"""
        if self.count_platforms > len(self.scene["Walls"]):
            self.number_of_platforms += 1
            coordinates = self.generate_platform_coordinates()
            platform_type = self.generate_type_platform()
            self.scene.add_sprite(
                "Walls", platform_type(coordinates[0], coordinates[1])
            )

    def generate_type_platform(
            self,
    ) -> Type[Union[SimplePlatform, PlatformJump, Trampoline]]:
        """Генерирует тип платформы"""
        simple_platforms_in_row = 12
        if self.number_of_platforms % simple_platforms_in_row:
            return SimplePlatform

        return choice([PlatformJump, Trampoline])

    # TODO проверить на ошибки от линтера и исправить их
    def generate_platform_coordinates(self) -> tuple:
        """Генерирует случайные координаты для новой платформы"""
        # pylint: disable=magic-value-comparison
        min_height_to_create = int(self.hero.max_height) + 300
        max_height_to_create = min_height_to_create + 600

        platform_x = randint(160, self.width - 160)
        platform_y = randint(min_height_to_create, max_height_to_create)

        while not self.check_platform_valid_coordinates(platform_x, platform_y):
            platform_x = randint(160, self.width - 160)
            platform_y = randint(min_height_to_create, max_height_to_create)

        return platform_x, platform_y

    def check_platform_valid_coordinates(self, platform_x: int, platform_y: int) -> bool:
        """
        Проверяет, что новая платформа не пересекает другие\n
        :param platform_x: координата новой платформы по Х
        :param platform_y: координата новой платформы по Y
        :return: False, если новая платформа пересекает другие; True, если всё хорошо
        """
        min_distance_between_platforms = 500
        min_distance = min_distance_between_platforms + 1
        for wall in self.scene["Walls"]:
            distance = norm(
                array([wall.center_x, wall.center_y]) - array([platform_x, platform_y])
            )
            min_distance = min(min_distance, distance)
        return min_distance > min_distance_between_platforms

    def delete_platforms(self):
        """Удаляет бесполезные платформы"""
        camera_y = self.camera.position[1]
        platforms = self.scene["Walls"]
        platforms_number = len(platforms)

        for i in range(platforms_number - 1, -1, -1):
            if platforms[i].center_y < camera_y:
                platforms.pop(i)

    # TODO проверить на жалобы от линтера
    def new_monster(self):
        """Добавление монстра в игру"""
        valid_for_creation = 3
        if self.number_of_platforms % valid_for_creation or len(self.scene["Monsters"]):
            return

        platform_for_monster = self.find_platform_for_monster()
        if platform_for_monster is None:
            return

        monsters = [Penguin, Zombie, Penguin2]
        monster = choice(monsters)(platform_for_monster)
        self.scene.add_sprite("Monsters", monster)

    # TODO проверить на жалобы от линтера
    def find_platform_for_monster(self) -> Platform or None:
        """Ищет платформу, на которой может появится монстр"""
        for wall in self.scene["Walls"]:
            wall: Platform
            if wall.center_y > self.camera.position[1] + self.height:
                return wall
        return None

    # TODO проверить на жалобы от линтера
    def delete_monster(self):
        """Удаление монстра"""
        monsters = self.scene["Monsters"]
        if not len(monsters):
            return

        camera_y = self.camera.position[1]

        if monsters[0].center_y < camera_y:
            monsters.pop()

    # Не трогать, даже если линтер жалуется
    def who_is_killed(self):
        """Проверка пересечения героя и монстров + убийство одного из них"""

    # TODO проверить на жалобы от линтера
    def on_update(self, delta_time: float):
        """Обновление местоположения всех объектов игры"""
        if self.is_fallen():
            close_window()
        if (
                self.number_of_platforms == DECREASE_PLATFORMS_LEVEL_1
                and self.count_platforms > COUNT_PLATFORMS - 1
        ):
            self.count_platforms -= 1
        self.hero.on_update(walls=self.scene["Walls"])
        for monster in self.scene["Monsters"]:
            monster.on_update()
        self.camera_under_control()
        self.hero_stay_visible()
        self.delete_platforms()
        self.new_platforms()
        self.delete_monster()
        self.new_monster()

    def is_fallen(self) -> bool:
        """Проверяет, упал ли герой"""
        return self.hero.top < self.hero.max_height - self.camera.viewport_height

    def hero_stay_visible(self):
        """Возвращает героя, если он вышел за боковые границы"""
        if self.hero.right < 0:
            self.hero.center_x = self.width
        if self.hero.left > self.width:
            self.hero.center_x = 0


def game(window: MyWindow = MyWindow()):
    """Запускает игру"""
    window.setup()
    run()


if __name__ == "__main__":
    game()
