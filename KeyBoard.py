
import tkinter as tk

def key_pressed(event):
    key = event.char
    print("Key Pressed:", key)

root = tk.Tk()
root.title("Python Keyboard")

# Define the keyboard layout
keyboard_layout = [
    ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p'],
    ['a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l'],
    ['z', 'x', 'c', 'v', 'b', 'n', 'm']
]

# Create buttons for each key
for row in keyboard_layout:
    row_frame = tk.Frame(root)
    row_frame.pack()
    for key in row:
        button = tk.Button(row_frame, text=key, width=5, height=2, command=lambda k=key: print("Button Pressed:", k))
        button.pack(side=tk.LEFT, padx=5, pady=5)

# Bind keyboard events
root.bind("<KeyPress>", key_pressed)

root.mainloop()

