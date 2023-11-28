import customtkinter as ctk
import tkinter as tk

from util.inputs import process_input
from util.machine import Machine
from util.generate_diagram import Diagram

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
        input_string = "#" + self.input_string_tb.get("1.0",'end-1c') + "#"
        self.machine.input_tape.tape = [char for char in input_string]
        
        self.update_input_tape()
        self.update_output_tape()
        
    def iterate_next(self):
        self.machine.next_state()
        self.update_mem_tapes()
        self.update_input_tape()
        self.update_output_tape()
        self.current_state_label.configure(text=f"Current State: {self.machine.currentState.name}")

    def update_mem_tapes(self):
        for _id, mem_tape in enumerate(self.aux_mem_list):
            if self.machine.memory[_id].get_type() == "TAPE_2D":
                mem_tape[1].delete("1.0", tk.END)
                input_text = self.machine.memory[_id].tape[self.machine.memory[_id].current_row].copy()
                input_text[self.machine.memory[_id].current_col] = f"|{self.machine.memory[_id].tape[self.machine.memory[_id].current_row][self.machine.memory[_id].current_col]}|"
                self.input_tape_tb.insert(tk.END, ''.join(input_text))
            elif self.machine.memory[_id].get_type() == "TAPE":
                mem_tape[1].delete("1.0", tk.END)
                input_text = self.machine.memory[_id].tape.copy()
                input_text[self.machine.memory[_id].current_position] = f"|{self.machine.memory[_id].current_position}|"
                self.input_tape_tb.insert(tk.END, ''.join(input_text))
            elif self.machine.memory[_id].get_type() == "STACK":
                mem_tape[1].delete("1.0", tk.END)
                self.input_tape_tb.insert(tk.END, ''.join(self.machine.memory[_id].stack))
            elif self.machine.memory[_id].get_type() == "QUEUE":
                mem_tape[1].delete("1.0", tk.END)
                self.input_tape_tb.insert(tk.END, ''.join(self.machine.memory[_id].QUEUE))

    def update_input_tape(self):
        self.input_tape_tb.delete("1.0", tk.END)
        if 0 <= self.machine.current_input < len(self.machine.input_tape):
            input_text = self.machine.input_tape.copy()
            input_text[self.machine.current_input] = f"|{self.machine.input_tape[self.machine.current_input]}|"
            self.input_tape_tb.insert(tk.END, ''.join(input_text))

    def update_output_tape(self):
        self.output_tape_tb.delete("1.0", tk.END)
        if 0 <= self.machine.current_output < len(self.machine.output_tape):
            output_text = self.machine.output_tape.copy()
            output_text[self.machine.current_output] = f"|{self.machine.output_tape[self.machine.current_output]}|"
            self.output_tape_tb.insert(tk.END, ''.join(output_text))

    def generate_state_diagram(self):
        # Create canvas
        canvas = tk.Canvas(self.state_diagram_frame, height=740, width=800, bg="white")
        canvas.pack(expand=True, fill="both")

        diagram = Diagram(self.machine, canvas)

        # Draw initial state
        diagram.draw_arrows()
        diagram.draw_states()

    def run(self):
        for widget in self.run_frame.winfo_children():
            widget.destroy()

        data_arr, logic_arr = process_input(self.tb_input.get("1.0",'end-1c'))
        
        self.machine = Machine(data_arr, logic_arr)

        # add input string text input and submit button
        self.input_string_label = ctk.CTkLabel(master=self.run_frame, text="Input String", font=("Roboto", 24), anchor=ctk.W)
        self.input_string_label.pack(pady=2)
        self.input_string_tb = ctk.CTkTextbox(master=self.run_frame, width=600, height=20)
        self.input_string_tb.pack(pady=10)
        self.input_string_button = ctk.CTkButton(master=self.run_frame, text="Submit", command=self.get_string_input)
        self.input_string_button.pack(pady=2)

        # add input tape
        self.input_tape_label = ctk.CTkLabel(master=self.run_frame, text="Input Tape", font=("Roboto", 24), anchor=ctk.W)
        self.input_tape_label.pack(pady=2)
        self.input_tape_tb = ctk.CTkTextbox(master=self.run_frame, width=600, height=20)
        self.input_tape_tb.pack(pady=10)
        self.iterator_next_button = ctk.CTkButton(master=self.run_frame, text="Next State", command=self.iterate_next)
        self.iterator_next_button.pack(pady=2)

        # add output tape
        self.output_tape_label = ctk.CTkLabel(master=self.run_frame, text="Output Tape", font=("Roboto", 24), anchor=ctk.W)
        self.output_tape_label.pack(pady=2)
        self.output_tape_tb = ctk.CTkTextbox(master=self.run_frame, width=600, height=20, state="disabled")
        self.output_tape_tb.pack(pady=10)

        # add memory segment text input per memory stack specified
        self.aux_mem_list = []
        
        for aux_mem in self.machine.memory:
            aux_mem_label = ctk.CTkLabel(master=self.run_frame, text=aux_mem.name, font=("Roboto", 24), anchor=ctk.W)
            aux_mem_label.pack(pady=2)
            aux_mem_tb = ctk.CTkTextbox(master=self.run_frame, width=600, height=20, state="disabled")
            aux_mem_tb.pack(pady=10)

            self.aux_mem_list.append((aux_mem_label, aux_mem_tb))

        self.current_state_label = ctk.CTkLabel(master=self.run_frame, text="Current State: None", font=("Roboto", 16), anchor=ctk.W)
        self.current_state_label.pack(pady=2)

        # add state diagram
        self.state_diagram_label = ctk.CTkLabel(master=self.run_frame, text="State Diagram", font=("Roboto", 24), anchor=ctk.W)
        self.state_diagram_label.pack(pady=2)
        self.state_diagram_frame = ctk.CTkFrame(
            master=self.run_frame,
            height=600,
            width=800
        )

        self.state_diagram_frame.pack()

        self.state_diagram_label = ctk.CTkLabel(master=self.run_frame, text="*Drag nodes around by holding down left click on a node, and releasing it at the desired position.", font=("Roboto", 12), anchor=ctk.W)
        self.state_diagram_label.pack(pady=2)

        self.generate_state_diagram()
        self.button.configure(state="disabled")