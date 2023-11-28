class TAPE:
    def __init__(self, name):
        self.name = name
        self.tape = []
        self.current_position = 0

    def get_current_symbol(self):
        return self.tape[self.current_position]

    def SCAN_RIGHT(self):
        self.current_position = self.current_position + 1
        return self.tape[self.current_position]

    def SCAN_LEFT(self):
        self.current_position = self.current_position - 1
        return self.tape[self.current_position]

    def move_left(self):
        self.current_position = self.current_position - 1
        self.ensure_size()
        return self.tape[self.current_position]

    def move_right(self):
        self.current_position = self.current_position + 1
        self.ensure_size()
        return self.tape[self.current_position]

    def ensure_size(self):
        if self.current_position >= len(self.tape):
            self.tape.append('#')
        elif self.current_position < 0:
            self.tape.insert(0, '#')

    def write(self, symbol):
        self.tape[self.current_position] = symbol

    def print_tape(self):
        print(self.tape)

    def RIGHT(self, input_val):
        self.move_right()
        self.write(input_val)

    def LEFT(self, input_val):
        self.move_left()
        self.write(input_val)

    def get_type(self):
        return "TAPE"

    def reset(self):
        self.tape = []
    
    def reset_pos(self):
        self.current_position = 0