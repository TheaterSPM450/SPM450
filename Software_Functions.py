from tkinter import *
import csv
import os
import time
from tkinter import filedialog
import Hardware_Functions as hf

# This tracks the position of the prop, and is used in the position_up and position_down functions.
# (as of 3-27-201 it is only for testing)
position = 0
path = os.getcwd()



# # This function used to have fields as a parameter that had to be passed to it
# # It seemed easier to just remove that parameter, and make fields a local variable in the func
# def makeform(root):
#     fields = ["speed", "ratio", "diameter", "position", "filename"]
#     entries = []
#     for field in fields:
#         row = Frame(root)
#         lab = Label(row, width=15, text=field, anchor='w')
#         ent = Entry(row)
#         row.pack(side=TOP, fill=X, padx=5, pady=5)
#         lab.pack(side=LEFT)
#         ent.pack(side=RIGHT, expand=YES, fill=X)
#         entries.append((field, ent))
#     return entries

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
        print(line)
        print(line[0])
        for i in range(5):
            profileEntries[i].delete(0, END)  # This deletes the current text in entry, starting at index 0, to 'END'
            profileEntries[i].insert(0, line[i])  # This inserts a new string at position 0 in the entry box

#This is a temporary function, that moves the slider using the position functions to the profile location
def run_profile(profileEntries,positionSliderList,profilePage):
    newPosition = int(profileEntries[3].get())
    global position
    positionDifference = abs(position - newPosition)
    for i in range(positionDifference):
        time.sleep(.001)
        if newPosition < position:
            position_down(positionSliderList)
        elif newPosition > position:
            position_up(positionSliderList)
        profilePage.update()
        print(str(newPosition) + "---" + str(position))


####################################################################################
# These are just test functions. It is attached to the left and right move button
# It simulates the position of the stage pro changing
# This function is designed to test the slider to make sure it is reading in a value
# Eventually that slider should read in an actual calculated position value
# The parameter is takes in is the entire slider widget


def position_up(positionSliderList):
    global position
    if position < 1000:
        position += 1
        hf.move(1)              #This is the hardware function that includes threading
        for i in positionSliderList:
            i.set(position)


def position_down(positionSliderList):
    global position
    if position > 0:
        position -= 1
        hf.move(-1)       #This is the hardware function that includes threading
        for i in positionSliderList:
            i.set(position)

######################################################################
