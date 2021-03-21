from tkinter import *

root = Tk()
root.geometry("800x400")

startPage = Frame(root)
calibratePage = Frame(root)


for frame in (startPage, calibratePage):
    frame.grid(row=0, column=0, sticky='news')


# initialize a horizontal slider
sliderValue = IntVar()          # declaring an int in tkinter
sliderValue.set(0)              # initializing it to zero
horiSlider = Scale(startPage, from_=0, to=100, orient=HORIZONTAL, variable=sliderValue, length=750, state=DISABLED)
horiSlider.grid(row=0, column=0)

calibrateButton = Button(startPage, text='Calibrate', command=calibratePage.tkraise)
calibrateButton.grid(row=0, column=0)

Label(calibratePage, text='Welcome to calibration').pack()

startPage.tkraise()
root.mainloop()
