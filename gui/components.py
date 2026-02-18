import tkinter as tk

def create_label(root, text="", font=("Arial", 12), bg="#000000", fg="white", wraplength=None):
    return tk.Label(root, text=text, font=font, bg=bg, fg=fg, wraplength=wraplength)
def create_button(root, text, command):
    return tk.Button(root, text=text, command=command)
