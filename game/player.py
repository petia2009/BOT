from game.field import FieldXO, Cell
import random


class Player:

    def __str__(self) -> str:
        return 'Player(id={0}, type={1})'.format(self.__player_id__, self.__player_type__)

    def __init__(self, player_type: str, player_id: str):
        self.__player_type__ = player_type
        self.__player_id__ = player_id

    def get_player_type(self):
        return self.__player_type__

    def get_player_id(self):
        return self.__player_id__

    def get_move_cell(self, field: FieldXO) -> Cell:
        return Cell(-1, -1)


class Bot(Player):

    def __init__(self, player_type: str):
        super().__init__(player_type, 'bot')

    def get_move_cell(self, field: FieldXO) -> Cell:
        x = random.randint(0, 2)
        y = random.randint(0, 2)
        while not field.get_field()[int(y)][int(x)] == '-':
            x = random.randint(0, 2)
            y = random.randint(0, 2)
        return Cell(x, y)
