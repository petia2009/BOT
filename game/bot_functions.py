import random


class BotsFunctions:
    counter = 0
    temp_arr = []

    def __init__(self, field):
        self.field = field

    def draw_field(self, field_to_render):
        rendered_field = "```Ваш ход: x\n  0 1 2\n"
        for i in range(len(field_to_render)):
            for j in range(len(field_to_render)):
                if j == 0:
                    rendered_field += str(i) + " "
                if j != len(field_to_render) - 1:
                    rendered_field += field_to_render[i][j] + "|"
                else:
                    rendered_field += field_to_render[i][j]
            rendered_field += "\n"
        rendered_field += "```"
        return rendered_field

    def computer_move_field(self):
        x = random.randint(0, 2)
        y = random.randint(0, 2)
        while not self.check_cell_is_free(x, y, self.field):
            x = random.randint(0, 2)
            y = random.randint(0, 2)
        self.field.change_field('o', x, y)
        return self.field.get_field()

    def check_cell_is_free(self, x, y, field):
        return field[int(y)][int(x)] != 'x' and field[int(y)][int(x)] != 'o'

    def check_for_win(self, field, player):
        for i in range(3):
            for j in range(3):
                self.temp_arr.append(field[j][i])

            for x in range(3):
                if self.temp_arr[x] == player:
                    self.counter += 1
            if self.counter == 3:
                return True
            else:
                self.counter = 0
                self.temp_arr = []

        for i in range(3):
            for j in range(3):
                self.temp_arr.append(field[i][j])
            for x in range(3):
                if self.temp_arr[x] == player:
                    self.counter += 1
            if self.counter == 3:
                return True
            else:
                self.counter = 0
                self.temp_arr = []

        cor_1_x = 0
        cor_1_y = 0
        cor_2_x = 1
        cor_2_y = 1
        cor_3_x = 2
        cor_3_y = 2
        for i in range(2):
            temp_arr_of_cor = [[cor_1_x, cor_1_y], [cor_2_x, cor_2_y], [cor_3_x, cor_3_y]]
            for j in range(3):
                self.temp_arr.append(field[temp_arr_of_cor[j][0]][temp_arr_of_cor[j][1]])
            for x in range(3):
                if self.temp_arr[x] == player:
                    self.counter += 1

            if self.counter == 3:
                return True
            else:
                self.counter = 0
                self.temp_arr = []
                cor_1_y = 2
                cor_3_y = 0
        return False

