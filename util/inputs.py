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

    return process_data(data_arr), process_logic(logic_arr)

def process_data(data_arr):
    output_arr = []
    for data in data_arr:
        output_arr.append(data.split())
    return output_arr

def process_logic(logic_arr):
    output_arr = []
    for state in logic_arr:
        output_arr.append(state.split())
    return output_arr