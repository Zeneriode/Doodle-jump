"""
Главный файл игры - реализация класса окна.
Окно генерирует сцену для уровня.
Файл запускает игру, запуск используется для тестирования.
"""
from arcade import (
    Camera,
    PhysicsEnginePlatformer,
    Scene,
    Window,
    close_window,
    color,
    key,
    run,
    set_background_color,
)
from game_platforms import PlatformJump, SimplePlatform, Trampoline
from hero import Hero


class MyWindow(Window):
    """Главное окно в игре"""

    def __init__(self, background: tuple[int, int, int] = color.PURPLE_NAVY):
        """Конструктор для создания обычного окна"""
        super().__init__(fullscreen=True)

        self.hero: Hero = ...
        self.scene: Scene = ...
        self.camera: Camera = ...
        self.engine: PhysicsEnginePlatformer = ...

        set_background_color(background)

    def setup(self):
        """Загружает и создает все необходимые объекты для игры/уровня/режима"""
        self.hero = Hero()

        self.scene = Scene()
        self.scene.add_sprite("Players", self.hero)
        self.scene.add_sprite_list("Walls", True)
        self.scene.add_sprite("Walls", SimplePlatform(1200, 170))
        self.scene.add_sprite("Walls", Trampoline(650, 190))
        self.scene.add_sprite("Walls", PlatformJump(200, 250))

        self.camera = Camera(960, 540)
        self.engine = PhysicsEnginePlatformer(self.hero, walls=self.scene["Walls"])

    def on_draw(self):
        """Прорисовка всех объектов и структур на экране"""
        self.clear()
        self.scene.draw()
        self.camera.use()

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
        pass

    def on_update(self, delta_time: float):
        """Обновление местоположения всех объектов игры"""
        self.hero.on_update(walls=self.scene["Walls"])
        self.engine.update()
        self.camera_under_control()


def game(window: MyWindow = MyWindow()):
    """Запускает игру"""
    window.setup()
    run()


if __name__ == "__main__":
    game()
