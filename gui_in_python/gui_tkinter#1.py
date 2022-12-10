# date: 20-12-20__________: how to take image in gui
# displaying_image using label
from tkinter import *
# from PIL import Image, ImageTk  # for display jpg images
import os

root = Tk()
root.geometry("850x650")

# display_image
photo = PhotoImage(file="../image/p2.png")
image_label = Label(image=photo)
image_label.pack()

# __________for jpg images:
# image = Image.open("photo.jpg")
# photo = ImageTk.PhotoImage(image)
#
# var_label = Label(image=photo)
# var_label.pack()

# show_text
text_label = Label(text="my first image in gui")
text_label.pack()

root.mainloop()
a = input()

# Quick quiz: display photos from the folder in gui.
