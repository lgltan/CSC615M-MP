class TAPE_2D:
    def __init__(self, name):
        self.name = name
        self.tape = [['#']]
        self.current_row = 0
        self.current_col = 0

    def get_current_symbol(self):
        return self.tape[self.current_row][self.current_col]

    def move_left(self):
        self.current_col = max(0, self.current_col - 1)
        self.ensure_columns()

    def move_right(self):
        self.current_col = min(len(self.tape[0]) - 1, self.current_col + 1)
        self.ensure_columns()

    def move_up(self):
        self.current_row = max(0, self.current_row - 1)
        self.ensure_rows()

    def move_down(self):
        self.current_row = min(len(self.tape) - 1, self.current_row + 1)
        self.ensure_rows()

    def ensure_columns(self):
        if self.current_col == len(self.tape[0]):
            for row in self.tape:
                row.append('#')

    def ensure_rows(self):
        if self.current_row == len(self.tape):
            self.tape.append(['#'] * len(self.tape[0]))

    def write(self, symbol):
        self.tape[self.current_row][self.current_col] = symbol

    def print_tape(self):
        for i, row in enumerate(self.tape):
            line = ' '.join(row)
            if i == self.current_row:
                line = line[:2 * self.current_col] + '[' + line[2 * self.current_col] + ']' + line[2 * self.current_col + 2:]
            print(line)

    def RIGHT(self, input_val):
        self.move_right()
        self.write(input_val)

    def LEFT(self, input_val):
        self.move_left()
        self.write(input_val)

    def UP(self, input_val):
        self.move_up()
        self.write(input_val)

    def DOWN(self, input_val):
        self.move_down()
        self.write(input_val)

    def get_type(self):
        return "TAPE_2D"