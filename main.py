import customtkinter

def SCAN():
    return

def SCAN_LEFT():
    return

def SCAN_RIGHT():
    return

def READ():
    return

def WRITE():
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

def print_here():
    print("hello")

def run():
    print_here()
    return

# ---------------------------------------------------------

customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("dark-blue")

root = customtkinter.CTk()
root.geometry("1920x1080")
root.title("CSC615M - Machine Project")

frame = customtkinter.CTkFrame(master=root)
frame.pack(pady=20, padx=60, fill="both", expand=True)

label = customtkinter.CTkLabel(master=frame, text="CSC615M: Machine Project - Tan, L.", font=("Roboto", 32))
label.pack(pady=12, padx=10)

label_data = customtkinter.CTkLabel(master=frame, text="Data", font=("Roboto", 24))
label_data.pack(pady=2, padx=10)
tb_data = customtkinter.CTkTextbox(master=frame, width=600, height=160)
tb_data.pack(pady=40, padx=80)

label_logic = customtkinter.CTkLabel(master=frame, text="Logic", font=("Roboto", 24))
label_logic.pack(pady=2, padx=10)
tb_logic = customtkinter.CTkTextbox(master=frame, width=600, height=160)
tb_logic.pack(pady=40, padx=80)

button = customtkinter.CTkButton(master=frame, text="Run", command=run)
button.pack(pady=40, padx=80)

root.mainloop()