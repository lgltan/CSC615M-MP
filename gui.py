import customtkinter as ctk

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

        # add a frame to be destroyed for run
        self.run_frame = ctk.CTkFrame(master=self.frame)
        self.run_frame.pack(pady=0, padx=0, fill="both", expand=True)

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

    def generate_state_diagram(self):
        self.machine
        return

    def run(self):
        self.machine = None

        for widget in self.run_frame.winfo_children():
            widget.destroy()

        # data_arr, logic_arr = process_input(self.tb_input.get("1.0",'end-1c'))
        
        # self.machine = Machine(data_arr, logic_arr)

        # add input string text input and submit button
        self.input_string_label = ctk.CTkLabel(master=self.run_frame, text="Input String", font=("Roboto", 24), anchor=ctk.W)
        self.input_string_label.pack(pady=2)
        self.input_string_tb = ctk.CTkTextbox(master=self.run_frame, width=600, height=20)
        self.input_string_tb.pack(pady=10)

        # add step iterator for input string step-by-step processing
        self.iterator_frame = ctk.CTkFrame(master=self.run_frame)
        self.iterator_frame.pack(pady=5, padx=5)
        self.iterator_prev_button = ctk.CTkButton(master=self.iterator_frame, text="< Previous", command=self.iterate_prev)
        self.iterator_prev_button.pack(pady=5, padx=2, side=ctk.LEFT)
        self.input_string_button = ctk.CTkButton(master=self.iterator_frame, text="Submit", command=self.get_string_input)
        self.input_string_button.pack(pady=5, padx=2, side=ctk.LEFT)
        self.iterator_reset_button = ctk.CTkButton(master=self.iterator_frame, text="Reset", command=self.iterate_reset)
        self.iterator_reset_button.pack(pady=5, padx=2, side=ctk.LEFT)
        self.iterator_next_button = ctk.CTkButton(master=self.iterator_frame, text="Next >", command=self.iterate_next)
        self.iterator_next_button.pack(pady=5, padx=2, side=ctk.LEFT)

        # TO DO: add memory segment text input per memory stack specified


        # add input tape
        self.input_tape_label = ctk.CTkLabel(master=self.run_frame, text="Input Tape", font=("Roboto", 24), anchor=ctk.W)
        self.input_tape_label.pack(pady=2)
        self.input_tape_tb = ctk.CTkTextbox(master=self.run_frame, width=600, height=20)
        self.input_tape_tb.pack(pady=10)

        # add output tape
        self.output_tape_label = ctk.CTkLabel(master=self.run_frame, text="Output Tape", font=("Roboto", 24), anchor=ctk.W)
        self.output_tape_label.pack(pady=2)
        self.output_tape_tb = ctk.CTkTextbox(master=self.run_frame, width=600, height=20)
        self.output_tape_tb.pack(pady=10)

        # add state diagram
        self.state_diagram_label = ctk.CTkLabel(master=self.run_frame, text="State Diagram", font=("Roboto", 24), anchor=ctk.W)
        self.state_diagram_label.pack(pady=2)
        self.state_diagram_frame = ctk.CTkScrollableFrame(
            master=self.run_frame,
            orientation="vertical", 
            label_anchor = "w",
            height=500,
            width=800,
            fg_color="azure1"
        )

        self.state_diagram_frame.pack(pady=4)
        self.generate_state_diagram()
        return