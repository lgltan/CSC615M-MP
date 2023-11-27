class TAPE:
    def __init__(self, name):
        self.name = name
        self.tape = ['#']
        self.tape_head = -1

    def EMPTY(self):
        self.tape = ['#']
        self.tape_head = -1

    def SCAN_LEFT(self):
        # if tape head is at 0
        if self.tape_head <= 0:
            self.tape_head = 0
            self.tape.insert(0, "#")
        else:
            self.tape_head = self.tape_head - 1
        
        return self.tape[self.tape_head]
    
    def SCAN_RIGHT(self):
        self.tape_head = self.tape_head + 1

        if len(self.tape) < self.tape_head + 1:
            self.tape.append("#")

        return self.tape[self.tape_head]
        

    def TAPE_RIGHT(self, input_val):
        self.tape_head = self.tape_head + 1

        if len(self.tape) < self.tape_head + 1:
            self.tape.append("#")
        
        self.tape[self.tape_head] = input_val
        
        return self.tape[self.tape_head]

    def TAPE_LEFT(self, input_val):
        if self.tape_head <= 0:
            self.tape_head = 0
            self.tape.insert(0, "#")
        else:
            self.tape_head = self.tape_head - 1

        self.tape[self.tape_head] = input_val
        
        return self.tape[self.tape_head]
