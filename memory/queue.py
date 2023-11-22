class QUEUE:
    def __init__(self, queue_name):
        self.queue_name = queue_name
        self.queue = []

    def EMPTY(self):
        self.queue = []
    
    def READ(self):
        if len(self.queue) == 0:
            print(f"QUEUE ERROR: {self.queue_name} is empty and cannot be read.")
            return
        return self.queue.pop(0)

    def WRITE(self, write_val):
        self.queue.append(write_val)

    def SCAN(self):
        return self.queue[0]