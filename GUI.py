from tkinter import *

root = Tk()
root.geometry("800x400")

startPage = Frame(root)
calibratePage = Frame(root)

startPage.place(x=0, y=0, width=800, height=400)
calibratePage.place(x=0, y=0, width=800, height=400)

# NICK NOTES: All buttons should be positioned using ".place" as opposed to .pack or .grid
# .place allows for specific positioning of buttons, based on the pixel number.
# (x,y,width,height)
# just make sure x and y is within the geometry of the frame. (800x400 at time of comment)


######################START PAGE###############################
# initialize a horizontal slider
sliderValue = IntVar()          # declaring an int in tkinter
sliderValue.set(0)              # initializing it to zero
horiSlider = Scale(startPage, from_=0, to=100, orient=HORIZONTAL, length=750, variable=sliderValue, state=DISABLED)
horiSlider.place(x=10, y=10, width=750, height=100)


calibrateButton = Button(startPage, text='Calibrate', command=calibratePage.tkraise)
calibrateButton.place(x=10, y=150, width=100, height=50)

profilesButton = Button(startPage, text='Profiles')
profilesButton.place(x=10, y=200, width=100, height=50)

leftMove = Button(startPage, text='LEFT', height=2, width=4)
leftMove.place(x=500, y=200, width=100, height=100)
rightMove = Button(startPage, text='RIGHT', height=2, width=4)
rightMove.place(x=600, y=200, width=100, height=100)



########################END START PAGE############################

#######################CALIBRATE PAGE#####################
Label(calibratePage, text='Welcome to calibration').grid(row=0, column=0)
doneButton = Button(calibratePage, text='Done', command=startPage.tkraise)
doneButton.place(x=10, y=150, width=100, height=50)


#####################END CALIBRATE PAGE#########################


startPage.tkraise()
root.mainloop()
