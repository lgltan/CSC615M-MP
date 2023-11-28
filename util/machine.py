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
    input_tape = None
    current_input = 0
    output_tape = []
    current_output = 0
    initial_state = None

    def __init__(self, data_arr, logic_arr):
        # init auxiliary memory
        for data in data_arr:
            mem_type, mem_name = data
            if mem_type == "STACK":
                self.memory.append(STACK(mem_name))
            elif mem_type == "QUEUE":
                self.memory.append(QUEUE(mem_name))
            elif mem_type == "TAPE":
                temp_holder = TAPE(mem_name)
                if self.input_tape == None:
                    self.input_tape = temp_holder
                self.memory.append(temp_holder)
            elif mem_type == "2D_TAPE":
                temp_holder = TAPE_2D(mem_name)
                if self.input_tape == None:
                    self.input_tape = temp_holder.tape[0]
                self.memory.append(temp_holder)
            else:
                print(f"ERR: Invalid Auxiliary Memory name {mem_type}")
        
        if self.input_tape == None:
            self.input_tape = TAPE("input_tape")

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
            if "SCAN" in logic or "SCAN RIGHT" in logic or "SCAN LEFT" in logic:
                memory_object = self.input_tape.name
            elif "READ" in logic or "WRITE" in logic or "RIGHT" in logic or "LEFT" in logic or "UP" in logic or "DOWN" in logic:
                memory_object = in_parenthesis[0]
                in_parenthesis.remove(in_parenthesis[0])
            else: # PRINT
                memory_object = self.input_tape

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

    def get_state_memory_obj(self):
        for mem_obj in self.memory:
            if mem_obj.name == self.currentState.memory_object:
                return mem_obj
        print("WARNING: Memory Object not found")
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

        if not current_mem_obj:
            current_mem_obj = self.input_tape

        valid_input = False

        # get all possible next states for NDA
        if self.currentState.transition_type == "R":
            read_char = current_mem_obj.READ_TOP()
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
            self.current_input = self.current_input + 1
            scan_char = self.input_tape.tape[self.current_input]
            for t_key, t_val in self.currentState.transitions.items():
                for val in t_val:
                    if scan_char == val:
                        valid_input = True
                        possible_states.append((t_key, val))
        elif self.currentState.transition_type == "SL":
            self.current_input = self.current_input - 1
            scan_char = self.input_tape.tape[self.current_input]
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
            if self.currentState.memory_object == self.input_tape.name:
                self.current_input = self.current_input + 1
            tape_char = current_mem_obj.move_right()
            current_mem_obj.move_left() # reset position for later

            for t_key, t_val in self.currentState.transitions.items():
                for val in t_val:
                    temp_val = val.split("/")
                    if tape_char == temp_val[0]: # if tape char == the symbol
                        valid_input = True
                        possible_states.append((t_key, val))
        elif self.currentState.transition_type == "LEFT":
            if self.currentState.memory_object == self.input_tape.name:
                self.current_input = self.current_input - 1

            tape_char = current_mem_obj.move_left()
            current_mem_obj.move_right() # reset position for later

            for t_key, t_val in self.currentState.transitions.items():
                for val in t_val:
                    temp_val = val.split("/")
                    if tape_char == temp_val[0]: # if tape char == the symbol
                        valid_input = True
                        possible_states.append((t_key, val))
        elif self.currentState.transition_type == "UP":
            tape_char = current_mem_obj.move_up()
            current_mem_obj.move_down() # reset position for later

            for t_key, t_val in self.currentState.transitions.items():
                for val in t_val:
                    temp_val = val.split("/")
                    if tape_char == temp_val[0]: # if tape char == the symbol
                        valid_input = True
                        possible_states.append((t_key, val))
        elif self.currentState.transition_type == "DOWN":
            tape_char = current_mem_obj.move_down()
            current_mem_obj.move_up() # reset position for later

            for t_key, t_val in self.currentState.transitions.items():
                for val in t_val:
                    temp_val = val.split("/")
                    if tape_char == temp_val[0]: # if tape char == the symbol
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
            current_mem_obj.WRITE(next_state[1][0])
        elif self.currentState.transition_type == "S":
            current_mem_obj.SCAN_RIGHT()
        elif self.currentState.transition_type == "SR":
            current_mem_obj.SCAN_RIGHT()
        elif self.currentState.transition_type == "SL":
            current_mem_obj.SCAN_LEFT()
        elif self.currentState.transition_type == "P":
            self.output_tape.append(next_state[1][0])
        elif self.currentState.transition_type == "RIGHT":
            replace_char = next_state[1].split('/')[1]
            current_mem_obj.RIGHT(replace_char)
        elif self.currentState.transition_type == "LEFT":
            replace_char = next_state[1].split('/')[1]
            current_mem_obj.LEFT(replace_char)
        elif self.currentState.transition_type == "UP":
            replace_char = next_state[1].split('/')[1]
            current_mem_obj.UP(replace_char)
        elif self.currentState.transition_type == "DOWN":
            replace_char = next_state[1].split('/')[1]
            current_mem_obj.DOWN(replace_char)

        # update current state to the next state
        for state in self.stateList:
            if state.name == next_state[0]:
                self.currentState = state

    def update_input_tape(self, list_input):
        for mem in self.memory:
            if mem.name == self.input_tape.name:
                mem.tape = list_input
                self.input_tape = mem