def process_input(input_data):
    section_split = input_data.split(".")

    data_arr = None
    logic_arr = None

    while "" in section_split:
        section_split.remove("")

    for section in section_split:
        if "DATA" in section:
            data_arr = section
        elif "LOGIC" in section:
            logic_arr = section

    if data_arr:
        data_arr = data_arr.replace("DATA", "").split("\n")
    else:
        print("WARNING: There is no DATA section.")
    if logic_arr:
        logic_arr = logic_arr.replace("LOGIC", "").split("\n")
    else:
        print("WARNING: There is no LOGIC section.")

    if data_arr:
        while "" in data_arr:
            data_arr.remove("")

    if logic_arr:
        while "" in logic_arr:
            logic_arr.remove("")

    if not data_arr:
        data_arr = []
        
    return process_data(data_arr), logic_arr

def process_data(data_arr):
    output_arr = []
    for data in data_arr:
        output_arr.append(data.split())
    return output_arr