# kinter_gui.py
#
# Author: Alex Kogan
#
# Overview: This file contains a test program utilizing Python Tkingter library to create
# a GUI for development purposes
#


# IMPORTS & INCLUDES
from tkinter import * # GUI lib
import tkinter as tk
import csv          #CSV lib
import os           # OS lib
import spm_model as spm    # Model code file


# CONSTANTS & VARIABLES___________________________________
fields = 'Gear Ratio', 'Position', 'Profile Name'
# var = tk.DoubleVar()


# INITIALIZATIONS_________________________________________

# Tk() defines a gui program window assigned to root
root = Tk()

# set minimum window size to 4:3 by setting resolution to 800x600
root.minsize(800, 600)

# window title
root.title("SPM450 Commander BETA")

ents = spm.makeform(root, fields)
root.bind('<Return>', (lambda event, e=ents: spm.fetch(e)))

# scale = Scale(root, variable = var )
# scale.pack(anchor=CENTER)

b1 = tk.Button(root, text='Save',command=(lambda e=ents: spm.fetch(e)))
b1.pack(side=tk.LEFT, padx=5, pady=5)
b2 = tk.Button(root, text='Quit', command=root.quit)
b2.pack(side=tk.LEFT, padx=5, pady=5)
b3 = tk.Button(root, text='Delete',command=(lambda e=ents: spm.delete_profile(e)))
b3.pack(side=tk.LEFT, padx=5, pady=5)

# Exit button program
q_button = Button(root, text = "Exit", command = root.quit, fg="#ffffff", bg="#ff0000", activebackground="#d00000").pack(side=tk.RIGHT, padx=40, pady=20)


root.mainloop()