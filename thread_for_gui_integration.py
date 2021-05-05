'''
thread_for_gui_integration.py

Author: Alex Kogan
Date: 4/24/2021

threading code for stepper control to integrate with GUI


'''
from tkinter import *
import time
import threading
import RPi.GPIO as GPIO
#import spm_control_akogan as control

#vars
do_loop = FALSE # used for thread termination, could be changed to "motor_enable" or something similar
SPEED = .00035 # pulse sleep time, in seconds as a float
POSITION = 0 # an accumulator variable which can be used for current position tracking
pulse = 40  # driver pulse signal GPIO pin 40
direction = 36  # driver pulse direction GPIO pin 36
threads = [] # thread queue

# GPIO Drivers
GPIO.setmode(GPIO.BOARD)
GPIO.setup(pulse, GPIO.OUT)
GPIO.output(pulse, GPIO.LOW)
GPIO.setup(direction, GPIO.OUT)
GPIO.output(direction, GPIO.LOW)

tk = Tk() # tk object

# set minimum window size to 4:3 by setting resolution to 800x600
tk.minsize(800, 600)



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
        numField.delete(0, END)
        numField.insert(0,str(POSITION))     


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









# exits program
def exitProgram():
	print("Exit Button pressed")
	tk.destroy()


#BUTTONS, ENTRIES and WIDGETS

#/////////////////////////////////////////////////////
#               <<<<< LEFT <<<<<
#/////////////////////////////////////////////////////
# left button (decrement field)
l_button = Button(tk, text='<<<< L <<<<', bg='yellow', justify='left')
l_button.pack()
# Button-1 is left mouse button.
# The following 2 lines bind the mouse click and release
# to separate function calls. Click down starts a thread,
# release changes a thread condition to false
l_button.bind("<Button-1>", lambda x: move(-1))
l_button.bind("<ButtonRelease-1>", stoploopevent2)

#/////////////////////////////////////////////////////
#               ***** DISPLAY *****
#/////////////////////////////////////////////////////
l1 = Label(tk, text="Position: ")
l1.pack()
# display field
numField = Entry(tk, bg='white', bd='4', state='normal', justify='center', width=10)
numField.pack()
numField.insert(0,str(POSITION))

#/////////////////////////////////////////////////////
#               >>>>> RIGHT >>>>>
#/////////////////////////////////////////////////////
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