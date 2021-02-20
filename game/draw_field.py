class Drawing_a_field:
    def __init__(self, field):
        self.field = field

    def draw_field(self):
        rendered_field = "```Ваш ход: x\n  0 1 2\n"
        for i in range(len(self.field)):
            for j in range(len(self.field)):
                if j == 0:
                    rendered_field += str(i) + " "
                if j != len(self.field) - 1:
                    rendered_field += self.field[i][j] + "|"
                else:
                    rendered_field += self.field[i][j]
            rendered_field += "\n"
        rendered_field += "```"
        return rendered_field
