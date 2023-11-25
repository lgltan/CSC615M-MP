from memory.stack import STACK
from memory.queue import QUEUE
from memory.tape import TAPE
from memory.tape2d import TAPE_2D
from util.state import State

class Machine:
    memory = []
    stateList = []
    currentState = 0

    def __init__(self, initialState):
        self.initialState = initialState
        self.currentState = 0
        self.stateList.append(initialState)

    def addState(self, state):
        self.stateList.append(state)

    def setCurrentState(self, currentState):
        for state_id, state in self.stateList:
            if state == currentState:
                self.currentState = state_id
