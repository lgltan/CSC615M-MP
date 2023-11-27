import tkinter as tk
import math

class State:
    def __init__(self, name, x, y):
        self.name = name
        self.x = x
        self.y = y
        self.connections = {}

def calculate_overlap(start, end):
    # Calculate the distance between the centers of the two states
    distance = math.sqrt((end.x - start.x)**2 + (end.y - start.y)**2)
    return distance < 40  # Adjust the threshold as needed

def draw_arrow(canvas, start, end, labels):
    start_x, start_y = start.x, start.y
    end_x, end_y = end.x, end.y

    angle = math.atan2(end_y - start_y, end_x - start_x)
    arrow_length = 20
    end_x = end_x - 20 * math.cos(angle)
    end_y = end_y - 20 * math.sin(angle)

    # Check if the arrows are pointing in opposite directions and overlap
    dot_product = (start_x - end_x) * (start_x - end_x) + (start_y - end_y) * (start_y - end_y)
    opposite_directions = dot_product < 0 and calculate_overlap(start, end)
    if opposite_directions:
        # Use quadratic Bezier curve control point
        control_x = (start_x + end_x) / 2
        control_y = (start_y + end_y) / 2 - 40  # Adjust the control point height as needed

        canvas.create_line(start_x, start_y, control_x, control_y, end_x, end_y, arrow=tk.LAST, smooth=tk.TRUE, tags=f"arrows arrows_{start.name}")

        # Calculate the position slightly above the midpoint of the Bezier curve
        text_x = (start_x + 2 * control_x + end_x) / 4
        text_y = (start_y + 2 * control_y + end_y) / 4 - 10

        # Place labels on top of each other
        for label in labels:
            canvas.create_text(text_x, text_y, text=label, tags=f"arrow_label arrows_{start.name}")
            text_y -= 10  # Adjust the vertical offset for multiple labels
    else:
        # Use a straight line
        canvas.create_line(start_x, start_y, end_x, end_y, arrow=tk.LAST, tags=f"arrows arrows_{start.name}")

        # Calculate the position slightly above the midpoint of the line
        text_x = (start_x + end_x) / 2
        text_y = (start_y + end_y) / 2 - 10

        # Place labels on top of each other
        for label in labels:
            canvas.create_text(text_x, text_y, text=label, tags=f"arrow_label arrows_{start.name}")
            text_y -= 10  # Adjust the vertical offset for multiple labels

def draw_self_arrow(canvas, start, labels):
    start_x, start_y = start.x, start.y
    control_x = start_x
    control_y = start_y - 40  # Adjust the control point height as needed
    end_x = start_x + 20
    end_y = start_y

    # Use quadratic Bezier curve control point
    canvas.create_line(start_x, start_y, control_x, control_y, end_x, end_y, arrow=tk.LAST, smooth=tk.TRUE, tags=f"arrows arrows_{start.name}")

    # Calculate the position slightly above the midpoint of the Bezier curve
    text_x = (start_x + control_x + end_x) / 3
    text_y = (start_y + control_y + end_y) / 3 - 10

    # Place labels on top of each other
    for label in labels:
        canvas.create_text(text_x, text_y, text=label, tags=f"arrow_label arrows_{start.name}")
        text_y -= 10  # Adjust the vertical offset for multiple labels


def create_circle(canvas, state):
    canvas.create_oval(state.x - 20, state.y - 20, state.x + 20, state.y + 20, fill="lightblue", tags=f"circles circle_{state.name}")
    canvas.create_text(state.x, state.y, text=state.name, tags=f"circles circle_{state.name}")

def on_press(event, state):
    # Store the initial position of the state
    state.start_x = event.x
    state.start_y = event.y

def on_release(event, state):
    # Calculate the change in position
    delta_x = event.x - state.start_x
    delta_y = event.y - state.start_y

    # Update the state's position
    state.x += delta_x
    state.y += delta_y

    draw_arrows(canvas)
    draw_states(canvas)

def draw_states(canvas):
    # delete all states first before redrawing them
    for state in states:
        canvas.delete(f"circle_{state.name}")

    for state in states:
        create_circle(canvas, state)
        # Bind press and release events to the on_press and on_release functions
        canvas.tag_bind(f"circle_{state.name}", "<ButtonPress-1>", lambda event, s=state: on_press(event, s))
        canvas.tag_bind(f"circle_{state.name}", "<ButtonRelease-1>", lambda event, s=state: on_release(event, s))

def draw_arrows(canvas):
    canvas.delete("arrows")
    canvas.delete("arrow_label")
    
    for i in range(len(states)):
        start_state = states[i]
        end_state = states[(i + 1) % len(states)]
        labels = start_state.connections.get(end_state, [])

        if start_state == end_state:
            draw_self_arrow(canvas, start_state, labels)
        else:
            draw_arrow(canvas, start_state, end_state, labels)

# Create tkinter window
root = tk.Tk()
root.title("State Connections")

# Create canvas
canvas = tk.Canvas(root, width=400, height=400, bg="white")
canvas.pack(expand=tk.YES, fill=tk.BOTH)

# Create states
A = State("A", 50, 150)
B = State("B", 200, 50)
C = State("C", 350, 150)

# Define connections
A.connections = {B: ["x", "z"]}  # Multiple characters for the same connection
B.connections = {C: ["z", "b", "a"]}  # Additional self-connection with "b" and "a"
C.connections = {A: ["z", "y"], B: ["x", "b"]}  # Connection from C to A and C to B to create overlapping arrows

# Store states in a list
states = [A, B, C]

# Draw initial state
draw_arrows(canvas)
draw_states(canvas)

root.mainloop()
