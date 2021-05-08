from tkinter import *
import RPi.GPIO as GPIO
import time
import threading
from math import pi

#vars
do_loop = FALSE # used for thread termination, could be changed to "motor_enable" or something similar
SPEED = .00035 # pulse sleep time, in seconds as a float
POSITION = 0 # an accumulator variable which can be used for current position tracking
pulse = 40  # driver pulse signal GPIO pin 40
direction = 36  # driver pulse direction GPIO pin 36

# GPIO Drivers
GPIO.setmode(GPIO.BOARD)
GPIO.setup(pulse, GPIO.OUT)
GPIO.output(pulse, GPIO.LOW)
GPIO.setup(direction, GPIO.OUT)
GPIO.output(direction, GPIO.LOW)

#tk = Tk() # tk object

# set minimum window size to 4:3 by setting resolution to 800x600
#tk.minsize(800, 600)



# THREAD FUNCTION
# loop function to run on thread for l_button and r_button click binding
def move_thread(x): # takes an input of -1 or 1 from caller
    global do_loop, POSITION, pulse, direction
    do_loop = TRUE
    if(x < 0): # set direction pin based x value, -1, counterclockwise
        GPIO.output(direction,GPIO.LOW)
    else: # set direction pin based x value, 1, clockwise
        GPIO.output(direction,GPIO.HIGH)
    while(do_loop):
        GPIO.output(pulse,GPIO.HIGH)
        time.sleep(SPEED)
        GPIO.output(pulse,GPIO.LOW)
        time.sleep(SPEED)
        POSITION += x
        #numField.delete(0, END)
        #numField.insert(0,str(POSITION))


# stop thread function
def stoploopevent2(self):
    global do_loop
    do_loop = FALSE
    time.sleep(.1) # delay to let thread finish
    GPIO.output(pulse,GPIO.LOW) # set pulse pin low


# thread start function for l_button and r_button
def move(x):
    th = threading.Thread(target= lambda: move_thread(x))
    #threads.append(th)
    th.daemon
    th.start()






# position_to_distance()
# takes position (motor pulses), transfer pulley diameter (inches), drive ratio
# and calculates position from calibration start point in feet
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


def sleep_to_rpm(t):
    return ((1 / t) / (400)) * 60 # RPM = ((1 second / sleeptime) / (2 phases * 200 pulses_per_rotation)) * 60 seconds


# rpm_to_speed()
# takes rpm[integer] and pulley diameter[float] and returns
# a linear speed in miles/hr (mph)
#
# INPUT: float, float
# OUTPUT: float
def rpm_to_speed(rpm, diameter):
    minutes = 60.0
    inches_per_mile = 63360.0
    circumference = diameter * pi
    return ((circumference * rpm * minutes) / inches_per_mile)


# speed_to_rpm()
# takes speed[float] in miles per hour (mph) and pulley diameter[float]
# and returns an rpm[float]
#
# INPUT: float, float
# OUTPUT: float
def speed_to_rpm(speed, diameter):
    minutes = 60.0
    inches_per_mile = 63360.0
    circumference = diameter * pi
    return ((inches_per_mile * speed) / (minutes * circumference))


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


# to test pulley diameter and ratio pulse times uncomment and plug in test values
# as (speed(mph), transfer pulley diameter(inches), ratio(if direct drive use 1.0))

pulseT = speed_to_pulse_time(1.5, .4375, 3.0)
rpm = sleep_to_rpm(pulseT)
print("\n========================================\n")
print("Pulse time: " + str(pulseT))
print("RPM: " + str(rpm))
print("distance: " + str(round(position_to_distance(200.0, 3.819718634, 1.0), 2)))
# print("RPM t: " + str(rpm_to_pulsesleep(60)))

print("\n========================================\n")






#Below is the older functions used to spin the motor.

def GPIO_Initialisation():
    global led
    led = 32  # testing purposes led pin 32
    global pulse
    pulse = 40  # driver pulse signal GPIO pin 40
    global direction
    direction = 36  # driver pulse direction GPIO pin 36

    freq = 100  # frequency variable for testing PWM library

    # GPIO Drivers
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(led, GPIO.OUT)
    GPIO.output(led, GPIO.LOW)
    GPIO.setup(pulse, GPIO.OUT)
    GPIO.output(pulse, GPIO.LOW)
    GPIO.setup(direction, GPIO.OUT)
    GPIO.output(direction, GPIO.LOW)

    # pi_pwm = GPIO.PWM(pulse, freq)
    # pi_pwm.start(50)


def setLow(pinNum):
    GPIO.output(pinNum, GPIO.LOW)


def setHigh(pinNum):
    GPIO.output(pinNum, GPIO.HIGH)


def checkOn(pinNum):
    if GPIO.input(pinNum):
        return True
    else:
        return False


def spinRight():
    print("spinRight button pressed")
    # Set Direction first
    setHigh(36)
    setHigh(40)
    # time.sleep(.000005) #comment out for fastest
    setLow(40)


# time.sleep(.1) #need for led testing


def spinLeft():
    print("spinLeft button pressed")
    
    # Set Direction first
    setLow(36)
    setHigh(40)
    # time.sleep(.000005) #comment out for fastest
    setLow(40)


# time.sleep(.1) #need for led testing


def spinHold():
    print("spinHold button pressed")
    setHigh(32)
    time.sleep(.1)
    setLow(32)
    time.sleep(.1)


def spin():
    # print("spinFuncRunning")
    if checkOn(40):
        setLow(40)
    # spinButton["text"] = "SPIN ON"
    else:
        setHigh(40)
    # spinButton["text"] = "SPIN OFF"


def spinForSetTime():
    loopCount = 3000
    #	interval=.15015 #seconds, halved due to on/off
    #	interval = calcRPM(60) # RPM = (1/interval) / (2 * 200) * 60sec
    interval = speed_to_pulse_time(.2, .1875, 1.0)  # enter as floats for percision
    while loopCount > 0:
        spin()
        time.sleep(interval)
        loopCount = loopCount - 1
    # print(loopCount)
    if checkOn(pulse):
        setLow(pulse)
