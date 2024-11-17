import tkinter as tk

from PIL import ImageTk
from PIL import Image


def insert_image_in_app(images, h=500, w=550):
    root = tk.Tk()
    root.geometry('900x700')
    root.configure(background="orange", highlightbackground="darkgrey", border=10)
    root.title("Image Display")

    # Load the image using PIL
    image = Image.open(images)
    photo = ImageTk.PhotoImage(image)

    # Create a label widget to hold the image
    image_label = tk.Label(root, image=photo)
    image_label.image = photo  # Keep a reference to avoid garbage collection
    image_label.pack()

    # Run the application
    root.mainloop()


if __name__=='__main__':
    insert_image_in_app(images = 'gelioma_image.jpg')
