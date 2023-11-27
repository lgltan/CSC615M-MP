from random import randint

class State:
    def __init__(self, stateName, transition_type=None, memory_object=None):
        self.name = stateName
        self.transitions = {}
        self.memory_object = memory_object
        self.x = randint(20, 780) # max size of frame x is 800
        self.y = randint(20, 720) # max size of frame y is 740

        if memory_object != None:
            self.transition_type = f"{transition_type}-{memory_object.name}"
        else:
            self.transition_type = transition_type

    def addTransition(self, readChar, writeChar=None):
        if writeChar == None:
            writeChar = readChar
        self.transitions[readChar] = writeChar