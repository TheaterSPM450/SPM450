from tkinter import *
from tkinter import messagebox as m
import csv
import os
import time
from tkinter import filedialog
# import Hardware_Functions as hf 

# This tracks the position of the prop, and is used in the position_up and position_down functions.
# (as of 3-27-201 it is only for testing)
position = 0
path = os.getcwd()


def calWarn():
    m.showwarning(title=None, message="You must calibrate the system before starting. Visit calibrate page.")


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
    trueDirectory = path+"/csv/"
    print("true holds:"+ trueDirectory)
    # This line brings up a file prompt that will allow the user to pick a file without the use of a keyboard
    loadedFiles = filedialog.askopenfilename(initialdir=trueDirectory, title= "popup", filetypes=(("csv files", "*.csv"), ("all files", "*.*")))

    # With that loaded file, here we simply load the values in the entry box for the user to see
    # To update entry boxes, we must first delete what is in it, and then insert our new string
    with open(loadedFiles) as f:
        reader = csv.reader(f)
        line = next(reader)
        for i in range(5):
            profileEntries[i].delete(0, END)  # This deletes the current text in entry, starting at index 0, to 'END'
            profileEntries[i].insert(0, line[i])  # This inserts a new string at position 0 in the entry box

#This is a temporary function, that moves the slider using the position functions to the profile location
# def run_profile(profileEntries,positionSliderList,profilePage):
#     newPosition = int(profileEntries[3].get())
#     global position
#     positionDifference = abs(position - newPosition)
#     for i in range(positionDifference):
#         time.sleep(.001)
#         if newPosition < position:
#             position_down(positionSliderList)
#         elif newPosition > position:
#             position_up(positionSliderList)
#         profilePage.update()
#         print(str(newPosition) + "---" + str(position))


####################################################################################