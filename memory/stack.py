class STACK:
    def __init__(self, stack_name):
        self.stack_name = stack_name
        self.stack = []

    def EMPTY(self):
        self.stack = []
    
    def READ(self):
        if len(self.stack) == 0:
            print(f"STACK ERROR: {self.stack_name} is empty and cannot be read.")
            return
        return self.stack.pop()

    def WRITE(self, write_val):
        self.stack.append(write_val)

    def SCAN(self):
        return self.stack[-1]