import tkinter as tk
from PIL import Image, ImageTk
from gui.open_image import open_image
from gui.components import create_label, create_button

def start_gui():
    """Start the Tkinter GUI for BLIP image captioning."""
    root = tk.Tk()
    root.title("BLIP Image Captioning")

    bg_image = Image.open("assets/ezerbouz.jpg")
    bg_photo = ImageTk.PhotoImage(bg_image)
    bg_label = tk.Label(root, image=bg_photo)
    bg_label.place(x=0, y=0, relwidth=1, relheight=1)

    top_text = create_label(root,
                            text="Hi! Ezer is with you, ready to describe any image you choose!",
                            font=("Arial", 16, "bold"))
    top_text.pack(pady=10)

    panel = create_label(root, bg="#000000")
    panel.pack(pady=10)

    caption_label = create_label(root, wraplength=400)
    caption_label.pack(pady=10)

    btn = create_button(root, "Choisir une image",
                        command=lambda: open_image(panel, caption_label))
    btn.pack(pady=10)

    root.mainloop()
