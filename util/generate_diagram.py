import tkinter as tk
import math
from util.machine import Machine
from util.state import State

class Diagram:
    def __init__(self, machine: Machine, canvas):
        self.machine = Machine
        self.canvas = canvas

    def calculate_overlap(self, start, end):
        # Calculate direction vector s
        s = (end.x - start.x, end.y - start.y)
        
        # Check if the lines are parallel
        if s[0] == 0 and s[1] == 0:
            # Lines are coincident, consider them overlapping
            return True
        
        # Calculate parameter intervals for the two line segments
        t_start1 = 0
        t_end1 = 1
        t_start2 = 0
        t_end2 = 1
        
        # If the lines are not parallel, calculate the parameter intervals
        if s[0] != 0:
            t_start1 = (5 - start.x) / s[0]
            t_end1 = (10 - start.x) / s[0]
            t_start2 = (7 - start.x) / s[0]
            t_end2 = (12 - start.x) / s[0]
        elif s[1] != 0:
            t_start1 = (5 - start.y) / s[1]
            t_end1 = (10 - start.y) / s[1]
            t_start2 = (7 - start.y) / s[1]
            t_end2 = (12 - start.y) / s[1]
        
        # Find the overlap interval
        overlap_start = max(t_start1, t_start2)
        overlap_end = min(t_end1, t_end2)
        
        # Check if there is an overlap
        return overlap_start <= overlap_end

    def draw_arrow(self, start, end, labels):
        start_x, start_y = start.x, start.y
        end_x, end_y = end.x, end.y

        angle = math.atan2(end_y - start_y, end_x - start_x)
        arrow_length = 20
        end_x = end_x - 20 * math.cos(angle)
        end_y = end_y - 20 * math.sin(angle)

        # Check if the arrows are pointing in opposite directions and overlap
        dot_product = (start_x - end_x) * (start_x - end_x) + (start_y - end_y) * (start_y - end_y)
        opposite_directions = dot_product < 0 and self.calculate_overlap(start, end)

        if opposite_directions:
            # Use quadratic Bezier curve control point
            control_x = (start_x + end_x) / 2
            control_y = (start_y + end_y) / 2 - 40  # Adjust the control point height as needed

            self.canvas.create_line(start_x, start_y, control_x, control_y, end_x, end_y, arrow=tk.LAST, smooth=tk.TRUE, tags=f"arrows arrows_{start.name}")

            # Calculate the position slightly above the midpoint of the Bezier curve
            text_x = (start_x + 2 * control_x + end_x) / 4
            text_y = (start_y + 2 * control_y + end_y) / 4 - 10

            # Place labels on top of each other
            for label in labels:
                self.canvas.create_text(text_x, text_y, text=label, tags=f"arrow_label arrows_{start.name}")
                text_y -= 10  # Adjust the vertical offset for multiple labels
        else:
            # Use a straight line
            self.canvas.create_line(start_x, start_y, end_x, end_y, arrow=tk.LAST, tags=f"arrows arrows_{start.name}")

            # Calculate the position slightly above the midpoint of the line
            text_x = (start_x + end_x) / 2
            text_y = (start_y + end_y) / 2 - 10

            # Place labels on top of each other
            for label in labels:
                self.canvas.create_text(text_x, text_y, text=label, tags=f"arrow_label arrows_{start.name}")
                text_y -= 10  # Adjust the vertical offset for multiple labels

    def draw_self_arrow(self, start, labels):
        start_x, start_y = start.x, start.y
        control_x = start_x
        control_y = start_y - 40  # Adjust the control point height as needed
        end_x = start_x + 20
        end_y = start_y

        # Use quadratic Bezier curve control point
        self.canvas.create_line(start_x, start_y, control_x, control_y, end_x, end_y, arrow=tk.LAST, smooth=tk.TRUE, tags=f"arrows arrows_{start.name}")

        # Calculate the position slightly above the midpoint of the Bezier curve
        text_x = (start_x + control_x + end_x) / 3
        text_y = (start_y + control_y + end_y) / 3 - 10

        # Place labels on top of each other
        for label in labels:
            self.canvas.create_text(text_x, text_y, text=label, tags=f"arrow_label arrows_{start.name}")
            text_y -= 10  # Adjust the vertical offset for multiple labels


    def create_circle(self, state):
        radius = 20
        self.canvas.create_oval(state.x - radius, state.y - radius, state.x + radius, state.y + radius, fill="lightblue", tags=f"circles circle_{state.name}")
        
        # Create a label beneath the circle
        if not state.transition_type:
            label_id = self.canvas.create_text(state.x, state.y + radius + 10, text=state.transition_type, tags=f"circle_label circle_{state.name}")

    def on_press(self, event, state):
        # Store the initial position of the state
        state.start_x = event.x
        state.start_y = event.y

    def on_release(self, event, state):
        # Calculate the change in position
        delta_x = event.x - state.start_x
        delta_y = event.y - state.start_y

        # Update the state's position
        state.x += delta_x
        state.y += delta_y

        self.draw_arrows()
        self.draw_states()

    def draw_states(self):
        # delete all states first before redrawing them
        for state in self.machine.stateList:
            self.canvas.delete(f"circle_{state.name}")

        for state in self.machine.stateList:
            self.create_circle(state)
            # Bind press and release events to the on_press and on_release functions
            self.canvas.tag_bind(f"circle_{state.name}", "<ButtonPress-1>", lambda event, s=state: self.on_press(event, s))
            self.canvas.tag_bind(f"circle_{state.name}", "<ButtonRelease-1>", lambda event, s=state: self.on_release(event, s))

    def draw_arrows(self):
        self.canvas.delete("arrows")
        self.canvas.delete("arrow_label")

        for state in self.machine.stateList:
            for key, labels in state.transitions.items():
                if state.name == key:
                    self.draw_self_arrow(state, labels)
                else:
                    end_state = -1
                    for temp_state in self.machine.stateList:
                        if temp_state.name == key:
                            end_state = temp_state
                    if end_state == -1:
                        print(f"ERR: Could not find target state for state {state.name}'s transition: {key}: {labels}")
                    self.draw_arrow(state, end_state, labels)