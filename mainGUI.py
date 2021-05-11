from tkinter import *
import Software_Functions as sf
# from PIL import ImageTk, Image
import values
import motor_control as motor
try:
    from configparser import ConfigParser
except ImportError:
    from ConfigParser import ConfigParser  # ver. < 3.0


values.init() # creates global variables


#----------------------------------------------------------------------
# Arman Alert - GLOBAL CONFIGS ######### 
# Tinker with ArmanPropertiesMock directory to fully understand how it works. The reason why I named with string_val..., int_val... is so that we parse proper types. 
# Reading data and parsing right when getting: string=config.get, bool=config.getboolean, int=config.getint, float=config.getfloat
# For now checkout the example under "An Example". Its 3 lines of code everytime we need to set a global property. And 1 line to get the current. 
# instantiate Parser
config = ConfigParser()
# parse existing file
config.read('spmProps.ini')
# Initial Prop Testing: reading all the current GlobalProperties
# globalDest = config.get('section_a', 'destination')
# globalUser = config.get('section_a', 'string_val_user')
# globalMetricForSpeed = config.get('section_a', 'string_val_inchFeetCentimeterPerSecond')
# globalSysOnOff = config.getboolean('section_a', 'bool_val_SystemOnMeansTrue')
# globalPropPosition = config.getint('section_a', 'int_val_propPosition')
# globalSpeed = config.getfloat('section_a', 'float_val_speed')
# print(globalDest)
# print(globalUser)
# print(globalMetricForSpeed)
# print(globalSysOnOff)
# print(globalPropPosition)
# print(globalSpeed)
# An Example:--------------Simple
# Lets say we have a field in the gui that sets the username
# (change input then run) Then update existing key in the spmProps.ini for centrally recognizing the change. 
# inputUsername = 'Nick'
# config.set('section_a', 'string_val_user', inputUsername)
# -----Update the Prop File itself : Must run after every SET Operation-------------
# with open('spmProps.ini', 'w') as configfile:
#     config.write(configfile)
# print(config.get('section_a', 'string_val_user'))
#----------------------------------------------------------------------

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

# Declaring the sliders now so that the can be called in button functions. This is required since
# widgets are sorted by the page they appear on
# positionSlider = Scale()
# positionSliderDebug = Scale()
# positionSliderCal = Scale()
# positionSliderPro = Scale()
positionSliderList = []
varList = []
varList2 = []

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

# This is the image that I feel deserves a spot on the start page
# startPageImage = ImageTk.PhotoImage(Image.open("SPMLogo.jpg"))
# Label(startPage, image=startPageImage).place(x=150, y=100, width=690, height=270)

# This debug button should lead to a page with buttons/functions that we want for testing but probably wont be
# included as part of product features. For final product, the simplest way to remove this is to simply comment out
# the debugButton.place line. This removes the button, and prevents access to testing functions, without having to
# alter code

# adding information fields (Alex Kogan)
# --------------------------------------------------------------------
# Speed display value
speedFrameStart = LabelFrame(startPage, text="SPEED (ft/s)")
speedFrameStart.place(x=10, y=100, width=120, height=50)

speedSpecStart = Label(startPage, text=str(round(motor.rpm_to_speed(motor.sleep_to_rpm(values.SPEED), values.pulley_diameter), 2)))
speedSpecStart.place(x=12, y=120, width=80, height=20)

# Speed display with buttons to change value
speedFrameStartBot = LabelFrame(startPage, text="SPEED (ft/s)")
speedFrameStartBot.place(x=400, y=430, width=120, height=50)

speedSpecStartBot = Label(startPage, text=str(round(motor.rpm_to_speed(motor.sleep_to_rpm(values.SPEED), values.pulley_diameter), 2)))
speedSpecStartBot.place(x=402, y=450, width=80, height=20)

speedDown = Button(startPage, text='-', command=(lambda: motor.speedDownUpdate(varList)))
speedDown.place(x=350, y=438, width=40, height=40)

speedUp = Button(startPage, text='+', command=(lambda: motor.speedUpUpdate(varList)))
speedUp.place(x=528, y=438, width=40, height=40)

# Position display value
positionFrameStart = LabelFrame(startPage, text="POSITION (ft)")
positionFrameStart.place(x=10, y=150, width=120, height=50)

positionSpecStart = Label(startPage, text=str(round(motor.position_to_distance(values.POSITION, values.pulley_diameter, values.drive_ratio), 2)))
positionSpecStart.place(x=12, y=170, width=80, height=20)

# Ratio display value
ratioFrameStart = LabelFrame(startPage, text="Drive Ratio")
ratioFrameStart.place(x=10, y=200, width=120, height=50)

ratioSpecStart = Label(startPage, text=str(values.drive_ratio))
ratioSpecStart.place(x=12, y=220, width=80, height=20)

# Ratio display with buttons to change values
ratioFrameStartBot = LabelFrame(startPage, text="Drive Ratio")
ratioFrameStartBot.place(x=400, y=480, width=120, height=50)

ratioSpecStartBot = Entry(startPage)
ratioSpecStartBot.place(x=405, y=500, width=80, height=20)

ratioDown = Button(startPage, text='-', command=(lambda: motor.ratioDownUpdate(varList2)))
ratioDown.place(x=350, y=488, width=40, height=40)

# ratioUp = Button(startPage, text='+', command=(lambda: motor.ratioUpUpdate(varList2)))
# ratioUp.place(x=528, y=488, width=40, height=40)

#--------------------------------------------------------------------
# This button leads us to the calibration page
calibrateButton = Button(startPage, text='Calibrate', command=calibratePage.tkraise)
calibrateButton.place(x=10, y=350, width=100, height=50)

# This button will lead us to the profile page
profilesButton = Button(startPage, text='Profiles', command=profilePage.tkraise)
profilesButton.place(x=10, y=400, width=100, height=50)

# This button exits. root.quit works on some devices and not others.
exitButton = Button(startPage, text="Exit", command=root.destroy)
exitButton.place(x=10, y=450, width=100, height=50)

leftMove = Button(startPage, text='LEFT')
leftMove.place(x=700, y=400, width=100, height=100)

rightMove = Button(startPage, text='RIGHT')
rightMove.place(x=800, y=400, width=100, height=100)

leftMove.bind("<Button-1>", lambda x: motor.move(-1,positionSliderList))
leftMove.bind("<ButtonRelease-1>", motor.stoploopevent2)

rightMove.bind("<Button-1>", lambda x: motor.move(1,positionSliderList))
rightMove.bind("<ButtonRelease-1>", motor.stoploopevent2)

sf.calWarn()

########################END START PAGE############################

#######################CALIBRATE PAGE#####################

Label(calibratePage, text='CALIBRATION').place(x=450, y=0, width=150, height=50)

positionSliderCal = Scale(calibratePage, from_=0, to=1000, orient=HORIZONTAL, length=1000)
positionSliderCal.place(x=10, y=30, width=1000, height=50)


# adding information fields (Alex Kogan)
#--------------------------------------------------------------------
# Speed display value
speedFrameCal = LabelFrame(calibratePage, text="SPEED (ft/s)")
speedFrameCal.place(x=10, y=100, width=120, height=50)

speedSpecCal = Label(calibratePage, text=str(round(motor.rpm_to_speed(motor.sleep_to_rpm(values.SPEED), values.pulley_diameter), 2)))
speedSpecCal.place(x=12, y=120, width=80, height=20)

# Speed display with buttons to change value
speedFrameCalBot = LabelFrame(calibratePage, text="SPEED (ft/s)")
speedFrameCalBot.place(x=400, y=430, width=120, height=50)

speedSpecCalBot = Label(calibratePage, text=str(round(motor.rpm_to_speed(motor.sleep_to_rpm(values.SPEED), values.pulley_diameter), 2)))
speedSpecCalBot.place(x=402 , y=450, width=80, height=20)

speedDown = Button(calibratePage, text='-', command=(lambda: motor.speedDownUpdate(varList)))
speedDown.place(x=340, y=433, width=50, height=50)

speedUp = Button(calibratePage, text='+', command=(lambda: motor.speedUpUpdate(varList)))
speedUp.place(x=528, y=433, width=50, height=50)

# Position display value
positionFrameCal = LabelFrame(calibratePage, text="POSITION (ft)")
positionFrameCal.place(x=10, y=150, width=120, height=50)

positionSpecCal = Label(calibratePage, text=str(values.POSITION))
positionSpecCal.place(x=12, y=170, width=80, height=20)

# Ratio display value
ratioFrameCal = LabelFrame(calibratePage, text="Drive Ratio")
ratioFrameCal.place(x=10, y=200, width=120, height=50)

ratioSpecCal = Label(calibratePage, text=str(values.drive_ratio))
ratioSpecCal.place(x=12, y=220, width=80, height=20)

# Ratio display with buttons to change values
ratioFrameCalBot = LabelFrame(calibratePage, text="Drive Ratio")
ratioFrameCalBot.place(x=400, y=480, width=120, height=50)

ratioSpecCalBot = Label(calibratePage, text=str(values.drive_ratio))
ratioSpecCalBot.place(x=402, y=500, width=80, height=20)

ratioDown = Button(calibratePage, text='-', command=(lambda: motor.ratioDownUpdate(varList2)))
ratioDown.place(x=350, y=488, width=40, height=40)

# ratioUp = Button(calibratePage, text='+', command=(lambda: motor.ratioUpUpdate(varList2)))
# ratioUp.place(x=528, y=488, width=40, height=40)

#--------------------------------------------------------------------


# The done button returns us to the start page
doneButtonCal = Button(calibratePage, text='Done', command=startPage.tkraise)
doneButtonCal.place(x=10, y=350, width=100, height=50)


# This border just creates a graphical box around the instructions
borderCal = LabelFrame(calibratePage, text="Instructions")
borderCal.place(x=250, y=130, width=600, height=300)

# This is the label for the instructions. The width and height have to be less then the border since these go inside
# of it. The text will overlap and hide the border if the width and height are too large
instructCal = Label(calibratePage, justify=LEFT, text='Step 1: Use manual control buttons to move prop carrier towards\n    drive unit untilthe end pulley drive is reached.\n    LEAVE ROOM BETWEEN CARRIER AND PULLEY.\nStep 2: Press "Start Point" button.\nStep 3: Use manual control buttons to move prop carrier to\n    opposite end of pulley drive.\n    LEAVE ROOM BETWEEN CARRIER AND PULLEY.\nStep 4: Press "End Position" button.\n\nIf finished press "Confirm". To recalibrate begin from Step 1')
instructCal.place(x=300, y=150, width=540, height=200)

# These are the buttons to set the start and end points of our moveable range
# It was originally discussed that it would be a single button that dynamically changes, but they seems
# more confusing for the user and more work for us. For the time being, its two buttons.
startPointCal = Button(calibratePage, text='Start Point',command=sf.setStartPoint)
startPointCal.place(x=350, y=350, width=100, height=60)
endPointCal = Button(calibratePage, text='End Point', command=sf.setEndPoint)
endPointCal.place(x=450, y=350, width=100, height=60)
confirmCal = Button(calibratePage, text='Confirm',command=(lambda: sf.confirmCalibration(positionSliderList))) # this button MUST call a function which changes CALIBRATED variable to True. This carriable must impede motor function when false
confirmCal.place(x=550, y=350, width=100, height=60)

leftMoveCal = Button(calibratePage, text='LEFT')
leftMoveCal.place(x=700, y=400, width=100, height=100)

rightMoveCal = Button(calibratePage, text='RIGHT')
rightMoveCal.place(x=800, y=400, width=100, height=100)

leftMoveCal.bind("<Button-1>", lambda x: motor.move(-1,positionSliderList))
leftMoveCal.bind("<ButtonRelease-1>", motor.stoploopevent2)

rightMoveCal.bind("<Button-1>", lambda x: motor.move(1,positionSliderList))
rightMoveCal.bind("<ButtonRelease-1>", motor.stoploopevent2)

#####################END CALIBRATE PAGE#########################

####################PROFILE PAGE##########################
Label(profilePage, text='PROFILE').place(x=450, y=0, width=150, height=50)

positionSliderPro = Scale(profilePage, from_=0, to=1000, orient=HORIZONTAL, length=1000)
positionSliderPro.place(x=10, y=30, width=1000, height=50)


# adding information fields (Alex Kogan)
#--------------------------------------------------------------------
# Speed display value
speedFrameProfile = LabelFrame(profilePage, text="SPEED (ft/s)")
speedFrameProfile.place(x=10, y=100, width=120, height=50)

speedSpecProfile = Label(profilePage, text=str(round(motor.rpm_to_speed(motor.sleep_to_rpm(values.SPEED), values.pulley_diameter), 2)))
speedSpecProfile.place(x=12, y=120, width=80, height=20)

# Speed display with buttons to change value
speedFrameProfileBot = LabelFrame(profilePage, text="SPEED (ft/s)")
speedFrameProfileBot.place(x=400, y=430, width=120, height=50)

speedSpecProfileBot = Label(profilePage, text=str(round(motor.rpm_to_speed(motor.sleep_to_rpm(values.SPEED), values.pulley_diameter), 2)))
speedSpecProfileBot.place(x=402 , y=450, width=80, height=20)

speedDown = Button(profilePage, text='-', command=(lambda: motor.speedDownUpdate(varList)))
speedDown.place(x=350, y=438, width=40, height=40)

speedUp = Button(profilePage, text='+', command=(lambda: motor.speedUpUpdate(varList)))
speedUp.place(x=528, y=438, width=40, height=40)

# Position display value
positionFrameProfile = LabelFrame(profilePage, text="POSITION (ft)")
positionFrameProfile.place(x=10, y=150, width=120, height=50)

positionSpecProfile = Label(profilePage, text=str(values.POSITION))
positionSpecProfile.place(x=12, y=170, width=80, height=20)

# Ratio display value
ratioFrameProfile = LabelFrame(profilePage, text="Drive Ratio")
ratioFrameProfile.place(x=10, y=200, width=120, height=50)

ratioSpecProfile = Label(profilePage, text=str(values.drive_ratio))
ratioSpecProfile.place(x=12, y=220, width=80, height=20)

# Ratio display with buttons to change values
ratioFrameProfileBot = LabelFrame(profilePage, text="Drive Ratio")
ratioFrameProfileBot.place(x=400, y=480, width=120, height=50)

ratioSpecProfileBot = Label(profilePage, text=str(values.drive_ratio))
ratioSpecProfileBot.place(x=402, y=500, width=80, height=20)

ratioDown = Button(profilePage, text='-', command=(lambda: motor.ratioDownUpdate(varList2)))
ratioDown.place(x=350, y=488, width=40, height=40)

# ratioUp = Button(profilePage, text='+', command=(lambda: motor.ratioUpUpdate(varList2)))
# ratioUp.place(x=528, y=488, width=40, height=40)

#--------------------------------------------------------------------


# The done button returns us to the start page
doneButtonPro = Button(profilePage, text='Done', command=startPage.tkraise)
doneButtonPro.place(x=10, y=350, width=100, height=50)

leftMovePro = Button(profilePage, text='LEFT')
leftMovePro.place(x=700, y=400, width=100, height=100)

rightMovePro = Button(profilePage, text='RIGHT')
rightMovePro.place(x=800, y=400, width=100, height=100)

leftMovePro.bind("<Button-1>", lambda x: motor.move(-1,positionSliderList))
leftMovePro.bind("<ButtonRelease-1>", motor.stoploopevent2)

rightMovePro.bind("<Button-1>", lambda x: motor.move(1,positionSliderList))
rightMovePro.bind("<ButtonRelease-1>", motor.stoploopevent2)


#profilePage.bind('<Return>', (lambda event, e=ents: sf.fetch(e)))

# These are the entry boxes and their labels. They are blank by default. The user can type into them, and store the
# typed info into csv files. When loading csv files, the csv data will be displayed in these entry boxes.
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

runPro = Button(profilePage, text='Run', command=(lambda: motor.auto_move(positionSliderList,positionPro)))
runPro.place(x=625, y=300, width=50, height=25)

savePro = Button(profilePage, text='Save', command=(lambda: sf.save_profile(profileEntries)))
savePro.place(x=700, y=300, width=50, height=25)

deletePro = Button(profilePage, text='Delete', command=(lambda: sf.delete_profile(profileEntries)))
deletePro.place(x=775, y=300, width=50, height=25)

loadPro = Button(profilePage, text='Load', command=lambda: sf.read_profile(profilePage, profileEntries))
loadPro.place(x=850, y=300, width=50, height=25)

####################END PROFILE PAGE#############################


positionSliderList = [positionSlider, positionSliderCal, positionSliderPro]
varList = [speedSpecStart, speedSpecStartBot, speedSpecCal, speedSpecCalBot, speedSpecProfile, speedSpecProfileBot]
varList2 = [ratioSpecStart, ratioSpecStartBot, ratioSpecCal, ratioSpecProfile]


# We call tkraise on startPage so that it is the first frame we see once we enter the main loop
# Whatever page is raised here will be the first page you see
startPage.tkraise()
root.mainloop()
