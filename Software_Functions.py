from tkinter import *
from tkinter import messagebox as m
import csv
import os
import time
from tkinter import filedialog
import motor_control as motor
import values

try:
    from configparser import ConfigParser
except ImportError:
    from ConfigParser import ConfigParser  # ver. < 3.0

config = ConfigParser()
# parse existing file
config.read('spmProps.ini')



# This tracks the position of the prop, and is used in the position_up and position_down functions.
# (as of 3-27-201 it is only for testing)
position = 0
path = os.getcwd()


def calWarn():
    m.showwarning(title=None, message="You must calibrate the system before starting. Visit calibrate page.")

def calWarn2():
    m.showwarning(title=None, message="loading these settings will require calibration before running!")
# profileEntries is a list of the entry textboxs found on the profile page.
# profileEntries should be [ratioPro, diameterPro, speedPro, positionPro, filenamePro]
# This function runs when the save button on the profilePage is pressed.
def save_profile(profileEntries):
    trueDirectory = path+"/csv/"
    print("true holds:"+ trueDirectory)
    csv_list = []
    for i in range(5):  # This loops through index's 0,1,2,3,4
        csv_list.append(profileEntries[i].get())   # Here we append the profile entry box's values into a list
    filename = trueDirectory + profileEntries[4].get() + '.csv'
    file = open(filename, 'w')
    writer = csv.writer(file)
    writer.writerow(csv_list)

# This function simply deletes the csv file that was given in the filename entry box
def delete_profile(profileEntries):
    trueDirectory = path+"/csv/"
    print("true holds:"+ trueDirectory)
    os.remove(trueDirectory + profileEntries[4].get() + '.csv')


# This function reads in all the names of the csv profiles, and prints them to a new window
# profilePage is the frame that all the buttons are displayed on.
# It is here incase we want to generate new buttons on load
# profileEntries is a list of the entry textboxes found on the profile page.
# profileEntries should be [ratioPro, diameterPro, speedPro, positionPro, filenamePro]
# This function runs when the load button on the profilePage is pressed.
def read_profile(profilePage, profileEntries):
    #global DESTINATION
    trueDirectory = path+"/csv/"
    print("true holds:"+ trueDirectory)
    # This line brings up a file prompt that will allow the user to pick a file without the use of a keyboard
    loadedFiles = filedialog.askopenfilename(initialdir=trueDirectory, title= "popup", filetypes=(("csv files", "*.csv"), ("all files", "*.*")))

    # With that loaded file, here we simply load the values in the entry box for the user to see
    # To update entry boxes, we must first delete what is in it, and then insert our new string
    with open(loadedFiles) as f:
        reader = csv.reader(f)
        line = next(reader)
        print("BEFORE HERE")
        for i in range(5):
            profileEntries[i].delete(0, END)  # This deletes the current text in entry, starting at index 0, to 'END'
            profileEntries[i].insert(0, line[i])  # This inserts a new string at position 0 in the entry box
            if(i==0):
                if(values.drive_ratio != float(profileEntries[0].get())): # loading this into current calibration isn't compatable
                    calWarn2()
            if(i==1):
                if(float(profileEntries[1].get()) != values.pulley_diameter): # loading this into current calibration isn't compatable
                    calWarn2()
            if (i == 3):
                if(values.DESTINATION < 0 or values.DESTINATION > values.END_limit):
                    m.showwarning(title=None, message="The position loaded is out of calibrated bounds. You can still run but the prop will stop short. Recalibrate if needed.")

                # config.set('section_a', 'destination', profileEntries[3].get())
                # # -----Update the Prop File itself : Must run after every SET Operation-------------
                # with open('spmProps.ini', 'w') as configfile:
                #     config.write(configfile)




def automatic_control(profilePage, profileEntries, varList, varList2, positionSliderList, positionPro):
    for i in range(5):
        if(i==0):
            if profileEntries[0].get() != "":
                if(values.drive_ratio != float(profileEntries[0].get())): # loading this into current calibration isn't compatable
                    values.CALIBRATED = False
                    calWarn()
                values.drive_ratio = float(profileEntries[0].get())
        if(i==1):
            if profileEntries[1].get() != "":
                if(float(profileEntries[1].get()) != values.pulley_diameter): # loading this into current calibration isn't compatable
                    values.CALIBRATED = False
                    calWarn()
                values.pulley_diameter = float(profileEntries[1].get())

        if(i==2):
            if profileEntries[2].get() != "":
                values.SPEED = motor.speed_to_pulse_time(float(profileEntries[2].get()), values.pulley_diameter, values.drive_ratio)
                print("LOADED SPEED: " + str(values.SPEED))
        if (i == 3):
            # print("profile Entry: " + str(profileEntries[3].get()))
            # DESTINATION = profileEntries[3].get()
            # print("destination\n")
            # print(DESTINATION)
            if profileEntries[3].get() != "":
                values.DESTINATION = int(motor.distance_to_position(float(profileEntries[3].get())))
                if(values.DESTINATION < 0 or values.DESTINATION > values.END_limit):
                    m.showwarning(title=None, message="The position loaded is out of calibrated bounds, please choose an appropriate position!")
    config.set('section_a', 'pulley_diameter', str(values.pulley_diameter))
    config.set('section_a', 'speed', str(values.SPEED))
    config.set('section_a', 'drive_ratio', str(values.drive_ratio))
    with open('spmProps.ini', 'w') as configfile:
        config.write(configfile)
    motor.ratio_update(varList2)
    motor.spec_speed_update(varList)
    motor.auto_move(positionSliderList, positionPro)

####################################################################################
def setStartPoint():
    values.tempStartPosition = values.POSITION  
    values.POSITION = 0 # zero current position sine this is the starting-end limit
    values.CALIBRATED = False # needed in case user starts recalibrating, to make sure they finish
    print("Start position set")

def setEndPoint():
    values.END_limit = values.POSITION #- values.tempStartPosition# set position value as ending-end limit
    print("End position set at "+ str(values.POSITION))

def confirmCalibration(positionSliderList):
    if ((values.END_limit) < 0):
        m.showwarning(title=None, message="You are calibrating backwards!\n\nRecalibrate starting\nfrom Step 1")
    else:
        values.CALIBRATED = True
        calibrateSliders(positionSliderList)

def calibrateSliders(positionSliderList):
    for i in positionSliderList:
        i.config(from_=0, to=values.END_limit)
