'''
kinter_thread.py

Author: Alex Kogan
Date: 3/15/2021

threading code for program execution
'''
from tkinter import *
import time
import threading

#vars
do_loop = FALSE # used for thread termination, could be changed to "motor_enable" or something similar

POSITION = 0 # an accumulator variable which can be used for current position tracking 
WAIT = .500 # sleep delay time variable for testing/development purposes

threads = [] # thread queue, may not be needed

tk = Tk() # tk object

# set minimum window size to 4:3 by setting resolution to 800x600
tk.minsize(800, 600)


# THREAD FUNCTION
# loop function to run on thread for startButton
def startloopevent():
    global do_loop # main thread do_loop access
    global POSITION # main thread POSITION access
    do_loop = TRUE # enable loop condition
    x = 0
    countlim = 1000
    # this loop is similar to stepper pulse actuation
    # instead the background color is changed between 2 states
    # with a pause in between
    while(do_loop and x < countlim):
        tk.configure(bg='grey')
        print("ON")
        time.sleep(WAIT)
        tk.configure(bg='azure')
        print("OFF")
        time.sleep(WAIT)
        POSITION += 1
        numField.delete(0, END)
        numField.insert(0,str(POSITION))
        x += 1
    

# THREAD FUNCTION
# loop function to run on thread for l_button and r_button click binding 
def startclicking(x): # takes an input of -1 or 1 from caller
    global do_loop
    global POSITION
    do_loop = TRUE
    while(do_loop):
        POSITION += x
        numField.delete(0, END)
        numField.insert(0,str(POSITION))
        time.sleep(WAIT)


# stop thread function
def stoploopevent():
    global do_loop
    do_loop = FALSE
    # th.destroy()


# stop thread function
def stoploopevent2(self):
    global do_loop
    do_loop = FALSE


# thread start function for startButton
def st_thread():
    th = threading.Thread(target=startloopevent) # create new thread running startloopevent function
    threads.append(th)
    th.daemon
    th.start()


# thread start function for l_button and r_button
def st_click(x):
    th = threading.Thread(target= lambda: startclicking(x))
    threads.append(th)
    th.daemon
    th.start()


# does 1 click operation altering POSITION variable and numField according to input
def click(x):
    global POSITION
    POSITION += x
    numField.delete(0, END)
    numField.insert(0,str(POSITION))


# exits program
def exitProgram():
	print("Exit Button pressed")
	tk.destroy()


#BUTTONS, ENTRIES and WIDGETS
# start loop
startButton = Button(tk, text="START Thread", command=st_thread, height = 5, width =10 )
startButton.pack()

# stop loop
stopButton = Button(tk, text="STOP Thread", command= stoploopevent, height = 5, width =10)
stopButton.pack()


# left button (decrement field)
l_button = Button(tk, text='<<<< L <<<<', bg='yellow', justify='left')
l_button.pack()
# Button-1 is left mouse button.
# The following 2 lines bind the mouse click and release
# to separate function calls. Click down starts a thread,
# release changes a thread condition to false
l_button.bind("<Button-1>", lambda x: st_click(-1))
l_button.bind("<ButtonRelease-1>", stoploopevent2)

# display field
numField = Entry(tk, bg='white', bd='4', state='normal', justify='center', width=10)
numField.pack()
numField.insert(0,str(POSITION))

# right button (increment field)
r_button = Button(tk, text='>>>> R >>>>', bg='orange', justify='right')
r_button.pack()
# Button-1 is left mouse button.
# The following 2 lines bind the mouse click and release
# to separate function calls. Click down starts a thread,
# release changes a thread condition to false
r_button.bind("<Button-1>", lambda x: st_click(1))
r_button.bind("<ButtonRelease-1>", stoploopevent2)



exitButton  = Button(tk, text = "Exit", command = exitProgram, height =2 , width = 10, bg='red', bd='4') 
exitButton.pack(side = BOTTOM)



tk.mainloop()