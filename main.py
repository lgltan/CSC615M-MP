# Tan, Lance Griffin L.
# CSC615M - Machine Project

import customtkinter

from memory.stack import STACK
from memory.queue import QUEUE
from memory.tape import TAPE, TAPE_2D
from util.inputs import process_input

def run():
    data_arr, logic_arr = process_input(tb_input.get("1.0",'end-1c'))
    print(f"Data Arr: {data_arr}")
    print(f"Logic Arr: {logic_arr}")
    return

# ---------------------------------------------------------

customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("dark-blue")

root = customtkinter.CTk()
root.geometry("1280x720")
root.title("CSC615M - Machine Project")

frame = customtkinter.CTkFrame(master=root)
frame.pack(pady=20, padx=60, fill="both", expand=True)

label = customtkinter.CTkLabel(master=frame, text="CSC615M: Machine Project - Tan, L.", font=("Roboto", 32))
label.pack(pady=40)

label_input = customtkinter.CTkLabel(master=frame, text="Input Section", font=("Roboto", 24))
label_input.pack(pady=2)
tb_input = customtkinter.CTkTextbox(master=frame, width=600, height=160)
tb_input.pack(pady=10)

button = customtkinter.CTkButton(master=frame, text="Run", command=run)
button.pack(pady=10)

root.mainloop()