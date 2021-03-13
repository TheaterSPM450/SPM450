from tkinter import *
import RPi.GPIO as GPIO
import time

# import tkFont

led = 32  # testing purposes led pin 32
pulse = 40  # driver pulse signal GPIO pin 40
direction = 36  # driver pulse direction GPIO pin 36

freq = 100  # frequency variable for testing PWM library


#GPIO Drivers
GPIO.setmode(GPIO.BOARD)
GPIO.setup(led, GPIO.OUT)
GPIO.output(led, GPIO.LOW)
GPIO.setup(pulse, GPIO.OUT)
GPIO.output(pulse, GPIO.LOW)
GPIO.setup(direction, GPIO.OUT)
GPIO.output(direction, GPIO.LOW)

# pi_pwm = GPIO.PWM(pulse, freq)
# pi_pwm.start(50)


# declaire base GUI window
win = Tk()

# myFont = tkFont.Font(family = 'Helvetica', size = 8, weight = 'bold')

def testThisMsg():
   	print("HIHIHIH")
def setLow(pinNum):
	GPIO.output(pinNum,GPIO.LOW)
def setHigh(pinNum):
	GPIO.output(pinNum,GPIO.HIGH)
def checkOn(pinNum):
	if GPIO.input(pinNum):
		return True
	else:
		return False


# calcRPM()
# takes a rpm value and returns a sleep duration
# value in terms of seconds for motor rpm control
#
# calculates 1 second divived by rpm value divided
# by 60, time 400(2 phase halfs times 200 pulses per revolution)
#
# INPUT: integer
# OUTPUT: float
def calcRPM(rpm):
    print((1 / (400 * (rpm / 60))))
    return (1 / (400 * (rpm / 60)))


def spinRight():
	print("spinRight button pressed")
	# Set Direction first
	setHigh(36)
	setHigh(40)
	#time.sleep(.000005) #comment out for fastest
	setLow(40)
	#time.sleep(.1) #need for led testing

def spinLeft():
	print("spinLeft button pressed")
	# Set Direction first
	setLow(36)
	setHigh(40)
	#time.sleep(.000005) #comment out for fastest
	setLow(40)
	#time.sleep(.1) #need for led testing

def spinHold():
	print("spinHold button pressed")
	setHigh(32)
	time.sleep(.1)
	setLow(32)
	time.sleep(.1)

def spin():
	#print("spinFuncRunning")
	if checkOn(40) :
		setLow(40)
		#spinButton["text"] = "SPIN ON"
	else:
		setHigh(40)
		#spinButton["text"] = "SPIN OFF"

def spinForSetTime():
	loopCount=3000
#	interval=.15015 #seconds, halved due to on/off
	interval = calcRPM(60) # RPM = (1/interval) / (2 * 200) * 60sec   
	while loopCount>0:
		spin()
		time.sleep(interval)
		loopCount=loopCount-1
		#print(loopCount)
	if checkOn(pulse):
		setLow(pulse)

def exitProgram():
	print("Exit Button pressed")
	GPIO.cleanup()
	win.destroy()	


win.title("First GUI")
win.geometry('800x480')

exitButton  = Button(win, text = "Exit", command = exitProgram, height =2 , width = 10) 
exitButton.pack(side = BOTTOM)

spinButton = Button(win, text = "SPIN ON", command = spin, height = 2, width =10 )
spinButton.pack()

spinForSetTimeButton = Button(win, text = "SpinForSetTime", command = spinForSetTime, height = 2, width =10)
spinForSetTimeButton.place(x=100,y=100)

#RepeatIsIn(ms)
spinHoldButton = Button(win, text = "spinHoldButton", repeatdelay=1, repeatinterval=1, command=spinHold, height = 2, width =10 )
spinHoldButton.place(x=100,y=200)

spinRightButton = Button(win, text = "RIGHT", repeatdelay=1, repeatinterval=1, command=spinRight, height = 5, width =10 )
spinRightButton.place(x=500,y=300)

spinLeftButton = Button(win, text = "LEFT", repeatdelay=20, repeatinterval=1, command=spinLeft, height = 5, width =10 )
spinLeftButton.place(x=200,y=300)

win.mainloop()