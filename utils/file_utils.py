from tkinter import filedialog
from PIL import Image, ImageTk

def open_image_file():
    file_path = filedialog.askopenfilename(
        filetypes=[("Image files", "*.jpg *.jpeg *.png *.bmp")])
    return file_path

def load_image_thumbnail(path, size=(400, 400)):
    image = Image.open(path)
    image.thumbnail(size)
    return ImageTk.PhotoImage(image)
