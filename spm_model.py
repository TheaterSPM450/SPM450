#''' spm_model.py contains spm software functions '''

# from tkinter import *
from tkinter import messagebox as m

def calWarn():
    m.showwarning(title=None, message="You must calibrate the system before starting. Visit calibrate page.")
