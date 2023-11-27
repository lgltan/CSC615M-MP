def process_input(input_data):
    section_split = input_data.split(".")

    while "" in section_split:
        section_split.remove("")

    for section in section_split:
        if "DATA" in section:
            data_arr = section
        elif "LOGIC" in section:
            logic_arr = section

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

    return process_data(data_arr), logic_arr

def process_data(data_arr):
    output_arr = []
    for data in data_arr:
        output_arr.append(data.split())
    return output_arr