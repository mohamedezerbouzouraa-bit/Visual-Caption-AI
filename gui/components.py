import tkinter as tk

def create_label(root, text="", font=("Arial", 12), bg="#000000", fg="white", wraplength=None):
    """Helper to create a Label."""
    return tk.Label(root, text=text, font=font, bg=bg, fg=fg, wraplength=wraplength)

def create_button(root, text, command):
    """Helper to create a Button."""
    return tk.Button(root, text=text, command=command)
