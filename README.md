# Tan, Lance Griffin L.
# CSC615M - Machine Project

# Installation:
Kindly install tkinter, and optionally, customtkinter.
Custom Tkinter is already included in the zip file.

# Running the program:
To run the program, simply run the main.py file in the root directory.

# Using the program:
1. Enter the input specifications in the first textbox labelled as "Input Specifications" then press the "Run" button

2. This should generate the rest of the textboxes as well as a state diagram for the machine.

3. To use the machine, first enter an "Input String" and press submit. The input string should appear in the "Input Tape" text box.

4. To iterate through the input, simply press "Next State:

4.1. *The machine implements a randomized non-deterministic approach, meaning if there is more than 1 possible choice given the next possible states, it will randomly select one of those options.

If there is any unexpected behavior, that means there was an error either due to the input or the machine. The error log can be seen in the terminal used to launch the program.

# Specifications
Input consists of two primary sections when defining the abstract machine: the DATA section and the LOGIC section.

1. Auxiliary Memory

In the DATA section, any auxiliary memory is declared. The section begins with a line containing .DATA The following are the types of memory that should be supported.

• STACK <stack_name>

This declares a stack with the given identifier. For example STACK S1 declares a stack named S1. The stack accesses memory in a Last-In-First-Out (LIFO) order.

• QUEUE <queue_name>

This declares a queue with the given identifier. For example QUEUE Q1 declares a queue named Q1. The queue accesses memory in a First-In-First-Out (FIFO) order.

• TAPE <tape_name>

This declares tape memory with the given identifier. For example TAPE T1 declares a tape named T1. The tape can be accessed freely by scanning it left and right, ala Turing Machine. For machines with at least one tape, the first tape declared is also designated as the input tape. 2D_TAPE <2D_tape_name> This declares tape memory with the given identifier. For example 2d_TAPE P1 declares a queue named P1. The tape can be accessed freely by scanning it left and right, ala Turing Machine, or up and down. For machines with at least one tape or 2D tape, the first tape-type memory declared is also designated as the input tape. If the first tape-type memory is a 2D Tape, the input is on the first/topmost row.

2. Logic

In the LOGIC section, each line defines a state’s behavior using the following syntax:
<SOURCE_STATE_NAME>] COMMAND (<SYMBOL_1>,<DESTINATION_STATE_NAME_1>), (<SYMBOL_2>,<DESTINATION_STATE_NAME_2>), ..., (<SYMBOL_N>,<DESTINATION_STATE_NAME_N>)
Only the commands LEFT and RIGHT do not follow this syntax (defined below).
For example

A] SCAN (1,A), (2,B), (3,A)

Defines the behavior of state A. Upon scanning a 1, the machine transitions into state A. Upon scanning a 2, the machine transitions into state B. Upon scanning a 1, the machine transitions into state A.

The following commands are supported by the machine definition language:

• SCAN - this command reads one symbol from the input

• PRINT - this command produces one output symbol

• SCAN RIGHT - this command is identical to SCAN. Specifically, this command reads one symbol from the input to the right of the tape head. The tape head then moves to that location.

• SCAN LEFT - this command reads one symbol from the input to the left of the tape head. The tape head then moves to that location.

• READ(<memory_object>) - this command reads one symbol from a given stack or queue. For example, if a STACK S1 was declared in the DATA section, a valid LOGIC definition is 1] READ(S1) (X,1), (Y,2). This means if X is “popped” from the stack, the machine stays in state 1, but if Y is popped, the machine moves to state 2.

• WRITE(<memory_object>) - this command reads one symbol from a given stack or queue. For example, if a QUEUE Q1 was declared in the DATA section, a valid LOGIC definition is 1] WRITE(Q1) (X,1), (Y,2). This is an example of nondeterminism in the machine. If the machine enqueues X in Q1, it will stay in state 1, but if it nondeterministically decides to enqueue Y instead, it will move to state 2.

• RIGHT(<tape_name>) - this command reads one symbol on an input tape to the right of the tape head and moves to that location. It also changes the state and overwrites that symbol with a new symbol. This instruction only applies to tapes or 2D tapes. This command uses a unique syntax:

<SOURCE_STATE_NAME>] RIGHT(<tape_name>) (<SYMBOL_1>/<REPLACEMENT_SYMBOL_1>,<DESTINATION_STATE_NAME_1>), (<SYMBOL_2>/<REPLACEMENT_SYMBOL_2>,<DESTINATION_STATE_NAME_2>), ..., (<SYMBOL_N>/<REPLACEMENT_SYMBOL_N>,<DESTINATION_STATE_NAME_N>)

For example, 1] RIGHT(T1) (0/X,1),(1/Y,2) means if the machine finds a 0 to the right of the tape head on T1, replace it with X, move the tape head to that location, and stay in state 1. If the machine instead finds a 1 to the right of the tape head, replace it with Y , move the tape head to that location, and move to state 2.

• LEFT(<tape_name>) - this command reads one symbol on an input tape to the left of the tape head and moves to that location. It also changes the state and overwrites that symbol with a new symbol. This instruction only applies to tapes or 2D tapes. This command uses a unique syntax:

<SOURCE_STATE_NAME>] LEFT(<tape_name>) (<SYMBOL_1>/<REPLACEMENT_SYMBOL_1>,<DESTINATION_STATE_NAME_1>), (<SYMBOL_2>/<REPLACEMENT_SYMBOL_2>,<DESTINATION_STATE_NAME_2>), ..., (<SYMBOL_N>/<REPLACEMENT_SYMBOL_N>,<DESTINATION_STATE_NAME_N>)

For example, 1] LEFT(T1) (0/X,1),(1/Y,2) means if the machine finds a 0 to the left of the tape head of T1, replace it with X, move the tape head to that location, and stay in state 1. If the machine instead finds a 1 to the left of the tape head, replace it with Y , move the tape head to that location, and move to state 2.

• UP(<2D_tape_name>) - this command reads one symbol on an input tape to the north of the tape head and moves to that location. It also changes the state and overwrites that symbol with a new symbol. This instruction only applies to 2D tapes. This command uses a unique syntax:

<SOURCE_STATE_NAME>] UP(<2D_tape_name>) (<SYMBOL_1>/<REPLACEMENT_SYMBOL_1>,<DESTINATION_STATE_NAME_1>), (<SYMBOL_2>/<REPLACEMENT_SYMBOL_2>,<DESTINATION_STATE_NAME_2>), ..., (<SYMBOL_N>/<REPLACEMENT_SYMBOL_N>,<DESTINATION_STATE_NAME_N>)

For example, 1] UP(P1) (0/X,1),(1/Y,2) means if the machine finds a 0 to the north of the tape head of P1, replace it with X, move the tape head to that location, and stay in state 1. If the machine instead finds a 1 to the north of the tape head, replace it with Y , move the tape head to that location, and move to state 2.

• DOWN(<2D_tape_name>) - this command reads one symbol on an input tape to the south of the tape head and moves to that location. It also changes the state and overwrites that symbol with a new symbol. This instruction only applies to 2D tapes. This command uses a unique syntax:

<SOURCE_STATE_NAME>] DOWN(<2D_tape_name>) (<SYMBOL_1>/<REPLACEMENT_SYMBOL_1>,<DESTINATION_STATE_NAME_1>), (<SYMBOL_2>/<REPLACEMENT_SYMBOL_2>,<DESTINATION_STATE_NAME_2>), ..., (<SYMBOL_N>/<REPLACEMENT_SYMBOL_N>,<DESTINATION_STATE_NAME_N>)

For example, 1] DOWN(P1) (0/X,1),(1/Y,2) means if the machine finds a 0 to the south of the tape head of P1, replace it with X, move the tape head to that location, and stay in state 1. If the machine instead finds a 1 to the south of the tape head, replace it with Y , move the tape head to that location, and move to state 2. Note that each state’s behavior is completely defined in a single line. This means only one command can be associated with
any of the states.

The first line in the .LOGIC section defines the initial state. There are two special reserved words for state names. accept as a state name means that when the machine enters that state, the string is accepted, and the machine halts execution. reject as a state name means that when the machine enters that state, the string is rejected, and the machine halts execution.