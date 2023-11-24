class State:
    def __init__(self, stateName):
        self.name = stateName
        self.transitions = []
    
    def addTransition(self, inputChar, outputChar):
        self.transitions.append(inputChar, outputChar)

    # mem? : Memory,
    # command : string,
    # accept : boolean,
    # initial : boolean,
    # run: () => StateOutput[]
    # isActive : boolean,
    # isND: boolean,
    # type: StateType