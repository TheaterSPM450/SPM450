'''
motor_control.py

Author: Alex Kogan
Date: 4/24/2021

updated 5/5/21

threading code for stepper control to integrate with GUI


'''
# from tkinter import *
import time
import threading
from math import pi
import RPi.GPIO as GPIO
import Software_Functions
try:
    from configparser import ConfigParser
except ImportError:
    from ConfigParser import ConfigParser  # ver. < 3.0

config = ConfigParser()
# parse existing file
config.read('spmProps.ini')


#vars
pulley_diameter = 1.5 
drive_ratio = 1.0
do_loop = False # used for thread termination, could be changed to "motor_enable" or something similar
SPEED = .0005 # pulse sleep time, in seconds as a float
POSITION = 0 # an accumulator variable which can be used for current position tracking
DESTINATION = 0
pulse = 40  # driver pulse signal GPIO pin 40
direction = 36  # driver pulse direction GPIO pin 36
threads = [] # thread queue

# GPIO Drivers
GPIO.setmode(GPIO.BOARD)
GPIO.setup(pulse, GPIO.OUT)
GPIO.output(pulse, GPIO.LOW)
GPIO.setup(direction, GPIO.OUT)
GPIO.output(direction, GPIO.LOW)

#=============================================================

# position_to_distance()
# IMPORTANT: the output of this function is only intended for GUI/user display purposes
#            not for control purposes
# takes position count, converts to distance in feet:
#   takes postion (motor pulses), transfer pulley diameter (inches), drive ratio
#   and calculates position from calibration start point (zero point) in feet 
# 
# calculates pulley circumference in feet
# returns distance by dividing position count by steps per revolution (200) * transfer pulley circumference * drive ratio
#
# INPUT: float, float, float
# OUTPUT: float
def position_to_distance(position, pulley_diameter, drive_ratio):
    pulley_circumference_ft = (pulley_diameter * pi) / 12
    return (position / 200) * pulley_circumference_ft * drive_ratio


# rpm_to_pulsesleep()
# takes a rpm value and returns a sleep duration
# value in terms of seconds for motor rpm control
#
# calculates 1 second divived by rpm value divided
# by 60, time 400(2 phase halfs times 200 pulses per revolution)
#
# INPUT: integer
# OUTPUT: float
def rpm_to_pulsesleep(rpm):
#    print((1 / (400.0 * (rpm / 60.0))))
    return (1 / (400.0 * (rpm / 60.0)))


# sleep_to_rpm()
# converts sleep delay to time (Speed) to rpm
#
#
#
def sleep_to_rpm(t):
    return ((1 / t) / (400)) * 60 # RPM = ((1 second / sleeptime) / (2 phases * 200 pulses_per_rotation)) * 60 seconds


# rpm_to_speed()
# takes rpm[integer] and pulley diameter[float] (inches) and returns
# a linear speed in feet/sec (ft/s)
#
# INPUT: float, float
# OUTPUT: float
def rpm_to_speed(rpm, diameter):
    seconds = 60.0
    inches_per_foot = 12
    circumference = (diameter/inches_per_foot) * pi
    return (circumference * rpm / seconds)


# speed_to_rpm()
# takes speed[float] in feet/sec (ft/s) and pulley diameter[float] (inches)
# and returns an rpm[float]
#
# INPUT: float, float
# OUTPUT: float
def speed_to_rpm(speed, diameter):
    seconds = 60.0
    inches_per_foot = 12
    circumference = (diameter/inches_per_foot) * pi
    return (speed * seconds) / circumference


# speed_to_pulse_time()
# 
#
# INPUTS:
#   speed - speed of cart as a float value representing miles per hour
#   drive_pulley_diameter - diameter of driven pulley (not motor pulley) in inches as a float value
#   drive_ratio - final gear ratio of drive as a float value
#
# OUTPUT: float decimal representing fraction of a second between driver pulse phases
def speed_to_pulse_time(speed, driven_pulley_diameter, drive_ratio):
    return rpm_to_pulsesleep(speed_to_rpm(speed, driven_pulley_diameter) / drive_ratio)

#===================================================================


# THREAD FUNCTION (manual control)
# loop function to run on thread for l_button and r_button click binding 
def move_thread(x,positionSliderList): # takes an input of -1 or 1 from caller
    global do_loop, POSITION, pulse, direction
    do_loop = True
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
        position_slider_update(positionSliderList)
        # numField.delete(0, END)
        # numField.insert(0,str(round(control.position_to_distance(POSITION, pulley_diameter, drive_ratio), 2)))
   


# PROGRAM THREAD FUNCTION (auto control)
# loop function to run on thread for execute program button 
def auto_move_thread(positionSliderList,positionPro): # takes no arguement, instead determines direction based on POSITION relative to DESTINATION
    global do_loop, POSITION, DESTINATION, pulse, direction
    config.read('spmProps.ini')
    Dest = int(config.get('section_a', 'destination'))
    print("FROM RUN: " + str(config.get('section_a', 'destination')))
    Dest = int(positionPro.get())
    do_loop = True
    x = 0
    #------------------DIRECTION SET----------------------------------
    if(Dest < POSITION):
        GPIO.output(direction,GPIO.LOW)
        x = -1
    else:
        GPIO.output(direction,GPIO.HIGH)
        x = 1
    #-----------------------------------------------------------------
    #-----------SOFT START functionallity-----------------------------
    new_SPEED = .01 # create new_speed copy set .5 (high wait for long step delay)
    deduction = (new_SPEED - SPEED) / 150  # calculate time deduction
    while(do_loop and POSITION != Dest):
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
        position_slider_update(positionSliderList)

        # numField.delete(0, END)
        # numField.insert(0,str(round(control.position_to_distance(POSITION, pulley_diameter, drive_ratio), 2)))


# stop thread function
def stoploopevent2(self):
    global do_loop
    do_loop = False
    time.sleep(.1) # delay to let thread finish
    GPIO.output(pulse,GPIO.LOW) # set pulse pin low


# thread start function for l_button and r_button
def move(x,positionSliderList):
    th = threading.Thread(target= lambda: move_thread(x,positionSliderList))
    threads.append(th)
    th.daemon
    th.start()

# thread start function for l_button and r_button
def auto_move(positionSliderList,positionPro):
    th = threading.Thread(target= auto_move_thread(positionSliderList,positionPro))
    threads.append(th)
    th.daemon
    th.start()


def position_slider_update(positionSliderList):
    global POSITION
    for i in positionSliderList:
        i.set(POSITION)








# exits program
# def exitProgram():
# 	print("Exit Button pressed")
# 	tk.destroy()


#BUTTONS, ENTRIES and WIDGETS

#/////////////////////////////////////////////////////
#               <<<<< LEFT <<<<<
#/////////////////////////////////////////////////////
# left button (decrement field)
# l_button = Button(tk, text='<<<< L <<<<', bg='yellow', justify='left')
# l_button.pack()

# Button-1 is left mouse button.
# The following 2 lines bind the mouse click and release
# to separate function calls. Click down starts a thread,
# release changes a thread condition to false

# l_button.bind("<Button-1>", lambda x: move(-1))
# l_button.bind("<ButtonRelease-1>", stoploopevent2)

#/////////////////////////////////////////////////////
#               ***** DISPLAY *****
#/////////////////////////////////////////////////////
# l1 = Label(tk, text="Position: ")
# l1.pack()

# display field
# numField = Entry(tk, bg='white', bd='4', state='normal', justify='center', width=10)
# numField.pack()
# numField.insert(0,str(POSITION))

#/////////////////////////////////////////////////////
#               >>>>> RIGHT >>>>>
#/////////////////////////////////////////////////////
# right button (increment field)
# r_button = Button(tk, text='>>>> R >>>>', bg='orange', justify='right')
# r_button.pack()

# Button-1 is left mouse button.
# The following 2 lines bind the mouse click and release
# to separate function calls. Click down starts a thread,
# release changes a thread condition to false

# r_button.bind("<Button-1>", lambda x: move(1))
# r_button.bind("<ButtonRelease-1>", stoploopevent2)



# exitButton  = Button(tk, text = "Exit", command = exitProgram, height =2 , width = 10, bg='red', bd='4') 
# exitButton.pack(side = BOTTOM)



# tk.mainloop()