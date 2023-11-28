class QUEUE:
    def __init__(self, name):
        self.name = name
        self.queue = ['#']

    def EMPTY(self):
        self.queue = ['#']
    
    def READ(self):
        if len(self.queue) == 0:
            print(f"QUEUE ERROR: {self.name} is empty and cannot be read.")
            return
        return self.queue.pop(0)
    
    def READ_TOP(self):
        if len(self.queue) == 0:
            print(f"QUEUE ERROR: {self.name} is empty and cannot be read.")
            return
        return self.queue[0]

    def WRITE(self, write_val):
        self.queue.append(write_val)

    def get_type(self):
        return "QUEUE"

    def reset(self):
        self.stack = ['#']
    
    def reset_pos(self):
        pass