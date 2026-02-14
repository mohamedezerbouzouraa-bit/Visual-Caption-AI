from tkinter import filedialog
from PIL import Image, ImageTk

def open_image_file():
    """Open file dialog and return image path."""
    file_path = filedialog.askopenfilename(
        filetypes=[("Image files", "*.jpg *.jpeg *.png *.bmp")]
    )
    return file_path

def load_image_thumbnail(path, size=(400, 400)):
    """Load image, create thumbnail, return PhotoImage."""
    image = Image.open(path)
    image.thumbnail(size)
    return ImageTk.PhotoImage(image)
