import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
from models.blip_model import generate_caption

def open_image(panel, caption_label):
    """Open an image, display it, and show caption."""
    file_path = filedialog.askopenfilename(
        filetypes=[("Image files", "*.jpg *.jpeg *.png *.bmp")]
    )
    if file_path:
        image = Image.open(file_path)
        image.thumbnail((400, 400))
        img = ImageTk.PhotoImage(image)
        panel.config(image=img)
        panel.image = img

        caption = generate_caption(file_path)
        caption_label.config(text=caption)

