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

            # get only strings surrounded by parenthesis
            in_parenthesis = re.findall(r'\((.*?)\)', logic)

            # get memory object
            if "READ" in logic or "WRITE" in logic or "RIGHT" in logic or "LEFT" in logic or "UP" in logic or "DOWN" in logic:
                memory_object = in_parenthesis[0]
                in_parenthesis.remove(in_parenthesis[0])

            state = State(stateName=state_name, transition_type=transition_type, memory_object=memory_object)

            for transition in in_parenthesis:
                temp_str = transition.replace(" ", "")
                temp = temp_str.split(",")
                cleaned_temp = [i for i in temp if i != "" or i != " "]
                state.addTransition(cleaned_temp[1], cleaned_temp[0])

            self.stateList.append(state)

            # initialize currentState
            if self.currentState == None:
                self.currentState = state
                self.initial_state = self.currentState

    def addState(self, state):
        self.stateList.append(state)

    def reset(self):
        self.currentState = self.initial_state
        self.input_tape = []
        self.current_input = 0
        self.output_tape = []
        self.current_output = 0

    def get_state_memory_obj(self):
        for mem_obj in self.memory:
            if mem_obj.name == self.currentState.memory_object:
                return mem_obj
        print("ERR: Memory Object not found")
        return None

    def next_state(self):
        # Check if the current state is accepting or rejecting
        if self.currentState.name == "accept":
            print("Machine has accepted the input.")
            return True
        elif self.currentState.name == "reject":
            print("Machine has rejected the input.")
            return False

        # tuples of the destination state, transition char
        possible_states = []

        current_mem_obj = self.get_state_memory_obj()
        valid_input = False

        # get all possible next states for NDA
        if self.currentState.transition_type == "R":
            read_char = current_mem_obj.READ()
            for t_key, t_val in self.currentState.transitions.items():
                for val in t_val:
                    if read_char == val:
                        valid_input = True
                        possible_states.append((t_key, val))
        elif self.currentState.transition_type == "W":
            for t_key, t_val in self.currentState.transitions.items():
                if t_key: # if the transition destination exists
                    valid_input = True
                    possible_states.append((t_key, t_val))
        elif self.currentState.transition_type == "S" or self.currentState.transition_type == "SR":
            scan_char = self.input_tape[self.current_input + 1]
            for t_key, t_val in self.currentState.transitions.items():
                for val in t_val:
                    if scan_char == val:
                        valid_input = True
                        possible_states.append((t_key, val))
        elif self.currentState.transition_type == "SL":
            scan_char = self.input_tape[self.current_input - 1]
            for t_key, t_val in self.currentState.transitions.items():
                for val in t_val:
                    if scan_char == val:
                        valid_input = True
                        possible_states.append((t_key, val))
        elif self.currentState.transition_type == "P":
            for t_key, t_val in self.currentState.transitions.items():
                if t_key: # if the transition destination exists
                    valid_input = True
                    possible_states.append((t_key, t_val))
        elif self.currentState.transition_type == "RIGHT":
            current_mem_obj.move_right()
            tape_char = current_mem_obj.get_current_symbol()

            for t_key, t_val in self.currentState.transitions.items():
                for val in t_val:
                    if tape_char == val:
                        valid_input = True
                        possible_states.append((t_key, val))

        # reject if invalid input
        if not valid_input:
            for state in self.stateList:
                if state.name == "reject":
                    self.currentState = state
            return False

        # NDA implementation: choose the next state randomly
        if possible_states:
            next_state = random.choice(possible_states)
        else:
            return False
        
        if self.currentState.transition_type == "R":
            current_mem_obj.READ()
        elif self.currentState.transition_type == "W":
            current_mem_obj.WRITE(next_state[1])
        elif self.currentState.transition_type == "S" or self.currentState.transition_type == "SR":
            self.current_input = self.current_input + 1
        elif self.currentState.transition_type == "SL":
            self.current_input = self.current_input - 1
        elif self.currentState.transition_type == "P":
            self.output_tape.append(next_state[1])
        elif self.currentState.transition_type == "RIGHT":
            current_mem_obj.RIGHT(next_state[1])
        elif self.currentState.transition_type == "LEFT":
            current_mem_obj.LEFT(next_state[1])
        elif self.currentState.transition_type == "UP":
            current_mem_obj.UP(next_state[1])
        elif self.currentState.transition_type == "DOWN":
            current_mem_obj.DOWN(next_state[1])

        # update current state to the next state
        for state in self.stateList:
            if state.name == next_state[0]:
                self.currentState = state