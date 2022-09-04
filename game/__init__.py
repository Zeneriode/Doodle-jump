import game.main as main
from game.main import MyWindow


def start_game(color: tuple[int, int, int] = None):
    if color is not None:
        window = MyWindow(color)
    else:
        window = MyWindow()

    main.game(window)
