class TAPE_2D:
    def __init__(self, name):
        self.name = name
        self.tape = []
        self.tape_x = 0
        self.tape_y = 0

    def EMPTY(self):
        self.tape = []
        self.tape_x = 0

    def SCAN_LEFT(self):
        # if tape head is at 0
        if self.tape_x <= 0:
            self.tape_x = 0
            self.tape.insert(0, "#")
        else:
            self.tape_x = self.tape_x - 1
        
        return self.tape[self.tape_x]
    
    def SCAN_RIGHT(self):
        self.tape_x = self.tape_x + 1

        if len(self.tape) < self.tape_x + 1:
            self.tape.append("#")

        return self.tape[self.tape_x]
        

    def TAPE_RIGHT(self, input_val):
        self.tape_x = self.tape_x + 1

        if len(self.tape) < self.tape_x + 1:
            self.tape.append("#")
        
        self.tape[self.tape_x] = input_val
        
        return self.tape[self.tape_x]

    def TAPE_LEFT(self, input_val):
        if self.tape_x <= 0:
            self.tape_x = 0
            self.tape.insert(0, "#")
        else:
            self.tape_x = self.tape_x - 1

        self.tape[self.tape_x] = input_val
        
        return self.tape[self.tape_x]

    def TAPE_UP():
        return

    def TAPE_DOWN():
        return