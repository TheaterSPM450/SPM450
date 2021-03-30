from tkinter import *
import time
import os
#import Hardware_Functions as hf
import Software_Functions as sf


# NICK ALERT ##########
# Hardware functionality may be commented out, simply so that people can work on code from their desktops
# I attempted to comment things out in a way that makes it easy to restore full functionality on RasPi
# For example
# savePro = Button(profilePage, text='Save')#, command=(lambda e=ents: sf.fetch(e)))
# This button has a # after the final parenthesis, so that i could test button without working function
# It can simply be restored by deleting the extra parenthesis and '#', as rest of line was preserved


# import tkFont
# myFont = tkFont.Font(family = 'Helvetica', size = 8, weight = 'bold')

# Some of the GPIO variable declarations and all functions were moved to Hardware_functions file
#hf.GPIO_Initialisation()

# This is some initialization from old profile window testing
profiles = []
loadedFiles = ""
fields = ["speed", "ratio", "diameter", "position", "filename"]

# declare base GUI window
root = Tk()
root.title("Stage Prop Mover 450")
root.geometry("1024x600")

# This is where we initialize the frames(or windows) for the program
# Each frame represents a separate page in the program that can be traveled to with a button press
startPage = Frame(root)
calibratePage = Frame(root)
profilePage = Frame(root)
debugPage = Frame(root)

pageWidth = 1024
pageHeight = 600
# The width and height of the frame should match root, or else there are issues with button placement
startPage.place(x=0, y=0, width=pageWidth, height=pageHeight)
calibratePage.place(x=0, y=0, width=pageWidth, height=pageHeight)
profilePage.place(x=0, y=0, width=pageWidth, height=pageHeight)
debugPage.place(x=0, y=0, width=pageWidth, height=pageHeight)

# NICK NOTES: All buttons should be positioned using ".place" as opposed to .pack or .grid
# .place allows for specific positioning of buttons, based on the pixel number.
# (x position, y position, width of object, height of object)
# just make sure x and y is within the geometry of the frame. (800x400 at time of comment)
# .place will not work if the frame is called using .grid or .pack


######################START PAGE###############################
Label(startPage, text='HOME PAGE').place(x=450, y=0, width=150, height=50)

# This is the slider that is tracking the position of the stage prop
# It is updated by the position_up/down functions which are currently tied to the left and right buttons
# Although the slider can be directly interacted with, doing so does not update the global position variable
# This behavior is intended, as we only want the prop to move on button presses
# The value associated with the slider will self-correct on the next button press
positionSlider = Scale(startPage, from_=0, to=1000, orient=HORIZONTAL, length=1000)
positionSlider.place(x=10, y=30, width=1000, height=50)

# This debug button should lead to a page with buttons/functions that we want for testing
# but probably wont be included as part of product features
# For final product, the simplest way to remove this is to simply comment out the debugButton.place line
# This removes the button, and prevents access to testing functions, without having to alter code

debugButton = Button(startPage, text='Debug', command=debugPage.tkraise)
debugButton.place(x=10, y=300, width=100, height=50)
# This button leads us to the calibration page
calibrateButton = Button(startPage, text='Calibrate', command=calibratePage.tkraise)
calibrateButton.place(x=10, y=350, width=100, height=50)

# This button will lead us to the profile page
profilesButton = Button(startPage, text='Profiles', command=profilePage.tkraise)
profilesButton.place(x=10, y=400, width=100, height=50)

# This button exits.
exitButton = Button(startPage, text="Exit", command=root.destroy)
exitButton.place(x=10, y=450, width=100, height=50)

# These are the manual control buttons, that simply move the stepper motor in the desired direction.
# Currently, the movement is not tied to any calibrated start or end point, nor can the speed be controlled.
leftMove = Button(startPage, text='LEFT', repeatdelay=20, repeatinterval=1, command=lambda: sf.position_down(positionSlider))#=hf.spinLeft)
leftMove.place(x=700, y=400, width=100, height=100)
rightMove = Button(startPage, text='RIGHT', repeatdelay=1, repeatinterval=1, command=lambda: sf.position_up(positionSlider))#=hf.spinRight)
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
instructCal = Label(calibratePage, text='Step 1: This is where the instructions will go')
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
leftMoveCal = Button(calibratePage, text='LEFT', repeatdelay=20, repeatinterval=1, command=lambda: sf.position_down(positionSlider))#=hf.spinLeft)
leftMoveCal.place(x=700, y=400, width=100, height=100)
rightMoveCal = Button(calibratePage, text='RIGHT', repeatdelay=1, repeatinterval=1, command=lambda: sf.position_up(positionSlider))#=hf.spinRight)
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
leftMovePro = Button(profilePage, text='LEFT', repeatdelay=20, repeatinterval=1, command=lambda: sf.position_down(positionSlider))#=hf.spinLeft)
leftMovePro.place(x=700, y=400, width=100, height=100)
rightMovePro = Button(profilePage, text='RIGHT', repeatdelay=1, repeatinterval=1, command=lambda: sf.position_up(positionSlider))#hf.spinRight)
rightMovePro.place(x=800, y=400, width=100, height=100)


# Some of this profile code is pasted from an older file and is still none functioning due to changes in the gui
# The button placements should be close to where they need to be
#ents = sf.makeform(profilePage)
#profilePage.bind('<Return>', (lambda event, e=ents: sf.fetch(e)))

Label(profilePage, text='Filename').place(x=700, y=110, width=70, height=15)
filenamePro = Entry(profilePage)
filenamePro.place(x=800, y=100, width=200, height=25)
Label(profilePage, text='Ratio').place(x=700, y=150, width=70, height=15)
ratioPro = Entry(profilePage)
ratioPro.place(x=800, y=140, width=200, height=25)
Label(profilePage, text='Diameter').place(x=700, y=190, width=70, height=15)
diameterPro = Entry(profilePage)
diameterPro.place(x=800, y=180, width=200, height=25)
Label(profilePage, text='Speed').place(x=700, y=230, width=70, height=15)
speedPro = Entry(profilePage)
speedPro.place(x=800, y=220, width=200, height=25)
Label(profilePage, text='Position').place(x=700, y=270, width=70, height=15)
positionPro = Entry(profilePage)
positionPro.place(x=800, y=260, width=200, height=25)

# This global variable holds the entry textbox's, so that we can later update the buttons
# with the current profile info using .set or .config. This variable will be passed into the save function.
profileEntries = [ratioPro, diameterPro, speedPro, positionPro, filenamePro]


savePro = Button(profilePage, text='Save', command=(lambda: sf.save_profile(profileEntries)))
savePro.place(x=700, y=300, width=50, height=25)
deletePro = Button(profilePage, text='Delete', command=(lambda: sf.delete_profile(profileEntries)))
deletePro.place(x=775, y=300, width=50, height=25)
loadPro = Button(profilePage, text='Load', command=lambda: sf.read_profile(profilePage, profileEntries))
loadPro.place(x=850, y=300, width=50, height=25)

####################END PROFILE PAGE#############################

####################DEBUG PAGE##########################

Label(debugPage, text='DEBUG').place(x=450, y=0, width=150, height=50)

spinButtonDebug = Button(debugPage, text="SPIN ON")#, command=hf.spin)
spinButtonDebug.place(x=400, y=350, width=100, height=50)

spinForSetTimeButtonDebug = Button(debugPage, text="SpinForSetTime")#, command=hf.spinForSetTime)
spinForSetTimeButtonDebug.place(x=500, y=350, width=100, height=50)
# # RepeatIsIn(ms)
spinHoldButton = Button(debugPage, text="spinHoldButton", repeatdelay=1, repeatinterval=1)#, command=hf.spinHold)
spinHoldButton.place(x=400, y=400, width=100, height=50)

doneButtonDebug = Button(debugPage, text='Done', command=startPage.tkraise)
doneButtonDebug.place(x=10, y=350, width=100, height=50)

####################END DEBUG PAGE##########################


# We call tkraise on startPage so that it is the first frame we see once we enter the main loop
# Whatever page is raised here will be the first page you see
startPage.tkraise()
root.mainloop()
