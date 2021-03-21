from tkinter import *
import RPi.GPIO as GPIO
import time
import spm_control_akogan as control


def exitProgram():
    print("Exit Button pressed")
    GPIO.cleanup()
    root.destroy()
