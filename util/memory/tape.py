class TAPE:
    def __init__(self, name):
        self.name = name
        self.tape = ['#']
        self.current_position = 0

    def get_current_symbol(self):
        return self.tape[self.current_position]

    def move_left(self):
        self.current_position = max(0, self.current_position - 1)
        self.ensure_size()

    def move_right(self):
        self.current_position = min(len(self.tape) - 1, self.current_position + 1)
        self.ensure_size()

    def ensure_size(self):
        if self.current_position == len(self.tape):
            self.tape.append('#')

    def write(self, symbol):
        self.tape[self.current_position] = symbol

    def print_tape(self):
        line = ''.join(self.tape)
        line = line[:self.current_position] + '[' + line[self.current_position] + ']' + line[self.current_position + 1:]
        print(line)

    def RIGHT(self, input_val):
        self.move_right()
        self.write(input_val)

    def LEFT(self, input_val):
        self.move_left()
        self.write(input_val)

    def get_type(self):
        return "TAPE"