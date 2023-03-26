"""
Реализация игры "Doodle Jump" на компьютер.
"""
from game import main
from game.main import MyWindow


def start_game(color: tuple[int, int, int] = (0, 0, -1)):
    """Запуск игры с конкретным цветом для заднего фона"""
    if color != (0, 0, -1):
        window = MyWindow(color)
    else:
        window = MyWindow()

    main.game(window)
