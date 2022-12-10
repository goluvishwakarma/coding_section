# gui(pack_visit collection) - graphics user interface application
from tkinter import *

variable_root = Tk()

# width x height
variable_root.geometry("645x445")

# width, height
variable_root.minsize(200, 100)

# it will take parameter as width, height
variable_root.maxsize(900, 900)

# label
label_var = Label(text="my 1st gui_application in python")
label_var.pack()

#  gui logic:
variable_root.mainloop()

#  Question -- other than Tkinter what are the other ways to create a GUI in python.
#  Answer -- kivy, WxPython and more ....

# Quick quiz: create a window 733 x 334, and enter a text 'welcome to pycharm'



