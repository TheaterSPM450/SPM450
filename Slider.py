from tkinter import *

root = Tk()

root.title('Slider beta')
root.geometry("400x400")

#Initializes global variable glo, sets it equal to the current slider
#position and prints it out using a label widget
def glob(v):
	global glo
	glo = horizontal.get()
	#my_label2 = Label(root, text = glo).pack()
#Initialization of a horizontal slider

horizontal = Scale(root, from_=0, to=10, length = 500,command = glob, tickinterval = 1, orient=HORIZONTAL)
horizontal.pack()

root.mainloop()