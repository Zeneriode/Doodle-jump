from arcade import (
    PhysicsEnginePlatformer,
    Scene,
    Sprite,
    Window,
    color,
    key,
    run,
    set_background_color,
    close_window,
)


class MyWindow(Window):
    """Главное окно в игре"""

    def __init__(self, background: tuple[int, int, int] = color.PURPLE_NAVY):
        """Конструктор для создания обычного окна"""
        super().__init__(fullscreen=True)

        self.hero: Sprite = ...
        self.engine: PhysicsEnginePlatformer = ...
        self.scene: Scene = ...

        set_background_color(background)

    def setup(self):
        """Загружает и создает все необходимые объекты для игры/уровня/режима"""
        self.hero = Sprite("assets/dynamic_pics/hero.piskel.png", 1)
        self.hero.center_x = 100
        self.hero.center_y = 740

        platform = Sprite("assets/static_pics/platform.png", 1)
        platform.center_x = 140
        platform.center_y = 70

        self.scene = Scene()
        self.scene.add_sprite("Players", self.hero)
        self.scene.add_sprite_list("Walls", True)
        self.scene.add_sprite("Walls", platform)

        self.engine = PhysicsEnginePlatformer(self.hero, walls=self.scene["Walls"])

    def on_draw(self):
        """Прорисовка всех объектов и структур на экране"""
        self.clear()
        self.scene.draw()

    def on_key_press(self, symbol: int, modifiers: int):
        """Выполняет команды, связанные с кнопками. Вызывается при нажатии на любую клавишу"""
        # Выход из игры
        if symbol == key.ESCAPE:
            close_window()

    def on_update(self, delta_time: float):
        """Обновление местоположения всех объектов игры"""
        self.engine.update()


def game(window: MyWindow = MyWindow()):
    """Запускает игру"""
    window.setup()
    run()


if __name__ == "__main__":
    game()
