# Tan, Lance Griffin L.
# CSC615M - Machine Project

import customtkinter

class STACK:
    def __init__(self, stack_name):
        self.stack_name = stack_name
        self.stack = []
    
    def READ(self):
        return self.stack.pop()

    def WRITE(self, write_val):
        self.stack.append(write_val)

    def SCAN(self):
        return self.stack[-1]

class QUEUE:
    def __init__(self, queue_name):
        self.queue_name = queue_name
        self.queue = []
    
    def READ(self):
        return self.queue.pop(0)

    def WRITE(self, write_val):
        self.queue.append(write_val)

    def SCAN(self):
        return self.queue[0]

def SCAN_LEFT():
    return

def SCAN_RIGHT():
    return

def TAPE_RIGHT():
    return

def TAPE_LEFT():
    return

def TAPE_PRINT():
    return

def TAPE_UP():
    return

def TAPE_DOWN():
    return

def process_input(input_data):
    section_split = input_data.split(".")

    while "" in section_split:
        section_split.remove("")

    if "DATA" in section_split[0]:
        data_arr = section_split[0]
    elif "DATA" in section_split[1]:
        data_arr = section_split[1]
    else:
        print("WARNING: Could not find .DATA section.")

    if "LOGIC" in section_split[0]:
        logic_arr = section_split[0]
    elif "LOGIC" in section_split[1]:
        logic_arr = section_split[1]
    else:
        print("WARNING: Could not find .LOGIC section.")

    data_arr = data_arr.replace("DATA", "").split("\n")
    logic_arr = logic_arr.replace("LOGIC", "").split("\n")

    while "" in data_arr:
        data_arr.remove("")

    while "" in logic_arr:
        logic_arr.remove("")

    if len(data_arr) == 0:
        print("WARNING: No .DATA given")
    if len(logic_arr) == 0:
        print("WARNING: No .LOGIC given")

    return data_arr, logic_arr

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