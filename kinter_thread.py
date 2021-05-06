'''
kinter_thread.py

Author: Alex Kogan
Date: 3/15/2021

threading code for program execution
'''
from tkinter import *
import time
import threading
import RPi.GPIO as GPIO
import spm_control_akogan as control

#vars
pulley_diameter = 1.5 
drive_ratio = 1.0
do_loop = FALSE # used for thread termination, could be changed to "motor_enable" or something similar
SPEED = .0005 # pulse sleep time, in seconds as a float
POSITION = 0 # an accumulator variable which can be used for current position tracking
DESTINATION = 0
pulse = 40  # driver pulse signal GPIO pin 40
direction = 36  # driver pulse direction GPIO pin 36
threads = [] # thread queue

# WAIT = .500 # sleep delay time variable for testing/development purposes without a RasPi (since RPi is only supported on on Pi)



# led = 32  # testing purposes led pin 32


# freq = 100  # frequency variable for testing PWM library


# GPIO Drivers
GPIO.setmode(GPIO.BOARD)
# GPIO.setup(led, GPIO.OUT)
# GPIO.output(led, GPIO.LOW)
GPIO.setup(pulse, GPIO.OUT)
GPIO.output(pulse, GPIO.LOW)
GPIO.setup(direction, GPIO.OUT)
GPIO.output(direction, GPIO.LOW)

tk = Tk() # tk object

# set minimum window size to 4:3 by setting resolution to 800x600
tk.minsize(800, 600)


# THREAD FUNCTION
# loop function to run on thread for startButton
# def startloopevent():
#     global do_loop # main thread do_loop access
#     global POSITION # main thread POSITION access
#     do_loop = TRUE # enable loop condition
#     x = 0
#     countlim = 1000
#     # this loop is similar to stepper pulse actuation
#     # instead the background color is changed between 2 states
#     # with a pause in between
#     while(do_loop and x < countlim):
#         tk.configure(bg='grey')
#         print("ON")
#         time.sleep(WAIT)
#         tk.configure(bg='azure')
#         print("OFF")
#         time.sleep(WAIT)
#         POSITION += 1
#         numField.delete(0, END)
#         numField.insert(0,str(POSITION))
#         x += 1
    

# THREAD FUNCTION
# loop function to run on thread for l_button and r_button click binding 
# def move_thread(x): # takes an input of -1 or 1 from caller
#     global do_loop, POSITION, pulse, direction
#     do_loop = TRUE
#     if(x < 0):
#         GPIO.output(direction,GPIO.LOW)
#     else:
#         GPIO.output(direction,GPIO.HIGH)

#     # create new_speed copy set .5 (high wait for long step delay)
#     # calculate increment to decreese
#     while(do_loop):
#         GPIO.output(pulse,GPIO.HIGH)
#         time.sleep(SPEED)
#         GPIO.output(pulse,GPIO.LOW)
#         time.sleep(SPEED)
#         POSITION += x
#         numField.delete(0, END)
#         numField.insert(0,str(POSITION))
        


#/////////////////////////////////////////////////////////////////////////////////////////////////////

# THREAD FUNCTION prototype
# loop function to run on thread for l_button and r_button click binding 
def move_thread(x): # takes an input of -1 or 1 from caller
    global do_loop, POSITION, pulse, direction
    do_loop = TRUE
    #------------------DIRECTION SET----------------------------------
    if(x < 0):
        GPIO.output(direction,GPIO.LOW)
    else:
        GPIO.output(direction,GPIO.HIGH)
    #-----------------------------------------------------------------
    #-----------SOFT START functionallity-----------------------------
    new_SPEED = .01 # create new_speed copy set .5 (high wait for long step delay)
    deduction = (new_SPEED - SPEED) / 150  # calculate time deduction
    while(do_loop):
        if(new_SPEED > SPEED):
            new_SPEED -= deduction
            # print("deducting")
            if(new_SPEED < SPEED):
                new_SPEED = SPEED
    #-----------------------------------------------------------------
        GPIO.output(pulse,GPIO.HIGH)
        time.sleep(new_SPEED)
        GPIO.output(pulse,GPIO.LOW)
        time.sleep(new_SPEED)
        POSITION += x
        numField.delete(0, END)
        numField.insert(0,str(round(control.position_to_distance(POSITION, pulley_diameter, drive_ratio), 2)))


#/////////////////////////////////////////////////////////////////////////////////////////////////////

# PROGRAM THREAD FUNCTION
# loop function to run on thread for execute program button 
def auto_move_thread(): # takes no arguement, instead determines direction based on POSITION relative to DESTINATION
    global do_loop, POSITION, DESTINATION, pulse, direction
    do_loop = TRUE
    #------------------DIRECTION SET----------------------------------
    if(DESTINATION < POSITION):
        GPIO.output(direction,GPIO.LOW)
    else:
        GPIO.output(direction,GPIO.HIGH)
    #-----------------------------------------------------------------
    #-----------SOFT START functionallity-----------------------------
    new_SPEED = .01 # create new_speed copy set .5 (high wait for long step delay)
    deduction = (new_SPEED - SPEED) / 150  # calculate time deduction
    while(do_loop and POSITION != DESTINATION):
        if(new_SPEED > SPEED):
            new_SPEED -= deduction
            # print("deducting")
            if(new_SPEED < SPEED):
                new_SPEED = SPEED
    #-----------------------------------------------------------------
        GPIO.output(pulse,GPIO.HIGH)
        time.sleep(new_SPEED)
        GPIO.output(pulse,GPIO.LOW)
        time.sleep(new_SPEED)
        POSITION += x
        numField.delete(0, END)
        numField.insert(0,str(round(control.position_to_distance(POSITION, pulley_diameter, drive_ratio), 2)))
   





# stop thread function
# def stoploopevent():
#     global do_loop
#     do_loop = FALSE
#     time.sleep(.1) # delay to let thread finish
#     GPIO.output(pulse,GPIO.LOW) # set pulse pin low


# stop thread function
def stoploopevent2(self):
    global do_loop
    do_loop = FALSE
    time.sleep(.1) # delay to let thread finish
    GPIO.output(pulse,GPIO.LOW) # set pulse pin low to prevent motor noise and vibration when stationary 


# thread start function for startButton
# def st_thread():
#     th = threading.Thread(target=startloopevent) # create new thread running startloopevent function
#     threads.append(th)
#     th.daemon
#     th.start()


# thread start function for l_button and r_button
def move(x):
    th = threading.Thread(target= lambda: move_thread(x))
    threads.append(th)
    th.daemon
    th.start()


# does 1 click operation altering POSITION variable and numField according to input
# def click(x):
#     global POSITION
#     POSITION += x
#     numField.delete(0, END)
#     numField.insert(0,str(POSITION))


# exits program
def exitProgram():
	print("Exit Button pressed")
	tk.destroy()


#BUTTONS, ENTRIES and WIDGETS
# start loop
# startButton = Button(tk, text="START Thread", command=st_thread, height = 5, width =10 )
# startButton.pack()

# stop loop
# stopButton = Button(tk, text="STOP Thread", command= stoploopevent, height = 5, width =10)
# stopButton.pack()


# left button (decrement field)
l_button = Button(tk, text='<<<< L <<<<', bg='yellow', justify='left')
l_button.pack()
# Button-1 is left mouse button.
# The following 2 lines bind the mouse click and release
# to separate function calls. Click down starts a thread,
# release changes a thread condition to false
l_button.bind("<Button-1>", lambda x: move(-1))
l_button.bind("<ButtonRelease-1>", stoploopevent2)

l1 = Label(tk, text="Position: ")
l1.pack()
# display field
numField = Entry(tk, bg='white', bd='4', state='normal', justify='center', width=10)
numField.pack()
numField.insert(0,str(round(control.position_to_distance(POSITION, pulley_diameter, drive_ratio), 2)))

# right button (increment field)
r_button = Button(tk, text='>>>> R >>>>', bg='orange', justify='right')
r_button.pack()
# Button-1 is left mouse button.
# The following 2 lines bind the mouse click and release
# to separate function calls. Click down starts a thread,
# release changes a thread condition to false
r_button.bind("<Button-1>", lambda x: move(1))
r_button.bind("<ButtonRelease-1>", stoploopevent2)



exitButton  = Button(tk, text = "Exit", command = exitProgram, height =2 , width = 10, bg='red', bd='4') 
exitButton.pack(side = BOTTOM)



tk.mainloop()