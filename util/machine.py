from util.memory.stack import STACK
from util.memory.queue import QUEUE
from util.memory.tape import TAPE
from util.memory.tape2d import TAPE_2D
from util.state import State

import re
import random

class Machine:
    memory = []
    stateList = []
    currentState = None
    input_tape = []
    current_input = 0
    output_tape = []
    current_output = 0

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

        # accept state is needed for accepters but not necessarily needed for transducers, so just check if there's an accept state and create it if there is one.
        if found_accept:
            self.stateList.append(State("accept"))
        # always need a reject state even if there's no connection that goes to it, in case the input alphabet isn't followed.
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
                transition_type = "S"
            elif "READ" in logic:
                transition_type = "R"
            elif "WRITE" in logic:
                transition_type = "W"
            elif "PRINT" in logic:
                transition_type = "P"
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
                temp_str = transition.replace(" ", "")
                temp = temp_str.split(",")
                cleaned_temp = [i for i in temp if i != "" or i != " "]
                state.addTransition(cleaned_temp[1], cleaned_temp[0])

            self.stateList.append(state)

            # initialize currentState
            if self.currentState == None:
                self.currentState = state

    def addState(self, state):
        self.stateList.append(state)

    def next_input(self, input_val):
        # Check if the current state is accepting or rejecting
        if self.currentState.name == "accept":
            print("Machine has accepted the input.")
            return True
        elif self.currentState.name == "reject":
            print("Machine has rejected the input.")
            return False
        
        # Check if the input value is a valid transition for the current state
        valid_input = False

        for transition_key, transition_val in self.currentState.transitions.items():
            if input_val in transition_val:
                valid_input = True

        if not valid_input:
            for state in self.stateList:
                if state.name == "reject":
                    self.currentState = state

        # Get all possible next states for the input value
        possible_next_states = []

        for state_key, state_val in self.currentState.transitions.items():
            if input_val in state_val:
                for state in self.stateList:
                    if state.name == state_key:
                        possible_next_states.append(state)

        # Choose one next state nondeterministically
        if possible_next_states:
            next_state = random.choice(possible_next_states)
            prevState = self.currentState
            self.currentState = next_state

            if prevState.transition_type == "R":
                for mem_obj in self.memory:
                    if prevState.memory_object == mem_obj.name:
                        mem_obj.READ()
            elif prevState.transition_type == "W":
                for mem_obj in self.memory:
                    if prevState.memory_object == mem_obj.name:
                        mem_obj.WRITE(input_val)
            elif prevState.transition_type == "SR":
                for mem_obj in self.memory:
                    if prevState.memory_object == mem_obj.name:
                        mem_obj.SCAN_RIGHT()
            elif prevState.transition_type == "SL":
                for mem_obj in self.memory:
                    if prevState.memory_object == mem_obj.name:
                        mem_obj.SCAN_LEFT()
            elif prevState.transition_type == "S":
                for mem_obj in self.memory:
                    if prevState.memory_object == mem_obj.name:
                        mem_obj.SCAN()
            elif prevState.transition_type == "P":
                for mem_obj in self.memory:
                    if prevState.memory_object == mem_obj.name:
                        mem_obj.PRINT()
            elif prevState.transition_type == "UP":
                for mem_obj in self.memory:
                    if prevState.memory_object == mem_obj.name:
                        mem_obj.TAPE_UP(input_val)
            elif prevState.transition_type == "DOWN":
                for mem_obj in self.memory:
                    if prevState.memory_object == mem_obj.name:
                        mem_obj.TAPE_DOWN(input_val)
            elif prevState.transition_type == "LEFT":
                for mem_obj in self.memory:
                    if prevState.memory_object == mem_obj.name:
                        mem_obj.TAPE_LEFT(input_val)
            elif prevState.transition_type == "RIGHT":
                for mem_obj in self.memory:
                    if prevState.memory_object == mem_obj.name:
                        mem_obj.TAPE_RIGHT(input_val)
            else:
                print(f"ERR: Invalid transition_type {self.currentState.transition_type}")

            # Return True if the machine is still in a valid state, False otherwise
            return not (self.currentState.name == "accept" or self.currentState.name == "reject")
        else:
            for state in self.stateList:
                if state.name == "reject":
                    self.currentState = state
            print(f"Error: No valid transition for input '{input_val}' in state '{self.currentState.name}'.")