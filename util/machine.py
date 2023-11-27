from util.memory.stack import STACK
from util.memory.queue import QUEUE
from util.memory.tape import TAPE
from util.memory.tape2d import TAPE_2D
from util.state import State

import re

class Machine:
    memory = []
    stateList = []
    currentState = 0

    def __init__(self, data_arr, logic_arr):
        # init auxiliary memory
        for data in data_arr:
            mem_type, mem_name = data
            if mem_type == "STACK":
                self.memory.append(STACK(mem_name))
            elif mem_type == "QUEUE":
                self.memory.append(QUEUE(mem_name))
            elif mem_type == "TAPE":
                self.memory.append(TAPE(mem_name))
            elif mem_type == "2D_TAPE":
                self.memory.append(TAPE_2D(mem_name))
            else:
                print(f"ERR: Invalid Auxiliary Memory name {mem_type}")

        found_accept = [string for string in logic_arr if "accept" in string]
        found_reject = [string for string in logic_arr if "reject" in string]

        if found_accept:
            self.stateList.append(State("accept"))

        if found_reject:
            self.stateList.append(State("reject"))

        # init stateList and connections
        for logic in logic_arr:
            state = None
            transition_type = None
            memory_object = None

            # get state_name
            transition_list = logic.split("]")
            state_name = transition_list[0]
            transition_list.remove(state_name)

            # set transition type
            if "SCAN RIGHT" in logic:
                transition_type = "SR"
            elif "SCAN LEFT" in logic:
                transition_type = "SL"
            elif "SCAN" in logic:
                transition_type = "SCAN"
            elif "READ" in logic:
                transition_type = "READ"
            elif "WRITE" in logic:
                transition_type = "WRITE"
            elif "PRINT" in logic:
                transition_type = "PRINT"
            elif "UP" in logic:
                transition_type = "UP"
            elif "DOWN" in logic:
                transition_type = "DOWN"
            elif "LEFT" in logic:
                transition_type = "LEFT"
            elif "RIGHT" in logic:
                transition_type = "RIGHT"
            else:
                print(f"ERR: No transition found in {logic}")

            state = State(stateName=state_name, transition_type=transition_type, memory_object=memory_object)

            # get only strings surrounded by parenthesis
            in_parenthesis = re.findall(r'\((.*?)\)', logic)

            # get memory object
            if "READ" in logic or "WRITE" in logic or "RIGHT" in logic or "LEFT" in logic or "UP" in logic or "DOWN" in logic:
                state.memory_object = in_parenthesis[0]
                in_parenthesis.remove(in_parenthesis[0])

            for transition in in_parenthesis:
                temp = transition.split(",")
                cleaned_temp = [i for i in temp if i != "" or i != " "]
                state.addTransition(cleaned_temp[1], cleaned_temp[0])

            self.stateList.append(state)

        self.currentState = self.stateList[0]

    def addState(self, state):
        self.stateList.append(state)