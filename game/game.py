from game.field import FieldXO
from game.player import Player, Bot


class Game:

    __field__: FieldXO = None
    __status__: bool = False
    __active_player__: Player

    def __init__(self, player_x_id: str, player_o_id: str):
        self.__playerX__ = self.__create_player(player_x_id, 'X')
        self.__playerO__ = self.__create_player(player_o_id, 'O')
        self.__active_player__ = self.__playerX__

    @staticmethod
    def __create_player(player_id: str, player_type: str) -> Player:
        if player_id == 'bot':
            return Bot(player_type=player_type)
        else:
            return Player(player_id=player_id, player_type=player_type)

    def change_status(self, status: bool):
        self.__status__ = status

    def get_status(self):
        return self.__status__

    def get_field(self):
        return self.__field__

    def new_game(self):
        self.__field__ = FieldXO()
        self.__status__ = True

    def end_game(self):
        self.__field__ = None
        self.__status__ = False

    def __player_move(self, x: int, y: int, player: Player) -> bool:
        if player.get_player_id() == self.__active_player__.get_player_id():
            if self.__field__.fill_cell(x, y, player.get_player_type()):
                self.__change_active_player()
                return True
            else:
                return False
        else:
            return False

    def __change_active_player(self):
        if self.__active_player__ == self.__playerX__:
            self.__active_player__ = self.__playerO__
        else:
            self.__active_player__ = self.__playerX__

    def provide_player_move(self, x: int, y: int, player_id: str) -> str:
        player = self.__define_player(player_id)
        if not self.__player_move(x, y, player):
            return "Клетка занята! или не ваш ход"
        if self.get_field().is_winner(player_type=player.get_player_type()):
            self.change_status(status=False)
            return "Вы выиграли!"
        if not self.get_field().has_empty_cell():
            self.change_status(status=False)
            return "Ничья"
        else:
            if self.__active_player__.get_player_id() == 'bot':
                player = self.__active_player__
                self.__bot_move(player)
                if self.get_field().is_winner(player_type=player.get_player_type()):
                    self.change_status(status=False)
                    return "Вы проиграли!"
                if not self.get_field().has_empty_cell():
                    self.change_status(status=False)
                    return "Ничья"
                return "Ваш ход"
        return "ожидание хода другого игрока"

    def __define_player(self, player_id: str) -> Player:
        if self.__playerX__.__player_id__ == player_id:
            return self.__playerX__
        elif self.__playerO__.__player_id__ == player_id:
            return self.__playerO__
        else:
            raise Exception('Не найден игрок с id={0}'.format(player_id))

    def __bot_move(self, player: Player):
        cell = player.get_move_cell(self.__field__)
        if not self.__player_move(cell.x, cell.y, player):
            raise Exception('Игровой бот сломался, выдает неправильные координаты хода, '
                            'cell={0} или не его ход, active_player={1}'.format(cell, self.__active_player__))

