class STACK:
    def __init__(self, name):
        self.name = name
        self.stack = ['#']

    def EMPTY(self):
        self.stack = ['#']
    
    def READ(self):
        if len(self.stack) == 0:
            print(f"STACK ERROR: {self.name} is empty and cannot be read.")
            return
        return self.stack.pop()

    def READ_TOP(self):
        if len(self.stack) == 0:
            print(f"STACK ERROR: {self.name} is empty and cannot be read.")
            return
        return self.stack[-1]

    def WRITE(self, write_val):
        self.stack.append(write_val)

    def get_type(self):
        return "STACK"

    def reset(self):
        self.stack = ['#']
    
    def reset_pos(self):
        pass