from game.bot_functions import BotsFunctions


class Game:
    __status__ = False
    __field__ = [
        ['-', '-', '-'],
        ['-', '-', '-'],
        ['-', '-', '-']
    ]

    __bot_functions__ = BotsFunctions(__field__)

    def __init__(self):
        self.__status__ = False

    def change_status(self, status: bool):
        self.__status__ = status

    def change_field(self, player, x, y):
        self.__field__[y][x] = player
        print(self.__field__)

    def get_status(self):
        return self.__status__

    def get_field(self):
        return self.__field__

    def update_field(self):
        self.__field__ = [
            ['-', '-', '-'],
            ['-', '-', '-'],
            ['-', '-', '-']
        ]




