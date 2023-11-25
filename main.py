# Tan, Lance Griffin L.
# CSC615M - Machine Project

import customtkinter as ctk

from memory.stack import STACK
from memory.queue import QUEUE
from memory.tape import TAPE 
from memory.tape2d import TAPE_2D
from util.inputs import process_input
from machine import Machine

class GUI(ctk.CTk):
    def __init__(self):
        super().__init__()
        ctk.set_appearance_mode("System")
        ctk.set_default_color_theme("dark-blue")

        self.geometry("1280x720")
        self.title("CSC615M - Machine Project")

        self.frame = ctk.CTkScrollableFrame(
            master=self, 
            orientation="vertical", 
            label_anchor = "w"
        )

        self.frame.pack(pady=20, padx=60, fill="both", expand=True)

        self.label = ctk.CTkLabel(master=self.frame, text="CSC615M: Machine Project - Tan, L.", font=("Roboto", 32))
        self.label.pack(pady=40)

        self.label_input = ctk.CTkLabel(master=self.frame, text="Input Specifications", font=("Roboto", 24))
        self.label_input.pack(pady=2)
        self.tb_input = ctk.CTkTextbox(master=self.frame, width=600, height=160)
        self.tb_input.pack(pady=10)

        self.button = ctk.CTkButton(master=self.frame, text="Run", command=self.run)
        self.button.pack(pady=10)

        # add input string text input and submit button
        self.input_string_label = ctk.CTkLabel(master=self.frame, text="Input String", font=("Roboto", 24), anchor=ctk.W)

        self.input_string_tb = ctk.CTkTextbox(master=self.frame, width=600, height=20)


        # add step iterator for input string step-by-step processing
        self.iterator_frame = ctk.CTkFrame(master=self.frame)
        self.iterator_prev_button = ctk.CTkButton(master=self.iterator_frame, text="< Previous", command=self.iterate_prev)
        self.input_string_button = ctk.CTkButton(master=self.iterator_frame, text="Submit", command=self.get_string_input)
        self.iterator_reset_button = ctk.CTkButton(master=self.iterator_frame, text="Reset", command=self.iterate_reset)
        self.iterator_next_button = ctk.CTkButton(master=self.iterator_frame, text="Next >", command=self.iterate_next)

        # TO DO: add memory segment text input per memory stack specified


        # add input tape
        self.input_tape_label = ctk.CTkLabel(master=self.frame, text="Input Tape", font=("Roboto", 24), anchor=ctk.W)
        self.input_tape_tb = ctk.CTkTextbox(master=self.frame, width=600, height=20)

        # add output tape
        self.output_tape_label = ctk.CTkLabel(master=self.frame, text="Output Tape", font=("Roboto", 24), anchor=ctk.W)
        self.output_tape_tb = ctk.CTkTextbox(master=self.frame, width=600, height=20)

        # add state diagram
        self.state_diagram_label = ctk.CTkLabel(master=self.frame, text="State Diagram", font=("Roboto", 24), anchor=ctk.W)
        self.state_diagram_frame = ctk.CTkScrollableFrame(
            master=self.frame,
            orientation="vertical", 
            label_anchor = "w",
            height=500,
            width=800,
            fg_color="azure1"
        )

    def get_string_input(self):
        return

    def iterate_next(self):
        return

    def iterate_prev(self):
        return

    def iterate_reset(self):
        return

    def update_input_tape(self):
        return

    def update_output_tape(self):
        return

    def generate_state_diagram(machine: Machine):
        return

    def run(self):
        data_arr, logic_arr = process_input(self.tb_input.get("1.0",'end-1c'))
        print(f"Data Arr: {data_arr}")
        print(f"Logic Arr: {logic_arr}")

        # display relevant
        self.input_string_label.pack(pady=2)
        self.input_string_tb.pack(pady=10)
        self.iterator_frame.pack(pady=5, padx=5)
        self.iterator_prev_button.pack(pady=5, padx=2, side=ctk.LEFT)
        self.input_string_button.pack(pady=5, padx=2, side=ctk.LEFT)
        self.iterator_reset_button.pack(pady=5, padx=2, side=ctk.LEFT)
        self.iterator_next_button.pack(pady=5, padx=2, side=ctk.LEFT)
        self.input_tape_label.pack(pady=2)
        self.input_tape_tb.pack(pady=10)
        self.output_tape_label.pack(pady=2)
        self.output_tape_tb.pack(pady=10)
        self.state_diagram_label.pack(pady=2)
        self.state_diagram_frame.pack(pady=4)
        return

# ---------------------------------------------------------

gui = GUI()
gui.mainloop()