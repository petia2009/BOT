class FieldXO:

    def __init__(self):
        self.__field__ = [
            ['-', '-', '-'],
            ['-', '-', '-'],
            ['-', '-', '-']
        ]
        self.count = 9
        self.size = 3

    def get_field(self):
        return self.__field__

    def fill_cell(self, x: int, y: int, cell_type: str) -> bool:
        if self.__field__[y][x] == '-':
            self.__field__[y][x] = cell_type
            self.count -= 1
            return True
        else:
            return False

    def has_empty_cell(self):
        return self.count != 0

    def is_winner(self, player_type: str):
        # проверка горизонтали
        for i in range(self.size):
            has_winner = False
            if self.__field__[i][0] != player_type:
                continue
            for j in range(1, self.size):
                if self.__field__[i][j] != player_type:
                    has_winner = False
                    break
                else:
                    has_winner = True
            if has_winner:
                return True

        # проверка вертикали
        for i in range(self.size):
            has_winner = False
            if self.__field__[0][i] != player_type:
                continue
            for j in range(1, self.size):
                if self.__field__[j][i] != player_type:
                    has_winner = False
                    break
                else:
                    has_winner = True
            if has_winner:
                return True

        # проверка диагоналей
        if (self.__field__[0][0] == player_type and self.__field__[2][2] == player_type) \
                or (self.__field__[0][2] == player_type and self.__field__[2][0] == player_type):
            return True

        return False


class Cell:

    def __str__(self) -> str:
        return 'Cell(x={0}, y={1})'.format(self.x, self.y)

    def __init__(self, x, y):
        self.x = x
        self.y = y

