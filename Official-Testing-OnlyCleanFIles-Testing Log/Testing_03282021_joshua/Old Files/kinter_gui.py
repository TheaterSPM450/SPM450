# kinter_gui.py
#
# Author: Alex Kogan
#
# Overview: This file contains a test program utilizing Python Tkingter library to create
# a GUI for development purposes
#


# IMPORTS & INCLUDES
from tkinter import * # GUI lib
import tkinter as tk
import csv          #CSV lib
import os           # OS lib
import spm_model as spm    # Model code file
import RPi.GPIO as GPIO
import time
import spm_control_akogan as control


# CONSTANTS & VARIABLES___________________________________
fields = 'Gear Ratio', 'Position', 'Profile Name'
start = 0
end = 0
position = 0
direction = FALSE

led_pin = 32  # testing purposes led pin 32
step_pin = 40  # driver pulse signal GPIO pin 40
direction_pin = 36  # driver pulse direction GPIO pin 36
freq = 100  # frequency variable for testing PWM library

# var = tk.DoubleVar()


# INITIALIZATIONS_________________________________________

# Tk() defines a gui program window assigned to root
root = Tk()

# set minimum window size to 4:3 by setting resolution to 800x600
root.minsize(800, 600)

# window title
root.title("SPM450 Commander BETA")

ents = spm.makeform(root, fields)
root.bind('<Return>', (lambda event, e=ents: spm.fetch(e)))

# scale = Scale(root, variable = var )
# scale.pack(anchor=CENTER)

def setLow(pinNum):
	GPIO.output(pinNum,GPIO.LOW)
def setHigh(pinNum):
	GPIO.output(pinNum,GPIO.HIGH)
def checkOn(pinNum):
	if GPIO.input(pinNum):
		return True
	else:
		return False

def spinRight():
	print("spinRight button pressed")
	# Set Direction first
	setHigh(36)
	setHigh(step_pin)
	#time.sleep(.000005) #comment out for fastest
	setLow(step_pin)
	#time.sleep(.1) #need for led testing

def spinLeft():
	print("spinLeft button pressed")
	# Set Direction first
	setLow(36)
	setHigh(step_pin)
	#time.sleep(.000005) #comment out for fastest
	setLow(step_pin)
	#time.sleep(.1) #need for led testing

def spin():
	#print("spinFuncRunning")
	if checkOn(step_pin) :
		setLow(step_pin)
		#spinButton["text"] = "SPIN ON"
	else:
		setHigh(step_pin)
		#spinButton["text"] = "SPIN OFF"

def spinForSetTime():
	loopCount=3000
#	interval=.15015 #seconds, halved due to on/off
#	interval = calcRPM(60) # RPM = (1/interval) / (2 * 200) * 60sec
	interval = control.speed_to_pulse_time(.2, .1875, 1.0) # enter as floats for percision
	while loopCount>0:
		spin()
		time.sleep(interval)
		loopCount=loopCount-1
		#print(loopCount)
	if checkOn(step_pin):
		setLow(step_pin)




b1 = tk.Button(root, text='Save', command=(lambda e=ents: spm.fetch(e)))
b1.pack(side=tk.LEFT, padx=5, pady=5)
b2 = tk.Button(root, text='Quit', command=root.quit)
b2.pack(side=tk.LEFT, padx=5, pady=5)
b3 = tk.Button(root, text='Delete', command=(lambda e=ents: spm.delete_profile(e)))
b3.pack(side=tk.LEFT, padx=5, pady=5)

# button 4 just displays the profiles currently available in their own window
b4 = tk.Button(root, text='Display profiles', command=spm.readProfiles).pack(side=tk.LEFT, padx=5, pady=5)

# Exit button program
q_button = Button(root, text="Exit", command=root.quit, fg="#ffffff", bg="#ff0000", activebackground="#d00000").pack(side=tk.RIGHT, padx=40, pady=20)

spinForSetTimeButton = Button(root, text = "SpinForSetTime", command = spinForSetTime, height = 2, width =10)
spinForSetTimeButton.place(x=100,y=100)

spinRightButton = Button(root, text = "RIGHT", repeatdelay=1, repeatinterval=1, command=spinRight, height = 5, width =10 )
spinRightButton.place(x=500,y=300)

spinLeftButton = Button(root, text = "LEFT", repeatdelay=20, repeatinterval=1, command=spinLeft, height = 5, width =10 )
spinLeftButton.place(x=200,y=300)

root.mainloop()
