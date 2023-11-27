from random import randint

class State:
    def __init__(self, stateName):
        self.name = stateName
        self.transitions = []
        self.pos_x = randint(20, 780) # max size of frame x is 800
        self.pos_y = randint(20, 480) # max size of frame y is 500
    
    def addTransition(self, readChar, writeChar=readChar):
        self.transitions.append((readChar, writeChar))