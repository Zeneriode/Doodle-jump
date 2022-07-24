from arcade import PhysicsEnginePlatformer, Sprite, SpriteList, Window, color, key, run, set_background_color, \
    close_window


class MyWindow(Window):
    """Главное окно в игре"""

    def __init__(self, background: tuple[int, int, int] = color.PURPLE_NAVY):
        """Конструктор для создания обычного окна"""
        super().__init__(fullscreen=True)

        self.hero: Sprite = ...
        self.players: SpriteList = ...
        self.platforms: SpriteList = ...
        self.engine: PhysicsEnginePlatformer = ...

        set_background_color(background)

    def setup(self):
        """Загружает и создает все необходимые объекты для игры/уровня/режима"""
        self.hero = Sprite("assets/hero.piskel.png", 1)
        self.hero.center_x = 100
        self.hero.center_y = 1.40

        self.players = SpriteList()
        self.players.append(self.hero)

        platform = Sprite("assets/platform.png", 1)
        platform.center_x = 140
        platform.center_y = 70

        self.platforms = SpriteList(use_spatial_hash=True)
        self.platforms.append(platform)

        self.engine = PhysicsEnginePlatformer(self.hero, walls=self.platforms)

    def on_draw(self):
        """Прорисовка всех объектов и структур на экране"""
        self.clear()
        self.players.draw()

        self.platforms.draw()

    def on_key_press(self, symbol: int, modifiers: int):
        """Выполняет команды, связанные с кнопками. Вызывается при нажатии на любую клавишу"""
        # Выход из игры
        if symbol == key.ESCAPE:
            close_window()

    def on_update(self, delta_time: float):
        """Обновление местоположения всех объектов игры"""
        self.engine.update()

        self.hero: Sprite = ...
        self.players: SpriteList = ...

        set_background_color(background)

    def setup(self):
        """Загружает и создает все необходимые объекты для игры/уровня/режима"""
        self.hero = Sprite("assets/main_hero.png", 1)
        self.hero.center_x = 100
        self.hero.center_y = 100

        self.players = SpriteList()
        self.players.append(self.hero)

    def on_draw(self):
        """Прорисовка всех объектов и структур на экране"""
        self.clear()
        self.players.draw()


def game(window: MyWindow = MyWindow()):
    """Запускает игру"""
    window.setup()
    run()


if __name__ == "__main__":
    game()
