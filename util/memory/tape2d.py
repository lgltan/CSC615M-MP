class TAPE_2D:
    def __init__(self, name, rows, cols):
        self.name = name
        self.tape = [['#' for _ in range(cols)] for _ in range(rows)]
        self.current_row = 0
        self.current_col = 0

    def EMPTY(self):
        return self.tape[self.current_row][self.current_col] == '#'

    def SCAN_LEFT(self):
        self.current_col -= 1
        if self.current_col < 0:
            self.current_col = 0

    def SCAN_RIGHT(self):
        self.current_col += 1
        if self.current_col >= len(self.tape[0]):
            self.current_col = len(self.tape[0]) - 1

    def TAPE_RIGHT(self, input_val):
        self.current_col += 1
        if self.current_col >= len(self.tape[0]):
            self.tape[0].append(input_val)

    def TAPE_LEFT(self, input_val):
        self.current_col -= 1
        if self.current_col < 0:
            self.tape[0].insert(0, input_val)
            self.current_col = 0

    def TAPE_UP(self, input_val):
        self.current_row -= 1
        if self.current_row < 0:
            self.tape.insert(0, [input_val for _ in range(len(self.tape[0]))])
            self.current_row = 0

    def TAPE_DOWN(self, input_val):
        self.current_row += 1
        if self.current_row >= len(self.tape):
            self.tape.append([input_val for _ in range(len(self.tape[0]))])

    def print_tape(self):
        for row in self.tape:
            print(' '.join(row))