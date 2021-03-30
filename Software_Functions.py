from tkinter import *
import csv
import os
from tkinter import filedialog

# This tracks the position of the prop, and is used in the position_up and position_down functions.
# (as of 3-27-201 it is only for testing)
position = 0


# This function used to have fields as a parameter that had to be passed to it
# It seemed easier to just remove that parameter, and make fields a local variable in the func
def makeform(root):
    fields = ["speed", "ratio", "diameter", "position", "filename"]
    entries = []
    for field in fields:
        row = Frame(root)
        lab = Label(row, width=15, text=field, anchor='w')
        ent = Entry(row)
        row.pack(side=TOP, fill=X, padx=5, pady=5)
        lab.pack(side=LEFT)
        ent.pack(side=RIGHT, expand=YES, fill=X)
        entries.append((field, ent))
    return entries


def fetch(entries):
    trueDirectory = "/home/pi/Desktop/SPM450Files/SPM450/csv/"
    # nickDirectory is just for when nick is coding on his home desktop.
    nickDirectory = "C:/Users/nickm/PycharmProjects/SPM450/csv/"
    csv_list = []
    text = ''
    for entry in entries:
        text = entry[1].get()
        if entry[0] == 'filename':
            break
        csv_list.append(text)
    filename = nickDirectory + text + '.csv'
    file = open(filename, 'w')
    writer = csv.writer(file)
    writer.writerow(csv_list)

# This is a rewrite of the fetch function, using slightly altered data structures
# profileEntries is a list of the entry textboxs found on the profile page.
# profileEntries should be [ratioPro, diameterPro, speedPro, positionPro, filenamePro]
# This function runs when the save button on the profilePage is pressed.
def save_profile(profileEntries):
    trueDirectory = "/home/pi/Desktop/SPM450Files/SPM450/csv/"
    # nickDirectory is just for when nick is coding on his home desktop.
    nickDirectory = "C:/Users/nickm/PycharmProjects/SPM450/csv/"
    csv_list = []
    for i in range(5):  # This loops through index's 0,1,2,3,4
        csv_list.append(profileEntries[i].get())   # Here we append the profile entry box's values into a list
    filename = nickDirectory + profileEntries[4].get() + '.csv'
    file = open(filename, 'w')
    writer = csv.writer(file)
    writer.writerow(csv_list)

# This function simply deletes the csv file that was given in the filename entry box
def delete_profile(profileEntries):
    trueDirectory = "/home/pi/Desktop/SPM450Files/SPM450/csv/"
    # nickDirectory is just for when nick is coding on his home desktop.
    nickDirectory = "C:/Users/nickm/PycharmProjects/SPM450/csv/"
    os.remove(nickDirectory + profileEntries[4].get() + '.csv')


# This function reads in all the names of the csv profiles, and prints them to a new window
# profilePage is the frame that all the buttons are displayed on.
# It is here incase we want to generate new buttons on load
# profileEntries is a list of the entry textboxes found on the profile page.
# profileEntries should be [ratioPro, diameterPro, speedPro, positionPro, filenamePro]
# This function runs when the load button on the profilePage is pressed.
def read_profile(profilePage, profileEntries):
    trueDirectory = "/home/pi/Desktop/SPM450Files/SPM450/csv/"
    # nickDirectory is just for when nick is coding on his home desktop.
    nickDirectory = "C:/Users/nickm/PycharmProjects/SPM450/csv"
    # This line brings up a file prompt that will allow the user to pick a file without the use of a keyboard
    loadedFiles = filedialog.askopenfilename(initialdir=nickDirectory, title= "popup", filetypes=(("csv files", "*.csv"), ("all files", "*.*")))

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

# This is legacy code from read_profile, from when we loaded file names into a global list variable
# It read all the csv file names from the csv directory, and stored them for file opening later
# Left the code here incase in finds some use later
    # for file in glob.glob("*.csv"):
    #     profiles.append(file)
    # top = Toplevel()
    # top.title("List of profiles")
    # for i in profiles:
    #     Label(top, text=i).pack()
    # label1 = Label(profilePage, text=loadedFiles)
    # label1.pack()

####################################################################################
# These are just test functions. It is attached to the left and right move button
# It simulates the position of the stage pro changing
# This function is designed to test the slider to make sure it is reading in a value
# Eventually that slider should read in an actual calculated position value
# The parameter is takes in is the entire slider widget


def position_up(positionSliderList):
    global position
    if position < 1000:
        position += 0.2
        for i in positionSliderList:
            i.set(position)


def position_down(positionSliderList):
    global position
    if position > 0:
        position -= 0.2
        for i in positionSliderList:
            i.set(position)

######################################################################
