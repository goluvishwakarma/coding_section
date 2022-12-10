from tkinter import *
import os
from PIL import ImageTk, Image


def getFileName(image):
    print(str(image))


gtk = Tk()


def showImages(folder):
    for images in os.listdir(os.getcwd()):
        if images.endswith("jpg"):
            im = Image.open(images)
            ImageTk.PhotoImage(im)
            # imageButton = Button(gtk, image=tkimage, command=getFileName(images))
            # imageButton.image = tkimage
            # imageButton.pack()


showImages(folder='D:\\##wallpaper')
getFileName('D:\\##wallpaper')

gtk.mainloop()
