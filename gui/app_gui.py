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

def start_gui():
    """Create and run the Tkinter GUI."""
    root = tk.Tk()
    root.title("BLIP Image Captioning")

    bg_image = Image.open("assets/ezerbouz.jpg")
    bg_photo = ImageTk.PhotoImage(bg_image)
    bg_label = tk.Label(root, image=bg_photo)
    bg_label.place(x=0, y=0, relwidth=1, relheight=1)

    top_text = tk.Label(root,
                        text="Hi! Ezer is with you, ready to describe any image you choose!",
                        font=("Arial", 16, "bold"), bg="#000000", fg="white")
    top_text.pack(pady=10)

    panel = tk.Label(root, bg="#000000")
    panel.pack(pady=10)

    caption_label = tk.Label(root, text="", wraplength=400, font=("Arial", 12),
                             bg="#000000", fg="white")
    caption_label.pack(pady=10)

    btn = tk.Button(root, text="Choisir une image",
                    command=lambda: open_image(panel, caption_label))
    btn.pack(pady=10)

    root.mainloop()
