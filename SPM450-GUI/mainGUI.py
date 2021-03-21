from tkinter import *
import time
#import Hardware_Functions as hf
#import Software_Functions

# import tkFont
# myFont = tkFont.Font(family = 'Helvetica', size = 8, weight = 'bold')

# Some of the GPIO variable declarations and all functions were moved to Hardware_functions file
#hf.GPIO_Initialisation()

# declare base GUI window
root = Tk()
root.title("Stage Prop Mover 450")
root.geometry("1024x600")

# This is where we initialize the frames(or windows) for the program
# Each frame represents a separate page in the program that can be traveled to with a button press
startPage = Frame(root)
calibratePage = Frame(root)
profilePage = Frame(root)

pageWidth = 1024
pageHeight = 600
# The width and height of the frame should match root, or else there are issues with button placement
startPage.place(x=0, y=0, width=pageWidth, height=pageHeight)
calibratePage.place(x=0, y=0, width=pageWidth, height=pageHeight)
profilePage.place(x=0, y=0, width=pageWidth, height=pageHeight)

# NICK NOTES: All buttons should be positioned using ".place" as opposed to .pack or .grid
# .place allows for specific positioning of buttons, based on the pixel number.
# (x position, y position, width of object, height of object)
# just make sure x and y is within the geometry of the frame. (800x400 at time of comment)
# .place will not work if the frame is called using .grid or .pack


######################START PAGE###############################
Label(startPage, text='HOME PAGE').place(x=450, y=0, width=150, height=50)


# This slider is cut directly from one of the submitted files. It is missing the functionality that came with it
# Eventually this will need to be tied to the calibrated settings to track position

sliderValue = IntVar()          # declaring an int in tkinter
sliderValue.set(0)              # initializing it to zero
horiSlider = Scale(startPage, from_=0, to=100, orient=HORIZONTAL, length=1000, variable=sliderValue, state=DISABLED)
horiSlider.place(x=10, y=30, width=1000, height=50)

# This button leads us to the calibration page
calibrateButton = Button(startPage, text='Calibrate', command=calibratePage.tkraise)
calibrateButton.place(x=10, y=350, width=100, height=50)

# This button will lead us to the profile page
profilesButton = Button(startPage, text='Profiles', command=profilePage.tkraise)
profilesButton.place(x=10, y=400, width=100, height=50)

# This button exits.
exitButton = Button(startPage, text="Exit", command=root.destroy)
exitButton.place(x=10, y=450,width=100, height=50)

# These are the manual control buttons, that simply move the stepper motor in the desired direction.
# Currently, the movement is not tied to any calibrated start or end point, nor can the speed be controlled.
leftMove = Button(startPage, text='LEFT')#, repeatdelay=20, repeatinterval=1, command=hf.spinLeft)
leftMove.place(x=700, y=400, width=100, height=100)
rightMove = Button(startPage, text='RIGHT')#, repeatdelay=1, repeatinterval=1, command=hf.spinRight)
rightMove.place(x=800, y=400, width=100, height=100)


########################END START PAGE############################

#######################CALIBRATE PAGE#####################

Label(calibratePage, text='CALIBRATION').place(x=450, y=0, width=150, height=50)

# The done button returns us to the start page
doneButtonCal = Button(calibratePage, text='Done', command=startPage.tkraise)
doneButtonCal.place(x=10, y=350, width=100, height=50)


# This border just creates a graphical box around the instructions
borderCal = LabelFrame(calibratePage, text="Instructions")
borderCal.place(x=250, y=60, width=600, height=200)

# This is the label for the instructions. The width and height have to be less then the border
# since these go inside of it. The text will overlap and hide the border if the width and height are too large
instructCal = Label(calibratePage, text='Step 1: Figure out what the instructions are')
instructCal.place(x=300, y=80, width=350, height=50)

# These are the buttons to set the start and end points of our moveable range
# It was originally discussed that it would be a single button that dynamically changes, but they seems
# more confusing for the user and more work for us. For the time being, its two buttons.
startPointCal = Button(calibratePage, text='Start Point')
startPointCal.place(x=400, y=350, width=100, height=60)
endPointCal = Button(calibratePage, text='End Point')
endPointCal.place(x=500, y=350, width=100, height=60)

# These buttons are a copy of the manual controls from the start page
# They have to be stored with separate variable names since all of these buttons are initialized before
# the main gui loop actually happens.
leftMoveCal = Button(calibratePage, text='LEFT')#, repeatdelay=20, repeatinterval=1, command=hf.spinLeft)
leftMoveCal.place(x=700, y=400, width=100, height=100)
rightMoveCal = Button(calibratePage, text='RIGHT')#, repeatdelay=1, repeatinterval=1, command=hf.spinRight)
rightMoveCal.place(x=800, y=400, width=100, height=100)


#####################END CALIBRATE PAGE#########################

####################PROFILE PAGE##########################
Label(profilePage, text='PROFILE').place(x=450, y=0, width=150, height=50)


# The done button returns us to the start page
doneButtonPro = Button(profilePage, text='Done', command=startPage.tkraise)
doneButtonPro.place(x=10, y=350, width=100, height=50)

# These buttons are a copy of the manual controls from the start page
# They have to be stored with separate variable names since all of these buttons are initialized before
# the main gui loop actually happens.
leftMovePro = Button(profilePage, text='LEFT')#, repeatdelay=20, repeatinterval=1, command=hf.spinLeft)
leftMovePro.place(x=700, y=400, width=100, height=100)
rightMovePro = Button(profilePage, text='RIGHT')#, repeatdelay=1, repeatinterval=1, command=hf.spinRight)
rightMovePro.place(x=800, y=400, width=100, height=100)

####################END PROFILE PAGE#############################


# We call tkraise on startPage so that it is the first frame we see once we enter the main loop
# Whatever page is raised here will be the first page you see
startPage.tkraise()
root.mainloop()





# I was unsure if these buttons are going to make it in the final design
# I've included them here since they were part of the gui before

# spinButton = Button(win, text="SPIN ON", command=spin, height = 2, width =10 )
# spinButton.pack()
#
# spinForSetTimeButton = Button(win, text="SpinForSetTime", command = spinForSetTime, height = 2, width =10)
# spinForSetTimeButton.place(x=100, y=100)
#
# # RepeatIsIn(ms)
# spinHoldButton = Button(win, text="spinHoldButton", repeatdelay=1, repeatinterval=1, command=spinHold, height = 2, width =10 )
# spinHoldButton.place(x=100, y=200)



