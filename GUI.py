from tkinter import *

root = Tk()
root.geometry("800x400")

# This is where we initialize the frames(or windows) for the program
# Each frame represents a separate page in the program that can be traveled to with a button press
startPage = Frame(root)
calibratePage = Frame(root)
profilePage = Frame(root)

# The width and height of the frame should match root, or else there are issues with button placement
startPage.place(x=0, y=0, width=800, height=400)
calibratePage.place(x=0, y=0, width=800, height=400)
profilePage.place(x=0, y=0, width=800, height=400)

# NICK NOTES: All buttons should be positioned using ".place" as opposed to .pack or .grid
# .place allows for specific positioning of buttons, based on the pixel number.
# (x position, y position, width of object, height of object)
# just make sure x and y is within the geometry of the frame. (800x400 at time of comment)
# .place will not work if the frame is called using .grid or .pack


######################START PAGE###############################
# This slider is cut directly from one of the submitted files. It is missing the functionality that came with it
# Eventually this will need to be tied to the calibrated settings to track position

sliderValue = IntVar()          # declaring an int in tkinter
sliderValue.set(0)              # initializing it to zero
horiSlider = Scale(startPage, from_=0, to=100, orient=HORIZONTAL, length=750, variable=sliderValue, state=DISABLED)
horiSlider.place(x=10, y=10, width=750, height=100)

# This button leads us to the calibration page
calibrateButton = Button(startPage, text='Calibrate', command=calibratePage.tkraise)
calibrateButton.place(x=10, y=150, width=100, height=50)

# This button will lead us to the profile page
profilesButton = Button(startPage, text='Profiles')
profilesButton.place(x=10, y=200, width=100, height=50)

# These are the manual control buttons, that simply move the stepper motor in the desired direction.
# Currently, the movement is not tied to any calibrated start or end point, nor can the speed be controlled.
leftMove = Button(startPage, text='LEFT')
leftMove.place(x=550, y=250, width=100, height=100)
rightMove = Button(startPage, text='RIGHT')
rightMove.place(x=650, y=250, width=100, height=100)


########################END START PAGE############################

#######################CALIBRATE PAGE#####################

Label(calibratePage, text='Welcome to calibration').grid(row=0, column=0)

# The done button returns us to the start page
doneButtonCal = Button(calibratePage, text='Done', command=startPage.tkraise)
doneButtonCal.place(x=10, y=250, width=100, height=50)


# This border just creates a graphical box around the instructions
borderCal = LabelFrame(calibratePage, text="Instructions")
borderCal.place(x=150, y=60, width=400, height=100)

# This is the label for the instructions. The width and height have to be less then the border
# since these go inside of it. The text will overlap and hide the border if the width and height are too large
instructCal = Label(calibratePage, text='Step 1: Figure out what the instructions are')
instructCal.place(x=160, y=80, width=350, height=50)

# These are the buttons to set the start and end points of our moveable range
# It was originally discussed that it would be a single button that dynamically changes, but they seems
# more confusing for the user and more work for us. For the time being, its two buttons.
startPointCal = Button(calibratePage, text='Start Point')
startPointCal.place(x=250, y=180, width=100, height=60)
endPointCal = Button(calibratePage, text='End Point')
endPointCal.place(x=350, y=180, width=100, height=60)

# These buttons are a copy of the manual controls from the start page
# They have to be stored with separate variable names since all of these buttons are initialized before
# the main gui loop actually happens.
leftMoveCal = Button(calibratePage, text='LEFT')
leftMoveCal.place(x=550, y=250, width=100, height=100)
rightMoveCal = Button(calibratePage, text='RIGHT')
rightMoveCal.place(x=650, y=250, width=100, height=100)


#####################END CALIBRATE PAGE#########################


# We call tkraise on startPage so that it is the first frame we see once we enter the main loop
# Whatever page is raised here will be the first page you see
startPage.tkraise()
root.mainloop()
