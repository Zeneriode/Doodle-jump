"""
Реализация игры "Doodle Jump" на компьютер.
"""
from game import main
from game.main import MyWindow


def start_game(color: tuple[int, int, int] = None):
    """Запуск игры с конкретным цветом для заднего фона"""
    if color is not None:
        window = MyWindow(color)
    else:
        window = MyWindow()

    main.game(window)
