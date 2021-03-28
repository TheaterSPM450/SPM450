from tkinter import *
import RPi.GPIO as GPIO
import time
import spm_control_akogan as control


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
    ##setHigh(36)
    ##setHigh(40)
    # time.sleep(.000005) #comment out for fastest
    ##setLow(40)


# time.sleep(.1) #need for led testing


def spinLeft():
    print("spinLeft button pressed")
    # Set Direction first
    ##setLow(36)
    ##setHigh(40)
    # time.sleep(.000005) #comment out for fastest
    ##setLow(40)


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
    interval = control.speed_to_pulse_time(.2, .1875, 1.0)  # enter as floats for percision
    while loopCount > 0:
        spin()
        time.sleep(interval)
        loopCount = loopCount - 1
    # print(loopCount)
    if checkOn(pulse):
        setLow(pulse)
